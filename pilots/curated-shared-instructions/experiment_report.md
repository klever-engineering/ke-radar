# Experiment Report - Curated shared instructions for software teams

## Summary
- Status: Completed (Recommend Continue)
- Duration: Same-day pilot (2026-01-28)
- Sandbox: Docker (local); pilot files staged under `/home/alian/radar_sandbox/` for container mount

## Measurements
### time_saved
- Baseline: 12.0 minutes (estimated manual assembly)
- Post-change: 2.0 minutes (estimated builder + selection)
- Delta: 10.0 minutes saved

### accuracy
- Baseline: 0.5 (3/6 required fields present)
- Post-change: 1.0 (6/6 required fields present)
- Delta: +0.5

### explainability
- Baseline: 0/5 rubric markers present
- Post-change: 5/5 rubric markers present
- Delta: +5

## Findings
- What worked: Curated fragments consistently generate a complete instruction pack with required fields and explainability markers.
- What did not: Baseline time is estimated, not instrumented; needs validation on real tasks. Docker required staging outside `/media` due to file-sharing restrictions.
- Surprises: Small additions (references/assumptions markers) significantly boost explainability score.

## Recommendation
- Next steps: Continue by applying the curated pack to a real radar task next week and measure with actual time-on-task.
- Dependencies: None; optional instrumentation for time tracking.
