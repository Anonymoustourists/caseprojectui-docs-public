<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Michigan Court PDF to Markdown Conversion Specification](#michigan-court-pdf-to-markdown-conversion-specification)
  - [Conversion Rules](#conversion-rules)
    - [1. Boilerplate Removal](#1-boilerplate-removal)
    - [2. Heading Structure Mapping](#2-heading-structure-mapping)
    - [3. Paragraph Reconstruction](#3-paragraph-reconstruction)
    - [4. Opinion Body Detection](#4-opinion-body-detection)
    - [5. Footnote Processing](#5-footnote-processing)
    - [6. Metadata Extraction](#6-metadata-extraction)
  - [Pattern Examples](#pattern-examples)
    - [Input PDF Text](#input-pdf-text)
    - [Output Markdown](#output-markdown)
    - [Metadata JSON Output](#metadata-json-output)
  - [Customization Guidelines](#customization-guidelines)
    - [Adding New Boilerplate Patterns](#adding-new-boilerplate-patterns)
    - [Modifying Heading Recognition](#modifying-heading-recognition)
    - [Adding Legal Abbreviations](#adding-legal-abbreviations)
  - [Quality Assurance](#quality-assurance)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Michigan Court PDF to Markdown Conversion Specification

This document describes the rule-based conversion patterns used by the "dumb" system to convert Michigan Court of Appeals and Supreme Court PDFs to Markdown format.

## Conversion Rules

### 1. Boilerplate Removal

The following patterns are automatically removed from the PDF text:

#### Standard Headers

- `STATE OF MICHIGAN` (normal and spaced-letter variants)
- `COURT OF APPEALS` (normal and spaced-letter variants)  
- `MICHIGAN SUPREME COURT`

#### Page Elements

- Page numbers in format `-3-`, `-12-`, etc.
- Timestamps like `2:15 PM`, `10:30 AM`
- Publication disclaimers starting with "If this opinion indicates..."

#### Case Metadata Lines (removed from body)

- Lines starting with `No. 123456`
- Lines starting with `LC No. 2023-001234-CZ`
- `UNPUBLISHED` or `PUBLISHED` status lines

### 2. Heading Structure Mapping

Court outline format is converted to Markdown headings:

| Court Format | Markdown | Example |
|--------------|----------|---------|
| `I. TITLE` | `# I. TITLE` | Main sections |
| `A. SUBTITLE` | `## A. SUBTITLE` | Subsections |
| `1. SUBPOINT` | `### 1. SUBPOINT` | Numbered points |
| `i. DETAIL` | `#### i. DETAIL` | Detailed points |

**Important**: The system preserves the original numbering tokens (I., A., 1., i.) rather than converting to generic Markdown headers.

### 3. Paragraph Reconstruction

The system reconstructs paragraphs by:

#### Line Joining Logic

- Lines ending with sentence punctuation (`.`, `!`, `?`) start new paragraphs
- **Exception**: Lines ending with legal abbreviations continue to next line
- Hyphenated words broken across lines are rejoined (`wor-\nds` → `words`)

#### Legal Abbreviations (do NOT end sentences)

- `MCL.` (Michigan Compiled Laws)
- `MRE.` (Michigan Rules of Evidence)  
- `U.S.` (United States)
- `Inc.`, `Co.`, `Ltd.`, `L.L.C.`, `L.L.P.` (Corporate suffixes)
- `Ct.`, `App.` (Court abbreviations)
- `No.` (Number)
- `v.` (versus)

#### Example

```
Input PDF lines:
"The defendant violated MCL
784.234 when he committed the assault. This was
clearly established at trial."

Output Markdown:
"The defendant violated MCL 784.234 when he committed the assault. This was clearly established at trial."
```

### 4. Opinion Body Detection

The system finds where the actual opinion begins by looking for:

#### Primary Markers

- `PER CURIAM.` - Most common start of COA opinions
- Lines starting with `OPINION`

#### Fallback Markers  

- First line matching heading patterns (`I.`, `A.`, `1.`, etc.)
- Everything before these markers is considered caption/metadata

### 5. Footnote Processing

#### Detection

- Lines matching pattern: `1) footnote text` or `1. footnote text`
- Must have substantial content (more than 3 words)
- Typically found at bottom of pages

#### Output Format

Main body footnote references can optionally be converted to `[^1]` format.

Footnotes are appended as:

```markdown
---

## Footnotes

[^1]: First footnote text here
[^2]: Second footnote text here
```

### 6. Metadata Extraction

The system extracts metadata from the first page:

#### Case Name

- From banner format: `COA 123456 PLAINTIFF V DEFENDANT Opinion...`
- From caption: Looking for `ALLCAPS NAME v ALLCAPS NAME` patterns
- Normalizes `V` to `v` for readability

#### Case Numbers

- Case No.: `No. 123456` format
- Lower Court No.: `LC No. 2023-001234-CZ` format

#### Judge Panel

- Lines starting with `Before:` followed by judge names

#### Date

- Full date format: `January 15, 2025`
- Extracted from first page text

#### Publication Status

- `PUBLISHED` if contains "FOR PUBLICATION"
- `UNPUBLISHED` otherwise

#### Court Type

- Automatically set to "Michigan Court of Appeals" for COA docs
- "Michigan Supreme Court" for MSC docs

## Pattern Examples

### Input PDF Text

```
STATE OF MICHIGAN
COURT OF APPEALS

JOHN DOE,                              UNPUBLISHED
                          Plaintiff-Appellant,    January 15, 2025
v                                      No. 123456
                                       LC No. 2023-001234-CZ
JANE SMITH,
                          Defendant-Appellee.

Before: Judge A, Judge B, and Judge C.

PER CURIAM.

I. BACKGROUND

The facts of this case are as follows. Plaintiff filed
a motion for summary disposition pursuant to MCL
600.2116. The trial court denied the motion.

A. Procedural History

The defendant filed a counter-motion. This motion was
also denied by the trial court.

1. The Initial Filing

On January 1, 2023, plaintiff filed his complaint
against defendant.

---
1) This is a footnote that explains something important
about the case.
```

### Output Markdown

```markdown
# I. BACKGROUND

The facts of this case are as follows. Plaintiff filed a motion for summary disposition pursuant to MCL 600.2116. The trial court denied the motion.

## A. Procedural History

The defendant filed a counter-motion. This motion was also denied by the trial court.

### 1. The Initial Filing

On January 1, 2023, plaintiff filed his complaint against defendant.

---

## Footnotes

[^1]: This is a footnote that explains something important about the case.
```

### Metadata JSON Output

```json
{
  "case_name": "John Doe v Jane Smith",
  "case_no": "123456",
  "lc_no": "2023-001234-CZ", 
  "judges": "Judge A, Judge B, and Judge C",
  "date": "January 15, 2025",
  "publication": "UNPUBLISHED",
  "lower_court": null,
  "court": "Michigan Court of Appeals",
  "source": "pdf2md_core.py"
}
```

## Customization Guidelines

### Adding New Boilerplate Patterns

Add to `COA_BOILERPLATE_PATTERNS` list:

```python
r"^\s*YOUR_CUSTOM_HEADER\s*$",
```

### Modifying Heading Recognition

Adjust `HEADING_REPLACERS` for different outline formats:

```python
(regex.compile(r"^(SECTION\s+\d+)\.(\s+)(.+)$"), r"# \1. \3"),
```

### Adding Legal Abbreviations

Extend `ABBR_TOKENS` set:

```python
ABBR_TOKENS = {
    "MCL.", "MRE.",  # existing
    "YOURSTATE.", "CUSTOM.",  # new additions
}
```

## Quality Assurance

The system includes several quality checks:

1. **Length Validation**: Ensures output isn't dramatically shorter than input (prevents over-summarization)
2. **Structure Preservation**: Maintains original paragraph count and heading structure
3. **Content Fidelity**: Does not paraphrase or summarize - only reformats

This rule-based approach ensures consistent, predictable output without the variability of AI-based systems.
