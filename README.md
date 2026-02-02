# Radar Technology Surveillance

This folder contains the AI Company technology surveillance program built on ThoughtWorks Technology Radar volumes 31-33. It defines the roadmap, SOP, templates, and pilot work for evaluating new practices, tools, and platforms.

## What lives here
- `ROADMAP.md`: prioritized backlog and sequencing for experiments.
- `SOP-Technology-Surveillance.md`: authoritative workflow for this program.
- `RUNBOOK.md`: how to run an experiment end to end.
- `AGENT_SPEC.md`: agent prompt/spec for the radar_researcher.
- `project-minutes.md`: session-level log of radar actions.
- `metrics/`: metric definitions and measurement guidance.
- `templates/`: reusable templates (pilot plan, experiment report, decision memo, ADR).
- `pilots/`: per-technology pilots, each with its own ADRs, demo, and evaluation assets.
- `documentation/`: experiment logs and anti-patterns.
- `scripts/`: helper scripts for pulling and parsing radar data.

## Branching convention
All experiment work lives on branches named `radar-<technology>`. Rebase regularly to `main`. Do not merge to `main` without explicit CTO approval.

## Data sources
ThoughtWorks Technology Radar PDFs are stored under `/radar/data/` and are the canonical raw inputs for volumes 31-33.
