# Generic Technology Roadmap

## Prioritization Signals
1. Strategic fit with Delivery & Engineering Excellence; Operations & DevSecOps priorities.
2. Pain relief (reliability, QA, explainability, agentic replacement of manual work).
3. Effort/risk (low-hanging fruit first).
4. Radar ring (Adopt > Trial > Assess).

## Scoring Rubric (1-5)
- Strategic fit (30%)
- Pain relief (40%)
- Effort (20%, inverted: lower effort scores higher)
- Ring weight (10%: Adopt=5, Trial=3, Assess=1)

## Generic Roadmap
| Technology | Quadrant | Why now | Est. Effort |
| --- | --- | --- | --- |
| Curated shared instructions for software teams | Techniques | ThoughtWorks Radar vol. 33 / Adopt ring; Directly improves agentic reliability + explainability and aligns with /AGENTS.md governance. | Low |
| Pre-commit hooks | Techniques | ThoughtWorks Radar vol. 33 / Adopt ring; Fast quality gates, reduces low-signal review churn. | Low |
| Software Bill of Materials (SBOM) | Techniques | ThoughtWorks Radar vol. 32 / Adopt ring; Improves compliance traceability and dependency transparency. | Low-Med |
| Threat modeling | Techniques | ThoughtWorks Radar vol. 32 / Adopt ring; Structured risk discovery before changes; supports reliability. | Med |
| Fuzz testing | Techniques | ThoughtWorks Radar vol. 32 / Adopt ring; Reliability boost, especially for parsers/automation scripts. | Med |
| Component testing | Techniques | ThoughtWorks Radar vol. 31 / Adopt ring; Strong QA signal for UI-heavy or componentized repos. | Med |
| Visual regression testing tools | Tools | ThoughtWorks Radar vol. 31 / Adopt ring; QA for UI regressions; good for documentation/UX surfaces. | Med |
| Testcontainers | Languages & Frameworks | ThoughtWorks Radar vol. 31 / Adopt ring; Reliable integration tests for automation workflows. | Med |
| Supabase | Platforms | Found via YouTube research; Accelerate backend prototyping | Low |
| Agentic Experience | Techniques | Found via YouTube research; Prioritize building what agents want | Low |
| Agent Economy | Techniques | Found via YouTube research; Emerging market where agents choose tools/subscriptions and shape procurement | Med |
| Agent-Friendly Documentation | Techniques | Internal research; Agent-friendly documentation with examples and clear contracts so agents can quickly assess certainty and accuracy | Low |
| Resend Examples | Techniques | Inspired by Resend docs/examples; exploration of https://resend.com for operator-friendly docs and agent guidance | Low |
| Mintlify Exploration | Techniques | Inspired by Mintlify (https://www.mintlify.com/) to make developer docs more agent-friendly—focus on structured knowledge, contextual examples, and clear contracts that agents can parse and trust | Med |
| AgentMail Exploration | Techniques | Investigate AgentMail (https://www.agentmail.to/) to understand automated agent-to-agent communication and orchestration, then apply those patterns to streamline how our agents coordinate pilots and share outcomes | Med |
| DSPy Exploration | Tools | Study DSPy (https://dspy.ai/) for its agent-optimized SQL/BI assistant capabilities; evaluate how its data-product heuristics can augment our pilots with richer insights, faster discovery, and more explainable results | Med |
| Knowledge Graphs for Context Engineering | Techniques | Internal research; Use knowledge graphs to model the context engineering domain so agents can traverse relationships, reason about entities, and keep contexts immutable | Med |
| Ontology-aware Prompt Template | Techniques | Design prompt templates that reference the organization ontology explicitly so LLMs can extract entities, relationships, and constraints with fewer hallucinations | Low |
| Sensible Defaults for AI Agents | Techniques | Develop a playbook of sensible defaults for agent behavior (safety settings, retry logic, data handling) so pilots can rely on consistent base assumptions before customizing | Low |
| Neo4j AI Systems | Techniques | Inspired by Neo4j AI Systems use case page (https://neo4j.com/use-cases/ai-systems/) to study graph-backed AI systems, focusing on how knowledge graphs and causal relationships improve reasoning and provenance | Med |
| Neo4j LLM Knowledge Graph Builder | Tools | Investigate Neo4j's LLM Knowledge Graph Builder capabilities to seed knowledge graphs from LLM output, improving structured reasoning and traceability for agents | Med |
| Dynamic Prompt Formats (DSPy + BAML) | Techniques | Inspired by DSPy enhancements (BAML schemas, TOON payloads, Teleprompters) to shrink prompts, keep structured outputs, and keep token costs low while the optimizer maintains signature contracts. Study how DSPy’s adapters improve structured output performance for complex nested inputs to inform our pilot’s dynamic prompt flows | Low |
| 12 Factor Agents | Techniques | Apply a 12-factor-style checklist to agents (codebase, config, backing services, process, port binding, concurrency, disposability, dev/prod parity, logs, admin) so pilots can treat agents as first-class services with predictable behavior | Low |
| Structured Output for Agents | Techniques | Prioritize structured output schemas so agents emit predictable fields (status, references, metrics) that downstream readers and tooling can parse without guessing; this reduces hallucination and simplifies programmatic verification | Low |
| Compounding Engineering | Techniques | Explore compounding engineering practices where small, repeatable agent experiments (automation, instrumentation, prompts) accumulate value through reuse and feedback loops, enabling larger improvements without linear effort | Low |
| Organization Prompt Library | Techniques | Research organizational prompt libraries to catalog reusable prompts, guardrails, and post-processing hooks so agents confidently apply proven patterns and share improvements | Low |
| LLM as a Judge | Techniques | Based on vol. 33 Assess guidance; evaluate using LLM judges to automatically flag hallucinations, enforce guardrails, and surface confidence gaps before agents act | Low |

## Backlog (Trial / Assess)
- Structured output from LLMs (32: Assess, 33: Trial) - improves accuracy and validation.
- LLM as a judge (33: Assess) - quality control for agent outputs.
- AI-powered UI testing (32: Assess, 33: Assess) - QA automation.
- Model Context Protocol (MCP) (33: Trial) - aligns with radar ops automation.
- OpenTelemetry (32: Adopt) - observability for agent-driven workflows.
- Renovate (32: Adopt) - dependency hygiene.

## Current Selection
Starting with **Curated shared instructions for software teams** (vol. 33, Adopt) because it directly targets reliability, explainability, and agentic consistency while keeping effort low.
