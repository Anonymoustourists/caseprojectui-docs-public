# AI Coding Agent Instructions (for VSC and Codex)
---
applyTo: "**"
---
# Case Project — Canonical Instructions for Copilot & Agents

This repository is a **ground-up rebuild**.
The **only source of truth** for how to work and what to preserve is in `/Documentation/`.

---

## 🔖 Read These First (in order)

1. `/Documentation/README.md` — AI & Developer Instruction Manual (scope, gates, workflow)
2. `/Documentation/index.md` — PR map (in-progress vs complete + categories)
3. `/Documentation/progress/progress.json` — component tree status
4. `/Documentation/progress/nextaction.md` — immediate priorities
5. **`/Documentation/Standards/json_data_contract_bible.md` — REQUIRED data-contract rules** ✅

---

## 🧩 Data-Contract Compliance (enforce this every time)

All code, tests, and schema work **must comply** with
`/Documentation/Standards/json_data_contract_bible.md`.

Copilot and other AI agents must:

- **Honor all Golden Invariants** in that file (stable IDs, Source→Event mapping, non-blocking legal tip, People participation, touched-only indexes).
- **Run shape validation (Zod)** on all API writes.
- **Call index writers** after any event/source/person create, update, or delete.
- **Preserve UI contract**:
  - EventDetailsView shows Linked Source chip + non-blocking legal tip.
  - Auto-event on source upload remains intact.
  - People↔Event/Source roles visible and round-trip correctly.

- **Add tests** for any new endpoint or schema field introduced.
- **Update the Bible itself** if a rule changes and reference that update in the PR manifest.

Violation = broken gate.
If unsure which rule applies, open `/Documentation/Standards/json_data_contract_bible.md` and follow its PR checklist.

---

## ⚙️ Non-Negotiable Verification Gates (prove-it mode)

A task is **not done** until:

- `npm run lint` ✅
- `npm run test` ✅
- `npm run build` ✅
- Manual smoke in browser with **no console errors** ✅
- **Live Browser Gate (MCP) passed** with artifacts (see section below) ✅
- Evidence appended to the correct runlog under `/Documentation/PRs/in-progress/…` or `/Documentation/PATCHES/…` ✅
- **Data-Contract Bible invariants confirmed** (`npm run validate:touched`) ✅
- **Documentation updated**: `TECHNICAL_REFERENCE.md` and `QUICK_REFERENCE.md` reflect any API, command, or architecture changes ✅

Paste the **last ~20 lines** of the above commands in the runlog.

---

## 🛰️ Live Browser Gate (MCP Chrome DevTools)

**Purpose:** prove the UI is clean: **0 console errors**, **0 failed network requests** for the tested flow, with reproducible evidence.

**Startup (one of):**

- `npm run dev:browser` (preferred, starts Chrome in debug mode and the MCP server), or
- VS Code Task: **Start MCP Chrome**.

**Attach & navigate:**

1. Ensure the app is running (e.g., `npm run dev`).
2. In your MCP client, `list_pages` → `select_page` for `http://localhost:5173`.
3. **Always take a fresh snapshot before interacting.**
   - `take_snapshot { verbose: true }`
   - Use **only** UIDs from the **current** snapshot.
   - **After any reload, route change, modal open, or DOM mutation: take a new snapshot** before clicking again.

4. Prefer stable actions:
   - Use `evaluate_script` to find elements by visible text, `scrollIntoView`, then `take_snapshot` and click by the new UID.
   - Avoid reusing UIDs captured before a reload/navigation.

**Collect artifacts:**

- `list_console_messages { pageSize: 200 }` → count `level ∈ {error, warning}`.
- `list_network_requests { pageSize: 200 }` → list any with `status >= 400`.
- `take_snapshot { verbose: false }` → screenshot of the tested view.

**Pass criteria:**

- After a hard reload (`evaluate_script(() => { location.reload(); return 'reloaded'; })`), the main flow shows:
  - `consoleErrors === 0`
  - `failedRequests === 0`

**Runlog evidence (paste under a “Live Browser Gate” header):**

- Counts: `consoleErrors=…`, `consoleWarnings=…`, `failedRequests=…`
- Screenshot (inline or link)
- Brief notes of the path tested (e.g., “Transcript → Text mode → Jump → Smart Q/A toggle”)
- Last ~20 lines of dev server output

---

## 🧭 PR Workflow (must follow)

- Before coding: ensure the PR exists in `/Documentation/index.md` under **In Progress** and in a **Work Category**.
- Create or update the **PR triplet** in `/Documentation/PRs/in-progress/`:
  - `pr<N>.md` — design/spec
  - `pr<N>-manifest.json` — machine-readable changes
  - `runlog-PR<N>.md` — verification evidence

- Confirm every PR passes the **Data-Contract Checklist** from the Bible (Sec. 8.1).
- When done:
  1. Move the PR triplet from `PRs/in-progress/` to `PRs/completed/` using `git mv`
  2. Move the PR to **Completed** in `/Documentation/index.md`
  3. Update references in `TECHNICAL_REFERENCE.md` and `QUICK_REFERENCE.md` if relevant

---

## 🚑 Allowed “Hotfix without PR”

Use **Hotfix Patch Notes** only for truly small, surgical fixes (typos, paths, logs).
Anything affecting schemas, API behavior, or UI contracts → open or continue a PR.

---

## 📜 Source of Truth Hierarchy

If instructions conflict:

1. `/Documentation/Standards/json_data_contract_bible.md` (highest for schema & behavior)
2. `/Documentation/README.md` (workflow)
3. `/Documentation/index.md` (PR map)
4. This file (meta-rules for Copilot/Agents)

---

## 🧠 Copilot Directive Footer (append to each generated PR description)

> **Copilot must confirm:**
>
> - All Golden Invariants from the Data-Contract Bible remain intact.
> - Mapping table (Source→Event) unchanged or explicitly updated.
> - Index writers and touched-only updates active.
> - EventDetailsView Linked-Source chip + non-blocking tip rendered correctly.
> - People participation and appearances preserved.
> - Lint/test/build evidence logged.
> - Bible updated if any rule changes.
> - **Live Browser Gate (MCP) passed** with artifacts, and **snapshot discipline** followed
>   (fresh `take_snapshot` after any reload/navigation/DOM change; no stale UIDs).

---

**In short:**
_“If it touches JSON, check the Bible. If it touches the UI, pass the Live Browser Gate.”_
