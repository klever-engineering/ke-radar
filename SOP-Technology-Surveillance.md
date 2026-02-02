# SOP - Technology Surveillance (ThoughtWorks Radar)

## Purpose
Provide a repeatable, auditable workflow to evaluate ThoughtWorks Radar recommendations (vols. 31-33), run sandboxed pilots, measure impact, and document outcomes for CTO approval.

## Scope
- Applies to all technology surveillance work under `/radar`.
- Uses ThoughtWorks Technology Radar volumes 31-33 as the source of candidate practices/tools/platforms.
- Experiments run in Docker sandboxes and produce documented artifacts.

## Owner
CTO

## Inputs
- ThoughtWorks Radar PDFs for vols. 31-33 (stored under `/radar/data/`).
- AE 2.0 Roadmap (`/playbooks/roadmap/ae2.0-strategic-roadmap.mdx`).
- /AGENTS.md (root).

## Outputs
- Roadmap update (`/radar/ROADMAP.md`).
- Pilot plan (`/radar/pilots/<technology>/pilot_plan.md`).
- ADR(s) inside the pilot (`/radar/pilots/<technology>/docs/adr/`).
- Experiment report + decision memo.
- Anti-patterns entry if experiment fails.
- Decision log entry (start + conclusion).

## Workflow
### 1) Intake
- Confirm requester (CTO) and experiment cadence (one at a time).
- Confirm scope: volumes 31-33 only.
- Confirm branch name: `radar-<technology>`.

### 2) Preparation
- Pull latest radar PDFs into `/radar/data/`.
- Extract blips into a structured list.
- Reconcile against AE 2.0 priorities (Delivery & Engineering Excellence, Operations & DevSecOps).

### 3) Prioritization
- Rank candidates using the scoring rubric in `/radar/ROADMAP.md`.
- Prefer Adopt ring, then Trial, then Assess.
- Favor low-effort, high-impact first.

### 4) Pilot Design
- Create `/radar/pilots/<technology>/`.
- Write `pilot_plan.md` using the template.
- Define hypothesis, metrics (time_saved, accuracy, explainability), and success criteria.
- Create ADR(s) documenting why the technology was chosen and how it will be evaluated.

### 5) Execution
- Run experiment inside a Docker sandbox.
- Capture baseline and post-change measurements.
- Produce a small demo or runnable code sample.

### 6) Review
- Write `experiment_report.md` with results and a recommendation (Adopt / Continue / Abandon).
- If the pilot fails, add a concise entry to `/radar/documentation/anti-patterns.md`.

### 7) Closure
- Log decision start and conclusion in `/repositories/ai-company-decision-log/decision_log.db`.
- Update `/radar/ROADMAP.md` if priorities change.
- Notify CTO and request explicit approval before any merge to `main`.

## Logging Rules
- Log **start** and **final conclusion** only (no intermediate logs required).
- Use the decision log CLI: `python /repositories/ai-company-decision-log/log_decision.py`.

## Escalations
- If no SOP exists for a required system, create a SOP request and pause execution.
- If an experiment requires access to Odoo, ClickUp, or other systems, request CTO approval before proceeding.

