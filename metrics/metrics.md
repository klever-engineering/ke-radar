# Metrics Definitions

## Core Metrics (Required)

### 1) time_saved
**Definition:** Estimated minutes saved per task by using the new practice/tool compared to baseline.
**Measurement:**
- Capture time-on-task for a fixed set of tasks (baseline vs post-change).
- time_saved = avg(baseline_minutes) - avg(post_minutes).

### 2) accuracy
**Definition:** Degree to which outputs meet required acceptance criteria.
**Measurement:**
- Define required fields/criteria for each task.
- accuracy = pass_rate = (tasks meeting criteria) / (total tasks).

### 3) explainability
**Definition:** Degree to which outputs include clear rationale and traceability.
**Measurement:**
- Use a 0-5 rubric (rationale, SOP/roadmap reference, evidence/citations, assumptions/risks, structured output).
- explainability_score = average rubric score across tasks.

## Optional Metrics (Require CTO approval)
- defect_escape_rate
- rework_rate
- operational_risk_score

## Collection
- Record metrics in CSV/JSON under the pilot folder.
- Plot locally if needed; start simple before introducing a full metrics stack.
