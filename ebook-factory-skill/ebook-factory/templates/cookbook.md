# Cookbook Template

## Page types

### Cover page
```
Prompt pattern:
"[style anchor] Book cover for a [theme] cookbook titled '[TITLE]',
[visual style] illustration style, appetizing food imagery,
warm inviting colors, professional cookbook cover design,
title text area at top, author name area at bottom"
```

### Section divider page
```
Prompt pattern:
"[style anchor] Section divider page for '[SECTION_NAME]' chapter,
decorative [theme]-themed border, centered section title area,
[visual style] illustration of [section-relevant food/scene],
elegant typography space, cookbook interior design"
```

### Recipe page — Standard (single page)
```
Layout:
┌─────────────────────────┐
│   RECIPE TITLE          │
│   Prep: Xmin | Cook: Xm │
├────────┬────────────────┤
│        │                │
│ IMAGE  │  INGREDIENTS   │
│ (main  │  - item 1      │
│  dish) │  - item 2      │
│        │  - item 3      │
├────────┴────────────────┤
│  INSTRUCTIONS           │
│  1. Step one...         │
│  2. Step two...         │
│  3. Step three...       │
└─────────────────────────┘

Image prompt pattern:
"[style anchor] [DISH_NAME], [visual style] illustration,
overhead/45-degree view, [plating style] on [plate/surface type],
[garnish details], [background setting], appetizing food photography style,
warm lighting, [color palette from style anchor]"
```

### Recipe page — Visual steps (double page)
```
Layout:
┌─────────────────────────┐
│   RECIPE TITLE          │
├────────┬────────────────┤
│ STEP 1 │ STEP 2         │
│ [img]  │ [img]          │
│ text   │ text           │
├────────┼────────────────┤
│ STEP 3 │ STEP 4         │
│ [img]  │ [img]          │
│ text   │ text           │
├────────┴────────────────┤
│ FINAL DISH [large img]  │
│ Serving suggestion text │
└─────────────────────────┘

Step image prompt pattern:
"[style anchor] cooking step: [ACTION_DESCRIPTION],
hands [doing action] with [ingredients],
[kitchen setting], close-up view, [visual style],
instructional cookbook illustration"
```

## Content generation prompts

### For researched recipes
When the agent needs to find recipes for a theme:
```
Research [CUISINE] cuisine and compile [N] authentic recipes.
For each recipe provide:
- Traditional name (original language + translation)
- Brief cultural context (1-2 sentences)
- Prep time and cook time
- Servings
- Ingredients with precise measurements
- Step-by-step instructions (numbered, clear, concise)
- Plating/serving suggestion
- Chef's tip or variation

Group recipes into logical sections:
- Appetizers / Starters
- Main courses
- Side dishes
- Desserts
- Breads & pastries
- Drinks (if applicable)
```

## Style anchor examples for cookbooks

### Cartoon style
```
"Bright colorful cartoon illustration style, bold outlines,
exaggerated proportions for food to look extra appetizing,
warm saturated colors, clean white backgrounds,
consistent 2D flat design with subtle shadows,
playful and inviting mood"
```

### Watercolor style
```
"Soft watercolor illustration style, delicate brushstrokes,
muted natural color palette with warm accents,
slight paper texture visible, organic flowing edges,
elegant and artistic food presentation,
light cream/white background"
```

### Photorealistic style
```
"Photorealistic food photography style, professional studio lighting,
shallow depth of field, rich saturated colors,
styled food on rustic wooden surfaces,
natural window light feel, editorial cookbook quality,
clean composition with negative space for text"
```

### Minimalist style
```
"Clean minimalist illustration style, simple geometric shapes,
limited color palette (max 4 colors), generous white space,
thin precise lines, modern Scandinavian design influence,
flat design with subtle gradients, sophisticated and clean"
```

## HTML template (Jinja2)

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .recipe-page { page-break-after: always; padding: 20px; }
    .recipe-title { font-size: 24px; font-weight: bold; margin-bottom: 8px; }
    .recipe-meta { font-size: 12px; color: #666; margin-bottom: 16px; }
    .recipe-image { width: 100%; max-height: 400px; object-fit: cover; border-radius: 8px; }
    .ingredients { background: #f9f6f1; padding: 16px; border-radius: 8px; }
    .ingredients h3 { margin-top: 0; }
    .ingredients ul { padding-left: 20px; }
    .instructions ol { line-height: 1.8; }
    .chef-tip { background: #fff3e0; padding: 12px; border-left: 4px solid #ff9800; margin-top: 16px; }
  </style>
</head>
<body>
  <div class="recipe-page">
    <h1 class="recipe-title">{{ recipe.title }}</h1>
    <p class="recipe-meta">
      Préparation : {{ recipe.prep_time }} | Cuisson : {{ recipe.cook_time }} | 
      Pour {{ recipe.servings }} personnes
    </p>
    <img class="recipe-image" src="{{ recipe.image_path }}" alt="{{ recipe.title }}" />
    <div class="ingredients">
      <h3>Ingrédients</h3>
      <ul>
        {% for ingredient in recipe.ingredients %}
        <li>{{ ingredient }}</li>
        {% endfor %}
      </ul>
    </div>
    <div class="instructions">
      <h3>Préparation</h3>
      <ol>
        {% for step in recipe.steps %}
        <li>{{ step }}</li>
        {% endfor %}
      </ol>
    </div>
    {% if recipe.tip %}
    <div class="chef-tip">
      <strong>💡 Astuce du chef :</strong> {{ recipe.tip }}
    </div>
    {% endif %}
  </div>
</body>
</html>
```

## CSS for EPUB

```css
@page {
  margin: 1cm;
}

body {
  font-family: Georgia, serif;
  line-height: 1.6;
  color: #333;
}

img {
  max-width: 100%;
  height: auto;
}

.recipe-page {
  page-break-after: always;
}
```
