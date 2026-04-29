# Manga / Comic Template

## Page types

### Cover page
```
Prompt pattern:
"[style anchor] Manga/comic book cover for '[TITLE]',
dynamic composition with main character in action pose,
dramatic lighting, title text area at top,
[genre]-themed visual elements, professional manga cover art,
Japanese manga style with [specific substyle]"
```

### Chapter title page
```
Prompt pattern:
"[style anchor] Chapter [N] title page: '[CHAPTER_TITLE]',
dramatic establishing shot of [scene/location],
mood-setting atmosphere, space for chapter number and title text,
manga interior art style"
```

### Standard manga page (4-6 panels)
```
Layout variants:

4-panel grid:                    5-panel dynamic:
┌──────┬──────┐                  ┌──────────────┐
│  P1  │  P2  │                  │     P1       │
│      │      │                  ├────┬─────────┤
├──────┼──────┤                  │ P2 │   P3    │
│  P3  │  P4  │                  │    │         │
│      │      │                  ├────┴──┬──────┤
└──────┴──────┘                  │  P4   │  P5  │
                                 └───────┴──────┘

6-panel action:
┌──────────────┐
│     P1       │
├───┬────┬─────┤
│P2 │ P3 │ P4  │
├───┴────┴─────┤
│   P5   │ P6  │
└────────┴─────┘

Prompt pattern:
"[style anchor] Manga page with [N] panels showing:
Panel 1: [scene description, character action, emotion, camera angle]
Panel 2: [scene description]
...
Panel N: [scene description]
Black and white manga style with screentones,
dynamic panel borders, speech bubble spaces,
professional manga interior art, right-to-left reading flow"
```

### Splash page (full-page illustration)
```
Prompt pattern:
"[style anchor] Full-page manga splash illustration,
[dramatic scene description], [character(s) in dynamic pose],
detailed background, intense [emotion/action],
professional manga art, high detail level,
space for speech bubbles at [position]"
```

## Character consistency system

### Character reference sheet
Before generating any story pages, create a character sheet:
```
"[style anchor] Character reference sheet for [CHARACTER_NAME]:
- Front view, 3/4 view, side view, back view
- Height reference, body proportions
- Key features: [hair color/style, eye color, distinctive marks]
- Default outfit details
- 3-4 facial expressions (neutral, happy, angry, surprised)
- Manga/anime art style, clean lines, white background,
  model sheet format, character design reference"
```

Include character description in EVERY subsequent prompt:
```
"[CHARACTER_NAME]: [age] [gender], [hair description], [eye color],
[height/build], wearing [outfit], [distinctive features]"
```

## Story generation structure

```
For a [N]-page manga, structure as:
- Page 1: Cover
- Page 2-3: Character introductions / setting establishment
- Pages 4-N-3: Rising action (conflict, challenges, development)
- Pages N-2 to N-1: Climax
- Page N: Resolution / cliffhanger

Each page needs:
- Panel count and layout type
- Per-panel: scene description, dialogue, sound effects
- Emotional beat / pacing note
- Camera angles (close-up, wide shot, dutch angle, bird's eye)
```

## Style anchor examples

### Shonen action
```
"Dynamic shonen manga style, bold thick lines, intense action poses,
speed lines for motion, dramatic screentone shading,
high contrast black and white, energetic composition,
expressive character faces, detailed backgrounds in establishing shots"
```

### Slice-of-life / Josei
```
"Soft josei manga style, thin elegant lines, gentle expressions,
detailed fashion and everyday settings, delicate screentone,
atmospheric backgrounds, subtle emotional storytelling,
clean compositions, beautiful character designs"
```

### Chibi / Comedy
```
"Cute chibi manga style, simplified round proportions,
exaggerated comedic expressions, minimal backgrounds,
bold simple lines, 2-3 head-tall characters,
playful panel layouts, comedic timing through panel size"
```
