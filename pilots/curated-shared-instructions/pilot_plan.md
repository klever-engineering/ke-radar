# Pilot Plan - Curated shared instructions for software teams

## Summary
- Technology: Curated shared instructions for software teams
- Radar volume: 33
- Ring: Adopt
- Quadrant: Techniques

## Hypothesis
A curated instruction pack will reduce prompt assembly time, increase output accuracy against SOP-defined acceptance criteria, and improve explainability by enforcing structured outputs and citation hooks.

## Success Criteria
- time_saved: >= 30% reduction in time to assemble task-specific instructions.
- accuracy: >= 20% improvement in pass rate against acceptance criteria.
- explainability: >= 20% improvement in reviewer rubric score (presence of rationale + traceability markers).

## Baseline
- Current process: Manual assembly of agent instructions from memory and ad-hoc references.
- Baseline measurements (estimate): 12 min to assemble an instruction pack; accuracy 0.5 (3/6 required fields); explainability 0/5.

## Experiment Design
- Scope: Instruction assembly for the radar_researcher workflow only.
- Sandbox: Docker container running the instruction pack builder and scoring scripts.
- Steps:
  1) Capture baseline prompt assembly time and output quality for 5 tasks.
  2) Implement curated instruction pack builder.
  3) Re-run the same tasks with the curated pack.
  4) Score time_saved, accuracy, explainability.
- Data to collect:
  - Task durations (minutes).
  - Pass/fail for required fields.
  - Explainability rubric scores.

## Risks & Mitigations
- Risk: Instruction pack too rigid and reduces flexibility.
  - Mitigation: Allow optional overlays and task-specific addenda.
- Risk: Scoring rubric is subjective.
  - Mitigation: Define a simple, repeatable checklist.

## Deliverables
- Demo/runnable code: `demo/instruction_pack_builder.py`
- ADR: `/docs/adr/adr-0001-curated-shared-instructions.md`
- Report + decision memo
