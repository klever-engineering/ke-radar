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
| Week | Technology | Quadrant | Why now | Est. Effort |
| --- | --- | --- | --- | --- |
| 1 | Curated shared instructions for software teams | Techniques | ThoughtWorks Radar vol. 33 / Adopt ring; Directly improves agentic reliability + explainability and aligns with /AGENTS.md governance. | Low |
| 2 | Pre-commit hooks | Techniques | ThoughtWorks Radar vol. 33 / Adopt ring; Fast quality gates, reduces low-signal review churn. | Low |
| 3 | Software Bill of Materials (SBOM) | Techniques | ThoughtWorks Radar vol. 32 / Adopt ring; Improves compliance traceability and dependency transparency. | Low-Med |
| 4 | Threat modeling | Techniques | ThoughtWorks Radar vol. 32 / Adopt ring; Structured risk discovery before changes; supports reliability. | Med |
| 5 | Fuzz testing | Techniques | ThoughtWorks Radar vol. 32 / Adopt ring; Reliability boost, especially for parsers/automation scripts. | Med |
| 6 | Component testing | Techniques | ThoughtWorks Radar vol. 31 / Adopt ring; Strong QA signal for UI-heavy or componentized repos. | Med |
| 7 | Visual regression testing tools | Tools | ThoughtWorks Radar vol. 31 / Adopt ring; QA for UI regressions; good for documentation/UX surfaces. | Med |
| 8 | Testcontainers | Languages & Frameworks | ThoughtWorks Radar vol. 31 / Adopt ring; Reliable integration tests for automation workflows. | Med |
| 9 | Supabase | Platforms | Found via YouTube research; Accelerate backend prototyping | Low |
| 10 | Agentic Experience | Techniques | Found via YouTube research; Prioritize building what agents want | Low |
| 11 | Agent Economy | Techniques | Found via YouTube research; Emerging market where agents choose tools/subscriptions and shape procurement | Med |
| 12 | Agent-Friendly Documentation | Techniques | Internal research; Agent-friendly documentation with examples and clear contracts so agents can quickly assess certainty and accuracy | Low |
| 13 | Resend Examples | Techniques | Inspired by Resend docs/examples; exploration of https://resend.com for operator-friendly docs and agent guidance | Low |
| 14 | Mintlify Exploration | Techniques | Inspired by Mintlify (https://www.mintlify.com/) to make developer docs more agent-friendly—focus on structured knowledge, contextual examples, and clear contracts that agents can parse and trust | Med |

## Backlog (Trial / Assess)
- Structured output from LLMs (32: Assess, 33: Trial) - improves accuracy and validation.
- LLM as a judge (33: Assess) - quality control for agent outputs.
- AI-powered UI testing (32: Assess, 33: Assess) - QA automation.
- Model Context Protocol (MCP) (33: Trial) - aligns with AE2.0 ops automation.
- OpenTelemetry (32: Adopt) - observability for agent-driven workflows.
- Renovate (32: Adopt) - dependency hygiene.

## Current Selection
Starting with **Curated shared instructions for software teams** (vol. 33, Adopt) because it directly targets reliability, explainability, and agentic consistency while keeping effort low.
