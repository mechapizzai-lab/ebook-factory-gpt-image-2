---
name: ebook-factory
description: >
  Generate complete visual ebooks where EVERY page is a full-page AI-generated image
  (cookbooks, manga, picture books, visual guides). All text (titles, ingredients,
  instructions, page numbers, table of contents) is rendered INSIDE the images by
  GPT Image 2 — there is zero HTML text in the final book. Uses Calibre for
  professional KDP formatting. Output language is French by default.
  Use when the user wants to create a visual book, illustrated ebook, manga, comic,
  picture book, cookbook, children's book, or any book where images ARE the pages.
  Triggers on: "create a book", "make an ebook", "generate a cookbook", "manga",
  "picture book", "illustrated book", "visual book", "livre de recettes",
  "bande dessinée", "livre illustré".
  Do NOT use for text-only books, academic papers, or documentation.
---

# Ebook Factory — AI Visual Book Generator

Generate complete ebooks where **every single page is a full-page image** generated
by AI. All text content (titles, body text, ingredients, instructions, table of
contents, page numbers) is rendered directly inside the images by GPT Image 2.
The final book is an assembly of full-page images formatted via Calibre for
Amazon KDP. Output language is **French** by default.

## Core principle — FULL-IMAGE PAGES

**CRITICAL**: This skill produces books where every page — including the cover,
table of contents, section dividers, content pages, and back cover — is a single
full-page image. There is NO separate HTML text layer. All text that appears in
the book is part of the image itself, rendered by GPT Image 2.

This means:
- Every image prompt MUST include the exact text to render on that page
- Text must be in the correct language (French by default)
- Typography, layout, and text placement are controlled via the image prompt
- The EPUB/PDF is essentially a fixed-layout image album
- GPT Image 2's strong text rendering capability is essential for this workflow

## Overview

This skill orchestrates a multi-phase pipeline:
1. **Analyze** the user's request and select a book template
2. **Prototype** a sample page, cover, and table of contents for validation
3. **Iterate** based on user feedback until approved
4. **Produce** all pages as full-page images with consistent style
5. **Export** via Calibre to fixed-layout KDP-ready formats

## Supported book types

| Type | Template | Typical pages | Key features |
|------|----------|---------------|--------------|
| Cookbook / Recipe book | `templates/cookbook.md` | 30-80 | Recipe structure, ingredient lists, step photos |
| Manga / Comic | `templates/manga.md` | 20-60 | Panel layouts, speech bubbles, character consistency |
| Children's picture book | `templates/picturebook.md` | 16-32 | Full-page illustrations, minimal text, age-appropriate |
| Visual guide / How-to | `templates/visualguide.md` | 20-50 | Step-by-step photos, diagrams, annotations |
| Art book / Portfolio | `templates/artbook.md` | 24-48 | Full-bleed images, minimal text, gallery layout |

## Dependencies

### Required
- Python 3.10+
- Calibre (`ebook-convert` CLI) — for format conversion and KDP export
- ebooklib — for fixed-layout EPUB assembly (images only)
- Pillow — for image validation, resizing, and DPI verification

### NOT needed (no HTML text layer)
- ~~Jinja2~~ — no text templating, all text is in images
- ~~BeautifulSoup4~~ — no HTML content processing

### Image generation
- **Codex**: uses built-in `image_gen` tool (no API key needed)
- **Claude Code**: requires `OPENAI_API_KEY` for GPT Image 2 via `scripts/generate_image.py`

### Setup
```bash
# Install Python dependencies
pip install ebooklib Pillow

# Install Calibre (macOS)
brew install calibre

# Install Calibre (Ubuntu/Debian)
sudo apt-get install calibre

# Install Calibre (Windows)
# Download from https://calibre-ebook.com/download
```

## Phase 1 — Analyze

When the user requests a book, extract these parameters:

```
Book type:     <cookbook | manga | picturebook | visualguide | artbook>
Theme:         <e.g., "Alsatian recipes", "space adventure", "garden flowers">
Visual style:  <e.g., "cartoon", "watercolor", "anime", "photorealistic", "minimalist">
Language:      <default: French — all text rendered in images must be in this language>
Page count:    <target, or "auto" to let template decide>
Format:        <KDP print | KDP ebook | both>  (default: both)
Dimensions:    <auto based on format, or user-specified>
Page size:     <auto from KDP format — all generated images must match this exact size>
```

### Language rule

ALL text rendered inside images MUST be in French by default (or the language
specified by the user). This includes:
- Cover title and subtitle
- Table of contents entries
- Section/chapter titles
- Recipe names, ingredient lists, instructions
- Story text, dialogue, captions
- Page numbers
- "Sommaire", "Table des matières", "Préparation", "Ingrédients", etc.

When writing image prompts, always specify:
`"All text in the image must be in French: [exact text to render]"`

### Page dimensions rule

Every generated image must have the EXACT same pixel dimensions, matching
the target book format. This ensures consistent assembly:

| Format | Image dimensions | Aspect ratio |
|--------|-----------------|--------------|
| KDP Ebook (Kindle) | 2560×1600px | 16:10 landscape |
| KDP Ebook (portrait) | 1600×2560px | 10:16 portrait |
| Print 6×9" (300 DPI) | 1800×2700px | 2:3 portrait |
| Print 8.5×11" (300 DPI) | 2550×3300px | ~3:4 portrait |

Store the chosen dimensions in `project_config.json` and use them for
EVERY image generation call.

### Content source decision

- If the user provides content (recipes, story, etc.): use it directly.
- If the user asks the agent to create content: research and generate it.
  - For recipes: search for authentic recipes, adapt and write original versions.
  - For stories: generate an original narrative arc.
  - For guides: research the topic and structure the content.
- If mixed: use provided content and fill gaps with generated content.

### Visual references system — Recurring characters, objects & locations

#### Detection

After analyzing the book request, determine if the book requires **recurring visual
elements** — characters, objects, or locations that must look consistent across
multiple pages. This is CRITICAL for:

| Book type | Recurring elements needed? | Typical references |
|-----------|--------------------------|-------------------|
| Manga / Comic | **YES — always** | Characters (protagonist, antagonist, secondary), key locations |
| Children's picture book | **YES — always** | Main character(s), pet/companion, home/setting |
| Cookbook | Sometimes | Recurring mascot/chef character, specific kitchen/setting |
| Visual guide | Rarely | Consistent objects being demonstrated |
| Art book | No | N/A |

#### User notification

If recurring visual elements are detected, the agent MUST notify the user
BEFORE proceeding to prototyping:

```
📎 Votre livre nécessite des éléments visuels récurrents pour garantir
la cohérence sur toutes les pages.

Veuillez placer vos images de référence dans le dossier :
  📁 project_dir/references/

Organisez-les comme suit :
  📁 references/
  ├── 📁 characters/          ← Personnages récurrents
  │   ├── hero_front.png      ← Vue de face du personnage principal
  │   ├── hero_side.png       ← Vue de profil
  │   ├── hero_expressions.png ← Planche d'expressions
  │   ├── villain.png          ← Antagoniste
  │   └── sidekick.png         ← Personnage secondaire
  ├── 📁 locations/            ← Lieux récurrents
  │   ├── home.png             ← Lieu principal
  │   ├── school.png           ← Lieu secondaire
  │   └── forest.png           ← Autre lieu
  └── 📁 objects/              ← Objets récurrents
      ├── magic_sword.png      ← Objet clé
      └── vehicle.png          ← Véhicule

📌 Conseils pour les images de référence :
  - Fond blanc ou uni de préférence
  - Plusieurs angles si possible (face, profil, dos)
  - Résolution minimum 512×512px
  - Style cohérent avec le style souhaité pour le livre
  - Une planche d'expressions faciales est très utile pour les personnages

💡 Si vous n'avez pas encore ces visuels, je peux les générer pour vous
   en Phase 2 (prototypage) — vous les validerez avant la production.

Vous avez des images de référence à fournir, ou je dois les créer ?
```

#### Auto-generation of reference sheets

If the user does NOT have reference images, the agent generates them:

1. **Character reference sheets**: Generate a model sheet for each recurring character
   ```
   "[style anchor] Character model sheet for [CHARACTER_NAME],
   white/neutral background, reference sheet format:
   - Top row: front view, 3/4 view, side view, back view (full body)
   - Middle row: close-up face with 4 expressions (neutral, happy, angry, sad)
   - Bottom row: key poses (action pose, sitting, running)
   [character description: age, gender, hair, eyes, build, outfit, distinctive features]
   Clean lines, consistent proportions, professional character design sheet"
   ```

2. **Location reference sheets**: Generate key establishing shots
   ```
   "[style anchor] Location reference illustration: [LOCATION_NAME],
   [detailed description of the place],
   establishing shot showing the full environment,
   [time of day / lighting / weather],
   [key architectural or natural features],
   reference sheet for maintaining visual consistency"
   ```

3. **Object reference sheets**: Generate key objects from multiple angles
   ```
   "[style anchor] Object reference sheet: [OBJECT_NAME],
   white background, multiple angles (front, side, top, detail close-up),
   [detailed description: size, color, material, distinctive features],
   professional prop design reference"
   ```

Save ALL generated reference sheets to `project_dir/references/` and present
them to the user for validation BEFORE generating any book pages.

#### Reference registry

Create a `references/registry.json` that maps each reference to its metadata:

```json
{
  "characters": [
    {
      "id": "hero",
      "name": "Akira",
      "file": "characters/hero_front.png",
      "files_all": [
        "characters/hero_front.png",
        "characters/hero_side.png",
        "characters/hero_expressions.png"
      ],
      "description": "Garçon de 14 ans, cheveux noirs en bataille, yeux verts, cicatrice sur la joue gauche, veste rouge avec capuche, jean bleu, baskets blanches",
      "appears_on_pages": [1, 3, 4, 5, 7, 8, 10, 12, 15, 18, 20]
    }
  ],
  "locations": [
    {
      "id": "home",
      "name": "La maison d'Akira",
      "file": "locations/home.png",
      "description": "Petite maison traditionnelle japonaise avec jardin, toit en tuiles grises, porte d'entrée en bois, cerisier dans le jardin",
      "appears_on_pages": [1, 5, 20]
    }
  ],
  "objects": [
    {
      "id": "sword",
      "name": "L'épée ancestrale",
      "file": "objects/magic_sword.png",
      "description": "Katana avec lame bleutée lumineuse, garde en or avec motif de dragon, poignée enveloppée de tissu rouge",
      "appears_on_pages": [8, 10, 12, 15, 18]
    }
  ]
}
```

#### Using references during image generation

When generating a page that contains recurring elements, the prompt MUST:

1. **Include the text description** of each recurring element from the registry
2. **Pass the reference image as input** to GPT Image 2 (edit/reference mode)
3. **Explicitly instruct** consistency:

```
"[STYLE ANCHOR]

This is page [N]. The image IS the entire book page.

RECURRING ELEMENTS ON THIS PAGE (must match reference images exactly):
- Character 'Akira': [full description from registry] — SEE REFERENCE IMAGE 1
- Location 'La forêt': [full description from registry] — SEE REFERENCE IMAGE 2

[rest of the page-specific prompt...]"
```

**On Codex:** use built-in `image_gen` with reference images attached as input
**On Claude Code:** use `scripts/generate_image.py --reference ref1.png ref2.png --prompt "..."`

#### Consistency verification

After generating each page with recurring elements:
1. Compare the generated character/object/location with the reference
2. Check: same hair color? same outfit? same proportions? same distinctive features?
3. If drift is detected: regenerate the page with stronger reference emphasis
4. Log consistency issues in `project_dir/logs/consistency.log`

### Style prompt construction

Build a **style anchor prompt** that will be prepended to every image generation call
to ensure visual consistency across the entire book:

```
Style anchor: "Full-page book illustration, [EXACT_PAGE_DIMENSIONS],
  [visual style], consistent art style throughout,
  [color palette description], [line weight/texture],
  [character design notes if applicable],
  all text in the image must be in French,
  professional book page quality, print-ready resolution,
  the image IS the entire page — text and visuals are part of the same image"
```

The style anchor MUST include:
1. The exact page dimensions (from page size rule)
2. The visual style
3. The language instruction ("all text in French")
4. The "full-page" instruction so GPT Image 2 treats the image as a complete book page
5. Typography guidance: font style, text size relative to page, text placement zones

Store this in `project_config.json` alongside all analysis results.

## Phase 2 — Prototype

Generate exactly 3 validation images. Remember: each is a FULL PAGE IMAGE
with all text rendered inside the image.

1. **Cover image** — Front cover with title, subtitle, author name rendered in the image
2. **Sample content page** — One representative page (e.g., a complete recipe page
   with the dish illustration, recipe title, ingredients list, and instructions
   ALL rendered as part of the image)
3. **Table of contents page** — A beautifully designed "Sommaire" page with all
   planned chapters/sections listed, styled consistently with the book's visual theme,
   ALL text rendered inside the image

### Image generation rules

**CRITICAL — Every image prompt must include:**
- The style anchor (from Phase 1)
- The exact page dimensions
- ALL text content to be rendered, in French, with exact wording
- Typography instructions (font style, size, placement)
- The instruction: "This image IS the entire book page. All text is part of the image."

**Example prompt for a cookbook TOC page:**
```
"[style anchor] Sommaire (table of contents) page for an Alsatian cookbook,
cartoon illustration style, warm colors, decorative Alsatian motifs border,
the page must display this exact text in French:

SOMMAIRE

Entrées
  Tarte flambée traditionnelle ........... 4
  Salade de cervelas ..................... 8
  Presskopf .............................. 12

Plats principaux
  Baeckeoffe .............................. 16
  Choucroute garnie ....................... 20
  Coq au Riesling ......................... 24

Desserts
  Kouglof ................................. 28
  Tarte aux quetsches ..................... 32
  Bredele de Noël ......................... 36

Beautiful typography, elegant layout, decorative food illustrations around borders,
this image IS the entire page, [EXACT_PAGE_DIMENSIONS]"
```

**On Codex:**
- Use built-in `image_gen` tool for all image generation
- Generate at highest available quality
- Save to `project_dir/prototype/`

**On Claude Code:**
- Use `scripts/generate_image.py` which calls GPT Image 2 API
- Use the exact page dimensions from project config
- Save to `project_dir/prototype/`

### Validation checkpoint

Present the 3 page images to the user and ask:
```
Voici le prototype de votre livre :

📕 Couverture : [show cover image]
📄 Page exemple : [show sample content page]
📋 Sommaire : [show TOC page image]

📊 Le livre complet contiendra X pages (= X images à générer)
💰 Coût estimé : ~X$ pour Y images

Que souhaitez-vous modifier ?
- Le style visuel (couleurs, trait, ambiance...)
- Le contenu (ajouter/retirer des sections, d'autres recettes...)
- La mise en page (placement du texte, taille de police...)
- La typographie (style de police, taille...)
- ✅ C'est parfait — lancer la génération complète
```

Do NOT proceed to Phase 4 without explicit user approval.

## Phase 3 — Iterate

If the user requests changes:

1. Parse the feedback into specific adjustments
2. Update `project_config.json` (style anchor, structure, etc.)
3. Regenerate ONLY the affected prototype assets
4. Return to the validation checkpoint

Repeat until the user approves.

### Style iteration tips

- If the user says "more colorful": increase saturation terms in style anchor
- If "different character": regenerate character design sheet first, then sample page
- If "different layout": switch page template variant, regenerate sample
- If structural change: update TOC, regenerate sample if the page type changed

## Phase 4 — Produce

Once approved, generate ALL book pages as full-page images.

### Production workflow

```
1. Create project directory structure:
   project_dir/
   ├── config/
   │   └── project_config.json    # All settings, style anchor, structure
   ├── references/                 # Visual reference assets (see Phase 1)
   │   ├── registry.json          # Reference registry with descriptions
   │   ├── characters/            # Character model sheets
   │   ├── locations/             # Location reference images
   │   └── objects/               # Object reference images
   ├── pages/
   │   ├── page_000_cover.png     # Front cover
   │   ├── page_001_toc.png       # Table of contents (Sommaire)
   │   ├── page_002_intro.png     # Introduction / avant-propos
   │   ├── page_003_content01.png # First content page
   │   ├── page_004_content02.png
   │   └── ...
   ├── prompts/
   │   ├── page_000.txt           # Exact prompt used for each page
   │   ├── page_001.txt           # (for reproducibility and debugging)
   │   └── ...
   ├── logs/
   │   └── consistency.log        # Visual consistency tracking
   ├── output/
   │   ├── book.epub              # Fixed-layout EPUB
   │   ├── book_kdp.epub          # KDP-optimized EPUB
   │   └── book_print.pdf         # Print-ready PDF (if requested)
   └── prototype/                  # Phase 2-3 validation assets
```

2. Generate the complete page list with exact prompts:
   - For each page, write the COMPLETE prompt including:
     - Style anchor (identical for every page)
     - Page-specific content (all text to render, in French)
     - Layout instructions (where text goes, where illustrations go)
     - Page dimensions (identical for every page)
     - **Reference elements**: check `references/registry.json` to see which
       recurring characters/locations/objects appear on this page,
       and include their descriptions + reference image inputs
   - Save each prompt to `prompts/page_NNN.txt` for traceability

3. Generate all images sequentially:
   - For each page, determine if it uses recurring visual elements:
     - **NO references needed** (e.g., TOC, section divider):
       → standard generation with style anchor + prompt
     - **References needed** (e.g., character appears on this page):
       → use GPT Image 2 in reference/edit mode, passing the relevant
         reference images as input alongside the prompt
   - For reference-based generation:
     - On Codex: attach reference images to `image_gen` call as input
     - On Claude Code: `scripts/generate_image.py --references
       references/characters/hero_front.png references/locations/home.png
       --prompt "[full page prompt]"`
   - Validate each generated image:
     - Correct pixel dimensions (must match project config exactly)
     - Not blank or corrupted
     - Text is legible and in the correct language
     - **Recurring elements match their references** (visual consistency check)
   - If an image fails validation, retry up to 3 times
   - Save to `pages/page_NNN_[description].png`

4. Build the fixed-layout EPUB:
   - Each "chapter" is a single HTML page containing ONE full-page image
   - HTML wrapper per page is minimal:
     ```html
     <?xml version="1.0" encoding="utf-8"?>
     <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta name="viewport" content="width=WIDTH, height=HEIGHT"/>
       <style>
         body { margin: 0; padding: 0; }
         img { width: 100%; height: 100%; object-fit: contain; }
       </style>
     </head>
     <body>
       <img src="../images/page_NNN.png" alt="Page NNN"/>
     </body>
     </html>
     ```
   - Set EPUB metadata: fixed-layout, title, author, language=fr
   - Cover image = first page image
   - NO text-based table of contents needed (the TOC is an image page)
   - Set logical TOC entries pointing to page images for navigation

### Image prompt structure for every page

EVERY page prompt follows this exact pattern:
```
"[STYLE ANCHOR]

This is page [N] of a [BOOK_TYPE]. The image IS the entire book page.
Page dimensions: [WIDTHxHEIGHT] pixels.
All text must be in French.

PAGE CONTENT:
[Exact description of what this page shows — illustrations AND text]

TEXT TO RENDER (exact wording in French):
[Title]: "[exact title text]"
[Body text]: "[exact body text, ingredients, instructions, etc.]"
[Page number]: "[N]"

LAYOUT:
[Where each element goes — top, center, bottom, left, right]
[Typography: font style, relative size, color]"
```

### Consistency enforcement

- Every image prompt MUST start with the identical style anchor
- Every image MUST use the identical page dimensions
- For character-driven books (manga, picture books):
  - Generate a character reference sheet first (front, side, expressions)
  - Include character description in every prompt: "the same character as
    described: [character description]"
  - Use the reference sheet as an edit/reference input when possible
- For cookbooks: maintain consistent plating style, background, and typography
- After every 5 images, visually compare with the approved prototype sample
  to detect style drift
- If style drift is detected: pause and adjust the prompt, do not continue

### Progress reporting

After every 5 pages generated, report progress:
```
📊 Progression : 15/40 pages générées
✅ Pages 11-15 terminées — cohérence de style vérifiée
⏱️ Temps restant estimé : ~12 minutes
```

## Phase 5 — Export via Calibre

### Important: Fixed-layout EPUB only

Since every page is a full-page image, the EPUB MUST be **fixed-layout** (pre-paginated).
This preserves the exact image dimensions and prevents reflowing.

### EPUB to KDP conversion

```bash
# KDP Ebook — fixed-layout EPUB (image-based book)
ebook-convert book.epub book_kdp.epub \
  --output-profile kindle_fire \
  --no-default-epub-cover \
  --cover front_cover.png \
  --title "Titre du livre" \
  --authors "Nom de l'auteur" \
  --language fr \
  --publisher "Éditeur" \
  --tags "livre,recettes,alsace"

# KDP Print-ready PDF
ebook-convert book.epub book_print.pdf \
  --pdf-page-size custom \
  --custom-size 8.5x11 \
  --pdf-page-margin-top 0 \
  --pdf-page-margin-bottom 0 \
  --pdf-page-margin-left 0 \
  --pdf-page-margin-right 0 \
  --cover front_cover.png \
  --pdf-no-cover
```

Note: margins are 0 because margins are already part of the page images.
The images themselves must include the necessary margins/bleed.

### KDP format specifications

| Format | Dimensions | Image DPI | Cover size |
|--------|-----------|-----------|------------|
| Ebook (fixed-layout EPUB) | matches page images | 150+ | 2560×1600px |
| Print 6×9" | 6×9 inches | 300 | 3744×2400px (wrap) |
| Print 8.5×11" | 8.5×11 inches | 300 | 4800×3120px (wrap) |

### Validation checklist

Before delivering the final output, verify:
- [ ] ALL pages are present as images (no missing pages)
- [ ] ALL images have identical dimensions
- [ ] Cover image meets KDP size requirements
- [ ] All text in images is legible and in French
- [ ] No blank or corrupted images
- [ ] Metadata is complete (title, author, language=fr, description)
- [ ] File size is under KDP limits (650MB for ebooks)
- [ ] EPUB is fixed-layout (pre-paginated)
- [ ] Page order is correct (cover → sommaire → content → fin)

### Final delivery

```
✅ Votre ebook est prêt !

📕 Fichiers générés :
  - book_kdp.epub (à uploader sur KDP comme manuscrit ebook)
  - book_print.pdf (à uploader sur KDP comme manuscrit print)
  - front_cover.png (à uploader sur KDP comme couverture)

📊 Statistiques :
  - X pages (X images générées)
  - Taille totale : X Mo
  - Format : conforme KDP, mise en page fixe
  - Langue : Français

📤 Prochaines étapes :
  1. Connectez-vous à kdp.amazon.com
  2. Créez un nouveau titre
  3. Uploadez book_kdp.epub comme manuscrit ebook
  4. Uploadez front_cover.png comme image de couverture
  5. Si impression : uploadez book_print.pdf comme manuscrit papier
  6. Remplissez les métadonnées KDP (prix, catégories, description)
```
  - X pages, Y images generated
  - Total size: Z MB
  - Format: KDP-compliant

📤 Next steps:
  1. Upload book_kdp.epub to KDP as your ebook manuscript
  2. Upload front_cover.png as your cover
  3. If print: upload book_print.pdf as print manuscript
  4. Fill in KDP metadata (pricing, categories, description)
```

## Error handling

- **Image generation fails**: retry 3 times with slight prompt variation,
  then ask user for guidance
- **Calibre not installed**: provide installation instructions per platform,
  offer to generate EPUB-only without KDP optimization
- **Style drift detected**: pause generation, show comparison with prototype,
  ask user if they want to continue or adjust the style anchor
- **API rate limits**: implement exponential backoff, report wait times to user

## Reference files

- `templates/cookbook.md` — Recipe book page templates and prompts
- `templates/manga.md` — Manga/comic page templates and panel layouts
- `templates/picturebook.md` — Children's picture book templates
- `templates/visualguide.md` — Visual guide/how-to templates
- `templates/artbook.md` — Art book/portfolio templates
- `references/kdp-specs.md` — Amazon KDP format specifications
- `references/style-anchors.md` — Pre-built style anchor examples
- `scripts/generate_image.py` — GPT Image 2 CLI wrapper (Claude Code fallback)
- `scripts/build_epub.py` — EPUB assembly from HTML+images
- `scripts/calibre_export.py` — Calibre conversion wrapper
- `scripts/validate_book.py` — Pre-submission quality checks
