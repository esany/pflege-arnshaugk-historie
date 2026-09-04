import copy
import json
import tempfile
import unittest
from pathlib import Path

from tools.document_evidence.roundtrip import EvidenceError, load_manifest, normalized_to_page, validate_manifest


MANIFEST = Path(__file__).parents[1] / "data" / "sachenbacher-2022-gold-v0.1.json"


class ManifestTests(unittest.TestCase):
    def test_real_gold_manifest_is_valid_and_bounded(self):
        data = load_manifest(MANIFEST)
        self.assertEqual(5, len(data["gold_cases"]))
        self.assertEqual(20, data["instance"]["page_count"])
        self.assertEqual(
            "41e56fb31cc2a547f83a2a55797ecbf9938e6b90a296f1d7afb85d6df3593f9a",
            data["instance"]["sha256"],
        )

    def test_bbox_conversion_is_tool_neutral(self):
        self.assertEqual((0.0, 0.0, 100.0, 50.0), normalized_to_page([0, 0, 1, 1], 100, 50))

    def test_out_of_page_bbox_fails_closed(self):
        data = json.loads(MANIFEST.read_text())
        data["gold_cases"][0]["locators"][0]["bbox"] = [-0.1, 0, 1, 1]
        with self.assertRaises(EvidenceError):
            validate_manifest(data)

    def test_duplicate_locator_fails_closed(self):
        data = json.loads(MANIFEST.read_text())
        duplicate = copy.deepcopy(data["gold_cases"][0]["locators"][0])
        data["gold_cases"][1]["locators"].append(duplicate)
        with self.assertRaises(EvidenceError):
            validate_manifest(data)

    def test_parser_relation_requires_explicit_evaluation(self):
        data = json.loads(MANIFEST.read_text())
        data["relations"][1]["authority"] = "parser-heuristic"
        data["relations"][1].pop("evaluation")
        with self.assertRaises(EvidenceError):
            validate_manifest(data)

    def test_changed_instance_bytes_fail_before_adapter(self):
        from tools.document_evidence.roundtrip import run

        with tempfile.TemporaryDirectory() as directory:
            bad_pdf = Path(directory) / "changed.pdf"
            bad_pdf.write_bytes(b"not the fingerprinted instance")
            with self.assertRaisesRegex(EvidenceError, "fingerprint mismatch"):
                run(MANIFEST, bad_pdf, Path(directory) / "out")


if __name__ == "__main__":
    unittest.main()
