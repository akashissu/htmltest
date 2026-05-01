# Architect Plan — PAP-276

## Scope Summary
Design a **chat application layout using HTML and CSS** inside the existing static single-page app. The requested UI must include:
- a sidebar with contacts,
- a conversation area,
- a message input box.

The result should feel **neat, responsive, and user-friendly**, with a clear visual hierarchy and practical spacing for desktop and mobile.

## Current Stack Inspection
From the sandbox inspection:
- The project is a **single static page** driven by `index.html`.
- Styling currently lives inside an embedded `<style>` block.
- No framework, package manager, or component architecture is visible.
- Existing UI uses:
  - CSS variables,
  - Grid/Flex layout,
  - rounded panels,
  - subtle shadows,
  - semantic sections.

This means the safest implementation path is a **single-file HTML/CSS rewrite or replacement** inside `index.html`.

## UX Goal
The page should look like a modern messaging interface with three immediately recognizable zones:
1. **Sidebar / contacts pane**
2. **Main conversation pane**
3. **Bottom input composer**

The interface should be easy to scan, with clear separation between navigation and conversation content.

## Recommended Visual Direction
Aim for a clean, modern messaging aesthetic:
- soft background gradient or muted neutral page background,
- white or lightly tinted panels,
- one strong accent color for active states and sent messages,
- rounded cards and bubbles,
- light borders and soft shadows,
- comfortable spacing and readable typography.

Recommended palette direction:
- cool blue / indigo / slate,
- or soft teal / navy / gray,
- with muted text for timestamps and previews.

## Recommended Implementation Strategy
Because the repo is plain HTML/CSS, implementation should:
1. Replace the current weather-specific layout in `index.html`.
2. Keep all code self-contained in the existing file.
3. Build the chat page with semantic sections and reusable classes.
4. Use CSS Grid for high-level desktop layout and Flexbox for internal alignment.

## Proposed Page Structure
Recommended structure:
- `<main class="chat-app">`
  - `<aside class="sidebar">`
    - app/header area
    - search field or label (optional but useful)
    - contacts list
  - `<section class="chat-panel">`
    - conversation header
    - scrollable message list area
    - message input/composer area

### Sidebar content
Suggested elements:
- title such as `Messages` or `Chats`
- optional search field for polish
- vertical list of contact previews

Each contact preview can include:
- avatar circle or image,
- contact name,
- message preview,
- timestamp,
- active/unread state.

### Conversation area content
Suggested elements:
- top header with active contact name + status
- message thread with alternating bubble alignment
- bottom composer with text input and send button

## Content Recommendation
Use a small mock chat dataset in static HTML to make the layout feel complete.

Recommended sample content:
- 4–6 contacts in the sidebar
- 5–8 chat bubbles in the active conversation
- a mixture of incoming and outgoing messages
- subtle timestamps or delivery state labels

This gives the page enough density to feel realistic without becoming cluttered.

## Layout Recommendation
### Desktop
Use a two-column layout:
- sidebar: fixed or capped width, approximately 280px–340px
- chat panel: flexible remaining width

Recommended outer approach:
- `.chat-app` uses CSS Grid with two columns
- overall container centered with max width
- full-height card feel inside viewport

### Tablet / Mobile
At narrower widths:
- reduce sidebar width first,
- then stack to a single column if needed,
- preserve the message composer at full width,
- keep touch-friendly spacing.

A strong fallback is:
- desktop/tablet: two-column layout
- mobile: single-column layout with sidebar above chat panel

## Styling Plan
### Global styling
Introduce chat-friendly CSS variables for:
- page background,
- panel background,
- border color,
- primary accent,
- text and muted text,
- sent and received bubble colors,
- radius and shadow values.

### Main app shell
Style the overall app container with:
- centered max width,
- rounded corners,
- soft shadow,
- overflow hidden,
- minimum height large enough to feel like a chat app window.

### Sidebar
Sidebar should include:
- subtle background contrast from the main chat area,
- right border divider,
- internal vertical spacing,
- clearly highlighted active contact row,
- hover states on contact items.

### Contact list items
Each contact row should have:
- avatar,
- name,
- preview,
- timestamp,
- optional unread badge.

Use compact, readable spacing and text truncation where needed.

### Conversation header
Header should show:
- contact avatar or initials,
- contact name,
- online/last seen status,
- optional action icons if desired, though not required.

### Message thread
Use a message list with:
- incoming bubbles aligned left,
- outgoing bubbles aligned right,
- distinct bubble background colors,
- readable max width per bubble,
- spacing between messages,
- optional tiny timestamps.

### Composer
The bottom composer should include:
- text input,
- send button,
- rounded input styling,
- clear separation from the message thread.

The composer should remain visually anchored at the bottom of the chat panel.

## Accessibility Guidance
The implementation should preserve accessibility by:
- using semantic elements (`aside`, `section`, `header`, `form`, `button`),
- keeping form controls keyboard-focusable,
- using clear color contrast,
- ensuring button text/icons remain legible,
- adding descriptive `aria-label` values where useful.

## Suggested Grunt Implementation Steps
1. Open `index.html`.
2. Replace weather-specific title, styles, and markup with chat-specific structure.
3. Build a two-pane chat layout using CSS Grid/Flexbox.
4. Add a sidebar with several contact previews.
5. Add a conversation panel with static sample messages.
6. Add a composer row with input and send button.
7. Add responsive breakpoints for tablet/mobile layouts.
8. Leave a Grunt handoff artifact summarizing changed files and verification steps.

## Suggested Pedant Review Focus
The Pedant should verify:
- all required UI areas exist: sidebar, conversation area, input box,
- layout is neat and responsive,
- active chat hierarchy is visually clear,
- message bubbles are readable and aligned correctly,
- sidebar items are legible and not overcrowded,
- no leftover weather-specific content/classes remain in the rendered UI,
- markup remains semantic and accessible.

## Files Expected To Change In Implementation Phase
Likely implementation changes should be limited to:
- `index.html`

Expected role artifacts later:
- `GRUNT_HANDOFF_PAP-276.md`
- `PEDANT_HANDOFF_PAP-276.md`
- `TERMINAL_LOGS_PAP-276_GRUNT.txt`

## Explicit Non-Goals For This Phase
- No HTML/CSS implementation in this architect phase
- No JavaScript chat functionality
- No backend or real-time messaging logic
- No PR creation
- No git push

## Handoff Summary
The next role should transform `index.html` into a polished static chat UI with a left contacts sidebar, a right conversation pane, and a bottom message composer. The implementation should stay single-file, responsive, and visually modern, with sample chat content that makes the layout feel realistic and easy to review.
