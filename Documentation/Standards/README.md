<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Documentation Standards](#documentation-standards)
  - [📘 JSON Data-Contract Bible](#-json-data-contract-bible)
  - [🎯 Quick Reference](#-quick-reference)
    - [For Developers](#for-developers)
    - [For AI Agents](#for-ai-agents)
  - [📚 Future Standards](#-future-standards)
  - [🔗 Related Documentation](#-related-documentation)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Documentation Standards

This directory contains canonical standards, contracts, and guidelines for the Case Project rebuild.

---

## 📘 JSON Data-Contract Bible

**File:** `json_data_contract_bible.md`

**Purpose:** Enforceable playbook preventing JSON drift across PRs.

**What It Covers:**

- **Golden Invariants** (7 non-negotiable rules)
- **Canonical Types** (TypeScript + Zod schemas for Event, Source, Participation)
- **Source→Event Mapping Table** (8 source types with auto-event creation)
- **Indexes** (touched-only, no global rebuilds)
- **API Contract** (minimal, stable endpoints)
- **Validation Layers** (shape, soft rules, referential)
- **UI Guarantees** (EventDetailsView, source chips, legal tips)
- **PR Checklists** (feature PRs vs refactor PRs)
- **Tests Matrix** (unit, integration, e2e minimums)
- **Runlog Evidence** (lint/test/build tails)
- **Migration Policy** (prototype: no migrations)
- **Tooling Stubs** (index writers, validate_touched)
- **Troubleshooting** (common drift gotchas)

**When to Use:**

- Before starting any PR that touches Events, Sources, or People
- When adding new API endpoints
- When modifying data structures
- When implementing validation logic
- During PR reviews to verify compliance

**Checklist Integration:**
Every PR description should include the relevant checklist from Section 8 of the Bible.

---

## 🎯 Quick Reference

### For Developers

1. **Starting a PR?** Check the Bible's Golden Invariants (Sec. 1)
2. **Adding an endpoint?** Update API Contract (Sec. 5) and add tests
3. **Changing types?** Update Canonical Types (Sec. 2) and Zod schemas
4. **Finishing a PR?** Use the checklist (Sec. 8.1) and paste runlog evidence (Sec. 10)

### For AI Agents

Append this to all Codex tasks involving Events, Sources, or People:

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

## 📚 Future Standards

Additional standards documents will be added here as the project matures:

- **API Design Standards** (RESTful conventions, error handling)
- **Component Architecture** (React patterns, state management)
- **Testing Standards** (coverage expectations, test organization)
- **Security Standards** (auth, data validation, file access)
- **Performance Standards** (bundle size, load times, memory)

---

## 🔗 Related Documentation

- Main Documentation: `/Documentation/README.md`
- PR Index: `/Documentation/Index.md`
- Progress Tracking: `/Documentation/progress/`
- PR History: `/Documentation/PRs/`

---

**Last Updated:** 2025-10-12  
**Maintainer:** Project Lead + AI Agents
