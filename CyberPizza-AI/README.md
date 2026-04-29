# CyberPizza AI

Mini-manga couleur cyberpunk de 10 pages, prepare pour un export KDP ebook en mise en page fixe.

## Format

- Type: manga couleur
- Langue: francais
- Pages: 10 images pleine page
- Dimensions: 1600x2560 px
- Cible: KDP ebook fixed-layout

## Ordre de production

1. Generer et valider les references dans `references/reference_prompts.md`.
2. Utiliser les descriptions de `references/registry.json` pour garder les personnages coherents.
3. Generer les pages avec les prompts `prompts/page_001_cover.txt` a `prompts/page_010_cliffhanger.txt`.
4. Placer les images finales dans `pages/` avec les memes noms de page.
5. Assembler ensuite l'EPUB fixe dans `output/`.

## Sorties generees

- `output/CyberPizza-AI-episode-1.epub`: EPUB fixe source, image-par-page.
- `output/CyberPizza-AI-episode-1-kdp.epub`: EPUB optimise via Calibre pour KDP ebook.
- `output/CyberPizza-AI-episode-1-image.pdf`: PDF image-direct de verification.
- `output/CyberPizza-AI-episode-1-print.pdf`: PDF produit via Calibre.
- `output/pages_1600x2560/`: pages normalisees au format cible.

## References a creer avant les pages

- `references/characters/nox_model_sheet.png`
- `references/characters/lina_model_sheet.png`
- `references/characters/mara_model_sheet.png`
- `references/characters/slice_crust_guard_model_sheet.png`
- `references/locations/neomarseille_reference.png`
- `references/locations/pizzeria_lab_reference.png`
- `references/objects/ai_core_reference.png`

## Note de coherence

Chaque page doit reutiliser le meme style anchor et les memes descriptions de personnages. Pour un manga, les model sheets doivent etre valides avant de produire les pages finales.
