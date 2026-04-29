from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config" / "project_config.json").read_text(encoding="utf-8"))
RECIPES = json.loads((ROOT / "recipes" / "cocktails.json").read_text(encoding="utf-8"))
PROMPTS = ROOT / "prompts"


STYLE = CONFIG["style_anchor"]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")


def recipe_prompt(index: int, recipe: dict) -> str:
    ingredients = "\n".join(f"- {item}" for item in recipe["ingredients"])
    steps = "\n".join(f"{i}. {step}" for i, step in enumerate(recipe["steps"], start=1))
    page_number = index + 2

    step_count = len(recipe["steps"])

    return f"""
{STYLE}

This is page {page_number} of a visual cocktail recipe book. The image IS the entire book page.
Page dimensions: 1600x2560 pixels.
All text must be in French.

PAGE CONTENT:
A gorgeous but achievable cocktail recipe page for "{recipe['name']}".
The cocktail must look delicious, iconic, and easy to make at home.
Hero photo: {recipe['visual']}.
Use the same visual system as every recipe: large hero cocktail image, clean ingredient block, visual step-by-step strip, small easy tip badge, elegant page number.
The page must visually show exactly how to make the cocktail with {step_count} clear illustrated step panels, one panel per method step.
If a step contains several gestures, split the visual inside that same panel into small sub-actions so nothing important is skipped.
The reader must understand the recipe by looking at the images, even before reading the text.

TEXT TO RENDER EXACTLY:
Title: "{recipe['name']}"
Tagline: "{recipe['tagline']}"
Verre: "{recipe['glass']}"

INGREDIENTS
{ingredients}

METHODE
{steps}

GARNITURE
{recipe['garnish']}

ASTUCE FACILE
{recipe['easy_tip']}

Page number: "{page_number}"

LAYOUT:
Top: recipe title, tagline, glass type, and a large appetizing finished cocktail hero image.
Middle: clean "INGREDIENTS" panel with all ingredients.
Lower half: {step_count} numbered visual step panels, each with a concrete instructional illustration and the matching method sentence. For complex gestures, show mini sub-actions inside the panel.
Bottom: "GARNITURE" and "ASTUCE FACILE" as small highlighted notes.
Typography must be large, readable, and consistent across pages.
No clutter, no tiny text, no watermark, no extra logos. Every step illustration must be concrete and instructional, not decorative.
"""


def main() -> None:
    toc_lines = "\n".join(f"{i + 3:02d}. {recipe['name']}" for i, recipe in enumerate(RECIPES))

    write(
        PROMPTS / "page_001_cover.txt",
        f"""
{STYLE}

This is the front cover of a visual cocktail recipe book. The image IS the entire page.
Page dimensions: 1600x2560 pixels.
All text must be in French.

PAGE CONTENT:
A super stylish cover showing a premium arrangement of iconic cocktails on a sleek modern bar: Mojito, Margarita, Negroni, Espresso Martini, Piña Colada, Aperol Spritz, Old Fashioned, and French 75. Bright appetizing drinks, fresh garnishes, condensation, glossy glassware, warm highlights, deep contrast. It must feel premium but accessible, like anyone can make these at home.

TEXT TO RENDER EXACTLY:
Title: "Cocktails Iconiques"
Subtitle: "20 recettes belles, faciles et inratables"
Author: "MechaPizzAI Lab"
Small note: "À consommer avec modération"

LAYOUT:
Large elegant title at the top, readable from a thumbnail. Cocktail arrangement in the center with vibrant colors. Subtitle below title. Author near bottom. Small moderation note at bottom edge. No watermark, no extra logos.
""",
    )

    write(
        PROMPTS / "page_002_sommaire.txt",
        f"""
{STYLE}

This is the table of contents page of a visual cocktail recipe book. The image IS the entire page.
Page dimensions: 1600x2560 pixels.
All text must be in French.

PAGE CONTENT:
Elegant sommaire page with a clean premium cocktail menu feeling. Background: softly lit modern bar, subtle silhouettes of colorful cocktails, fresh citrus, mint, ice, and bar tools. Keep text area clean and highly readable.

TEXT TO RENDER EXACTLY:
SOMMAIRE

{toc_lines}

Note: "Des recettes simples, belles et faisables à la maison."
Page number: "2"

LAYOUT:
Title "SOMMAIRE" at top. Two neat columns for the 20 cocktail names. Small note at bottom. Typography elegant, high contrast, large enough to read. No clutter, no watermark, no extra logos.
""",
    )

    for i, recipe in enumerate(RECIPES, start=1):
        page = i + 2
        write(PROMPTS / f"page_{page:03d}_{recipe['id']}.txt", recipe_prompt(i, recipe))


if __name__ == "__main__":
    main()
