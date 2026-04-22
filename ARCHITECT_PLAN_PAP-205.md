# ARCHITECT PLAN — PAP-205

## Ticket
Design a chat application layout using HTML and CSS.

## Scope Summary
Build a chat page featuring:
- sidebar contacts
- conversation area
- message input box

Design direction:
- neat
- responsive
- user-friendly

Constraints for implementation phase:
- HTML and CSS first
- keep changes production-safe and minimal
- no PR creation in non-scribe roles

---

## Current Stack / Structure Observations
Repository snapshot at planning time:
- Main frontend entrypoint is `index.html`
- Styling is currently inline inside a `<style>` block in `index.html`
- No external build tooling detected from the repo root
- Current page is a **fitness dashboard** single-file implementation
- Repo conventions suggest full-page replacements are acceptable when the ticket changes page type significantly

### Implication
A chat application layout is structurally different from the current dashboard. The cleanest implementation is a **single-page replacement in `index.html`**, keeping the same one-file delivery pattern and using inline CSS unless Grunt finds a safer reason to split it.

---

## High-Level Recommendation
Implement PAP-205 as a complete chat UI page in `index.html`.

Why this is the right move:
- the requested information architecture is different from the current dashboard
- trying to preserve dashboard sections would create visual clutter
- a chat layout benefits from a deliberate two-panel shell with height management
- a focused replacement reduces regression risk from unrelated old styles

---

## Recommended Page Structure
Use a single responsive app shell with two primary columns.

Suggested structure:
- `<main class="chat-page">`
- `<section class="chat-shell">`
  - `<aside class="chat-sidebar">`
  - `<section class="chat-main">`

Suggested class blocks:
- `.chat-page`
- `.chat-shell`
- `.chat-sidebar`
- `.chat-sidebar__header`
- `.chat-search`
- `.chat-contact-list`
- `.chat-contact`
- `.chat-contact--active`
- `.chat-contact__avatar`
- `.chat-contact__body`
- `.chat-contact__preview`
- `.chat-main`
- `.chat-main__header`
- `.chat-thread`
- `.chat-day-label`
- `.chat-message`
- `.chat-message--incoming`
- `.chat-message--outgoing`
- `.chat-message__bubble`
- `.chat-composer`
- `.chat-composer__input`
- `.chat-composer__send`

---

## Information Architecture Plan

### 1) Sidebar contacts area
Purpose:
- help the page read immediately as a chat application
- provide scanable contact/conversation entry points

Recommended contents:
- app/product title
- optional small utility action (new chat icon/button)
- search field
- 5–7 contact rows

Each contact row should include:
- avatar or initial badge
- contact name
- short message preview
- timestamp
- optional unread badge
- active/current selection state on one item

Design notes:
- rows should be compact but comfortably tappable
- longer preview text should truncate, not wrap into tall uneven cards
- selected contact should be visibly distinct without overwhelming the layout

### 2) Conversation header
Purpose:
- establish who the current chat is with
- visually separate the contact list from the active thread

Recommended contents:
- selected contact avatar
- contact name
- lightweight status text like “Online” or “Last active 2m ago”
- optional utility buttons (call, more, info) as decorative/placeholder UI

### 3) Conversation thread
Purpose:
- display the active conversation clearly with readable message grouping

Recommended contents:
- a day divider such as “Today” or “Tuesday”
- 6–10 sample messages
- mix of incoming and outgoing messages
- visible timestamps in or near bubbles

Message guidance:
- incoming and outgoing bubbles should align differently
- max width should be capped for readability on large screens
- messages should support multi-line wrapping cleanly
- use sample copy that feels realistic and professional

### 4) Message input box / composer
Purpose:
- fulfill the core ticket requirement with a clear interactive affordance

Recommended contents:
- text input or textarea
- optional attachment icon/button placeholder
- send button

Recommended behavior at layout level:
- anchored at bottom of chat panel
- large enough tap targets for mobile
- clear placeholder text such as `Type a message...`

---

## Layout Strategy

### Desktop
Recommended layout:
- sidebar fixed around 280px–340px
- main conversation panel fills remaining width
- full app centered in viewport with generous padding
- thread should have a defined vertical space so it feels like a real chat client rather than a long document

### Tablet
- preserve two-column layout if space allows
- slightly reduce padding and gaps
- keep sidebar readable and avoid overly narrow message column

### Mobile
Recommended layout:
- stack sidebar above conversation panel
- keep contact rows scrollable within their section if needed
- keep composer full width
- bubble widths should expand but still leave breathing room

Critical mobile safeguards:
- no horizontal scrolling
- no clipped timestamps or badges
- search and composer should remain easy to tap

---

## Visual Style Direction
Aim for a modern messaging UI with calm polish.

Recommended design language:
- soft cards or glassmorphism panels
- rounded message bubbles
- subtle gradients or accent highlights
- clean hierarchy and good spacing
- strong contrast between primary text and supporting metadata

Possible palette direction:
- cool blue/teal/green accents
- neutral dark or lightly frosted surfaces
- muted grays for timestamps/previews

Overall feel should be:
- tidy
- contemporary
- calm
- practical

---

## CSS Implementation Guidance
Grunt should prioritize these style concerns:

### Structural styling
- full-height page shell
- responsive two-column grid
- distinct sidebar and main panel surfaces
- overflow management for contact list and thread

### Contact list styling
- equal internal spacing
- avatar alignment consistency
- truncated text for name/preview rows
- active/hover/focus states

### Message styling
- clear distinction between incoming and outgoing bubbles
- comfortable line height
- capped bubble width
- subtle timestamp styling
- spacing that makes the thread easy to scan

### Composer styling
- visible but not oversized input region
- send button with clear emphasis
- focus-visible styling for accessibility

---

## Accessibility / Correctness Requirements
- use semantic sectioning and heading structure
- add accessible labels to search and message input
- preserve visible `:focus-visible` states
- ensure text contrast is strong enough for previews, statuses, and timestamps
- keep DOM order logical when stacked on mobile
- ensure long text wraps instead of overflowing

---

## Suggested Content Plan

### Contacts
Use varied sample entries such as:
- Maya Chen
- Design Sync
- Julian Park
- Product Team
- Noah Reed

### Thread
Use realistic short-form collaboration chat content, for example:
- feedback on layout
- responsive polish
- handoff timing
- simple status updates

### Composer placeholder
- `Type a message...`

---

## Reliability / Regression Risks
Grunt should watch for:
- old dashboard-specific styles leaking into the new layout
- missing height constraints causing the thread to expand awkwardly
- long contact names or previews overflowing on narrow screens
- outgoing/incoming bubbles becoming visually too similar
- composer controls stacking awkwardly on small mobile widths
- decorative effects reducing readability

---

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a chat application
- verify sidebar contacts, conversation area, and message input box are all present
- verify desktop layout uses a clear two-panel structure
- verify mobile layout stacks cleanly without horizontal overflow
- verify contact text truncation behaves correctly
- verify long message text wraps inside bubbles
- verify focus states are visible on search, contacts, and send controls
- verify the page feels neat and user-friendly rather than crowded

---

## Files Expected to Change in Grunt Phase
Primary expected file:
- `index.html`

Optional only if Grunt decides it is safer:
- split CSS to a separate file, but only if that reduces risk and remains minimal

---

## Artifact for Next Role
Grunt should replace the current dashboard page with a responsive chat layout in `index.html`, using a contacts sidebar, active conversation panel, and bottom composer area, with polished HTML/CSS structure and careful mobile behavior.
