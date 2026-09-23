# Bounded Rebuild Execution Contract v0.1

**Status:** `owner-execution-constraint / technical assurance / model-agnostic`  
**Owners:** #48 technical derivation, #59 development/verification, #61 work-context/handoff  
**Requirement authority:** #42 remains unchanged  
**Traceability:** #63  

## Purpose

This contract makes a repository-rebuild Work Order executable by Codex or a
comparable coding executor with a small, sufficient context. It is a delivery
constraint over existing governance and accepted Requirements. It is not a new
Requirement, product capability, agent class, workflow engine, or selection
authority.

The canonical record is a small JSON object. The execution context is derived
from that record and the current repository; it is not a second truth store.

## Required record

Every bounded rebuild order must contain:

- `work_order_ref`, `work_owner_ref`, and `primary_function`;
- a `causal_driver_slice` with Goal/Need/Pain references and applicable constraints;
- the already accepted Requirements and their explicit acceptance and verification references;
- `authority` with semantic and acceptance owners;
- an exact `scope.included_files` list, each with purpose and allowed change;
- `minimal_context.required_refs` with a reason and a maximum reference count;
- positive and negative test references;
- explicit `stop_handoff_when` and `persistence_target`;
- a `return_contract` whose format is `delta-only`, including the complete handoff packet;
- explicit non-goals excluding product multi-agent/workflow architecture.

No field may select a model, provider, token budget, temperature, or reasoning
setting. Model choice remains an execution-environment concern.

## Execution and return

The executor may inspect and change only the exact file list. It may implement
the accepted bounded task, run the named checks, and update the named
persistence target. It may not invent Requirements, decide scholarly meaning,
change authority, broaden scope, or create product-agent architecture.

The return contains only:

```text
delta
verification
open_points
handoff:
  from / to / trigger / established / unresolved / request /
  acceptance / persistence_target
```

An unresolved result is valid. If authority, acceptance, required evidence,
or exact scope is missing, the executor stops and returns a handoff rather than
repairing the missing governance from plausibility.

## Deterministic test boundary

`tools/operational/execution_order.py` checks structure, accepted Requirement
IDs, authority alignment, exact file scope, context boundedness, positive /
negative test presence, model agnosticism, and handoff completeness. It does
not judge historical truth, Method Truth, scientific sufficiency, or Owner
Acceptance. Those remain with the existing domain and owner boundaries.

The regression suite deliberately includes failures for scope drift, missing
authority, incomplete acceptance, broad context, Requirement invention,
handoff loss, model-specific fields, and missing product/workflow exclusions.
