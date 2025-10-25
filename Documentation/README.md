<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Documentation Directory Overview](#documentation-directory-overview)
  - [🗺️ Directory Quick Reference](#️-directory-quick-reference)
    - [📚 Main Guides (Start Here!)](#-main-guides-start-here)
    - [📁 Directory Reference](#-directory-reference)
  - [2️⃣ Core Principles](#2️⃣-core-principles)
  - [3️⃣ System Architecture Overview](#3️⃣-system-architecture-overview)
    - [Frontend](#frontend)
    - [Backend](#backend)
    - [Project Layout](#project-layout)
  - [4️⃣ The PR-Driven Development Model](#4️⃣-the-pr-driven-development-model)
    - [🆕 Starting a New PR](#-starting-a-new-pr)
    - [✅ Completing a PR](#-completing-a-pr)
  - [5️⃣ Directory Map](#5️⃣-directory-map)
  - [6️⃣ Verification Gates](#6️⃣-verification-gates)
  - [7️⃣ Work Categories](#7️⃣-work-categories)
  - [8️⃣ Tooling \& Automation](#8️⃣-tooling--automation)
  - [9️⃣ AI Agent Workflow](#9️⃣-ai-agent-workflow)
    - [Phase 1 — Context Load](#phase-1--context-load)
    - [Phase 2 — Task Selection](#phase-2--task-selection)
    - [Phase 3 — Implementation](#phase-3--implementation)
    - [Phase 4 — Handoff](#phase-4--handoff)
  - [🔟 Maintenance Rules](#-maintenance-rules)
  - [🧩 Transition Notes from Old Layout](#-transition-notes-from-old-layout)
  - [🧠 Summary](#-summary)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Documentation Directory Overview

**🚀 Quick Start**: Looking for something? Start with **[`index.md`](index.md)** - your master PR tracker and work category index.

Every feature, data structure, and subsystem is implemented as a **Pull Request (PR)** documented in `/Documentation/PRs/`.

The documentation serves two audiences:

- **Developers** rebuilding the system
- **AI agents** continuing work autonomously or semi-autonomously

---

## 🗺️ Directory Quick Reference

### 📚 Main Guides (Start Here!)

| Guide | Audience | Purpose |
|-------|----------|---------|
| **[USER_GUIDE.md](USER_GUIDE.md)** | End users | Complete guide to using the app |
| **[TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md)** | Developers | Architecture, APIs, data models, development |
| **[index.md](index.md)** | Everyone | PR tracker, work categories, project status |
| **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** | Developers | Command cheat sheet |

### 📁 Directory Reference

| What You Need | Where to Look |
|---------------|---------------|
| **PR status & tracking** | [`index.md`](index.md) - Master index of all PRs |
| **How to use the app** | [`USER_GUIDE.md`](USER_GUIDE.md) - Complete user documentation |
| **Technical documentation** | [`TECHNICAL_REFERENCE.md`](TECHNICAL_REFERENCE.md) - Architecture & APIs |
| **Common commands** | [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md) |
| **Project glossary** | [`project_terminology.md`](project_terminology.md) |
| **Active PR documentation** | `PRs/in-progress/` - PRs currently being worked on |
| **Completed PR documentation** | `PRs/completed/` - Finished PRs with full triplets |
| **Small hotfixes** | `PATCHES/` directory - Quick fixes that didn't need PRs |
| **Meeting notes** | `history/SESSIONS/` directory - Session logs and notes |
| **Data contracts** | `Standards/json_data_contract_bible.md` - Golden invariants |
| **Polish/cleanup history** | `archive/` directory - Archived polish documentation |

**Latest polish work (October 2025)**:
- ✅ Reduced lint errors from 252 → 0
- ✅ Generated TOCs for 150+ markdown files
- ✅ Removed unused dependencies (framer-motion, slate-react)
- ✅ Fixed markdown formatting across all documentation

---

## 2️⃣ Core Principles

| Principle                          | Description                                                                            |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| **Ground-Up Rebuild**              | No legacy code dependencies; all layers reconstructed cleanly.                         |
| **File-First Architecture**        | Each data unit (source, canonical text, notes, manifests) exists as versionable files. |
| **Transparency & Reproducibility** | Every PR has a manifest + runlog; any build can be replayed.                           |
| **Human + Machine Symmetry**       | Markdown for people, JSON for tooling — same information, two forms.                   |
| **Continuous Verification**        | Each PR must lint, test, build, and pass manual verification.                          |

---

## 3️⃣ System Architecture Overview

### Frontend

- **Framework:** React 18 + Vite + TypeScript
- **Core Components:**
  `DocumentViewer`, `NotesViewer`, `CitePicker`, `BlockRenderer`, `OverlayManager`, `ProjectShell`
- **Goals:** Simpler state model, consistent overlays, unified navigation.

### Backend

- **Framework:** Node.js + Express + TypeScript
- **Responsibilities:**

  - File I/O and canonical storage access
  - Ingestion (PDF, AV, transcripts)
  - Export and validation endpoints
  - Project-scoped file routing

### Project Layout

```
/server/         ← backend
/src/            ← frontend
/Documentation/  ← manifests, runlogs, PR history, and AI instructions
```

---

## 4️⃣ The PR-Driven Development Model

All progress occurs through **documented PRs** tracked in `/Documentation/Index.md`.

Each PR includes a triplet:

- `pr<N>.md` — design document
- `pr<N>-manifest.json` — machine-readable change list
- `runlog-PR<N>.md` — implementation log with evidence

**Location**:
- While working: `PRs/in-progress/`
- When complete: `PRs/completed/`

### 🆕 Starting a New PR

1. **Check the Index**
   Open `/Documentation/Index.md`.

   - If your PR isn’t listed, add it under **In Progress PRs** with a short summary.
   - Place it in the correct **Work Category** (see section 7).

2. **Create Files** in `/Documentation/PRs/in-progress/`

   ```
   /Documentation/PRs/in-progress/pr<N>.md
   /Documentation/PRs/in-progress/pr<N>-manifest.json
   /Documentation/PRs/in-progress/runlog-PR<N>.md
   ```

3. **Implement Feature**

   - Follow architectural conventions.
   - Keep manifests current as you modify files.

### ✅ Completing a PR

1. **Finalize Manifest:** include `added`, `modified`, `deleted`, tests, scripts, docs.
2. **Complete Runlog:** summarize work; include test/build output and manual checks.
3. **Verify Gates:**

   ```
   npm run lint
   npm run test
   npm run build
   ```

4. **Move Files:** `git mv PRs/in-progress/pr<N>* PRs/completed/`
5. **Update Documentation:**
   - Move PR from _In Progress_ → _Complete_ in `index.md`
   - Update `TECHNICAL_REFERENCE.md` if API/architecture changed
   - Update `QUICK_REFERENCE.md` if commands added/changed
6. **Commit & Push** with message `PR<N>: [summary]`.

---

## 5️⃣ Directory Map

```
/Documentation/
├── README.md                 ← this instruction file
├── Index.md                  ← master PR list & work categories
├── USER_GUIDE.md            ← complete user documentation
├── TECHNICAL_REFERENCE.md   ← complete technical documentation
├── QUICK_REFERENCE.md       ← command cheat sheet
├── /Standards/
│   └── json_data_contract_bible.md  ← JSON contracts, invariants, and gates
├── /progress/
│   ├── manifest.json         ← canonical data registry (app-level)
│   ├── progress.json         ← component-tree tracker
│   └── nextaction.md         ← immediate priorities
├── PRs/
│   ├── in-progress/         ← active PRs
│   │   ├── README.md
│   │   ├── pr<N>.md
│   │   ├── pr<N>-manifest.json
│   │   └── runlog-PR<N>.md
│   └── completed/           ← finished PRs
│       ├── README.md
│       ├── pr<N>.md
│       ├── pr<N>-manifest.json
│       └── runlog-PR<N>.md
```

All PR material lives under `/Documentation/PRs/` (separated by status).
All high-level navigation (Index, overview, manifests) remains in `/Documentation/`.
All data contracts and standards live under `/Documentation/Standards/`.
All comprehensive guides (USER_GUIDE, TECHNICAL_REFERENCE, QUICK_REFERENCE) stay at root.

---

## 6️⃣ Verification Gates

| Stage             | Command                           | Requirement                      |
| ----------------- | --------------------------------- | -------------------------------- |
| Linting           | `npm run lint`                    | No errors                        |
| Unit Tests        | `npm run test`                    | 100 % pass                       |
| Build             | `npm run build`                   | Successful build                 |
| Manual Smoke Test | Open local app                    | Functional UI, no console errors |
| Documentation     | Updated manifest + runlog + Index | Consistent entries               |

The runlog is the audit trail proving these steps passed.

**📘 Data Contract Compliance:** All PRs must respect the **JSON Data-Contract Bible** at `/Documentation/Standards/json_data_contract_bible.md`. This ensures:

- Golden Invariants (stable IDs, categories, auto-event on upload, etc.)
- Source→Event mapping table adherence
- Touched-only indexing (no global rebuilds)
- Non-blocking validation (prototype stance)

---

## 7️⃣ Work Categories

| Category              | Description                                     |
| --------------------- | ----------------------------------------------- |
| 🏗️ Foundation & UI    | Core framework, overlay system, performance, UX |
| 📂 Project Management | Project shells, registries, scoped sources      |
| 📥 Source Ingestion   | PDF/AV/text ingestion → canonical conversion    |
| ✏️ Source Editing     | Block editing, cite creation, inline edits      |
| 📄 Source View        | Document viewer, PDF↔text sync, AV playback     |
| 📝 Notes & Notebooks  | Rich text notes, formatting, templates          |
| 📤 Exporting          | MD → Word/PDF export, integrity, bundling       |
| ⚙️ Infrastructure     | Validation scripts, schema tools, dashboards    |

Each PR in the Index should fall under one of these.

---

## 8️⃣ Tooling & Automation

| Script                   | Purpose                                              |
| ------------------------ | ---------------------------------------------------- |
| `validate_manifests.mjs` | Validates all `*-manifest.json` files against schema |
| `migrate_manifests.mjs`  | Normalizes manifest structure                        |
| `aggregate_runlogs.mjs`  | Generates `combined-runlogs.md`                      |
| `session_report.mjs`     | Creates `session-report-YYYY-MM-DD.md` summaries     |

Schema definition lives at `/Documentation/manifest-schema.json` (when finalized).

---

## 9️⃣ AI Agent Workflow

### Phase 1 — Context Load

1. Read `/Documentation/README.md` (this file).
2. Read `Documentation/progress/index.md` for current status.
3. Review latest `session-report-YYYY-MM-DD.md`.

### Phase 2 — Task Selection

Use `Documentation/progress/index.md` and `Documentation/progress/progress.json` to identify incomplete PRs.
Confirm task priority with `Documentation/progress/nextaction.md`

### Phase 3 — Implementation

Follow PR workflow above.
Update manifest and runlog continuously.

### Phase 4 — Handoff

- Commit all documentation artifacts.
- Add or update session report.
- Push branch for review.

---

## 🔟 Maintenance Rules

- Always keep **Index.md** current — it is the project plan.
- After each PR:

  - Update `progress.json` component statuses.
  - Append latest output to combined runlogs.
  - Generate new session report.

- If directory structure changes, document it at the top of this README.

---

## 🧩 Transition Notes from Old Layout

Old path references (`docs/textstorageoverhaul/_Unified/…`) have been replaced by:

```
Documentation/PRs/
```

If you run any legacy commands, update them:

```bash
# Example fix
jq . Documentation/PRs/pr5-manifest.json
```

No other structural differences require code changes unless the backend hard-coded doc paths.

---

## 🧠 Summary

- The rebuild treats **/Documentation** as the canonical development log.
- Each **PR is both implementation and documentation unit**.
- The **Index** and **progress.json** together describe total project state.
- When starting work:

  1. Read Index
  2. Create PR triplet
  3. Build, test, document
  4. Update Index and reports

---

**Next step:** open [`/Documentation/Index.md`](./Index.md), locate your PR, or create a new one under _In Progress PRs_.
