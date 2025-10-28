<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [JSON Data-Contract "Bible" for Case-Project-UI](#json-data-contract-bible-for-case-project-ui)
  - [0) Purpose](#0-purpose)
  - [1) Golden Invariants (pin these on every PR)](#1-golden-invariants-pin-these-on-every-pr)
  - [2) Canonical Types (TypeScript + Zod)](#2-canonical-types-typescript--zod)
    - [2.1 Event](#21-event)
    - [2.2 Source](#22-source)
    - [2.3 People Participation](#23-people-participation)
  - [3) Mapping Table (Source → Event)](#3-mapping-table-source-%E2%86%92-event)
  - [4) Indexes (touched-only)](#4-indexes-touched-only)
  - [5) API Contract (minimal, stable)](#5-api-contract-minimal-stable)
  - [6) Validation Layers (prototype stance)](#6-validation-layers-prototype-stance)
  - [7) UI Guarantees](#7-ui-guarantees)
  - [8) PR Checklists (paste into each PR description)](#8-pr-checklists-paste-into-each-pr-description)
    - [8.1 Feature PR (e.g., PR61/PR62)](#81-feature-pr-eg-pr61pr62)
    - [8.2 Refactor PR](#82-refactor-pr)
  - [9) Tests Matrix (minimums)](#9-tests-matrix-minimums)
  - [10) Runlog Evidence (copy-paste tail)](#10-runlog-evidence-copy-paste-tail)
  - [11) Migration Policy](#11-migration-policy)
  - [12) Tooling Stubs (ready to add)](#12-tooling-stubs-ready-to-add)
  - [13) Troubleshooting Drift (common gotchas)](#13-troubleshooting-drift-common-gotchas)
  - [14) "Codex Footer" (paste at the end of Codex tasks)](#14-codex-footer-paste-at-the-end-of-codex-tasks)
  - [15) What to do **right now**](#15-what-to-do-right-now)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# JSON Data-Contract "Bible" for Case-Project-UI

A compact, enforceable playbook so JSON doesn't drift. Paste this into `/Documentation/Standards/json_data_contract_bible.md` and keep it in PRs.

---

## 0) Purpose

SQL yells when you drift. JSON doesn't. This "Bible" gives you **contracts + gates + checklists** so behaviors like **auto-event on source upload**, **category filters**, **source linking**, and **People↔Event/Source roles** stay true across PRs.

---

## 1) Golden Invariants (pin these on every PR)

1. **Stable IDs**: All entities use ULIDs (`id`) that never change.
2. **Event Categories**: `event.category ∈ {"legal","factual","investigatory"}`.
3. **Auto-Event on Upload**: Ingesting any supported `source.type` must create **exactly one** `event` linked to that source (prototype: no backfills).
4. **Events may exist without a source** (prototype flexibility), but UI **nudges** to link if `category==="legal"`.
5. **Participation Links**: People can be attached to **events** and **sources** as `participants[]` with a `role`.
6. **Cites are read-through**: A CITE always points to a concrete anchor (block/time/page) that is resolvable to a `source` and optionally to an `event`.
7. **Touched-only indexing**: Indexes update **only for edited/created** items (no global rebuilds in prototype).

> If a change violates an invariant, either (a) fix the implementation or (b) update this Bible and cite the reason in the PR.

---

## 2) Canonical Types (TypeScript + Zod)

### 2.1 Event

```ts
export type EventCategory = "legal" | "factual" | "investigatory";

export type EventItem = {
  id: string; // ULID
  title: string; // system title
  customTitle?: string; // user override
  category: EventCategory;
  date?: string; // "YYYY-MM-DD"
  datetime?: string; // ISO 8601
  wizard?: {
    entity: "events";
    type: string; // e.g. "hearing", "police_report"
    answers: Record<string, any>;
    template_id: string;
    spec_version: number;
  };
  data: Record<string, any>;
  sourceId?: string;
  sourceType?: string;
  citeIds?: string[];
  participants?: Participation[];
  createdFrom?: "wizard" | "selection" | "source_upload";
  createdAt?: string;
  updatedAt?: string;
  typeId?: string;
  stableKey?: string;
};
```

### 2.2 Source

```ts
export type SourceItem = {
  id: string; // ULID
  type:
    | "transcript"
    | "court-filing"
    | "opinion"
    | "police-report"
    | "av-interview"
    | "bodycam"
    | "dashcam"
    | "911-call";
  name: string;
  path?: string;
  metadata?: Record<string, any>;
  participants?: Participation[]; // People linked to this source
  createdAt?: string;
  updatedAt?: string;
};
```

### 2.3 People Participation

```ts
export type PersonRole =
  | "speaker"
  | "witness"
  | "defendant"
  | "complainant"
  | "interviewee"
  | "interviewer"
  | "declarant"
  | "officer"
  | "caller_911"
  | "dispatcher_911"
  | "attorney"
  | "judge"
  | "other";

export type Participation = {
  personId: string; // ULID of Person
  role: PersonRole;
  eventId?: string; // optional anchor
  sourceId?: string; // optional anchor
  startMs?: number;
  endMs?: number; // AV anchor
  page?: number; // PDF anchor
  note?: string;
  addedAt?: string;
  addedBy?: string;
};
```

### 2.4 Case (PR87)

```ts
export type CourtKind = "district" | "circuit" | "mcoa" | "msc";

export type CaseCourt = {
  kind: CourtKind;
  code?: string; // For district/circuit only. Up to 3 letters/digits, e.g., "36", "41A", "14B"
  numbers: string[]; // One or more docket/case numbers
  judges?: string[]; // Optional: one or more judges tied to THIS case for the selected court
  isDefault?: boolean; // If true, this is the default court for the case (max one per case)
};

export type CaseItem = {
  id: string; // ULID
  title: string; // e.g., "People v. Smith"
  description?: string;
  courts: CaseCourt[]; // ≥1; each with ≥1 number
  isDefault?: boolean; // If true, this is the default case for the project (max one per project)
  createdAt?: string;
  updatedAt?: string;
};
```

**Golden Invariants (Cases)**:

1. Each Case has ≥1 court.
2. Each listed court has ≥1 docket/case number.
3. For district/circuit, `code` is required (1–5 chars matching regex `^[A-Za-z0-9-]{1,5}$`). For mcoa/msc, `code` is forbidden.
4. `judges[]` is optional and scoped to the specific CaseCourt entry.
5. Max one `isDefault=true` court per case; max one `isDefault=true` case per project.

**Court Dropdown Data**:

- `constants/mi_courts.ts` provides labeled options for District/Circuit selection (sourced from Wikipedia, Oct 28, 2025).
- Update on a touched-only basis when court structures change.

> Use Zod schemas mirroring these types for **shape validation** at API boundaries.

---

## 3) Mapping Table (Source → Event)

These mappings **must** exist and be used by ingest:

| source.type   | event.type (title seed) | category      |
| ------------- | ----------------------- | ------------- |
| transcript    | Court Hearing           | legal         |
| court-filing  | Court Filing            | legal         |
| opinion       | Court Filing            | legal         |
| police-report | Police Report           | investigatory |
| av-interview  | A/V Interview           | investigatory |
| bodycam       | Body Camera             | investigatory |
| dashcam       | Dash Camera             | investigatory |
| 911-call      | 911 Call                | investigatory |

**Invariant #3**: creation is **1:1** and immediate on successful upload.

---

## 4) Indexes (touched-only)

Persist **small** JSON indexes; update them only when related entities change:

- `eventsBySource.json`: `{ [sourceId]: string[] /* eventIds */ }`
- `eventsByCategory.json`: `{ legal:string[], factual:string[], investigatory:string[] }`
- `sourcesByPerson.json`: `{ [personId]: string[] /* sourceIds */ }`
- `eventsByPerson.json`: `{ [personId]: string[] /* eventIds */ }`
- `citesByEvent.json`: `{ [eventId]: string[] /* citeIds */ }`

> Never scan full stores inside UI. Prefer these lookups.

---

## 5) API Contract (minimal, stable)

- `PUT /api/events/:id/source` → `{ sourceId }` links/replaces source.
- `POST /api/events/:id/duplicate` → clones, suffix "(Copy)", sets `requiresModification: true` in response.
- `DELETE /api/events/:id` → removes event (non-destructive to sources/cites).
- `GET /api/events/by-source/:sourceId` → `[EventSummary]`.
- `GET /api/events?category=...` → `[EventSummary]`.
- `POST /api/events/:id/participants` / `DELETE .../participants/:idx`.
- `POST /api/sources/:id/participants` / `DELETE .../participants/:idx`.
- `GET /api/people/:personId/appearances` → `{ events:[], sources:[] }`.

**Rule**: If you add an endpoint, add a **contract note** to this Bible and a test.

---

## 6) Validation Layers (prototype stance)

- **Layer A: Shape** (Zod): run on every API write. Reject missing required fields, bad enums, wrong types.
- **Layer B: Soft rules**: no blocking for unlinked `legal` events—render UI tips instead.
- **Layer C: Referential**: **disabled** in prototype (no sweeping checks), but provide a `validate-now` script devs can run locally.

Sample `validate-now` (touched files only):

```bash
node tools/validate_touched.js  # identifies changed entities in this branch
# For each changed entity:
# 1) parse via Zod
# 2) warn (console) if legal event has no source
# 3) warn if participants reference unknown personId/sourceId/eventId (no fail)
```

---

## 7) UI Guarantees

- **EventDetailsView** shows **Linked Source** chip with Link/Replace; shows **non-blocking** tip for `legal && !sourceId`.
- **Source upload** → toast "Event created: <title>" (optional navigate).
- **People Panel** shows **Appearances** tabs (Events, Sources) with role badges.
- **Cite create** from transcript speaker block → suggests linking that speaker to the event/source.

---

## 8) PR Checklists (paste into each PR description)

### 8.1 Feature PR (e.g., PR61/PR62)

- [ ] Respects **Golden Invariants** (Sec. 1).
- [ ] Source→Event mapping unchanged (or updated here if intended).
- [ ] All new/changed types updated in `types/` and Zod schemas.
- [ ] Index writers updated for all create/update/delete paths you touched.
- [ ] UI: EventDetailsView source chip & legal-tip behavior unchanged.
- [ ] People participation UI present where relevant (Events/Sources).
- [ ] Added/updated **unit**, **integration**, and **e2e** tests (Sec. 9).
- [ ] Appended lint/test/build tails to runlog.
- [ ] This Bible updated if contracts changed.

### 8.2 Refactor PR

- [ ] No change to mapping table or invariants unless explicitly documented.
- [ ] Index updates still triggered on touched entities.
- [ ] CI runs **validate_touched** and tests.

---

## 9) Tests Matrix (minimums)

| Area                 | Unit                                 | Integration                                                     | E2E                                                           |
| -------------------- | ------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------- |
| Event source link    | shape validation                     | `PUT /events/:id/source` updates event & `eventsBySource`       | Link/Replace from EventDetailsView reflects instantly         |
| Auto-event on upload | mapper returns correct type/category | ingest → new event with `sourceId`                              | Upload police report → see event in list with source icon     |
| Legal tip            | rendering logic                      | n/a                                                             | Tip shows for `legal && !sourceId`, disappears after linking  |
| Duplicate/Delete     | title suffix & requiresModification  | `DELETE` removes & index prunes                                 | Duplicate requires 1 edit before save; Delete returns to list |
| People participation | schema shape                         | add/remove participant updates `eventsByPerson/sourcesByPerson` | Person panel lists appearances with role badges               |
| Cites suggestion     | n/a                                  | transcript block speaker recognized                             | Creating cite prompts person suggestion                       |

---

## 10) Runlog Evidence (copy-paste tail)

Every PR must include the last ~20 lines of:

```
npm run lint
npm test
npm run build
```

…and a short **Manual Smoke** list (2–4 bullets) showing the invariant behaviors still hold.

---

## 11) Migration Policy

- **Prototype**: **No migrations.** Ignore legacy drift; only update touched records.
- **Hardening phase (future)**: introduce `gate:data` script to fail CI on:
  - `legal` events without `sourceId` (if/when you decide to enforce)
  - unknown `personId/eventId/sourceId` in participants
  - cites pointing to missing anchors

> Until then, keep gates non-blocking and focused on new writes.

---

## 12) Tooling Stubs (ready to add)

**`tools/index_writer.ts`** (called by routes/services that change data):

```ts
export async function onEventWrite(ev: EventItem) {
  await updateEventsByCategory(ev);
  if (ev.sourceId) await addEventToEventsBySource(ev.sourceId, ev.id);
  if (ev.participants) await updateEventsByPersonIndex(ev.id, ev.participants);
}

export async function onEventDelete(ev: EventItem) {
  await removeEventFromCategory(ev);
  if (ev.sourceId) await removeEventFromEventsBySource(ev.sourceId, ev.id);
  await removeEventFromEventsByPersonIndex(ev.id);
}
```

**`tools/validate_touched.js`** (prototype warnings only):

```js
// pseudo:
const touched = getTouchedEntitiesFromGitDiff();
for (const ev of touched.events) {
  zEvent.parse(ev); // shape
  if (ev.category === "legal" && !ev.sourceId)
    warn("Legal event without source", ev.id);
}
for (const link of touched.participations) {
  if (!maybePerson(link.personId)) warn("Unknown personId", link);
}
process.exit(0); // never fail prototype
```

---

## 13) Troubleshooting Drift (common gotchas)

- **New source uploaded but no event created** → ingest path isn't calling `createEventForSource()`.
- **Event list slow** → you're scanning instead of using `eventsByCategory`.
- **Legal tip not showing** → UI lost the `category` prop or state mapping.
- **People appearances empty** → participation wasn't added, or indexes not updated on write.
- **Duplicate saves without change** → the `requiresModification` flag isn't checked in UI.

---

## 14) "Codex Footer" (paste at the end of Codex tasks)

```
Honor the JSON Data-Contract Bible at Documentation/Standards/json_data_contract_bible.md:
- Keep Golden Invariants intact.
- Use the Source→Event mapping table for ingest.
- Update touched-only indexes on write/delete.
- Maintain EventDetailsView source chip + non-blocking legal tip.
- Preserve People participation links and appearances.
Run lint/test/build and paste tails into the PR runlog.
```

---

## 15) What to do **right now**

- Add this file to `/Documentation/Standards/json_data_contract_bible.md`. ✅
- In PR61 & PR62 descriptions, include the **PR checklist** (Sec. 8.1).
- Ask Codex to:
  1. Add Zod schemas mirroring Sec. 2 to your API boundaries (if not already present).
  2. Add `tools/index_writer.ts` hooks to event/source write paths.
  3. Add `tools/validate_touched.js` (prototype warnings only) and a `npm run validate:touched` script.

This way, even without SQL, your JSON stays honest, predictable, and future-proof.
