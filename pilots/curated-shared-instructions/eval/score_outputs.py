#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def score_accuracy(output: dict) -> float:
    required = output.get("required_fields", [])
    present = output.get("present_fields", [])
    if not required:
        return 0.0
    hits = len([field for field in required if field in present])
    return hits / len(required)


def main() -> None:
    parser = argparse.ArgumentParser(description="Score baseline vs post outputs for the curated instructions pilot.")
    parser.add_argument("--baseline", required=True, help="Baseline JSON output")
    parser.add_argument("--post", required=True, help="Post-change JSON output")
    args = parser.parse_args()

    baseline = load_json(Path(args.baseline))
    post = load_json(Path(args.post))

    baseline_accuracy = score_accuracy(baseline)
    post_accuracy = score_accuracy(post)

    baseline_explain = float(baseline.get("explainability_score", 0))
    post_explain = float(post.get("explainability_score", 0))

    baseline_time = float(baseline.get("time_minutes", 0))
    post_time = float(post.get("time_minutes", 0))

    result = {
        "time_saved": max(baseline_time - post_time, 0),
        "accuracy_baseline": baseline_accuracy,
        "accuracy_post": post_accuracy,
        "explainability_baseline": baseline_explain,
        "explainability_post": post_explain,
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
