# Technology Surveillance Roadmap (Vols. 31-33)

## Prioritization Signals
1. Strategic fit with AE 2.0 (Delivery & Engineering Excellence; Operations & DevSecOps).
2. Pain relief (reliability, QA, explainability, agentic replacement of manual work).
3. Effort/risk (low-hanging fruit first).
4. Radar ring (Adopt > Trial > Assess).

## Scoring Rubric (1-5)
- Strategic fit (30%)
- Pain relief (40%)
- Effort (20%, inverted: lower effort scores higher)
- Ring weight (10%: Adopt=5, Trial=3, Assess=1)

## Roadmap (One experiment per week)
| Week | Technology | Volume | Ring | Quadrant | Why now | Est. Effort |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Curated shared instructions for software teams | 33 | Adopt | Techniques | Directly improves agentic reliability + explainability and aligns with /AGENTS.md governance. | Low |
| 2 | Pre-commit hooks | 33 | Adopt | Techniques | Fast quality gates, reduces low-signal review churn. | Low |
| 3 | Software Bill of Materials (SBOM) | 32 | Adopt | Techniques | Improves compliance traceability and dependency transparency. | Low-Med |
| 4 | Threat modeling | 32 | Adopt | Techniques | Structured risk discovery before changes; supports reliability. | Med |
| 5 | Fuzz testing | 32 | Adopt | Techniques | Reliability boost, especially for parsers/automation scripts. | Med |
| 6 | Component testing | 31 | Adopt | Techniques | Strong QA signal for UI-heavy or componentized repos. | Med |
| 7 | Visual regression testing tools | 31 | Adopt | Tools | QA for UI regressions; good for documentation/UX surfaces. | Med |
| 8 | Testcontainers | 31 | Adopt | Languages & Frameworks | Reliable integration tests for automation workflows. | Med |

## Backlog (Trial / Assess)
- Structured output from LLMs (32: Assess, 33: Trial) - improves accuracy and validation.
- LLM as a judge (33: Assess) - quality control for agent outputs.
- AI-powered UI testing (32: Assess, 33: Assess) - QA automation.
- Model Context Protocol (MCP) (33: Trial) - aligns with AE2.0 ops automation.
- OpenTelemetry (32: Adopt) - observability for agent-driven workflows.
- Renovate (32: Adopt) - dependency hygiene.

## Current Selection
Starting with **Curated shared instructions for software teams** (vol. 33, Adopt) because it directly targets reliability, explainability, and agentic consistency while keeping effort low.

