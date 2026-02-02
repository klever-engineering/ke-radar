# Migration Plan: Radar Generic Parts → klever-engineering/ke-radar

## Date: 2026-02-02

## Owner: CTO

---

## Objective

Separate **generic radar methodology** (goes to `klever-engineering/ke-radar`) from AE **AI Company specific implementations** (stays in `ai-company`).

This allows:

- Generic radar framework to be reusable across Klever Engineering projects
- AI Company to consume radar as a tool under `/tools/`
- Specific AI Company radar experiments to live in branches of AI Company repos
- Generic pilots to stay in `ke-radar` as reference implementations

---

## Repository Structure

### klever-engineering/ke-radar (NEW - Generic Framework)

```
ke-radar/
├── README.md                          # Framework overview
├── METHODOLOGY.md                     # How radar surveillance works
├── RUNBOOK.md                         # Generic experiment execution guide
├── templates/                         # Reusable templates
│   ├── pilot_plan.md
│   ├── experiment_report.md
│   ├── decision_memo.md
│   └── adr-0000-template.md
├── scripts/                           # Generic scripts
│   ├── extract_radar_blips.py        # Parse ThoughtWorks PDFs
│   └── score_technology.py           # Scoring rubric calculator
├── metrics/                           # Metric definitions
│   └── metrics.md
├── documentation/                     # Generic documentation
│   ├── anti-patterns.md
│   └── experiments/
│       └── index.md
├── data/                              # ThoughtWorks Radar PDFs (vols 31-33)
│   ├── tw-radar-vol-31.pdf
│   ├── tw-radar-vol-32.pdf
│   └── tw-radar-vol-33.pdf
└── pilots/                            # Generic reference pilots
    └── curated-shared-instructions/   # Example pilot (generic)
        ├── pilot_plan.md
        ├── experiment_report.md
        ├── decision_memo.md
        ├── docs/adr/
        ├── demo/
        └── eval/
```

### AI Company (AFTER migration - Radar as Tool)

```
ai-company/
├── playbooks/
│   └── companies/
│       └── aleph-engineering/
│           └── ae2.0/
│               └── 07.production/
│                   └── regular-operations/
│                       └── SOP-Technology-Surveillance.md  # Production SOP
├── tools/
│   └── ke-radar/                      # Full clone of ke-radar (work here, push upstream)
│       ├── README.md
│       ├── METHODOLOGY.md
│       ├── RUNBOOK.md
│       ├── ROADMAP.md                 # AI Company roadmap (push to ke-radar)
│       ├── AGENT_SPEC.md
│       ├── project-minutes.md         # AI Company session log
│       ├── templates/
│       ├── scripts/
│       ├── metrics/
│       ├── documentation/
│       ├── data/
│       └── pilots/
└── shared-instructions/               # AI Company curated instructions (pilot result)
    ├── base.md
    ├── areas/
    └── agents/
```

---

## Migration Steps

### Phase 1: Create ke-radar Repository with ALL Content

**Action**: Create `klever-engineering/ke-radar` with complete radar content

**Files to migrate** (ALL files from `ai-company/radar/` → `ke-radar/`):

```bash
# Everything goes to ke-radar
radar/README.md → ke-radar/README.md
radar/METHODOLOGY.md → ke-radar/METHODOLOGY.md (create from RUNBOOK)
radar/RUNBOOK.md → ke-radar/RUNBOOK.md
radar/ROADMAP.md → ke-radar/ROADMAP.md
radar/AGENT_SPEC.md → ke-radar/AGENT_SPEC.md
radar/project-minutes.md → ke-radar/project-minutes.md
radar/SOP-Technology-Surveillance.md → ke-radar/SOP-Technology-Surveillance.md (generic version)
radar/templates/ → ke-radar/templates/
radar/scripts/ → ke-radar/scripts/
radar/metrics/ → ke-radar/metrics/
radar/documentation/ → ke-radar/documentation/
radar/data/ → ke-radar/data/
radar/pilots/ → ke-radar/pilots/
```

**Commands**:

```bash
# Create ke-radar with ALL content
mkdir -p /media/alian/DATA/Projects/ke/ke-radar
cd /media/alian/DATA/Projects/ke/ke-radar
git init
git remote add origin git@github.com:klever-engineering/ke-radar.git

# Copy everything from ai-company/radar
cp -r /media/alian/DATA/Projects/AI-Company/radar/* .

# Initial commit
git add .
git commit -m "feat: initial radar framework

Complete technology surveillance framework based on ThoughtWorks Radar.
Source: ai-company/radar/ (2026-02-02)"

git push -u origin main
```

### Phase 2: Clone ke-radar into AI Company /tools/ke-radar/

**Action**: Replace `/radar/` with clone of `ke-radar`

```bash
cd /path/to/ai-company

# Remove old radar directory
rm -rf radar/

# Clone ke-radar into tools/ke-radar
git clone git@github.com:klever-engineering/ke-radar.git tools/ke-radar

# Work in tools/ke-radar, push changes upstream to ke-radar
cd tools/ke-radar
git remote -v  # Should show origin -> klever-engineering/ke-radar
```

### Phase 3: Move SOP to Playbooks (Production Operations)

**Action**: Extract SOP to AE2.0 Production Regular Operations

```bash
cd /path/to/ai-company

# Copy SOP to playbooks
cp tools/ke-radar/SOP-Technology-Surveillance.md \
   playbooks/companies/aleph-engineering/ae2.0/07.production/regular-operations/SOP-Technology-Surveillance.md

# Update SOP header with playbook metadata
# (edit file to add SOP number, owner, etc.)
```

### Phase 4: Update References

**Files to update**:

1. `/AGENTS.md` - Update radar references:

   - `/radar/` → `/tools/ke-radar/`
   - Reference SOP at playbooks location (`07.production/regular-operations/`)
2. `/agentic-context/AGENTS-INSTRUCTIONS.md` - Update source paths:

   - Radar source: `/tools/ke-radar/data/`
   - Radar roadmap: `/tools/ke-radar/ROADMAP.md`
3. Any other files referencing `/radar/`

---

## Branching Strategy

### Generic Pilots (in ke-radar)

- Live on `main` branch as reference implementations
- Example: `pilots/curated-shared-instructions/`

### AI Company Specific Experiments (in ai-company)

- Live on branches named `radar-<technology>`
- Example: `radar-model-context-protocol`, `radar-structured-llm-output`
- Merge to `main` only after CTO approval and ADR documentation

---

## Validation Checklist

After migration:

- [ ] `klever-engineering/ke-radar` repo created and pushed
- [ ] Generic templates, scripts, metrics, docs in ke-radar
- [ ] ThoughtWorks PDFs in ke-radar/data/
- [ ] Reference pilot (curated-shared-instructions) in ke-radar/pilots/
- [ ] AI Company `/radar/` removed
- [ ] AI Company `/tools/ke-radar/` cloned from ke-radar
- [ ] SOP moved to `/playbooks/.../07.production/regular-operations/`
- [ ] AI Company `/shared-instructions/` documented as pilot result
- [ ] All references updated (AGENTS.md, AGENTS-INSTRUCTIONS.md, notebooklm docs)
- [ ] tools/ke-radar/README.md explains integration
- [ ] Decision log entry for this refactoring

---

## Timeline

**Estimated duration**: 2-3 hours

**Sequence**:

1. Create ke-radar content (1 hour)
2. Push to GitHub (5 min)
3. Restructure ai-company (30 min)
4. Update references (30 min)
5. Validate and document (30 min)

---

## Rollback Plan

If issues arise:

1. Restore `/radar/` from git history: `git checkout HEAD~1 -- radar/`
2. Delete `/tools/ke-radar/`: `rm -rf tools/ke-radar/`
3. Keep ke-radar as-is (can be used for future extraction)

---

## Benefits

**For Klever Engineering**:

- Reusable radar framework across all projects
- Generic pilots as learning resources
- Consistent technology evaluation methodology

**For AI Company**:

- Cleaner separation of concerns (framework vs usage)
- Radar becomes a tool, not a project
- Specific experiments isolated in branches
- Shared instructions benefit is preserved

---

*Migration plan prepared: 2026-02-02*
*Execute: Pending CTO approval*
