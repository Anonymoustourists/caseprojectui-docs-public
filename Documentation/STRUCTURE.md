# Documentation Structure

**Last Updated**: October 14, 2025  
**Status**: ✅ Clean and organized per primaryinstructions.instructions.md

---

## Directory Layout

```
Documentation/
├── README.md                    # Documentation overview & guide references
├── index.md                     # Master PR tracker & work categories
├── USER_GUIDE.md               # Complete user-facing documentation
├── TECHNICAL_REFERENCE.md      # Complete technical documentation
├── QUICK_REFERENCE.md          # Command cheat sheet
├── project_terminology.md      # Glossary
├── STATUS.md                   # Project status
├── todo.md                     # Current TODO items
│
├── PRs/                        # Pull Request documentation
│   ├── in-progress/           # Active PRs being worked on
│   │   ├── README.md          # In-progress directory guide
│   │   ├── pr{N}.md           # PR design/spec files
│   │   ├── pr{N}-manifest.json
│   │   └── runlog-PR{N}.md
│   └── completed/             # Finished PRs
│       ├── README.md          # Completed directory guide
│       ├── pr{N}.md
│       ├── pr{N}-manifest.json
│       └── runlog-PR{N}.md
│
├── PATCHES/                    # Hotfix patches (non-PR changes)
│   ├── README.md              # Patch workflow guide
│   ├── patch-YYYY-MM-DD-{slug}.md
│   └── *.manifest.json        # Optional manifests
│
├── Standards/                  # Data contracts & coding standards
│   └── json_data_contract_bible.md
│
├── AppSections/               # App feature documentation
├── TextExtract/               # Text extraction pipeline docs
├── UserHelp/                  # End-user help articles
├── devnotes/                  # Developer scratch notes
│
├── archive/                   # Archived polish/cleanup docs
│   ├── CLEANUP_COMPLETE.md
│   ├── DEPENDENCY_ANALYSIS.md
│   ├── DOCS_CLEANUP_PLAN.md
│   ├── POLISH_CHECKLIST.md
│   ├── SETUP_POLISH.md
│   ├── lint-cleanup-progress.md
│   └── pr-polish-phase1.md
│
└── history/                   # Historical tracking data
    ├── SESSIONS/             # Meeting notes & session logs
    ├── progress/             # Progress tracking JSON
    └── runlogs/              # Historical test/build outputs
```

---

## File Naming Conventions

### PRs (in `PRs/in-progress/` or `PRs/completed/`)

- **Design/Spec**: `pr{N}.md` or `PR{N}.md`
- **Manifest**: `pr{N}-manifest.json`
- **Runlog**: `runlog-PR{N}.md`
- **Related Docs**: `PR{N}-{descriptor}.md` (e.g., `PR35-CHECKLIST.md`)

**Location**:
- Active work → `PRs/in-progress/`
- Completed work → `PRs/completed/`

### Patches (in `PATCHES/` directory)

- **Patch File**: `patch-YYYY-MM-DD-{short-slug}.md`
- **Manifest** (optional): `patch-YYYY-MM-DD-{short-slug}.manifest.json`
- **Legacy Format** (still valid): `{DESCRIPTOR}.md` (e.g., `FIX-DATE-PRESERVATION.md`)

---

## Indexing Requirements

### PRs

All PRs must be listed in `index.md` under:
- **🚧 In Progress / Incomplete PRs** (while working)
- **✅ Completed PRs** (when done)
- Appropriate **Work Category** section

### Patches

All patches must be listed in `index.md` under:
- **🔧 Completed Hotfixes**

Format: `- [x] **YYYY-MM-DD** — [slug](PATCHES/patch-file.md) — Description`

---

## Clean Structure Verification

**✅ No duplicates**: Each file exists in only one location  
**✅ No orphans**: All PRs and patches indexed in `index.md`  
**✅ Proper naming**: Files follow conventions above  
**✅ Clear hierarchy**: Active work at root, historical in subdirectories  

---

## Quick Navigation

### For Users
→ Start with `USER_GUIDE.md`

### For Developers  
→ Start with `TECHNICAL_REFERENCE.md`

### For Contributors
→ Check `index.md` for current work, then read relevant PRs

### For New Features
→ Follow PR workflow in `README.md` and `.github/instructions/primaryinstructions.instructions.md`

### For Small Fixes
→ Follow patch workflow in `PATCHES/README.md`

---

## Recent Cleanup (October 14, 2025)

**Phase 1**: Duplicate removal
- 23 duplicate/obsolete files from `PRs/`
- `PRs/ROOT_ARCHIVE/` directory (duplicates)
- `PRs/PR-32/` and `PRs/PR-33/` directories (old structure)

**Phase 2**: Archival organization
- Polish docs → `archive/`
- Historical tracking → `history/`
- Misnamed patches → `PATCHES/` with proper naming

**Phase 3**: Status-based organization (October 14, 2025)
- Created `PRs/in-progress/` for active work (~50 files)
- Created `PRs/completed/` for finished PRs (~110 files)
- Added README.md in each subdirectory
- Physical location now mirrors PR status

**Result**:
- Clear separation of active vs completed work
- Easier navigation (13 in-progress vs 40+ completed)
- All patches in `PATCHES/` following naming conventions
- Everything catalogued in `index.md`

---

**Maintained By**: Development team  
**Governance**: `.github/instructions/primaryinstructions.instructions.md`
