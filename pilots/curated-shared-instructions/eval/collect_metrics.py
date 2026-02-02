#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = [
    "ROLE:",
    "GOAL:",
    "OUTPUTS:",
    "CONSTRAINTS:",
    "METRICS:",
    "EXECUTION FLOW:",
]

EXPLAINABILITY_MARKERS = [
    "RATIONALE:",
    "REFERENCES:",
    "EVIDENCE:",
    "ASSUMPTIONS:",
    "STRUCTURED OUTPUT:",
]


def scan_pack(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    present = set()
    for marker in REQUIRED_FIELDS + EXPLAINABILITY_MARKERS:
        if marker in text:
            present.add(marker)
    return present


def build_payload(present: set[str], minutes: float) -> dict:
    required = [marker for marker in REQUIRED_FIELDS]
    present_required = [marker for marker in required if marker in present]
    explainability_score = sum(1 for marker in EXPLAINABILITY_MARKERS if marker in present)
    return {
        "required_fields": required,
        "present_fields": present_required,
        "time_minutes": minutes,
        "explainability_score": explainability_score,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect baseline/post metrics from instruction packs.")
    parser.add_argument("--baseline", required=True, help="Baseline pack text")
    parser.add_argument("--post", required=True, help="Post-change pack text")
    parser.add_argument("--baseline-minutes", type=float, required=True)
    parser.add_argument("--post-minutes", type=float, required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    baseline_present = scan_pack(Path(args.baseline))
    post_present = scan_pack(Path(args.post))

    baseline_payload = build_payload(baseline_present, args.baseline_minutes)
    post_payload = build_payload(post_present, args.post_minutes)

    (out_dir / "baseline.json").write_text(json.dumps(baseline_payload, indent=2), encoding="utf-8")
    (out_dir / "post.json").write_text(json.dumps(post_payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
