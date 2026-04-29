from __future__ import annotations

import html
import shutil
import zipfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "pages"
OUTPUT_DIR = ROOT / "output"
BUILD_DIR = OUTPUT_DIR / "epub_build"
NORMALIZED_DIR = OUTPUT_DIR / "pages_1600x2560"

TITLE = "CyberPizza AI"
AUTHOR = "MechaPizzAI Lab"
LANGUAGE = "fr"
WIDTH = 1600
HEIGHT = 2560


def normalize_images() -> list[Path]:
    NORMALIZED_DIR.mkdir(parents=True, exist_ok=True)
    output_paths: list[Path] = []

    for source in sorted(PAGES_DIR.glob("page_*.png")):
        target = NORMALIZED_DIR / source.name
        with Image.open(source) as image:
            image = image.convert("RGB")
            resized = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
            resized.save(target, "PNG", optimize=True)
        output_paths.append(target)

    return output_paths


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build_epub(images: list[Path]) -> Path:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    (BUILD_DIR / "META-INF").mkdir(parents=True)
    (BUILD_DIR / "OEBPS" / "images").mkdir(parents=True)
    (BUILD_DIR / "OEBPS" / "text").mkdir(parents=True)

    write_text(BUILD_DIR / "mimetype", "application/epub+zip")
    write_text(
        BUILD_DIR / "META-INF" / "container.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
""",
    )

    manifest_items = []
    spine_items = []
    nav_items = []

    for index, image_path in enumerate(images, start=1):
        image_name = image_path.name
        page_id = f"page_{index:03d}"
        xhtml_name = f"{page_id}.xhtml"
        shutil.copy2(image_path, BUILD_DIR / "OEBPS" / "images" / image_name)

        write_text(
            BUILD_DIR / "OEBPS" / "text" / xhtml_name,
            f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="{LANGUAGE}" xml:lang="{LANGUAGE}">
<head>
  <title>{html.escape(TITLE)} - Page {index}</title>
  <meta name="viewport" content="width={WIDTH}, height={HEIGHT}"/>
  <style>
    html, body {{
      margin: 0;
      padding: 0;
      width: {WIDTH}px;
      height: {HEIGHT}px;
      background: #000;
    }}
    img {{
      display: block;
      width: {WIDTH}px;
      height: {HEIGHT}px;
    }}
  </style>
</head>
<body>
  <img src="../images/{html.escape(image_name)}" alt="Page {index}"/>
</body>
</html>
""",
        )

        manifest_items.append(
            f'    <item id="{page_id}" href="text/{xhtml_name}" media-type="application/xhtml+xml"/>'
        )
        manifest_items.append(
            f'    <item id="{page_id}_img" href="images/{image_name}" media-type="image/png"/>'
        )
        spine_items.append(f'    <itemref idref="{page_id}"/>')
        nav_items.append(f'      <li><a href="text/{xhtml_name}">Page {index}</a></li>')

    write_text(
        BUILD_DIR / "OEBPS" / "nav.xhtml",
        f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{LANGUAGE}">
<head><title>Navigation</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>{html.escape(TITLE)}</h1>
    <ol>
{chr(10).join(nav_items)}
    </ol>
  </nav>
</body>
</html>
""",
    )

    write_text(
        BUILD_DIR / "OEBPS" / "content.opf",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:cyberpizza-ai-episode-1</dc:identifier>
    <dc:title>{html.escape(TITLE)}</dc:title>
    <dc:creator>{html.escape(AUTHOR)}</dc:creator>
    <dc:language>{LANGUAGE}</dc:language>
    <dc:publisher>MechaPizzAI Lab</dc:publisher>
    <meta property="rendition:layout">pre-paginated</meta>
    <meta property="rendition:orientation">portrait</meta>
    <meta property="rendition:spread">none</meta>
    <meta name="cover" content="page_001_img"/>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
{chr(10).join(manifest_items)}
  </manifest>
  <spine page-progression-direction="ltr">
{chr(10).join(spine_items)}
  </spine>
</package>
""",
    )

    epub_path = OUTPUT_DIR / "CyberPizza-AI-episode-1.epub"
    if epub_path.exists():
        epub_path.unlink()

    with zipfile.ZipFile(epub_path, "w") as epub:
        epub.write(BUILD_DIR / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(BUILD_DIR.rglob("*")):
            if path.is_file() and path.name != "mimetype":
                epub.write(path, path.relative_to(BUILD_DIR).as_posix(), compress_type=zipfile.ZIP_DEFLATED)

    return epub_path


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    images = normalize_images()
    if len(images) != 10:
        raise SystemExit(f"Expected 10 pages, found {len(images)}")
    epub_path = build_epub(images)
    print(epub_path)


if __name__ == "__main__":
    main()
