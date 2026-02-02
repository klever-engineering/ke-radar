# Runbook - Technology Surveillance

## 0) Preconditions
- You are on a branch named `radar-<technology>`.
- Docker is available.
- Radar PDFs for volumes 31-33 are stored in `/radar/data/`.

## 1) Update Radar Data
- Run: `python3 /radar/scripts/extract_radar_blips.py`.
- Verify `/radar/data/radar_blips.json` is updated.

## 2) Update Roadmap
- Review `/radar/ROADMAP.md` scores and adjust if new context exists.
- Pick the next experiment (Adopt > Trial > Assess).

## 3) Create Pilot
- Create folder: `/radar/pilots/<technology>/`.
- Copy templates:
  - `/radar/templates/pilot_plan.md` -> `pilot_plan.md`
  - `/radar/templates/experiment_report.md` -> `experiment_report.md`
  - `/radar/templates/decision_memo.md` -> `decision_memo.md`
- Create ADR: `/radar/templates/adr-0000-template.md` -> `/docs/adr/adr-XXXX-<title>.md`

## 4) Run Experiment (Docker)
- Build and run the Docker sandbox defined in the pilot folder.
- Capture baseline, then apply change, then capture post-change metrics.

## 5) Document Outcomes
- Fill `experiment_report.md` with measurements and recommendation.
- Update `/radar/documentation/anti-patterns.md` if the pilot fails.

## 6) Log Decisions
- Log experiment start and conclusion using `/repositories/ai-company-decision-log/log_decision.py`.

## 7) Notify CTO
- Share the decision memo and request merge approval.

