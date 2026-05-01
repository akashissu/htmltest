# Architect Plan — PAP-275

## Scope Summary
Create a **recipe cards section using only HTML and CSS** inside the existing single-file static page. Each card should include:
- food image,
- recipe title,
- cooking time,
- short description.

The visual direction should be **colorful, warm, and visually appealing**, while still staying clean and readable on desktop and mobile.

## Current Stack Inspection
Based on repository inspection:
- The project is a **single static page** in `index.html`.
- CSS is currently embedded in a `<style>` block inside `index.html`.
- There is **no package.json, framework, bundler, or component system** visible.
- The existing page uses:
  - CSS custom properties (`:root` variables),
  - responsive layout with CSS Grid,
  - rounded cards, shadows, and soft gradients,
  - semantic HTML sections and articles.

## Design Direction
The recipe section should feel:
- bright and appetizing,
- image-forward,
- easy to scan,
- responsive without JavaScript,
- visually richer than the current weather layout while still matching its polished style.

Recommended aesthetic:
- warm cream / peach / coral / golden accent palette,
- large rounded section container,
- image cards with soft shadows,
- subtle hover lift on cards,
- strong typography hierarchy for titles,
- compact metadata chip or row for cooking time.

## Recommended Implementation Strategy
Because the repo is a single-file static HTML/CSS sandbox, the simplest and safest implementation is:
1. **Replace or repurpose the current main content in `index.html`** with a recipe-focused section.
2. Keep all styling in the existing internal `<style>` block.
3. Build the section with semantic HTML:
   - one parent section,
   - one section heading + intro copy,
   - a responsive card grid,
   - one `<article>` per recipe card.

## Proposed HTML Structure
Use a structure along these lines:
- `<main class="recipe-section">`
  - intro/header block
    - eyebrow or badge (optional)
    - `<h1>` section title
    - short supporting paragraph
  - `<div class="recipe-grid">`
    - repeated `<article class="recipe-card">`
      - image wrapper
      - `<img>` for food photo
      - content block
        - recipe title
        - time row / badge
        - short description

## Card Content Recommendation
Target **3 to 6 cards**. Four cards is a good middle ground for a polished demo.

Suggested example fields per card:
- **Title**: e.g. `Creamy Tomato Pasta`
- **Cooking time**: e.g. `25 min`
- **Description**: one sentence, ~12–22 words
- **Image**: appetizing food photo from a stable remote source or an existing local asset if available

## Image Strategy
Since no asset pipeline is visible, the Grunt should choose one of these:
1. **Preferred:** use stable remote image URLs in plain `<img>` tags for the demo.
2. **Fallback:** use CSS gradients/placeholders if remote images are undesirable in this environment.

If using remote images, choose images that are:
- directly renderable in the browser,
- reasonably sized,
- visually distinct,
- food-focused and bright.

## Layout Recommendation
### Desktop
- Use CSS Grid with `repeat(auto-fit, minmax(...))`
- 2–4 columns depending on viewport width
- generous gap spacing

### Mobile
- Collapse to 1 column on narrow screens
- Maintain readable padding and large tap-friendly card spacing

## Styling Plan
### Global/theme updates
Introduce or replace variables with a recipe-friendly palette, for example:
- page background: warm gradient or light cream,
- section/card backgrounds: white or soft ivory,
- accent colors: coral, orange, golden yellow, leafy green,
- muted text for descriptions,
- stronger shadow for card depth.

### Recipe section container
Style the main wrapper with:
- max-width constraint,
- centered layout,
- roomy padding,
- rounded corners,
- polished shadow.

### Header/intro
Include:
- prominent heading,
- short supporting copy,
- optional small badge like `Fresh picks` or `Easy recipes`.

### Card styling
Each card should include:
- rounded corners,
- overflow hidden for image clipping,
- image at fixed aspect ratio via CSS,
- white background,
- soft border or subtle shadow,
- hover transition (`transform`, `box-shadow`) for desktop polish.

### Image treatment
Recommended:
- `width: 100%`
- fixed height or `aspect-ratio`
- `object-fit: cover`

### Cooking time presentation
Represent cooking time as one of:
- a pill badge,
- a compact metadata row,
- or a small highlighted inline block with an icon/emoji if the final styling supports it.

## Accessibility Guidance
The implementation should preserve or improve accessibility by:
- using real `<img>` elements with descriptive `alt` text,
- keeping heading hierarchy simple,
- ensuring color contrast remains readable,
- avoiding decorative text that is too faint,
- not relying on color alone to communicate time/info.

## Content Recommendation
Use concise, appetizing descriptions. Example categories that create visual variety:
- pasta,
- salad,
- grilled entrée,
- dessert or breakfast item.

This creates stronger visual contrast across cards and helps the section feel intentionally curated.

## Suggested Grunt Implementation Steps
1. Open `index.html`.
2. Replace the current weather-specific title, classes, and body content with a recipe-section layout.
3. Rewrite CSS variables and component styles to support a recipe-card visual system.
4. Add 4 recipe cards with:
   - image,
   - title,
   - cooking time,
   - short description.
5. Verify responsive behavior by checking narrow and wide layouts.
6. Leave a handoff note describing what changed and any image-source choices.

## Suggested Pedant Review Focus
The Pedant should verify:
- all recipe cards include the 4 required content pieces,
- layout is responsive,
- visuals feel colorful and intentionally designed,
- HTML remains semantic and reasonably accessible,
- CSS is not cluttered with dead weather-specific styles,
- images display correctly and do not distort.

## Files Expected To Change In Implementation Phase
Likely implementation changes should be limited to:
- `index.html`

Optional artifact files from later roles:
- `GRUNT_HANDOFF_PAP-275.md`
- `PEDANT_HANDOFF_PAP-275.md`
- `TERMINAL_LOGS_PAP-275_GRUNT.txt`

## Explicit Non-Goals For This Phase
- No HTML/CSS implementation in this architect phase
- No framework setup
- No JavaScript behavior
- No git push
- No PR creation

## Handoff Summary
The next role should implement a **single-file, responsive, colorful recipe cards section** in `index.html`, using embedded CSS and semantic HTML articles. Aim for four cards, strong food imagery, pill-style cooking-time metadata, and polished spacing/shadows to make the section feel modern and appetizing.
