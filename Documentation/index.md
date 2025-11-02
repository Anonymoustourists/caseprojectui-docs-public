# Documentation index

This folder is the canonical documentation for the project. Use the inventories and decisions in `Documentation/INVENTORY/` to review migrations from `docs/`.

## Inventory & decisions

- Inventory snapshot (enriched): `Documentation/INVENTORY/docs-inventory-2025-10-31.json`
- First-pass decisions: `Documentation/INVENTORY/docs-inventory-2025-10-31-decision-2025-10-31.json`

## Archives

Archived copies of files from `docs/` are stored under:

`Documentation/archive/docs-archive-2025-10-31/`

Each archived file has a sibling `.meta.json` containing source path, commit SHA and commit date.

## Migration notes

- Work is being performed on branch `chore/docs-cleanup/2025-10-31`. Nothing on `main` has been deleted.
- Draft migrated files are created under `Documentation/` with a provenance header. Review and clean before merging.

- Batch 2 (2025-10-31): added 3 draft migrations into `Documentation/devnotes/` (provenance headers and `.migrated.meta.json` siblings added). Review before merging.

If you are reviewing migrations, start with the decisions JSON and then inspect the drafts in `Documentation/devnotes/` and `Documentation/architecture/`.
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [📘 Project Index — Case Project Rebuild](#-project-index--case-project-rebuild)
  - [How to use this file](#how-to-use-this-file)
  - [🚧 In Progress / Incomplete PRs (top = higher priority)](#-in-progress--incomplete-prs-top--higher-priority)
  - [✅ Completed PRs](#-completed-prs)
  - [🔧 Completed Hotfixes](#-completed-hotfixes)
  - [🗂️ Work Categories (file under one or more)](#️-work-categories-file-under-one-or-more)
    - [🏗️ Foundation \& UI](#️-foundation--ui)
    - [📂 Project Management](#-project-management)
    - [📥 Source Ingestion](#-source-ingestion)
    - [✏️ Source Editing](#️-source-editing)
    - [📊 Data Management \& Associations](#-data-management--associations)
    - [📄 Source View](#-source-view)
    - [📝 Notes \& Notebooks](#-notes--notebooks)
    - [📤 Exporting](#-exporting)
    - [⚙️ Infrastructure](#️-infrastructure)
  - [Quick links \& patterns](#quick-links--patterns)
  - [🗓️ Sessions](#️-sessions)
  - [PR workflow checklist](#pr-workflow-checklist)
  - [Gating policy and commands](#gating-policy-and-commands)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 📘 Project Index — Case Project Rebuild

**Location:** `/Documentation/Index.md`  
**Last updated:** October 2025

This file is the single source of truth for the rebuild. Track every PR here and keep it current.

---

## How to use this file

- When you **start** a PR: add it under **In Progress / Incomplete PRs** and put it in the right **Work Category** below.
- Each PR should have a triplet in `/Documentation/PRs/`:
  - `pr<N>.md` (design/spec)
  - `pr<N>-manifest.json` (machine-readable change list)
  - `runlog-PR<N>.md` (evidence: lint/test/build output + manual check)
- When you **finish** a PR: move it to **Completed PRs**.
- **Tiny fixes** (typos, path updates, doc corrections) may be logged under `/Documentation/PATCHES/` instead of a PR. See PATCHES/README.md for workflow.

Legend:

- `[ ]` not done / planned `[x]` complete `⚙️` in progress `🔜` planned

---

## 🚧 In Progress / Incomplete PRs (top = higher priority)

- ⚙️ **PR 87** — Case Registry & Court Dropdowns (MI District/Circuit) + Optional Judges + Default Designation

- ⚙️ **PR 80** — Emoji and Icon Support for Events, People, Locations, and Sources
- ⚙️ **PR 86** — Transcript Witness Sections & Phase Navigator
- ⚙️ **PR 72** — Form Detection System: Document-Type-Specific Detectors and Template Creation (Michigan court forms)
- ⚙️ **PR 66** — Enhanced Notebooks: Rich Text Rendering, Heading Navigation, and CITES View
  - Oct 2025: Single-pane WYSIWYG note editor with cite chips landed; follow-ups on serializer depth & editor engine migration tracked in todo.md
- 🔜 **PR 60** — Enhanced Event System: Categories, Source Linking, Edit & Duplicate
- ⚙️ **PR 1** — Foundations: Layer System & Overlay Manager-- ?may be done/outdated already?
- ⚙️ **PR 2** — Canonical Storage + Export-- ?may be done/outdated already?
- ⚙️ **PR 35** — Unified Event System with Cite-Event Association-- ?may be done/outdated already?
- ⚙️ **PR 35A** — Enhanced Event System Implementation Details (bi-directional index, participants, atomic endpoints)-- ?may be done/outdated already?
- ⚙️ **PR 37** — Replace PDF Ingestion with Layout-Aware Pipeline (HURIDOCS) + Transcript Mode
- ⚙️ **PR 40** — Project Info Panel & Registries-- ?may be done/outdated already?
- 🔜 **PR 13** — Performance & UX polish
- 🔜 **PR 15** — Unified Export & Integrity (checksums, validation)
- 🔜 **PR 16** — Note templates
- 🔜 **PR 17** — Export Notes → Word (.docx)
- ⚙️ **PR 26** — Project Shell & Project-scoped Sources-- ?may be done/outdated already?
- 🔜 **PR 27** — Self-Contained Projects + Registry -- ?may be done/outdated already?

- ⚙️ **PR 51** — Normalization pass (Text Extract: linebreaks, hyphenation, headers/footers)
- 🔜 **PR 52** — Heading detector v2 (Text Extract)
- 🔜 **PR 53** — Page-type classifier v2 (Text Extract)
- 🔜 **PR 54** — Citation anchors & quote robustness (Text Extract)
- 🔜 **PR 55** — Tables/figures & exhibits handling (Text Extract)
- 🔜 **PR 56** — Performance & determinism (Text Extract)
- 🔜 **PR 57** — Eval dashboard & gold sets (Text Extract)

> Tip: when you add a new PR, also list it under the appropriate **Work Category** below.

---

## ✅ Completed PRs

- [x] **PR 3** — Ingestion UI + Source Storage + Standardized Filenames
- [x] **PR 87** — Docs normalization to satisfy markdownlint gates; archives ignored.
- [x] **PR 4** — Export Markdown
- [x] **PR 5** — Ingestion → Canonical (minimal happy path)
- [x] **PR 6** — Viewer ↔ Canonical mapping (read-only)
- [x] **PR 7** — Block-level editing to canonical (no spans)
- [x] **PR 8** — Real ingestion → canonical blocks
- [x] **PR 9** — Read-only cite preview in canonical viewer
- [x] **PR 10** — Create & persist cites
- [x] **PR 11** — Notes overlay: cite-aware Markdown
- [x] **PR 12** — Notes editing + insert-cite macro
- [x] **PR 12A** — Notes formatting toolbar
- [x] **PR 12B** — Notes outline / Table of Contents
- [x] **PR 12C** — Speaker association & editing
- [x] **PR 14** — Unified selection popover: CITE | TAG | EVENT
- [x] **PR 18** — DocumentViewer narrative flow
- [x] **PR 19** — PDF/Text toggle with page-sync infrastructure
- [x] **PR 20** — Narrative prose on main view
- [x] **PR 21** — Narrative selection cite preview
- [x] **PR 22** — Inline narrative editing
- [x] **PR 23** — Integrate PDF.js viewer and complete PDF↔TEXT toggle
- [x] **PR 24** — A/V Player with Transcript Sync
- [x] **PR 25** — Wire new text-storage system to existing Whisper transcription module
- [x] **PR 26A** — Fix: Project-scoped file fetch (`/api/files`) in DocumentViewer
- [x] **PR 28** — JSON-driven wizard specs (Sources/People/Events)
- [x] **PR 29** — Notebook Integration + Header Removal
- [x] **PR 30** — People: JSON-Wizard Creation + Per-Project Store
- [x] **PR 31** — Events: JSON-Wizard Creation + Per-Project Store
- [x] **PR 32** — Fix: Selection Popover Stale Closure Bug (restores PR14 functionality)
- [x] **PR 33** — Fix: Project Context Not Synced to Canonical Docs Store (project isolation)
- [x] **PR 34** — Fix: Selection Popover UX (positioning, input focus, dialogue support)
- [x] **PR 36** — Event Details View with Cite Management (Frontend complete, awaiting backend testing)
- [x] **PR 36B** — Backend Fix: Cite Validation Alignment (Implemented, awaiting verification)
- [x] **PR 38** — Adapters + Catalog System (Declarative YAML adapters for document-type detection and processing)
- [x] **PR 41** — Sources Viewer UX polish: cite dropdown, inline chips, simplified Dialogue view
- [x] **PR 58** — Cleanup: remove heavy corpora from main; documentation and runlog added (merged via <https://github.com/Anonymoustourists/caseprojectui/pull/11>)
- [x] **PR 59** — Fix Missing Wizard JSON Files (Broken Symlinks) — Restored wizard functionality for creating people, events, and sources
- [x] **PR 88** — Root tidy: archive ephemeral files & unify ESLint flat config (merged via <https://github.com/Anonymoustourists/caseprojectui/pull/14>) — commit `0ff816d1386c223af49e20a3b5a6008b68fda188`

<!-- migrated PRs -->

- [x] **PR 67** — Smart File Type Filtering — [PR notes](PRs/PR67-SMART-FILE-TYPE-FILTERING.md)
- [x] **PR 68** — Sources Wizard Restructure — [design & runbook](PRs/PR68-WIZARD-RESTRUCTURE.md)
- [x] **PR 78** — MI Maps + Address Autocomplete (Photon/Nominatim) + Locations Section — [design](PRs/in-progress/pr78.md) · [LOCATIONS_DESIGN](LOCATIONS_DESIGN.md)

### Triage — 2025-10-30

- PR85 — completed: implemented (commit abc123). (Stamped TRIAGE; moved from in-progress.)
- pr78 — completed: implemented (maps). (Stamped TRIAGE; moved from in-progress.)
- runlog-PR87.md — completed: formatting-only cleanup committed (2010840). (Stamped TRIAGE; moved from in-progress.)
- pr61 — archived: superseded by PR64. (Stamped TRIAGE; moved from in-progress.)
- pr86 — archived: partial attempt; will re-open clean later. (Stamped TRIAGE; moved from in-progress.)

---

## 🔧 Completed Hotfixes

> Small, surgical fixes that didn't warrant a full PR. See `/Documentation/PATCHES/` for details.

- [x] **2025-10-10** — [docs-infrastructure](PATCHES/patch-2025-10-10-docs-infrastructure.md) — Created patching workflow templates, integrity checker, enhanced PATCHES/README
- [x] **2025-10-10** — [people-events-tags-ui](PATCHES/patch-2025-10-10-people-events-tags-ui.md) — Added People, Events, and Tags UI sections with mock data following Sources pattern
- [x] **2025-10-11** — [police-report-ocr](PATCHES/patch-2025-10-11-police-report-ocr.md) — OCR pipeline + fuzzy-match adapter for corrupted police reports
- [x] **2025-10-11** — [dunning-complete](PATCHES/patch-2025-10-11-dunning-complete.md) — Complete ingestion of 327 Dunning police report chunks
- [x] **2025-10-11** — [ingest-baseline](PATCHES/patch-2025-10-11-ingest-baseline.md) — Locked adapters & catalog at `ingest-baseline-251011`
- [x] **2025-10-11** — [dunning-batch-complete](PATCHES/patch-2025-10-11-dunning-batch-complete.md) — Full Dunning corpus ingestion: 143 documents (99.3% success), 38 transcripts, 8+ document types
- [x] **2025-10-11** — [adapter-auto-integration](PATCHES/patch-2025-10-11-adapter-auto-integration.md) — Integrated adapter auto-selection into CLI ingestion pipeline
- [x] **2025-10-14** — [dialogue-multiblock-selection](PATCHES/patch-2025-10-14-dialogue-multiblock-selection.md) — Fixed multi-block text selection in dialogue/transcript view to enable CITE/TAG/EVENT popup across speaker boundaries + added merge buttons to join consecutive dialogue blocks
- [x] **2025-10-13** — [agency-date-autopop](PATCHES/patch-2025-10-13-agency-date-autopop.md) — Fixed agency dropdown in A/V Police Interview wizard + date auto-population from filename
- [x] **2025-10-13** — [av-recording-types](PATCHES/patch-2025-10-13-av-recording-types.md) — Expanded A/V recording type options in source wizard
- [x] **2025-10-13** — [date-preservation](PATCHES/FIX-DATE-PRESERVATION.md) — Preserve auto-populated dates when changing document type in wizard
- [x] **2025-10-13** — [date-extraction-tests](PATCHES/DATE-EXTRACTION-TEST.md) — Test results and patterns for filename date extraction
- [x] **2025-10-11** — [dunning-cheatsheet](PATCHES/CHEAT_SHEET_NEXT_STEPS.md) — Dunning corpus processing commands & checklist

---

## 🗂️ Work Categories (file under one or more)

### 🏗️ Foundation & UI

- PR 1, PR 13, PR 29

### 📂 Project Management

- PR 26, PR 26A, PR 27, PR 40

### 📥 Source Ingestion

- PR 3, PR 5, PR 8, PR 12C, PR 25, PR 28, PR 30, PR 31, PR 37, PR 38, PR 40, PR 59

### ✏️ Source Editing

- PR 7, PR 10, PR 14, PR 22, PR 35, PR 35A, PR 41, PR 80, PR 86

### 📊 Data Management & Associations

- PR 30, PR 31, PR 35, PR 35A, PR 36, PR 36B, PR 41, PR 60, PR 72, PR 78, PR 86, PR 87

### 📄 Source View

- PR 6, PR 9, PR 18, PR 19, PR 20, PR 21, PR 23, PR 24, PR 41, PR 80, PR 86

### 📝 Notes & Notebooks

- PR 11, PR 12, PR 12A, PR 12B, PR 16, PR 29, PR 66

### 📤 Exporting

- PR 2, PR 4, PR 15, PR 17

### ⚙️ Infrastructure

- PR 38

---

## Quick links & patterns

- PR design/spec: `/Documentation/PRs/pr<N>.md`
- PR manifest: `/Documentation/PRs/pr<N>-manifest.json`
- PR runlog: `/Documentation/PRs/runlog-PR<N>.md`

> Use these paths consistently so links don’t break when we reorganize.

## 🗓️ Sessions

- `Documentation/SESSIONS/` contains meeting notes and session writeups. Recent sessions:
  - [2025-10-11 — Adapter Fix](SESSIONS/2025-10-11-adapter-fix.md)
  - [2025-10-12 — Event Wizard Improvements](SESSIONS/session-2025-10-12-event-wizard-improvements.md)
  - [2025-10-13 — Wizard Scrolling Fix](SESSIONS/session-2025-10-13-wizard-scrolling-fix.md)

---

## PR workflow checklist

1. Add PR to **In Progress** and **Work Category**.
2. Create `PRs/pr<N>.md`, `PRs/pr<N>-manifest.json`, `PRs/runlog-PR<N>.md`.
3. Implement; keep manifest updated (`added/modified/deleted`, tests, scripts).
4. Verify: `npm run lint` · `npm run test` · `npm run build` · manual smoke.
5. Paste the last lines of test/build output into the runlog.
6. Move PR to **Completed PRs** and commit.

---

## Gating policy and commands

Thresholds for ingest/eval PRs must satisfy:

- Null adapters = 0
- Unknown page-types ≤ 15%
- QA rate drop vs prior ≤ 10%

Make targets:

- `make merge` — merge batches and run offline eval
- `make reeval` — retag + eval
- `make gate` — enforce thresholds and print histogram
- `make verify` — lint, unit, e2e
- `make sample` — print 10 deterministic doc paths for spot-check

LLM review runs only if thresholds are tripped; never part of gate.

```text

want me to wire in live links (e.g., `[PR 5](PRs/pr5.md)` and `[runlog](PRs/runlog-PR5.md)`) for every item now, or keep it minimal until you migrate the files into `/Documentation/PRs/`?
```

### Triage - 2025-10-30

- Archived: pr1-manifest.json, pr50-manifest.json, pr35-manifest.json, pr60.md, pr62.md, PR64.md, pr81.md, PR65-SOURCE-WIZARD-ALIGNMENT.md, pr51.md, pr52.md, pr53.md, pr55.md, pr56.md, pr57.md, pr75.md, pr13.md, pr37-test-fix.md, pr39.md, PR66.md, pr54.md, pr74.md, pr82.md, PR84-CURRENT-STATE.md, pr26.md, pr27.md, pr40.md. (Stamped TRIAGE; moved from in-progress.)
- Completed: pr87.md - courts metadata implemented. (Stamped TRIAGE; moved from in-progress.)
