# ADR-0001 - Curated shared instructions for software teams

## Status
Accepted

## Date
2026-01-28

## Context
The CTO needs scalable, reliable agent execution with consistent quality and explainability. Manual prompt assembly is slow, inconsistent, and hard to audit. ThoughtWorks Radar vol. 33 lists "Curated shared instructions for software teams" in Adopt.

## Decision
Pilot a curated instruction pack builder for the radar_researcher agent to standardize prompts, reduce assembly time, and improve output quality.

## Consequences
- Positive: Faster prompt assembly, more consistent outputs, easier auditing.
- Risks: Over-standardization could reduce flexibility for edge cases.
- Follow-up: Evaluate metrics and decide whether to expand to other agents.

## Alternatives Considered
- Continue manual prompt assembly (rejected due to inconsistency).
- Build a generic agent framework without curated instructions (rejected; weak governance).

## References
- `/radar/pilots/curated-shared-instructions/pilot_plan.md`
- `/radar/ROADMAP.md`
- ThoughtWorks Radar vol. 33 PDF
