#!/usr/bin/env python3
import argparse
from pathlib import Path


def build_pack(input_dir: Path) -> str:
    parts = []
    for path in sorted(input_dir.glob("*.md")):
        parts.append(path.read_text(encoding="utf-8").strip())
    return "\n\n".join(parts).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a curated instruction pack from markdown fragments.")
    parser.add_argument("--input", required=True, help="Folder containing *.md fragments")
    parser.add_argument("--output", required=True, help="Output file path")
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_path = Path(args.output)
    output_path.write_text(build_pack(input_dir), encoding="utf-8")


if __name__ == "__main__":
    main()
