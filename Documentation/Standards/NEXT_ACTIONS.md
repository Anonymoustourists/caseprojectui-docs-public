<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [JSON Data-Contract Bible — Next Actions](#json-data-contract-bible--next-actions)
  - [✅ Completed](#-completed)
  - [🎯 Immediate Next Steps (Bible Sec. 15)](#-immediate-next-steps-bible-sec-15)
    - [Step 1: Add Zod Schemas (Priority: HIGH)](#step-1-add-zod-schemas-priority-high)
    - [Step 2: Add Index Writers (Priority: HIGH)](#step-2-add-index-writers-priority-high)
    - [Step 3: Add Validation Script (Priority: MEDIUM)](#step-3-add-validation-script-priority-medium)
  - [📋 Verification Checklist](#-verification-checklist)
  - [🎓 Learning Resources](#-learning-resources)
  - [📝 Notes](#-notes)
    - [Why These Three Steps?](#why-these-three-steps)
    - [Prototype vs Production](#prototype-vs-production)
    - [Integration Timeline](#integration-timeline)
  - [🔗 Related Files](#-related-files)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# JSON Data-Contract Bible — Next Actions

**Priority:** High  
**Status:** Foundation Complete, Tooling Needed  
**Date:** 2025-10-12

---

## ✅ Completed

1. **Bible Document Created**
   - 15 sections covering all JSON contracts
   - Golden Invariants defined
   - Source→Event mapping table documented
   - PR checklists provided
   - Tests matrix specified

2. **Documentation Integration**
   - PR61 checklist added
   - PR62 checklist added
   - README.md updated with Standards reference
   - Standards directory overview created
   - Implementation summary documented

3. **Verification**
   - All files lint-clean
   - Markdown properly formatted
   - Cross-references consistent

4. **STEP 1: Zod Schemas ✅** (Date: 2025-10-12)
   - Created 4 schema files (events, sources, people, index)
   - 100 total test cases (44 events, 25 people, 31 sources)
   - Integrated into PR61 API endpoints
   - All tests passing (100/100)
   - Lint clean, build successful
   - Mirrors Bible §2 exactly

---

## 🎯 Immediate Next Steps (Bible Sec. 15)

### Step 1: Add Zod Schemas (Priority: HIGH)

**Goal:** Mirror Bible Sec. 2 types in runtime-validated schemas

**Files to Create:**

```
tools/schemas/events.ts
tools/schemas/sources.ts
tools/schemas/people.ts
```

**Content:**

```typescript
// tools/schemas/events.ts
import { z } from 'zod';

export const zEventCategory = z.enum(['legal', 'factual', 'investigatory']);

export const zEventItem = z.object({
  id: z.string().ulid(),
  title: z.string(),
  customTitle: z.string().optional(),
  category: zEventCategory,
  date: z.string().optional(), // "YYYY-MM-DD"
  datetime: z.string().datetime().optional(),
  wizard: z.object({
    entity: z.literal('events'),
    type: z.string(),
    answers: z.record(z.any()),
    template_id: z.string(),
    spec_version: z.number()
  }).optional(),
  data: z.record(z.any()),
  sourceId: z.string().optional(),
  sourceType: z.string().optional(),
  citeIds: z.array(z.string()).optional(),
  participants: z.array(zParticipation).optional(),
  createdFrom: z.enum(['wizard', 'selection', 'source_upload']).optional(),
  createdAt: z.string().optional(),
  updatedAt: z.string().optional(),
  typeId: z.string().optional(),
  stableKey: z.string().optional()
});

// tools/schemas/people.ts
export const zPersonRole = z.enum([
  'speaker', 'witness', 'defendant', 'complainant',
  'interviewee', 'interviewer', 'declarant', 'officer',
  'caller_911', 'dispatcher_911', 'attorney', 'judge', 'other'
]);

export const zParticipation = z.object({
  personId: z.string(),
  role: zPersonRole,
  eventId: z.string().optional(),
  sourceId: z.string().optional(),
  startMs: z.number().optional(),
  endMs: z.number().optional(),
  page: z.number().optional(),
  note: z.string().optional(),
  addedAt: z.string().optional(),
  addedBy: z.string().optional()
});
```

**Integration Points:**

- Add to `server/src/routes/events.ts` endpoint handlers
- Validate req.body before writes
- Return 400 with Zod errors on validation failure

**Test:**

```typescript
// tests/unit/schemas/events.test.ts
import { zEventItem } from '../../../tools/schemas/events';

test('validates complete event', () => {
  const event = { id: '01HX...', title: 'Test', category: 'legal', data: {} };
  expect(() => zEventItem.parse(event)).not.toThrow();
});

test('rejects invalid category', () => {
  const event = { id: '01HX...', title: 'Test', category: 'invalid', data: {} };
  expect(() => zEventItem.parse(event)).toThrow();
});
```

**Acceptance:**

- [ ] Schemas match Bible Sec. 2 exactly
- [ ] Used in all event/source/people write endpoints
- [ ] Unit tests for valid/invalid cases
- [ ] Lint/test/build pass

---

### Step 2: Add Index Writers (Priority: HIGH)

**Goal:** Auto-update JSON indexes on touched entities only

**File to Create:**

```
tools/index_writer.ts
```

**Content:**

```typescript
import { EventItem } from '../shared/types';
import { readJSON, writeJSON } from './json_helpers';

// Index paths
const EVENTS_BY_SOURCE = 'indexes/eventsBySource.json';
const EVENTS_BY_CATEGORY = 'indexes/eventsByCategory.json';
const EVENTS_BY_PERSON = 'indexes/eventsByPerson.json';

export async function onEventWrite(projectSlug: string, ev: EventItem) {
  // Update category index
  await updateEventsByCategory(projectSlug, ev);
  
  // Update source index if linked
  if (ev.sourceId) {
    await addEventToEventsBySource(projectSlug, ev.sourceId, ev.id);
  }
  
  // Update person indexes if participants present
  if (ev.participants) {
    await updateEventsByPersonIndex(projectSlug, ev.id, ev.participants);
  }
}

export async function onEventDelete(projectSlug: string, ev: EventItem) {
  // Remove from category index
  await removeEventFromCategory(projectSlug, ev);
  
  // Remove from source index if linked
  if (ev.sourceId) {
    await removeEventFromEventsBySource(projectSlug, ev.sourceId, ev.id);
  }
  
  // Remove from person indexes
  await removeEventFromEventsByPersonIndex(projectSlug, ev.id);
}

async function updateEventsByCategory(projectSlug: string, ev: EventItem) {
  const path = `projects/${projectSlug}/${EVENTS_BY_CATEGORY}`;
  const index = await readJSON(path, { legal: [], factual: [], investigatory: [] });
  
  // Remove from all categories first
  for (const cat of ['legal', 'factual', 'investigatory']) {
    index[cat] = index[cat].filter(id => id !== ev.id);
  }
  
  // Add to correct category
  if (!index[ev.category].includes(ev.id)) {
    index[ev.category].push(ev.id);
  }
  
  await writeJSON(path, index);
}

// Similar functions for other indexes...
```

**Integration Points:**

- Call from `server/src/routes/events.ts` after create/update/delete
- Call from `server/src/index.ts` after auto-event creation
- Call from `server/src/routes/sources.ts` for participant changes

**Test:**

```typescript
// tests/integration/indexes/events.test.ts
test('onEventWrite updates category index', async () => {
  const event = { id: '01HX...', category: 'legal', ... };
  await onEventWrite('test-project', event);
  
  const index = await readJSON('projects/test-project/indexes/eventsByCategory.json');
  expect(index.legal).toContain('01HX...');
});
```

**Acceptance:**

- [ ] All 5 indexes implemented (eventsBySource, eventsByCategory, eventsByPerson, sourcesByPerson, citesByEvent)
- [ ] Hooks added to all write paths
- [ ] Integration tests verify updates
- [ ] No global rebuilds (touched-only)

---

### Step 3: Add Validation Script (Priority: MEDIUM)

**Goal:** Non-blocking warnings for prototype issues

**File to Create:**

```
tools/validate_touched.js
```

**Content:**

```javascript
#!/usr/bin/env node

import { execSync } from 'child_process';
import { readFileSync } from 'fs';
import { zEventItem } from './schemas/events.js';

// Get changed files from git
const changedFiles = execSync('git diff --name-only HEAD', { encoding: 'utf-8' })
  .split('\n')
  .filter(f => f.includes('/events/') && f.endsWith('.json'));

console.log(`Validating ${changedFiles.length} touched event files...\n`);

let warnings = 0;

for (const file of changedFiles) {
  try {
    const content = readFileSync(file, 'utf-8');
    const event = JSON.parse(content);
    
    // Shape validation (Zod)
    try {
      zEventItem.parse(event);
    } catch (err) {
      console.warn(`⚠️  Shape validation failed: ${file}`);
      console.warn(`   ${err.errors[0].message}`);
      warnings++;
      continue;
    }
    
    // Soft rule: legal events should have sources
    if (event.category === 'legal' && !event.sourceId) {
      console.warn(`ℹ️  Legal event without source: ${file}`);
      console.warn(`   Consider linking a source document.`);
      warnings++;
    }
    
    // Soft rule: check participant references (non-blocking)
    if (event.participants) {
      for (const p of event.participants) {
        // Could check if personId exists, but non-blocking in prototype
        if (!p.personId) {
          console.warn(`⚠️  Participant missing personId: ${file}`);
          warnings++;
        }
      }
    }
    
  } catch (err) {
    console.error(`❌ Parse error: ${file}`);
    console.error(`   ${err.message}`);
    warnings++;
  }
}

console.log(`\n✅ Validation complete: ${warnings} warnings`);
console.log('(Warnings are informational; no failures in prototype mode)');
process.exit(0); // Never fail in prototype
```

**Package.json Script:**

```json
{
  "scripts": {
    "validate:touched": "node tools/validate_touched.js"
  }
}
```

**Test:**

```bash
# Create test event with issue
echo '{"id":"test","category":"legal","data":{}}' > test-event.json
git add test-event.json

# Run validation
npm run validate:touched
# Should warn: "Legal event without source"
```

**Acceptance:**

- [ ] Script identifies changed event/source files via git diff
- [ ] Zod shape validation runs on each
- [ ] Soft warnings for legal events without sources
- [ ] Soft warnings for missing participant references
- [ ] Always exits 0 (non-blocking)
- [ ] npm script added

---

## 📋 Verification Checklist

After completing Steps 1-3:

- [ ] Zod schemas created and tested
- [ ] Index writers implemented and integrated
- [ ] Validation script created and npm script added
- [ ] All new code lints clean
- [ ] All new tests pass
- [ ] PR61 uses schemas in endpoints
- [ ] PR62 uses index writers for participants
- [ ] Documentation updated (if needed)

---

## 🎓 Learning Resources

**Zod Documentation:**

- <https://zod.dev/>
- Shape validation, refinements, transforms

**Index Design Patterns:**

- Keep indexes small (arrays of IDs only)
- Update on write, not on read
- One index per lookup pattern

**Git Diff Parsing:**

- `git diff --name-only HEAD` for changed files
- `git diff --cached --name-only` for staged files
- Filter by path patterns for entity types

---

## 📝 Notes

### Why These Three Steps?

1. **Zod Schemas** = Runtime type safety (catches bad data at API boundaries)
2. **Index Writers** = Performance (no scanning, instant lookups)
3. **Validation Script** = Developer feedback (catch issues early, non-blocking)

Together, these enforce the Bible's contracts without requiring SQL-level constraints.

### Prototype vs Production

**Prototype (now):**

- Shape validation only (Zod)
- Soft warnings (informational)
- Touched-only updates
- No migrations

**Production (later):**

- Add referential validation (optional)
- Add duplicate prevention
- Add bulk backfill tools
- Add CI gates (configurable)

### Integration Timeline

1. **Today:** Complete Steps 1-3 (foundation)
2. **PR61 Finish:** Use schemas in event endpoints
3. **PR62 Start:** Use index writers for participants
4. **PR63+:** Add validation to CI pipeline

---

## 🔗 Related Files

- Bible: `/Documentation/Standards/json_data_contract_bible.md`
- PR61 Spec: `/Documentation/PRs/pr61.md`
- PR62 Spec: `/Documentation/PRs/pr62.md`
- Implementation: `/Documentation/Standards/IMPLEMENTATION.md`

---

**Ready to Start:** Yes, all prerequisites complete.  
**Estimated Effort:** 2-4 hours for all three steps.  
**Next Action:** Begin Step 1 (Zod Schemas).
