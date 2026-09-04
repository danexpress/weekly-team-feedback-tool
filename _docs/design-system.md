# Design System

Read this before touching any UI-facing code — a screen, a component,
or copy. The goal is that the retrospective board, feedback form, and
summary all feel like one product, not three separately-designed
screens.

## Foundations

### Color

- **Start / Stop / Continue** each get one consistent accent color used
  everywhere they appear (the feedback form's three sections, cards,
  cluster headers). Don't introduce a fourth ad-hoc color for a new
  status — extend the existing palette instead.
- **Status colors** are separate from the Start/Stop/Continue accents:
  - Discussion status: Discussed / Skipped / Deferred each get a
    distinct, consistent color.
  - Action item status: Open / Done.
  - Upload processing status: pending / processing / done / failed.
- Reserve red/warning colors for destructive actions and failure
  states only — don't use them decoratively.
- All text/background pairings must meet WCAG AA contrast.

### Typography & spacing

- One type scale and one spacing scale, used consistently — don't
  introduce one-off font sizes or margins per screen.
- Feedback card text is short by design (per the product plan); the
  card component should be built for 1–2 lines of text, not a long-form
  text block.

## Core components

Build these once and reuse them everywhere, rather than re-implementing
per screen:

- **Card** — a single Start/Stop/Continue entry. States: default,
  anonymous, being edited (own card only), read-only.
- **Anonymous badge** — one consistent visual treatment wherever an
  anonymous card appears. It must never render an author name or
  initials, even in a tooltip or on hover.
- **Cluster** — a container of cards with a rename affordance, a vote
  count (hidden until voting closes), and a discussion-status badge.
- **Vote control** — shows a team member's remaining votes (starts at
  3) and lets them stack multiple on one cluster. Must work without
  drag-and-drop as a fallback (tap/click to add a vote), since not
  every interaction can assume a mouse.
- **Status badge** — shared component for discussion status, action
  item status, and upload status; only the color/label set changes.
- **Empty state** — every list (cards, clusters, action items,
  retrospectives) needs a designed empty state, not a blank screen.

## Interaction states

Every interactive component needs an explicit design for:

- Loading (e.g. clustering suggestions still processing, transcript
  still uploading)
- Empty (nothing submitted yet)
- Error (submission failed, upload failed)
- Populated / default

Don't ship a component that only handles the happy path.

## Accessibility

- Every interactive element must be reachable and operable by
  keyboard, including moving a card between clusters and casting a
  vote — these cannot be mouse/drag-only.
- Anonymity must hold up for screen reader users too: no author
  information in the accessible name/label of an anonymous card.
- Focus order should follow the visual/logical order of each screen
  (form sections, board columns, agenda list).

## Realtime updates

Because the retrospective board updates live for everyone in the room
(reveal, cluster changes, vote-close, discussion status), any UI change
to the board must define what happens when a change arrives from
another user while you're mid-interaction (e.g. you're dragging a card
when someone else renames its cluster). Prefer a subtle, non-disruptive
update (no layout jump, no lost in-progress input) over silently
overwriting local state.
