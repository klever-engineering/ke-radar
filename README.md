# KE Radar - Technology Evaluation Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A structured framework for evaluating emerging technologies, tools, and practices through systematic pilots and experiments. KE Radar provides templates, workflows, and metrics to help teams make evidence-based technology adoption decisions.

## 🎯 Purpose

KE Radar enables organizations to:

- **Discover** technology candidates from various sources (ThoughtWorks Radar, industry trends, team proposals)
- **Evaluate** them using structured pilots with clear success criteria
- **Decide** on adoption with documented evidence and metrics
- **Track** results through standardized templates and workflows

This framework is technology-agnostic - use it to evaluate any tool, practice, or platform regardless of source.

## 🔬 What Makes This Different

Instead of relying on secondhand recommendations, KE Radar helps you:

- Run **hands-on pilots** with your actual use cases
- Collect **quantified metrics** (not just opinions)
- Document **decisions with rationale** (Architecture Decision Records)
- Build **institutional knowledge** through experiment reports

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/klever-engineering/ke-radar.git
cd ke-radar
```

### 2. Review the Roadmap

Check [`ROADMAP.md`](ROADMAP.md) for queued technology candidates and experiment priorities.

### 3. Run Your First Evaluation

Follow the [`RUNBOOK.md`](RUNBOOK.md) workflow:

1. **Plan**: Copy `templates/pilot_plan.md` → `pilots/<technology>/pilot_plan.md`
2. **Define**: Set scope, hypothesis, and success criteria
3. **Build**: Create proof-of-concept demo
4. **Evaluate**: Measure results against rubric
5. **Decide**: Document with ADR

### 4. Use the Templates

Located in [`templates/`](templates/):

- **`pilot_plan.md`** - Experiment definition and planning
- **`experiment_report.md`** - Results documentation
- **`decision_memo.md`** - Executive summary
- **`adr-0000-template.md`** - Architecture Decision Record

## 📁 Repository Structure

```
ke-radar/
├── README.md                   # This file
├── ROADMAP.md                  # Prioritized evaluation queue
├── RUNBOOK.md                  # Experiment execution workflow
├── SOP-Technology-Surveillance.md  # Standard Operating Procedure
├── templates/                  # Reusable templates
│   ├── pilot_plan.md
│   ├── experiment_report.md
│   ├── decision_memo.md
│   └── adr-0000-template.md
├── pilots/                     # Technology evaluations
│   └── <technology-name>/
│       ├── pilot_plan.md
│       ├── experiment_report.md
│       ├── decision_memo.md
│       ├── demo/               # Proof of concept code
│       ├── eval/               # Evaluation scripts
│       └── docs/adr/           # Architecture Decision Records
├── scripts/                    # Automation helpers
├── metrics/                    # Scoring rubrics and definitions
├── documentation/              # Guides and learnings
└── data/                       # Source materials (e.g., ThoughtWorks Radar PDFs)
```

## 🔬 Example Pilot: Curated Shared Instructions

See [`pilots/curated-shared-instructions/`](pilots/curated-shared-instructions/) for a complete reference implementation:

- **Pilot Plan**: Problem definition, hypothesis, success criteria
- **Demo**: Working proof-of-concept with instruction pack builder
- **Evaluation**: Metrics collection and scoring rubrics
- **ADR**: Final decision documentation with rationale
- **Results**: Quantified improvements (accuracy, consistency, traceability)

## 📊 Evaluation Framework

Each technology goes through five phases:

1. **Discovery** - Identify candidate technology
2. **Planning** - Define experiment scope and metrics
3. **Experimentation** - Build demo, collect data
4. **Evaluation** - Score against rubric, measure impact
5. **Decision** - Document with ADR, recommend action (Adopt/Trial/Assess/Hold)

See [`metrics/metrics.md`](metrics/metrics.md) for scoring methodology.

## 🎓 Decision Framework

We use a simplified adoption ladder:

- **Adopt**: Proven through pilot, ready for production
- **Trial**: Promising results, continue with broader pilot
- **Assess**: Needs more research or different use case
- **Hold**: Not recommended based on pilot results

## 🗺️ Technology Sources

This framework is source-agnostic. Technology candidates can come from:

- **ThoughtWorks Technology Radar** (volumes 31-33 PDFs in `data/`)
- **Industry publications** and conferences
- **Team proposals** and pain points
- **Vendor evaluations** and RFPs
- **Open source trends** and GitHub activity

Parse ThoughtWorks Radar with: `python scripts/extract_radar_blips.py`

## 🤝 Contributing

We welcome contributions! Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for:

- How to propose new technology evaluations
- Pilot contribution guidelines
- Code of conduct
- Pull request process

## 📋 Workflow

The standard workflow is documented in [`SOP-Technology-Surveillance.md`](SOP-Technology-Surveillance.md):

1. **Intake**: Add technology to roadmap with prioritization
2. **Branch**: Create `radar-<technology>` branch
3. **Execute**: Follow RUNBOOK workflow
4. **Review**: Present findings to stakeholders
5. **Decide**: Create ADR with recommendation
6. **Merge**: Only after approval (see branching conventions)

## 🔍 Branching Convention

All pilot work lives on branches named `radar-<technology>`. 

- Rebase regularly to `main`
- Do not merge to `main` without stakeholder approval
- Each branch contains one complete pilot (plan → demo → eval → decision)

## 🤖 Usage with AI Coding Agents

**KE Radar is designed for AI-assisted pilot execution.** The structured templates, runbooks, and specifications enable coding agents (GitHub Copilot, Claude Code, Codex) to autonomously create and run technology evaluations.

### Agent-Driven Workflow

Instead of manually creating pilots, use natural language prompts:

```
"Test the next technology from the radar roadmap"
"Prepare the next pilot according to ROADMAP.md"
"Run the pilot for <technology-name>"
"Create evaluation report for the current pilot"
"Generate decision memo based on pilot results"
"Scan the codebase and propose relevant technologies to evaluate"
```

### Codebase-Driven Technology Discovery

**Agents can analyze your project to suggest relevant pilots:**

Ask the agent to scan your codebase and propose technologies based on actual needs:

```
"Analyze the codebase and suggest technologies from the radar that would address current pain points"
"Review our architecture and propose relevant pilots from ROADMAP.md"
"Identify technical debt areas and recommend technologies to evaluate"
```

**How it works:**

1. Agent scans project structure, dependencies, patterns, and pain points
2. Agent correlates findings with technologies in `ROADMAP.md` and radar sources
3. Agent prioritizes suggestions based on:
   - **Relevance**: Technologies that address discovered issues
   - **Impact**: Potential improvements to quality, velocity, or maintainability
   - **Feasibility**: Compatibility with existing stack and team skills
4. Agent generates prioritized queue with rationale linking each technology to specific codebase findings

**Result**: Pilots become context-aware and directly relevant to your project's actual needs, not generic recommendations.

### How Agents Work with KE Radar

1. **Agent reads context**: Consults `RUNBOOK.md`, `AGENT_SPEC.md`, `ROADMAP.md`, and templates
2. **Agent creates structure**: Creates `radar-<technology>` branch with complete pilot scaffolding
3. **Agent executes pilot**: Follows five-phase workflow (Discovery → Planning → Experimentation → Evaluation → Decision)
4. **Agent generates artifacts**: Produces pilot plans, experiment logs, ADRs, evaluation reports using standard templates
5. **Human reviews and approves**: You validate results before merging to `main`

### Prerequisites for Agent Use

Agents rely on these framework components:

- **`RUNBOOK.md`**: Step-by-step pilot execution procedures
- **`AGENT_SPEC.md`**: Agent persona, capabilities, constraints
- **`templates/`**: Standardized formats for all artifacts
- **`ROADMAP.md`**: Prioritized technology backlog
- **`metrics/`**: Quantified success criteria and scoring rubrics

**Benefits**: Rapid experimentation velocity while maintaining governance through templates, review gates, and documented decision criteria.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar) for inspiring structured technology evaluation
- All contributors who have shared experiment learnings

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/klever-engineering/ke-radar/issues)
- **Discussions**: [GitHub Discussions](https://github.com/klever-engineering/ke-radar/discussions)

## 🗺️ Current Roadmap

See [`ROADMAP.md`](ROADMAP.md) for evaluation queue:

1. Model Context Protocol (MCP)
2. Structured LLM Output
3. Agentic Tool Use
4. LLM Context Management
5. And more...

---

**Start evaluating technologies with evidence, not hype!** 🚀
