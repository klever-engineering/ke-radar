#!/usr/bin/env python3
import json
import re
import subprocess
import urllib.request
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

VOLUMES = {
    "33": {
        "url": "https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2025/11/tr_technology_radar_vol_33_en.pdf",
        "ranges": {
            "Techniques": (1, 31),
            "Platforms": (32, 56),
            "Tools": (57, 84),
            "Languages and Frameworks": (85, 114),
        },
    },
    "32": {
        "url": "https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2025/04/tr_technology_radar_vol_32_en.pdf",
        "ranges": {
            "Techniques": (1, 22),
            "Platforms": (23, 50),
            "Tools": (51, 82),
            "Languages and Frameworks": (83, 105),
        },
    },
    "31": {
        "url": "https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2024/10/tr_technology_radar_vol_31_en.pdf",
        "ranges": {
            "Techniques": (1, 23),
            "Platforms": (24, 41),
            "Tools": (42, 74),
            "Languages and Frameworks": (75, 105),
        },
    },
}

RINGS = {"Adopt", "Trial", "Assess", "Hold"}
HEADINGS = {"The Radar", "Techniques", "Platforms", "Tools", "Languages and Frameworks"}


def download_pdf(volume: str, url: str) -> Path:
    pdf_path = DATA_DIR / f"tr_technology_radar_vol_{volume}_en.pdf"
    if not pdf_path.exists():
        urllib.request.urlretrieve(url, pdf_path)
    return pdf_path


def ensure_text(pdf_path: Path) -> Path:
    txt_path = pdf_path.with_suffix(".txt")
    if not txt_path.exists():
        subprocess.run(["pdftotext", str(pdf_path), str(txt_path)], check=True)
    return txt_path


def parse_items(text: str) -> list[dict]:
    items = []
    ring = None
    current = None

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line in RINGS:
            ring = line
            continue
        match = re.match(r"^(\d+)\.\s*(.*)$", line)
        if match:
            if current:
                items.append(current)
            number = int(match.group(1))
            name = match.group(2).strip()
            current = {"number": number, "name": name, "ring": ring}
            continue
        if current:
            if line in HEADINGS or line.startswith("©") or line == "—":
                items.append(current)
                current = None
                continue
            current["name"] = (current["name"] + " " + line).strip()

    if current:
        items.append(current)

    return items


def assign_quadrant(number: int, ranges: dict) -> str | None:
    for quadrant, (start, end) in ranges.items():
        if start <= number <= end:
            return quadrant
    return None


def main() -> None:
    all_items = []

    for volume, meta in VOLUMES.items():
        pdf_path = download_pdf(volume, meta["url"])
        txt_path = ensure_text(pdf_path)
        text = txt_path.read_text(encoding="utf-8", errors="replace")
        parsed = parse_items(text)
        seen = set()
        for item in parsed:
            number = item.get("number")
            ring = item.get("ring")
            if number is None or ring is None:
                continue
            if number in seen:
                continue
            quadrant = assign_quadrant(number, meta["ranges"])
            if not quadrant:
                continue
            seen.add(number)
            all_items.append(
                {
                    "volume": int(volume),
                    "number": number,
                    "name": item["name"].replace("  ", " ").strip(),
                    "ring": ring,
                    "quadrant": quadrant,
                }
            )

    output_path = DATA_DIR / "radar_blips.json"
    output_path.write_text(json.dumps(sorted(all_items, key=lambda x: (x["volume"], x["number"])), indent=2), encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
