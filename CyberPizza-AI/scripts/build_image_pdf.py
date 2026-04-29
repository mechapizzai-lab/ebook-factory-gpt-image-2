from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "output" / "pages_1600x2560"
OUTPUT = ROOT / "output" / "CyberPizza-AI-episode-1-image.pdf"


def main() -> None:
    image_paths = sorted(PAGES_DIR.glob("page_*.png"))
    if len(image_paths) != 10:
        raise SystemExit(f"Expected 10 normalized pages, found {len(image_paths)}")

    pages = []
    for path in image_paths:
        with Image.open(path) as img:
            pages.append(img.convert("RGB").copy())

    first, rest = pages[0], pages[1:]
    first.save(OUTPUT, "PDF", save_all=True, append_images=rest, resolution=300.0)
    print(OUTPUT)


if __name__ == "__main__":
    main()
