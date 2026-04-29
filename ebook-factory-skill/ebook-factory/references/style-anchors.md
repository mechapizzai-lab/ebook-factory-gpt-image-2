# Style Anchor Reference

Pre-built style anchor prompts for common visual styles.
These are prepended to EVERY image generation call in a project
to ensure visual consistency across the entire book.

## How to use

1. Pick a base style that matches the user's request
2. Customize with theme-specific details
3. Store in `project_config.json` as `style_anchor`
4. The production pipeline prepends this to every image prompt

## Cartoon styles

### Classic cartoon
```
Bright colorful cartoon illustration, bold black outlines,
cel-shaded flat colors with subtle gradients, exaggerated
proportions, warm friendly palette, clean vector-like quality,
consistent 2D illustration style throughout
```

### Modern flat illustration
```
Modern flat illustration style, geometric shapes, limited
color palette (5-6 colors max), no outlines, clean edges,
subtle texture overlay, contemporary design aesthetic,
minimalist but expressive, professional editorial illustration
```

### Retro / Vintage cartoon
```
Retro 1950s illustration style, muted warm color palette,
halftone dot texture, slightly rough edges, mid-century
modern aesthetic, nostalgic and charming, hand-drawn feel
with vintage printing imperfections
```

## Realistic styles

### Photorealistic
```
Photorealistic illustration, professional photography quality,
natural lighting, rich detail and texture, shallow depth of
field where appropriate, warm color grading, editorial quality,
high dynamic range, shot on professional camera aesthetic
```

### Hyperrealistic digital painting
```
Hyperrealistic digital painting, visible brushwork adding
artistic quality, dramatic lighting with rich shadows,
oil painting texture, museum-quality fine art,
sophisticated color harmony, professional illustration
```

## Artistic styles

### Watercolor
```
Soft watercolor illustration, visible brushstrokes and
paint bleeding effects, gentle color transitions, light
paper texture, organic and flowing, limited palette with
harmonious colors, artistic and elegant
```

### Ink and wash
```
Traditional ink wash illustration style, bold black ink
lines with gray wash shading, minimal color accents,
calligraphic line quality, East Asian art influence,
elegant and expressive, white space as compositional element
```

### Gouache / Tempera
```
Gouache painting style, opaque rich colors, matte finish,
slightly textured surface, bold and vibrant, warm and
inviting, children's book illustration quality, visible
but controlled brushstrokes
```

## Manga / Anime styles

### Classic manga (B&W)
```
Professional black and white manga illustration, clean
precise inking, screentone shading, dynamic compositions,
expressive character faces, detailed when needed with
strategic simplification, speed lines for action,
Japanese manga publishing quality
```

### Full-color manga
```
Full-color manga illustration style, anime-influenced
color palette, cel-shaded coloring with soft gradients,
clean precise lines, vivid saturated colors, dynamic
compositions, professional light novel illustration quality
```

### Chibi / Kawaii
```
Cute chibi illustration style, super-deformed proportions
(2-3 heads tall), simple round shapes, pastel color palette
with bright accents, minimal detail, maximum expressiveness,
kawaii aesthetic, clean and adorable
```

## Specialized styles

### Technical / Instructional
```
Clean technical illustration style, precise lines,
neutral color palette (grays, blues, subtle accents),
clear labeling areas, isometric perspective where helpful,
professional instructional manual quality, uncluttered
compositions with generous white space
```

### Fantasy / Storybook
```
Fantasy storybook illustration, rich and detailed,
golden-hour warm lighting, magical atmosphere with subtle
glow effects, ornate borders and decorative elements,
classic fairy tale illustration quality, enchanting
and immersive, deep jewel-tone color palette
```

### Pop art
```
Bold pop art illustration style, Ben-Day dots, primary
colors with black outlines, high contrast, graphic and
punchy, Andy Warhol and Roy Lichtenstein influenced,
commercial art aesthetic, eye-catching and energetic
```

## Customization guide

When the user describes a style not covered above, construct
a style anchor using this template:

```
[Art medium/technique], [line quality description],
[color palette description], [texture/surface quality],
[mood/atmosphere], [reference influences if applicable],
[quality level], consistent style throughout
```

### Key elements to always include:
1. **Medium**: what it looks like (watercolor, digital, ink, etc.)
2. **Lines**: bold/thin/clean/rough/none
3. **Colors**: palette range, saturation, temperature
4. **Texture**: smooth/textured/paper grain/etc.
5. **Mood**: warm/cool/dramatic/playful/elegant
6. **Consistency phrase**: "consistent style throughout" or similar
