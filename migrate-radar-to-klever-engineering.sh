#!/bin/bash
# migrate-radar-to-klever-engineering.sh
# Executes the radar migration plan
# Run from AI Company root: ./radar/migrate-radar-to-klever-engineering.sh

set -e  # Exit on error

echo "=== Radar Migration to klever-engineering/ke-radar ==="
echo "Date: $(date +%Y-%m-%d)"
echo ""

# Configuration
KE_RADAR_PATH="${KE_RADAR_PATH:-$HOME/Projects/ke-radar}"
AI_COMPANY_PATH="$(pwd)"

echo "📍 AI Company path: $AI_COMPANY_PATH"
echo "📍 Target ke-radar path: $KE_RADAR_PATH"
echo ""

# Validate we're in ai-company root
if [ ! -d "radar" ]; then
    echo "❌ Error: Must run from AI Company root (radar/ directory not found)"
    exit 1
fi

echo "✅ Validated AI Company root"
echo ""

# === PHASE 1: Create ke-radar repository ===
echo "📦 PHASE 1: Creating ke-radar repository"
echo ""

if [ -d "$KE_RADAR_PATH" ]; then
    echo "⚠️  Warning: $KE_RADAR_PATH already exists"
    read -p "Delete and recreate? (y/N): " confirm
    if [ "$confirm" = "y" ]; then
        rm -rf "$KE_RADAR_PATH"
        echo "✅ Removed existing directory"
    else
        echo "❌ Aborted"
        exit 1
    fi
fi

mkdir -p "$KE_RADAR_PATH"
cd "$KE_RADAR_PATH"

echo "📝 Initializing git repository"
git init
git remote add origin git@github.com:klever-engineering/ke-radar.git

# Create directory structure
echo "📁 Creating directory structure"
mkdir -p templates scripts metrics documentation/experiments data pilots

# Copy generic content
echo "📋 Copying generic content from ai-company/radar"

# Templates (fully generic)
cp "$AI_COMPANY_PATH/radar/templates/"* templates/
echo "  ✅ Templates copied"

# Scripts
cp "$AI_COMPANY_PATH/radar/scripts/"*.py scripts/
echo "  ✅ Scripts copied"

# Metrics
cp "$AI_COMPANY_PATH/radar/metrics/metrics.md" metrics/
echo "  ✅ Metrics copied"

# Documentation
if [ -f "$AI_COMPANY_PATH/radar/documentation/anti-patterns.md" ]; then
    cp "$AI_COMPANY_PATH/radar/documentation/anti-patterns.md" documentation/
fi
if [ -d "$AI_COMPANY_PATH/radar/documentation/experiments" ]; then
    cp -r "$AI_COMPANY_PATH/radar/documentation/experiments" documentation/
fi
echo "  ✅ Documentation copied"

# Data (ThoughtWorks PDFs)
if [ -d "$AI_COMPANY_PATH/radar/data" ]; then
    cp -r "$AI_COMPANY_PATH/radar/data/"* data/ 2>/dev/null || true
    echo "  ✅ Data files copied"
fi

# Generic pilot (curated-shared-instructions as reference)
if [ -d "$AI_COMPANY_PATH/radar/pilots/curated-shared-instructions" ]; then
    cp -r "$AI_COMPANY_PATH/radar/pilots/curated-shared-instructions" pilots/
    echo "  ✅ Reference pilot copied"
fi

# Create generic README
cat > README.md << 'EOF'
# Klever Engineering Radar Framework

Generic technology surveillance framework based on ThoughtWorks Technology Radar methodology.

## Purpose

Provide reusable templates, scripts, and methodology for evaluating new technologies, tools, and practices across Klever Engineering projects.

## What's Included

- **templates/**: Reusable templates for pilot plans, experiment reports, decision memos, ADRs
- **scripts/**: Helper scripts for extracting and scoring radar blips
- **metrics/**: Metric definitions for evaluating technologies
- **documentation/**: Anti-patterns, experiment index, methodology guides
- **data/**: ThoughtWorks Technology Radar PDFs (volumes 31-33)
- **pilots/**: Generic reference pilots demonstrating the framework

## How to Use

1. Clone this repo alongside your project
2. Copy templates to your project's radar experiments
3. Use scripts to extract and prioritize technologies
4. Follow RUNBOOK.md for experiment execution
5. Create ADRs documenting decisions

## Integration Examples

- **AI Company**: Uses this framework under `/tools/radar/` with project-specific roadmap and SOP

## Source

Extracted from `aleph-engineering-gmbh/ai-company` radar program (2026-02-02).  
Generic methodology maintained here for reuse across Klever Engineering projects.

---

*Framework version: 1.0.0*  
*Last updated: 2026-02-02*
EOF

echo "  ✅ README.md created"

# Create METHODOLOGY.md
cat > METHODOLOGY.md << 'EOF'
# Radar Methodology

## Overview

Technology surveillance using ThoughtWorks Technology Radar as the input source, with structured experiments to validate adoption.

## Workflow

1. **Intake**: Identify technology from radar volumes 31-33
2. **Prioritization**: Score using rubric (strategic fit, pain relief, effort, ring)
3. **Pilot Design**: Create pilot plan with hypothesis, metrics, success criteria
4. **Execution**: Run sandboxed experiment
5. **Evaluation**: Measure against metrics, document learnings
6. **Decision**: Adopt, defer, or reject with ADR

## Scoring Rubric

- **Strategic fit (30%)**: Alignment with project goals
- **Pain relief (40%)**: Impact on current pain points
- **Effort (20%)**: Implementation complexity (inverted: lower effort scores higher)
- **Ring weight (10%)**: Adopt=5, Trial=3, Assess=1

## Success Criteria

Experiments must demonstrate:
- Measurable improvement (time_saved, accuracy, etc.)
- Low integration friction
- Clear operational path
- Documented learnings (success or failure)

## Failure Handling

Failed experiments are valuable. Document:
- What didn't work
- Why it didn't work
- Anti-patterns to avoid
- Alternative approaches to consider

---

*See RUNBOOK.md for step-by-step execution guide*
EOF

echo "  ✅ METHODOLOGY.md created"

# Copy RUNBOOK (generic parts)
if [ -f "$AI_COMPANY_PATH/radar/RUNBOOK.md" ]; then
    cp "$AI_COMPANY_PATH/radar/RUNBOOK.md" .
    echo "  ✅ RUNBOOK.md copied"
fi

# Initial commit
echo ""
echo "💾 Creating initial commit"
git add .
git commit -m "feat: initial radar framework extraction from ai-company

Generic radar methodology, templates, scripts, and reference pilot.

Source: aleph-engineering-gmbh/ai-company/radar/ (2026-02-02)
Extracted generic parts for reuse across Klever Engineering projects.

Includes:
- Templates for pilot plans, experiment reports, decision memos, ADRs
- Scripts for radar blip extraction and scoring
- Metrics framework
- ThoughtWorks Radar volumes 31-33 data
- Reference pilot: curated-shared-instructions

Framework version: 1.0.0"

echo "✅ Initial commit created"
echo ""
echo "📤 Ready to push to GitHub"
echo "   Run: cd $KE_RADAR_PATH && git push -u origin main"
echo ""

# === PHASE 2: Restructure AI Company ===
echo "🔄 PHASE 2: Restructuring AI Company"
echo ""

cd "$AI_COMPANY_PATH"

# Create tools/radar structure
echo "📁 Creating tools/radar/"
mkdir -p tools/radar

# Move AI Company specific files
echo "📋 Moving AI Company specific files"
mv radar/SOP-Technology-Surveillance.md tools/radar/
mv radar/ROADMAP.md tools/radar/
mv radar/AGENT_SPEC.md tools/radar/
mv radar/project-minutes.md tools/radar/
echo "  ✅ Files moved to tools/radar/"

# Create tools/radar/README.md
cat > tools/radar/README.md << 'EOF'
# Radar Tool Integration

AI Company uses the [klever-engineering/ke-radar](https://github.com/klever-engineering/ke-radar) framework for technology surveillance.

## Quick Start

1. Clone ke-radar alongside ai-company:
   ```bash
   cd ~/Projects
   git clone git@github.com:klever-engineering/ke-radar.git
   ```

2. Run radar workflow per `SOP-Technology-Surveillance.md`

3. Track AI Company specific roadmap in `ROADMAP.md`

4. Log sessions in `project-minutes.md`

## Structure

- **ke-radar repo**: Generic framework, templates, scripts, reference pilots
- **ai-company/tools/radar/**: AI Company specific roadmap, SOP, agent spec, session log
- **Experiment branches**: `radar-<technology>` branches in ai-company repo for specific tests

## Current Experiments

See `ROADMAP.md` for prioritized backlog.

## Integration Points

### Context Sources
- ThoughtWorks Radar data: `klever-engineering/ke-radar/data/`
- Radar roadmap: `tools/radar/ROADMAP.md`
- Experiment reports: Branch `radar-<technology>` specific

### Agents
- **radar_researcher**: Spec in `AGENT_SPEC.md`
- Queries ke-radar for candidates, tracks experiments, documents decisions

### SOPs
- Technology Surveillance SOP: `SOP-Technology-Surveillance.md`
- References ke-radar RUNBOOK for experiment execution

---

*Migrated from /radar/ on 2026-02-02*  
*Generic framework: klever-engineering/ke-radar*
EOF

echo "  ✅ tools/radar/README.md created"

# Remove old radar directory
echo ""
echo "🗑️  Removing old /radar/ directory"
read -p "Confirm removal of /radar/? (y/N): " confirm_delete
if [ "$confirm_delete" = "y" ]; then
    rm -rf radar/
    echo "✅ /radar/ removed"
else
    echo "⚠️  Kept /radar/ directory (manual cleanup needed)"
fi

echo ""
echo "✅ PHASE 2 Complete: AI Company restructured"
echo ""

# === Summary ===
echo "=== Migration Summary ==="
echo ""
echo "✅ ke-radar repository created at: $KE_RADAR_PATH"
echo "   - Generic templates, scripts, metrics, docs"
echo "   - ThoughtWorks Radar data"
echo "   - Reference pilot (curated-shared-instructions)"
echo ""
echo "✅ AI Company restructured:"
echo "   - /radar/ → /tools/radar/"
echo "   - AI Company specific: SOP, roadmap, agent spec, minutes"
echo ""
echo "📋 Next Steps:"
echo "   1. cd $KE_RADAR_PATH && git push -u origin main"
echo "   2. cd $AI_COMPANY_PATH && git add tools/radar/"
echo "   3. Update references in AGENTS.md, AGENTS-INSTRUCTIONS.md"
echo "   4. Git commit with refactor message"
echo "   5. Log decision in decision_log.db"
echo ""
echo "🎉 Migration ready for validation!"
