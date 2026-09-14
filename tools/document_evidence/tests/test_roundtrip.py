import copy
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from tools.document_evidence.roundtrip import EvidenceError, load_manifest, normalized_to_page, validate_manifest


MANIFEST = Path(__file__).parents[1] / "data" / "sachenbacher-2022-reference-v0.1.json"


class ManifestTests(unittest.TestCase):
    def test_real_reference_manifest_is_valid_and_bounded(self):
        data = load_manifest(MANIFEST)
        self.assertEqual(5, len(data["reference_cases"]))
        self.assertEqual(20, data["instance"]["page_count"])
        self.assertEqual(
            "41e56fb31cc2a547f83a2a55797ecbf9938e6b90a296f1d7afb85d6df3593f9a",
            data["instance"]["sha256"],
        )

    def test_published_map_is_not_split_into_reference_key_locator(self):
        data = load_manifest(MANIFEST)
        case = next(item for item in data["reference_cases"] if item["case_id"] == "REF51-04-PRIMARY-ZONE-MODEL")
        locator_ids = {item["locator_id"] for item in case["locators"]}
        self.assertIn("L51-04-MAP-A", locator_ids)
        self.assertNotIn("L51-04-KEY-B", locator_ids)
        relation = next(item for item in data["relations"] if item["relation_id"] == "R51-06")
        self.assertEqual("L51-04-MAP-A", relation["to_locator_id"])

    def test_bbox_conversion_is_tool_neutral(self):
        self.assertEqual((0.0, 0.0, 100.0, 50.0), normalized_to_page([0, 0, 1, 1], 100, 50))

    def test_out_of_page_bbox_fails_closed(self):
        data = json.loads(MANIFEST.read_text())
        data["reference_cases"][0]["locators"][0]["bbox"] = [-0.1, 0, 1, 1]
        with self.assertRaises(EvidenceError):
            validate_manifest(data)

    def test_duplicate_locator_fails_closed(self):
        data = json.loads(MANIFEST.read_text())
        duplicate = copy.deepcopy(data["reference_cases"][0]["locators"][0])
        data["reference_cases"][1]["locators"].append(duplicate)
        with self.assertRaises(EvidenceError):
            validate_manifest(data)

    def test_parser_relation_requires_explicit_evaluation(self):
        data = json.loads(MANIFEST.read_text())
        data["relations"][1]["authority"] = "parser-heuristic"
        data["relations"][1].pop("evaluation")
        with self.assertRaises(EvidenceError):
            validate_manifest(data)

    def test_invalid_page_indices_fail_closed(self):
        for index in (-1, 20, 1.5, True):
            with self.subTest(index=index):
                data = load_manifest(MANIFEST)
                data["reference_cases"][0]["locators"][0]["pdf_page_index"] = index
                with self.assertRaisesRegex(EvidenceError, "pdf_page_index"):
                    validate_manifest(data)

    def test_invalid_geometry_fails_closed(self):
        for geometry in ([], [100], [100, float("nan")], [100, -1]):
            with self.subTest(geometry=geometry):
                data = load_manifest(MANIFEST)
                data["reference_cases"][0]["locators"][0]["page_geometry_points"] = geometry
                with self.assertRaisesRegex(EvidenceError, "page geometry"):
                    validate_manifest(data)

    def test_noncritical_parser_evaluation_cannot_be_arbitrary(self):
        data = load_manifest(MANIFEST)
        data["relations"][0].update(authority="parser-heuristic", research_critical=False, evaluation="unchecked")
        with self.assertRaises(EvidenceError):
            validate_manifest(data)

    def test_cli_propagates_failed_report(self):
        from tools.document_evidence.roundtrip import main
        with patch("sys.argv", ["roundtrip", "manifest", "pdf", "output"]), patch(
            "tools.document_evidence.roundtrip.run", return_value={"result": "fail"}
        ), patch("builtins.print"):
            self.assertEqual(1, main())

    def test_changed_instance_bytes_fail_before_adapter(self):
        from tools.document_evidence.roundtrip import run

        with tempfile.TemporaryDirectory() as directory:
            bad_pdf = Path(directory) / "changed.pdf"
            bad_pdf.write_bytes(b"not the fingerprinted instance")
            with self.assertRaisesRegex(EvidenceError, "fingerprint mismatch"):
                run(MANIFEST, bad_pdf, Path(directory) / "out")


if __name__ == "__main__":
    unittest.main()
