# Design System Document: Festival Mainstage Pitch

## 1. Overview & Creative North Star: "The Sonic Brutalist"
This design system is built to capture the electric, visceral energy of a front-row experience. It moves away from the polite, rounded "tech-friendly" aesthetics of modern SaaS, embracing instead a "Sonic Brutalist" philosophy. This means raw edges, high-contrast typography, and deep immersive voids that mirror the darkness of a concert hall before the first chord hits.

**The Creative North Star:**
The goal is to create a digital stage. We break the standard "template" look through intentional asymmetry—placing content off-center to mimic the unpredictable movement of a crowd—and by layering sharp-edged geometric scaffolding over organic, blurred photography. Every layout should feel like a high-end gig poster: curated, impactful, and loud.

---

## 2. Colors: Neon in the Void
The palette is built on a foundation of "Deep Void" tones (`surface`, `background`) punctuated by "Light Leak" accents that mimic stage lighting.

### The "No-Line" Rule
Prohibit the use of 1px solid borders for sectioning. Structural boundaries must be defined solely through background color shifts. To separate a section, transition from `surface` to `surface-container-low` or `surface-container-high`. If a boundary is needed for a "data block," use a neon glow—not a line—to define the edge.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. 
- **Base:** `surface` (#170624) or `surface-container-lowest` (#000000) for the deepest immersion.
- **Floating Containers:** Use `surface-container` or `surface-bright` to pull a card forward.
- **Nesting:** Place a `surface-container-highest` card inside a `surface-container-low` section to create a sense of mechanical depth without using drop shadows.

### The "Glass & Gradient" Rule
To avoid a flat, "digital" feel, use **Cyan Surge** (`primary`) and **Magenta Overdrive** (`secondary`) in linear gradients (45-degree angles) for high-impact CTAs. For floating overlays, apply a backdrop-blur (12px-20px) to `surface-variant` at 60% opacity, allowing the neon photography beneath to bleed through like light through smoke.

---

## 3. Typography: The Headliners
The typography pairing balances the technical precision of stage production with the human element of the artist.

*   **Display & Headlines (Space Grotesk):** Use for impact. These are your "billboard" fonts. The wide, geometric characters evoke the structural nature of stage scaffolding. Scale aggressively—`display-lg` (3.5rem) should feel massive against the dark void.
*   **Body & Titles (Epilogue):** Epilogue provides a raw, sans-serif warmth. It is highly legible but feels more "editorial" than "systematic." Use `title-lg` for pull quotes and `body-lg` for pitch narratives to maintain a high-end, zine-like quality.

---

## 4. Elevation & Depth: Tonal Layering
Traditional material design uses shadows to simulate light; this system uses *tonal shifts* to simulate stage presence.

*   **The Layering Principle:** Depth is achieved by stacking surface tiers. A `surface-container-lowest` (#000000) element appearing on a `surface-bright` (#3c204f) background creates a "cut-out" effect, mimicking a stage silhouette.
*   **Ambient Shadows:** If a floating effect is required (e.g., for a high-priority tooltip), use a glow rather than a shadow. Use `primary` or `secondary` at 15% opacity with a 40px blur to mimic a spotlight reflection.
*   **The "Ghost Border" Fallback:** If accessibility requires a border, use `outline-variant` (#544061) at 20% opacity. **Never use 100% opaque borders.**
*   **Sharp Edges:** All `borderRadius` tokens are set to `0px`. Roundness is forbidden. Sharp corners convey the "scaffolding" and "brutalist" intent.

---

## 5. Components: The Rigging

### Buttons
*   **Primary:** Sharp-edged. Background: `primary_container` (#00ffff). Text: `on_primary` (#006767). No border. On hover, apply a `primary_fixed` glow.
*   **Secondary:** Sharp-edged. Outline only using `secondary` (#ff51fa) at 2px weight. Text: `secondary`.
*   **Tertiary:** `tertiary` (#ffd16f) text only, all caps, tracked out 10% (0.1rem).

### Cards & Data Blocks
*   **Prohibition:** No divider lines. Separate content using `spacing-6` (2rem) or `surface` color shifts.
*   **Neon Data Blocks:** For key metrics (e.g., ticket sales), use a `primary` left-hand border (4px) to create a "Neon Surge" accent against a `surface-container-high` background.

### Audio Level Meters (Progress Bars)
*   Instead of horizontal bars, use vertical stacks of blocks mimicking a mixing desk. Use `primary` for the base, transitioning to `tertiary` (Amber Spot) and finally `error` (Magenta/Red) for the "peak" levels.

### Gig Poster Chips
*   Small, rectangular blocks with `label-md` text. Use `surface-variant` for backgrounds with `on_surface_variant` text to keep them secondary to the photography.

### Input Fields
*   Underline-only style using `outline`. On focus, the underline transforms into a `primary` glow. Error states use `error_dim` (#d73357) with a slight flicker animation if possible.

---

## 6. Do’s and Don’ts

### Do:
*   **Use Asymmetry:** Shift imagery to the left and text to the right. Let elements overlap.
*   **Embrace the Void:** Allow large areas of `surface-container-lowest` (#000000) to exist. It makes the neon accents pop.
*   **Apply "Light Leaks":** Use `secondary` or `tertiary` gradients at 5% opacity across the corners of the screen to simulate stage lights.
*   **Scale Typography:** Make the difference between `display-lg` and `body-md` extreme.

### Don’t:
*   **No Rounded Corners:** Never use `border-radius`. This is a hard-edged system.
*   **No Gray Shadows:** If it needs to float, it needs a colored glow or a tonal lift.
*   **No Generic Icons:** Use icons that feel architectural or technical (thin lines, 90-degree angles).
*   **No Center-Aligning Everything:** Center alignment feels like a template. Keep it left-heavy or intentionally staggered.