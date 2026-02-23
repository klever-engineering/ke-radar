#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import string
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Any
import urllib.request
import urllib.error
ROOT = Path(__file__).resolve().parent
CONFIG_DIR = ROOT / ".ke-radar"
CONFIG_PATH = CONFIG_DIR / "config.json"
ROADMAP_PATH = ROOT / "ROADMAP.md"
TEMPLATES_DIR = ROOT / "templates"
PILOTS_DIR = ROOT / "pilots"
BACKLOG_MARKER = "## Backlog"


def load_config() -> dict[str, Any]:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


def save_config(config: dict[str, Any]) -> None:
    CONFIG_DIR.mkdir(exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(config, indent=2), encoding="utf-8")


def ensure_api_key(config: dict[str, Any]) -> str:
    key = config.get("openai_api_key") or config.get("api_key")
    if not key:
        raise SystemExit("OpenAI API key missing. Run `ke-radar init` with `--api-key`.")
    return key


def parse_roadmap() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    raw_lines = ROADMAP_PATH.read_text(encoding="utf-8").splitlines()
    for line in raw_lines:
        trimmed = line.strip()
        if not trimmed.startswith("|") or "---" in trimmed:
            continue
        columns = [col.strip() for col in trimmed.strip("|").split("|")]
        if not columns or columns[0].lower() == "week":
            continue
        try:
            week = int(columns[0])
        except ValueError:
            continue
        rows.append(
            {
                "week": week,
                "technology": columns[1],
                "volume": columns[2] if len(columns) > 2 else "",
                "ring": columns[3] if len(columns) > 3 else "",
                "quadrant": columns[4] if len(columns) > 4 else "",
                "why": columns[5] if len(columns) > 5 else "",
                "effort": columns[6] if len(columns) > 6 else "",
            }
        )
    return rows


def add_roadmap_row(row: str) -> None:
    content = ROADMAP_PATH.read_text(encoding="utf-8")
    if BACKLOG_MARKER in content:
        insert_index = content.index(BACKLOG_MARKER)
        before = content[:insert_index].rstrip()
        after = content[insert_index:]
        new_content = f"{before}\n{row}\n\n{after.lstrip()}"
        ROADMAP_PATH.write_text(new_content, encoding="utf-8")
    else:
        with ROADMAP_PATH.open("a", encoding="utf-8") as out:
            out.write(f"{row}\n")


def slugify(text: str) -> str:
    trimmed = text.lower().strip()
    allowed = set(string.ascii_lowercase + string.digits + "-")
    slug = []
    for char in trimmed:
        if char in allowed:
            slug.append(char)
        elif char in string.whitespace:
            slug.append("-")
    slugified = "".join(slug)
    slugified = re.sub(r"-+", "-", slugified)
    return slugified.strip("-") or "pilot"


def create_pilot_scaffold(candidate: dict[str, Any]) -> Path:
    slug = slugify(candidate["technology"])
    dest = PILOTS_DIR / slug
    if dest.exists():
        raise SystemExit(f"Pilot directory already exists: {dest}")
    print("[1/5] Creating pilot directories")
    demo_dir = dest / "demo"
    eval_dir = dest / "eval"
    adr_dir = dest / "docs" / "adr"
    metrics_dir = dest / "metrics"
    for folder in (dest, demo_dir, eval_dir, adr_dir, metrics_dir):
        folder.mkdir(parents=True, exist_ok=True)
    print("[2/5] Copying templates")
    for template in ("pilot_plan.md", "experiment_report.md", "decision_memo.md"):
        src = TEMPLATES_DIR / template
        dst = dest / template
        if src.exists():
            shutil.copy(src, dst)
    metadata = {
        "technology": candidate["technology"],
        "week": candidate["week"],
        "ring": candidate["ring"],
        "quadrant": candidate["quadrant"],
        "why": candidate["why"],
        "effort": candidate["effort"],
    }
    (dest / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (demo_dir / "README.md").write_text(
        textwrap.dedent(
            f"""
            # Demo for {candidate['technology']}

            This folder holds the runnable sandbox described in the pilot plan.
            """
        ),
        encoding="utf-8",
    )
    (eval_dir / "README.md").write_text(
        textwrap.dedent(
            """
            # Evaluation artifacts

            Place scripts and metrics captured during the pilot here.
            """
        ),
        encoding="utf-8",
    )
    adr_template = adr_dir / f"adr-0000-{slug}.md"
    adr_template.write_text(
        textwrap.dedent(
            f"""
            # ADR - {candidate['technology']}

            ## Status
            Proposed

            ## Context
            Pilot for {candidate['technology']} ({candidate['why']})

            ## Decision
            To be written after experiment completes.
            """
        ),
        encoding="utf-8",
    )
    (metrics_dir / "run-log.md").write_text(
        textwrap.dedent(
            """
            # Metrics Run Log

            Record baseline and post-change measurements during the pilot.
            """
        ),
        encoding="utf-8",
    )
    print("[3/5] Metadata and supporting files created")
    print("[4/5] Pilot scaffolding ready")
    print(f"[5/5] Pilot available at {dest}")
    return dest


def pilot_command(args: argparse.Namespace) -> None:
    rows = parse_roadmap()
    if not rows:
        raise SystemExit("ROADMAPP entries not found.")
    if args.auto:
        suggestion = llm_suggest(rows, load_config())
        topic = suggestion.get("topic")
        print(f"Suggested topic: {topic}")
        candidate = next((row for row in rows if row["technology"] == topic), None)
        if not candidate:
            raise SystemExit("Suggested topic not found in roadmap.")
    elif args.topic:
        candidate = next((row for row in rows if row["technology"].lower() == args.topic.lower()), None)
        if not candidate:
            raise SystemExit(f"Topic not found: {args.topic}")
    elif args.week:
        candidate = next((row for row in rows if row["week"] == args.week), None)
        if not candidate:
            raise SystemExit(f"Week {args.week} not defined in roadmap.")
    else:
        print("Select a pilot to scaffold:")
        for idx, row in enumerate(rows, start=1):
            print(f"  {idx}. {row['technology']} (week {row['week']} | {row['ring']})")
        choice = input("Enter number: ").strip()
        if not choice.isdigit():
            raise SystemExit("Invalid selection")
        idx = int(choice) - 1
        if idx < 0 or idx >= len(rows):
            raise SystemExit("Selection out of range")
        candidate = rows[idx]
    print(f"Preparing pilot for {candidate['technology']}")
    create_pilot_scaffold(candidate)


def add_command(args: argparse.Namespace) -> None:
    rows = parse_roadmap()
    next_week = args.week or (max((row["week"] for row in rows), default=0) + 1)
    why = args.why or "TBD"
    row = f"| {next_week} | {args.topic} | {args.volume} | {args.ring} | {args.quadrant} | {why} | {args.effort} |"
    add_roadmap_row(row)
    print(f"Added {args.topic} as week {next_week} to the roadmap")


def suggest_command(args: argparse.Namespace) -> None:
    config = load_config()
    rows = parse_roadmap()
    if not rows:
        raise SystemExit("No roadmap entries to suggest from.")
    suggestion = llm_suggest(rows, config)
    print("Suggestion:")
    print(f"  Technology: {suggestion.get('topic')}")
    print(f"  Justification: {suggestion.get('reason')}")


def llm_suggest(options: list[dict[str, Any]], config: dict[str, Any]) -> dict[str, str]:
    api_key = ensure_api_key(config)
    prompt_lines = [
        "Evaluate the following candidate pilots for AE2.0 radar experimentation:",
    ]
    for opt in options:
        prompt_lines.append(
            f"- {opt['technology']} (Week {opt['week']}, Ring {opt['ring']}, Quadrant {opt['quadrant']}, Effort {opt['effort']}): {opt['why']}"
        )
    prompt_lines.append(
        "Prefer candidates that maximize predictable future revenue, increase adaptability and reliability, and improve agent experience. Return JSON {\"topic\": string, \"reason\": string}."
    )
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You suggest technology pilots prioritizing revenue, adaptability/reliability, and agent experience."},
            {"role": "user", "content": "\n".join(prompt_lines)},
        ],
        "temperature": 0.2,
    }
    try:
        response = call_openai(payload, api_key)
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"LLM request failed: {exc.read().decode()}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"Unable to reach OpenAI: {exc}")
    choices = response.get("choices") or []
    if not choices:
        return {"topic": options[0]["technology"], "reason": "No choices returned."}
    content = choices[0]["message"]["content"]
    try:
        parsed = json.loads(content)
        if isinstance(parsed, dict) and parsed.get("topic"):
            return parsed
    except json.JSONDecodeError:
        pass
    return {"topic": options[0]["technology"], "reason": content.strip()}


def call_openai(payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def init_command(args: argparse.Namespace) -> None:
    config = load_config()
    api_key = args.api_key or config.get("openai_api_key") or config.get("api_key")
    if not api_key:
        api_key = input("OpenAI API key: ").strip()
    config.update(
        {
            "openai_api_key": api_key,
            "initialized_at": datetime.utcnow().isoformat() + "Z",
            "repository": str(ROOT),
        }
    )
    save_config(config)
    print(f"Stored configuration at {CONFIG_PATH}")


def main() -> None:
    parser = argparse.ArgumentParser(description="ke-radar CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    init_parser = subparsers.add_parser("init", help="Initialize ke-radar in this repo")
    init_parser.add_argument("--api-key", help="OpenAI API key to use for suggestions")
    init_parser.set_defaults(func=init_command)
    add_parser = subparsers.add_parser("add", help="Add a candidate to the roadmap")
    add_parser.add_argument("topic", help="Technology name")
    add_parser.add_argument("--week", type=int, help="Week number override")
    add_parser.add_argument("--volume", default="33", help="ThoughtWorks Radar volume")
    add_parser.add_argument("--ring", default="Adopt", help="Ring label")
    add_parser.add_argument("--quadrant", default="Techniques", help="Quadrant section")
    add_parser.add_argument("--why", help="Why now?")
    add_parser.add_argument("--effort", default="Low", help="Effort estimate for the pilot")
    add_parser.set_defaults(func=add_command)
    pilot_parser = subparsers.add_parser("pilot", help="Scaffold a pilot from the roadmap")
    pilot_parser.add_argument("--topic", help="Technology to target")
    pilot_parser.add_argument("--week", type=int, help="Week number to match")
    pilot_parser.add_argument("--auto", action="store_true", help="Let the suggestion engine pick the pilot")
    pilot_parser.set_defaults(func=pilot_command)
    suggest_parser = subparsers.add_parser("suggest", help="Ask the LLM which roadmap candidate to try next")
    suggest_parser.set_defaults(func=suggest_command)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
