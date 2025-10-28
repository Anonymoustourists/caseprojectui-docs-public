<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [JSON Data-Contract Bible — Implementation Summary](#json-data-contract-bible--implementation-summary)
  - [What Was Done](#what-was-done)
    - [1. Created the Bible Document ✅](#1-created-the-bible-document-)
    - [2. Integrated with PR Workflow ✅](#2-integrated-with-pr-workflow-)
    - [3. Key Sections](#3-key-sections)
  - [Golden Invariants (Quick Reference)](#golden-invariants-quick-reference)
  - [Source→Event Mapping Table](#source%E2%86%92event-mapping-table)
  - [PR Checklist (Sec. 8.1)](#pr-checklist-sec-81)
  - [Files Modified](#files-modified)
    - [Created](#created)
    - [Modified](#modified)
  - [Verification ✅](#verification-)
  - [Next Steps (From Bible Sec. 15)](#next-steps-from-bible-sec-15)
    - [Immediate (Before PR61/PR62 Completion)](#immediate-before-pr61pr62-completion)
    - [Medium Term (PR63+)](#medium-term-pr63)
    - [Long Term (Hardening Phase)](#long-term-hardening-phase)
  - [How to Use This Bible](#how-to-use-this-bible)
    - [For Developers](#for-developers)
    - [For AI Agents](#for-ai-agents)
    - [For Code Reviews](#for-code-reviews)
  - [Troubleshooting Common Issues](#troubleshooting-common-issues)
  - [Integration Points](#integration-points)
    - [With PR61](#with-pr61)
    - [With PR62](#with-pr62)
    - [With Overall Documentation](#with-overall-documentation)
  - [Success Metrics](#success-metrics)
  - [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# JSON Data-Contract Bible — Implementation Summary

**Date:** 2025-10-12  
**Status:** ✅ Complete

---

## What Was Done

### 1. Created the Bible Document ✅

- **File:** `/Documentation/Standards/json_data_contract_bible.md`
- **Size:** 15 sections, ~450 lines
- **Coverage:** Complete playbook for JSON drift prevention

### 2. Integrated with PR Workflow ✅

- Added checklists to PR61 and PR62 specifications
- Updated `/Documentation/README.md` with Standards reference
- Created `/Documentation/Standards/README.md` overview

### 3. Key Sections

| Section | Title             | Purpose                   |
| ------- | ----------------- | ------------------------- |
| 0       | Purpose           | Why this Bible exists     |
| 1       | Golden Invariants | 7 non-negotiable rules    |
| 2       | Canonical Types   | TypeScript + Zod schemas  |
| 3       | Mapping Table     | Source→Event (8 types)    |
| 4       | Indexes           | Touched-only JSON indexes |
| 5       | API Contract      | Minimal, stable endpoints |
| 6       | Validation Layers | Shape, soft, referential  |
| 7       | UI Guarantees     | EventDetailsView behavior |
| 8       | PR Checklists     | Feature vs Refactor       |
| 9       | Tests Matrix      | Unit, integration, e2e    |
| 10      | Runlog Evidence   | Lint/test/build tails     |
| 11      | Migration Policy  | Prototype: no migrations  |
| 12      | Tooling Stubs     | Index writers, validation |
| 13      | Troubleshooting   | Common drift gotchas      |
| 14      | Codex Footer      | AI agent instructions     |
| 15      | What to Do Now    | Next steps                |

---

## Golden Invariants (Quick Reference)

1. **Stable IDs** — All entities use ULIDs
2. **Event Categories** — `legal | factual | investigatory`
3. **Auto-Event on Upload** — 1:1 event creation for mapped sources
4. **Optional Sources** — Events can exist without sources (soft nudge for legal)
5. **Participation Links** — People attached to Events/Sources with roles
6. **Cites are Read-Through** — Always resolve to concrete anchors
7. **Touched-Only Indexing** — No global rebuilds in prototype

---

## Source→Event Mapping Table

| Source Type   | Event Type    | Category      |
| ------------- | ------------- | ------------- |
| transcript    | Court Hearing | legal         |
| court-filing  | Court Filing  | legal         |
| opinion       | Court Filing  | legal         |
| police-report | Police Report | investigatory |
| av-interview  | A/V Interview | investigatory |
| bodycam       | Body Camera   | investigatory |
| dashcam       | Dash Camera   | investigatory |
| 911-call      | 911 Call      | investigatory |

---

## PR Checklist (Sec. 8.1)

Use this for every feature PR:

- [ ] Respects **Golden Invariants**
- [ ] Source→Event mapping unchanged (or updated + documented)
- [ ] Types updated in `types/` and Zod schemas
- [ ] Index writers updated for all touched paths
- [ ] EventDetailsView source chip & legal-tip behavior preserved
- [ ] People participation UI present where relevant
- [ ] Tests added/updated (unit, integration, e2e)
- [ ] Lint/test/build evidence in runlog
- [ ] Bible updated if contracts changed

---

## Files Modified

### Created

- `/Documentation/Standards/json_data_contract_bible.md` (main document)
- `/Documentation/Standards/README.md` (directory overview)
- `/Documentation/Standards/IMPLEMENTATION.md` (this file)

### Modified

- `/Documentation/PRs/pr61.md` (added checklist)
- `/Documentation/PRs/pr62.md` (added checklist)
- `/Documentation/README.md` (added Standards section, verification gates)

---

## Verification ✅

```bash
npm run lint
# Result: The task succeeded with no problems.
```

All documentation files are valid Markdown with consistent formatting.

---

## Next Steps (From Bible Sec. 15)

### Immediate (Before PR61/PR62 Completion)

1. **Add Zod Schemas** (`tools/schemas/`)
   - Mirror Bible Sec. 2 (EventItem, SourceItem, Participation)
   - Use at API boundaries (routes validation)

2. **Add Index Writers** (`tools/index_writer.ts`)
   - `onEventWrite()`, `onEventDelete()`
   - `onSourceWrite()`, `onSourceDelete()`
   - Update indexes: eventsBySource, eventsByCategory, eventsByPerson, sourcesByPerson

3. **Add Validation Script** (`tools/validate_touched.js`)
   - Git diff parser to find changed entities
   - Zod shape validation
   - Soft warnings for prototype issues
   - Add `npm run validate:touched` script

### Medium Term (PR63+)

4. **Enhance Tests**
   - Add integration tests for index updates
   - Add e2e tests matching Bible Sec. 9 matrix
   - Verify auto-event creation end-to-end

5. **UI Enhancements**
   - Verify all UI Guarantees (Sec. 7) implemented
   - Add People Panel with Appearances tabs
   - Add cite suggestion from speaker blocks

### Long Term (Hardening Phase)

6. **Referential Validation** (optional)
   - Add `validate:data` script for CI
   - Check unknown personId/eventId/sourceId references
   - Verify cites resolve to valid anchors
   - Make failures configurable (warn vs block)

---

## How to Use This Bible

### For Developers

**Starting a PR:**

1. Read Golden Invariants (Sec. 1)
2. Check if your changes affect the mapping table (Sec. 3)
3. Review relevant types (Sec. 2)

**During Development:**

1. Use API Contract (Sec. 5) for endpoint design
2. Follow validation approach (Sec. 6)
3. Maintain UI Guarantees (Sec. 7)

**Before Submitting:**

1. Complete PR Checklist (Sec. 8.1)
2. Add runlog evidence (Sec. 10)
3. Update Bible if contracts changed

### For AI Agents

Add this footer to all tasks involving Events, Sources, or People:

```
Honor the JSON Data-Contract Bible at Documentation/Standards/json_data_contract_bible.md:
- Keep Golden Invariants intact.
- Use the Source→Event mapping table for ingest.
- Update touched-only indexes on write/delete.
- Maintain EventDetailsView source chip + non-blocking legal tip.
- Preserve People participation links and appearances.
Run lint/test/build and paste tails into the PR runlog.
```

### For Code Reviews

1. Verify checklist completed
2. Check invariants preserved
3. Confirm types match Bible
4. Validate test coverage
5. Review runlog evidence

---

## Troubleshooting Common Issues

| Symptom                                  | Likely Cause                                   | Fix                                   |
| ---------------------------------------- | ---------------------------------------------- | ------------------------------------- |
| New source uploaded but no event created | Ingest not calling `createEventForSource()`    | Add hook in upload endpoint           |
| Event list slow                          | Scanning instead of using indexes              | Use `eventsByCategory.json` lookup    |
| Legal tip not showing                    | Lost `category` prop or state mapping          | Check EventDetailsView category logic |
| People appearances empty                 | Participation not added or indexes not updated | Verify index writer hooks             |
| Duplicate saves without change           | `requiresModification` flag not checked        | Add validation in save handler        |

---

## Integration Points

### With PR61

- [x] Checklist added to pr61.md
- [x] Auto-event mapping matches Bible Sec. 3
- [x] EventDetailsView matches UI Guarantees (Sec. 7)
- [ ] Index writers needed for event CRUD
- [x] Validation follows Sec. 6 (shape only)

### With PR62

- [x] Checklist added to pr62.md
- [ ] Participation type matches Bible Sec. 2.3
- [ ] Index writers for eventsByPerson, sourcesByPerson
- [ ] People Panel UI per Sec. 7
- [ ] Tests per Sec. 9 matrix

### With Overall Documentation

- [x] Referenced in `/Documentation/README.md`
- [x] Standards directory created
- [x] Overview document created
- [ ] Mentioned in `/Documentation/Index.md` (optional)

---

## Success Metrics

✅ **Bible document created** (450+ lines, 15 sections)  
✅ **PR checklists integrated** (PR61, PR62)  
✅ **README updated** (Standards section)  
✅ **Lint passed** (no errors)  
⏳ **Zod schemas added** (next step)  
⏳ **Index writers implemented** (next step)  
⏳ **Validation script added** (next step)

---

## References

- Main Bible: `/Documentation/Standards/json_data_contract_bible.md`
- Standards Overview: `/Documentation/Standards/README.md`
- PR61 Spec: `/Documentation/PRs/pr61.md`
- PR62 Spec: `/Documentation/PRs/pr62.md`
- Main Docs: `/Documentation/README.md`

---

**Status:** Foundation complete, tooling implementation pending.  
**Next:** Implement Zod schemas, index writers, and validation script per Bible Sec. 15.
