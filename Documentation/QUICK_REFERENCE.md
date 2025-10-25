<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Quick Reference: Polish Phase Commands](#quick-reference-polish-phase-commands)
  - [🧹 Sweep Dead Code](#-sweep-dead-code)
  - [🔍 Code Quality](#-code-quality)
  - [📚 Documentation](#-documentation)
  - [📊 Bundle & Performance](#-bundle--performance)
  - [✅ Full Verification Suite](#-full-verification-suite)
  - [🎨 Common Fixes](#-common-fixes)
    - [Remove unused imports automatically](#remove-unused-imports-automatically)
    - [Clean up specific file](#clean-up-specific-file)
    - [Fix markdown issues](#fix-markdown-issues)
    - [Update component status](#update-component-status)
  - [🚦 Pre-commit (Automatic)](#-pre-commit-automatic)
  - [📋 Checklists](#-checklists)
  - [🆘 Quick Troubleshooting](#-quick-troubleshooting)
  - [🎓 Best Practices](#-best-practices)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Quick Reference: Polish Phase Commands

> **TL;DR**: Commands for code quality, documentation, and build polish

---

## 🧹 Sweep Dead Code

```bash
# Find orphaned files (not imported anywhere)
npm run sweep:orphans

# Find unused exports
npm run sweep:exports

# Find unused dependencies
npm run sweep:deps

# Run all sweeps at once
npm run sweep
```

**Output**: `.sweep-orphans.txt` (gitignored)

---

## 🔍 Code Quality

```bash
# Lint JavaScript/TypeScript
npm run lint

# Fix auto-fixable issues
npm run lint -- --fix

# Run tests
npm run test

# Run tests in watch mode
npm run test:watch

# Build production bundle
npm run build

# Validate Bible compliance
npm run validate:touched
```

---

## 📚 Documentation

```bash
# Lint all markdown files
npm run docs:lint

# Auto-fix markdown issues
npm run docs:lint -- --fix

# Generate table of contents
npm run docs:toc

# Run all doc checks
npm run docs:verify

# Generate status dashboard
npm run docs:status
```

**Output**: `Documentation/STATUS.md`

---

## 📊 Bundle & Performance

```bash
# Check bundle size (must build first)
npm run build
npm run perf:budget
```

**Current budget**: 250 KB for JS assets  
**Config**: See `size-limit` in `package.json`

---

## ✅ Full Verification Suite

```bash
# Everything at once
npm run lint && \
npm run test && \
npm run build && \
npm run perf:budget && \
npm run docs:verify && \
npm run validate:touched
```

Or use the existing verify script:

```bash
npm run verify  # Runs post_patch.mjs checks
```

---

## 🎨 Common Fixes

### Remove unused imports automatically

```bash
npm run lint -- --fix
```

### Clean up specific file

```bash
npx eslint --fix src/path/to/file.jsx
```

### Fix markdown issues

```bash
npx markdownlint --fix 'Documentation/**/*.md'
```

### Update component status

1. Edit `Documentation/progress/progress.json`
2. Run `npm run docs:status`
3. Review `Documentation/STATUS.md`

---

## 🚦 Pre-commit (Automatic)

Husky runs automatically on `git commit`:

- ESLint --fix on staged `.js`, `.jsx`, `.ts`, `.tsx`
- Markdownlint --fix on staged `.md`
- Prettier --write on all staged files

**To bypass** (not recommended):

```bash
git commit --no-verify
```

---

## 📋 Checklists

- **Full checklist**: `Documentation/POLISH_CHECKLIST.md`
- **Setup guide**: `Documentation/SETUP_POLISH.md`
- **Data contract**: `Documentation/Standards/json_data_contract_bible.md`
- **Primary instructions**: `.github/instructions/primaryinstructions.instructions.md`

---

## 🆘 Quick Troubleshooting

**Too many lint errors?**

```bash
# Fix automatically
npm run lint -- --fix

# Or disable specific rules temporarily (not recommended)
# Add to eslint.config.js
```

**Orphan hunter wrong?**

```bash
# Entry points configured in tools/orphan_hunter.mjs
# Default: src/main.jsx, server/src/index.ts
```

**Bundle too big?**

Run the production build and inspect emitted assets.

**UI cannot reach backend (`net::ERR_CONNECTION_REFUSED`)?**

- Restart `./start` and ensure the Express server is running.
- If you are on macOS with IPv6 default, run `CASE_PROXY_HOST=127.0.0.1 ./start` (or set `HOST=0.0.0.0` for LAN).

```bash
# Analyze what's large
npm run build
ls -lh dist/assets/

# Consider lazy loading:
# - PDF.js viewer
# - AV player
# - Notebook editor
```

**Markdown linting too strict?**

```bash
# Edit .markdownlint.json
# Disable rules: "MD###": false
```

---

## 🎓 Best Practices

1. **Run sweeps weekly** during cleanup sessions
2. **Fix lint errors immediately** (don't accumulate debt)
3. **Document status changes** in progress.json
4. **Keep bundle under budget** (lazy-load heavy features)
5. **Use PR triplets** (spec + manifest + runlog)
6. **Check the Bible** before touching JSON schemas

---

**Print this and tape it to your monitor!** 📌
