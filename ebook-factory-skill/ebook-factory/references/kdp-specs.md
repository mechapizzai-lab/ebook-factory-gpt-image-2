# Amazon KDP Format Specifications

## Ebook (Kindle)

### Accepted formats
- EPUB (preferred, converted by KDP to KF8/AZW3)
- KPF (Kindle Package Format via Kindle Create)
- DOCX, PDF (fallback, less control)

### Cover image
- Minimum: 625×1000px (1:1.6 ratio)
- Recommended: 2560×1600px
- Maximum file size: 50MB
- Format: JPEG or TIFF
- RGB color space (not CMYK)
- No bleed needed for ebook covers

### Interior images
- Minimum: 300px on shortest side
- Recommended: 1000-1500px on shortest side for detail
- Maximum: 5000px on longest side
- Format: JPEG (quality 80+) or PNG
- RGB color space
- File size: keep individual images under 5MB

### EPUB specifications
- EPUB 2 or EPUB 3 accepted
- Maximum file size: 650MB
- HTML + CSS for layout
- Embedded fonts allowed (subset recommended)
- JavaScript NOT supported
- Fixed-layout EPUB supported for image-heavy books

### Fixed-layout vs Reflowable
- **Reflowable**: text reflows to fit screen (standard ebooks, novels)
- **Fixed-layout**: maintains exact positioning (cookbooks, picture books, manga)
- For visual books: USE FIXED-LAYOUT EPUB

### Fixed-layout EPUB setup
```xml
<!-- In content.opf metadata -->
<meta property="rendition:layout">pre-paginated</meta>
<meta property="rendition:orientation">auto</meta>
<meta property="rendition:spread">auto</meta>

<!-- Each page specifies viewport -->
<!-- In each HTML file -->
<meta name="viewport" content="width=1200, height=1600"/>
```

## Print (Paperback / Hardcover)

### Trim sizes (most common for visual books)
| Size | Interior dimensions | Use case |
|------|-------------------|----------|
| 6×9" | 6×9 inches | Standard cookbook |
| 7×10" | 7×10 inches | Large format cookbook |
| 8×10" | 8×10 inches | Coffee table / art book |
| 8.5×11" | 8.5×11 inches | Full-size cookbook, workbook |

### Margins (minimum)
- **Outside margin**: 0.25" (6.35mm)
- **Top/Bottom margin**: 0.25" (6.35mm)
- **Inside (gutter) margin**: depends on page count
  - 24-150 pages: 0.375" (9.5mm)
  - 151-300 pages: 0.5" (12.7mm)
  - 301-500 pages: 0.625" (15.9mm)
  - 501-700 pages: 0.75" (19mm)
  - 701-828 pages: 0.875" (22.2mm)

### Bleed
- If images extend to page edge: add 0.125" (3.175mm) bleed on all sides
- Full-bleed document size = trim size + 0.25" width + 0.25" height
- Example: 8.5×11" with bleed = 8.75×11.25"

### Cover specifications (print)
```
Cover width = bleed + back cover + spine + front cover + bleed
Cover height = bleed + trim height + bleed

Spine width calculation:
- Black & white interior: page count × 0.0025"
- Color interior: page count × 0.002347"

Example for 40-page color 8.5×11" book:
- Spine: 40 × 0.002347" = 0.094"
- Width: 0.125 + 8.5 + 0.094 + 8.5 + 0.125 = 17.344"
- Height: 0.125 + 11 + 0.125 = 11.25"
- Resolution: 300 DPI minimum
```

### Print interior
- Resolution: 300 DPI minimum for images
- Color space: RGB or CMYK (KDP converts)
- Format: PDF (PDF/X-1a recommended)
- No crop marks, registration marks, or color bars
- Fonts must be embedded in PDF

## Calibre conversion commands

### EPUB for Kindle (reflowable)
```bash
ebook-convert input.epub output.epub \
  --output-profile kindle_oasis \
  --no-default-epub-cover \
  --cover cover.jpg \
  --title "Title" \
  --authors "Author" \
  --language en \
  --book-producer "Ebook Factory" \
  --smarten-punctuation \
  --subset-embedded-fonts
```

### Fixed-layout EPUB for Kindle
```bash
ebook-convert input.epub output.epub \
  --output-profile kindle_fire \
  --no-default-epub-cover \
  --cover cover.jpg \
  --title "Title" \
  --authors "Author"
```

### PDF for KDP Print
```bash
ebook-convert input.epub output.pdf \
  --paper-size custom \
  --custom-size 8.5x11 \
  --pdf-page-margin-top 18 \
  --pdf-page-margin-bottom 18 \
  --pdf-page-margin-left 36 \
  --pdf-page-margin-right 18 \
  --pdf-no-cover \
  --cover cover.jpg
```

## Quality checklist

### Before upload
- [ ] Cover meets minimum resolution (2560×1600 for ebook)
- [ ] All images load correctly
- [ ] Table of contents works (clickable for ebook)
- [ ] No blank pages
- [ ] Text is readable at smallest Kindle screen size
- [ ] File size under 650MB (ebook) or 1.5GB (print)
- [ ] Metadata complete: title, author, language, description
- [ ] ISBN (optional but recommended for print)

### Common rejection reasons
- Cover image too low resolution
- Interior images blurry or pixelated
- Missing or broken table of contents
- Bleed issues on print (images don't extend to bleed edge)
- Font embedding issues
- File size too large
