# Children's Picture Book Template

## Page types

### Cover
```
Prompt pattern:
"[style anchor] Children's picture book cover for '[TITLE]',
[main character] in a [key scene from story],
whimsical and inviting, bright cheerful colors,
title text area at top, author area at bottom,
professional children's book cover illustration"
```

### Title page (interior)
```
Prompt pattern:
"[style anchor] Interior title page, small vignette illustration
of [main character or key object], centered on white/cream background,
simple and elegant, space for title and author name,
children's book interior design"
```

### Story spread (double page)
```
Layout:
┌─────────────────────────────────────────┐
│                                         │
│          FULL ILLUSTRATION              │
│       (spans both pages)                │
│                                         │
│                                         │
├─────────────────────────────────────────┤
│  Text line 1 of the story...            │
│  Text line 2 of the story...            │
└─────────────────────────────────────────┘

Prompt pattern:
"[style anchor] Children's book illustration:
[scene description with character action and emotion],
[setting/background details],
[time of day/weather/mood],
wide panoramic composition for double-page spread,
space at bottom for 2-3 lines of text,
[visual style], warm and engaging for ages [age range]"
```

### Story page (single, text-heavy)
```
Layout:
┌─────────────────────────┐
│   ILLUSTRATION           │
│   (top 60% of page)     │
│                         │
├─────────────────────────┤
│                         │
│   Story text paragraph   │
│   continues here with    │
│   larger font for young  │
│   readers...             │
│                         │
└─────────────────────────┘
```

### End page
```
Prompt pattern:
"[style anchor] Final illustration for children's picture book,
[resolution scene — character happy/content/home],
warm and satisfying conclusion feeling,
'The End' vignette style, gentle and peaceful mood"
```

## Story generation rules

### Age-appropriate content
- Ages 0-3: 10-16 pages, 1-2 sentences per page, simple concepts
- Ages 3-5: 16-24 pages, 2-4 sentences per page, simple narrative arc
- Ages 5-8: 24-32 pages, paragraph per page, developed story with conflict

### Narrative structure
```
Pages 1-2:    Introduce character and their world
Pages 3-4:    Introduce the want/need/problem  
Pages 5-8:    First attempts, rising challenges
Pages 9-12:   Things get harder, emotional low point
Pages 13-14:  Breakthrough / clever solution
Pages 15-16:  Resolution and warm ending
```

### Character consistency
Generate a character sheet FIRST with:
- Simple, memorable design (max 3-4 colors per character)
- Recognizable silhouette
- Clear, expressive face
- Consistent outfit

Include EXACT character description in every prompt.

## Style anchor examples

### Watercolor storybook
```
"Soft watercolor children's book illustration, gentle brushstrokes,
pastel color palette with warm accents, dreamy atmospheric quality,
detailed but not overwhelming backgrounds, expressive characters
with large friendly eyes, storybook quality, reminiscent of
classic picture book illustration, light paper texture"
```

### Bold and modern
```
"Modern children's book illustration, bold flat colors,
clean geometric shapes with rounded corners, limited color palette,
strong graphic design influence, playful compositions,
contemporary picture book style, bright and cheerful,
digital illustration with hand-drawn charm"
```

### Collage / Mixed media
```
"Mixed media children's book illustration, paper collage textures,
layered cutout effect, rich tactile quality, bold primary colors,
playful arrangements, craft-like aesthetic,
textured backgrounds with visible paper grain,
Eric Carle inspired mixed media"
```

## HTML template

```html
<div class="spread">
  <div class="illustration">
    <img src="{{ page.image_path }}" alt="{{ page.alt_text }}" />
  </div>
  <div class="story-text">
    <p>{{ page.text }}</p>
  </div>
</div>
```

## CSS for picture book EPUB

```css
@page { margin: 0; }

.spread {
  page-break-after: always;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.illustration {
  flex: 3;
  overflow: hidden;
}

.illustration img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.story-text {
  flex: 1;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.story-text p {
  font-family: 'Georgia', serif;
  font-size: 18px;
  line-height: 1.6;
  text-align: center;
  max-width: 80%;
}
```
