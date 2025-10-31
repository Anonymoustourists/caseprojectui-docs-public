<!-- markdownlint-disable MD001 MD025 MD036 -->

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Wizard Template Variables \& JSON Guide](#wizard-template-variables--json-guide)
  - [Wizard JSON Guide](#wizard-json-guide)
    - [Basic Structure](#basic-structure)
    - [Field Types Reference](#field-types-reference)
    - [Conditional Fields with `show_if`](#conditional-fields-with-show_if)
    - [Person Selector After Interview Type](#person-selector-after-interview-type)
    - [Dropdown of Case Numbers with Manual Entry](#dropdown-of-case-numbers-with-manual-entry)
    - [Multiple Conditions with `in`](#multiple-conditions-with-in)
    - [Dynamic Field Defaults](#dynamic-field-defaults)
    - [Multi-Person Selection](#multi-person-selection)
    - [Logic Rules for Auto-Fill](#logic-rules-for-auto-fill)
    - [Complex Filename Templates](#complex-filename-templates)
    - [Validation Patterns](#validation-patterns)
    - [Complete Real-World Example](#complete-real-world-example)
  - [Project Info Access](#project-info-access)
    - [Available Variables](#available-variables)
    - [Example Usage in Sources Wizard](#example-usage-in-sources-wizard)
    - [Example Usage in People Wizard](#example-usage-in-people-wizard)
    - [Example Usage in Events Wizard](#example-usage-in-events-wizard)
  - [Registry Lookups](#registry-lookups)
    - [Available Registry Types](#available-registry-types)
    - [Using Registries in Wizards](#using-registries-in-wizards)
    - [Example: Police Report Wizard](#example-police-report-wizard)
  - [Setting Project Info](#setting-project-info)
  - [Managing Registries](#managing-registries)
    - [App-Wide Defaults](#app-wide-defaults)
    - [Per-Project Overrides](#per-project-overrides)
  - [Template Filters](#template-filters)
  - [Summary](#summary)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Wizard Template Variables & JSON Guide

This directory contains wizard specifications for creating Sources, People, Events, and other entities. All wizard JSON files support template variables for dynamic field defaults and filename generation.

**Quick Links:**

- [Wizard JSON Guide](#wizard-json-guide) — How to write wizard specs

- [Project Info Access](#project-info-access) — Using case metadata in templates

- [Registry Lookups](#registry-lookups) — Shared dropdown lists

- [Template Filters](#template-filters) — Formatting variables

---

## Wizard JSON Guide

### Basic Structure

All wizard specs follow this structure:

```json
{
  "version": 1,
  "entity": "source",
  "types": [
    {
      "id": "transcript",
      "label": "Transcript",
      "view": "dialogue",
      "fields": ``````[...]``````,
      "logic": ``````[...]``````,
      "filename": ``````[...]``````
    }
  ],
  "lookups": {...},
  "helpers": {...}
}
```text

### Field Types Reference

| Type          | Description                       | Example                   |
| ------------- | --------------------------------- | ------------------------- |
| `text`        | Single-line text input            | Name, case number         |
| `textarea`    | Multi-line text input             | Description, notes        |
| `number`      | Number input                      | Volume number, page count |
| `date`        | Date picker                       | Hearing date              |
| `datetime`    | Date + time picker                | Interview timestamp       |
| `boolean`     | Checkbox                          | "Is custodial?"           |
| `select`      | Dropdown (single choice)          | Court type, hearing type  |
| `multiselect` | Dropdown (multiple choices)       | Multiple charges          |
| `lookup`      | Dropdown from registry            | Agency, judge             |
| `multilookup` | Multiple selections from registry | Officers present          |
| `phone`       | Phone number input                | Witness phone             |

### Conditional Fields with `show_if`

Show/hide fields based on other field values.

**Example: Show volume number only for Trial transcripts**

```json
{
  "id": "transcript",
  "label": "Transcript",
  "fields": [
    {
      "id": "hearing_type",
      "label": "Hearing Type",
      "type": "select",
      "options": ``````["Trial", "Motion", "Prelim", "Sentencing"]``````,
      "required": true
    },
    {
      "id": "volume",
      "label": "Volume Number",
      "type": "number",
      "show_if": { "hearing_type": "Trial" },
      "help": "Volume number for multi-volume trials"
    },
    {
      "id": "witness_name",
      "label": "Witness Testifying",
      "type": "text",
      "show_if": { "hearing_type": "Trial" }
    }
  ]
}
```text

**Result:** The `volume` and `witness_name` fields only appear after user selects "Trial".

### Person Selector After Interview Type

**Example: Show person lookup for witness interviews**

```json
{
  "id": "av_interview",
  "label": "A/V Interview",
  "fields": [
    {
      "id": "interview_type",
      "label": "Interview Type",
      "type": "select",
      "options": ``````["Witness", "Suspect", "Expert", "Victim"]``````,
      "required": true
    },
    {
      "id": "person",
      "label": "Person Interviewed",
      "type": "lookup",
      "source": "people",
      "show_if": { "interview_type": "Witness" },
      "help": "Select from existing people or create new"
    },
    {
      "id": "agency",
      "label": "Law Enforcement Agency",
      "type": "lookup",
      "source": "agencies",
      "show_if": { "interview_type": "Suspect" }
    }
  ]
}
```text

### Dropdown of Case Numbers with Manual Entry

**Example: Select from existing case numbers OR enter new one**

```json
{
  "id": "court_type",
  "label": "Court Type",
  "type": "select",
  "options": ``````["Circuit", "District", "Appeals"]``````,
  "required": true
},
{
  "id": "case_number_preset",
  "label": "Case Number",
  "type": "select",
  "options": [
    "12-34567-FH",
    "13-45678-FC",
    "14-56789-FY",
    "(Enter custom)"
  ],
  "show_if": { "court_type": "Circuit" },
  "help": "Select existing or choose 'Enter custom' for new case"
},
{
  "id": "case_number_custom",
  "label": "Enter Custom Case Number",
  "type": "text",
  "show_if": { "case_number_preset": "(Enter custom)" },
  "pattern": "^``````[0-9]``````{2}-``````[0-9]``````{5}-``````[A-Z]``````{2}$",
  "help": "Format: XX-XXXXX-XX"
}
```text

**Better approach using project info:**

```json
{
  "id": "case_number",
  "label": "Case Number",
  "type": "text",
  "default": "{{projectInfo.case_number}}",
  "show_if": { "court_type": "Circuit" },
  "help": "Defaults to project case number, edit if needed"
}
```text

### Multiple Conditions with `in`

**Example: Show field only for certain court types**

```json
{
  "id": "court",
  "label": "Court",
  "type": "select",
  "options": ``````["Circuit", "District", "COA", "MSC", "Federal"]``````,
  "required": true
},
{
  "id": "federal_district",
  "label": "Federal District",
  "type": "select",
  "options": ``````["E.D. Mich.", "W.D. Mich.", "6th Circuit"]``````,
  "show_if": { "court": { "in": ``````["Federal"]`````` } }
},
{
  "id": "state_judge",
  "label": "Judge",
  "type": "lookup",
  "source": "judges",
  "show_if": { "court": { "in": ``````["Circuit", "District"]`````` } }
}
```text

### Dynamic Field Defaults

**Example: Pre-fill fields based on project info**

```json
{
  "id": "hearing",
  "label": "Court Hearing",
  "fields": [
    {
      "id": "case_number",
      "label": "Case Number",
      "type": "text",
      "default": "{{projectInfo.case_number}}",
      "required": true
    },
    {
      "id": "court",
      "label": "Court",
      "type": "text",
      "default": "{{projectInfo.circuit_court}}"
    },
    {
      "id": "judge",
      "label": "Judge",
      "type": "text",
      "default": "{{projectInfo.trial_judge}}"
    }
  ]
}
```text

### Multi-Person Selection

**Example: Select multiple officers for a custodial interview**

```json
{
  "id": "is_custodial",
  "label": "Custodial Interrogation?",
  "type": "boolean"
},
{
  "id": "officers",
  "label": "Officers Present",
  "type": "multilookup",
  "source": "people",
  "role": "Officer",
  "show_if": { "is_custodial": true },
  "help": "Select all officers present during interrogation"
},
{
  "id": "agency",
  "label": "Agency",
  "type": "lookup",
  "source": "agencies",
  "show_if": { "is_custodial": true }
}
```text

### Logic Rules for Auto-Fill

Use `logic` to automatically set fields based on other fields.

**Example: Auto-set view type based on document type**

```json
{
  "logic": [
    {
      "set": { "view": "dialogue", "subtype": "Trial" },
      "when": { "hearing_type": "Trial" }
    },
    {
      "set": { "view": "narrative" },
      "when": { "hearing_type": { "in": ``````["Motion", "Sentencing"]`````` } }
    },
    {
      "set": { "has_testimony": true },
      "when": { "hearing_type": { "in": ``````["Trial", "Prelim"]`````` } }
    }
  ]
}
```text

### Complex Filename Templates

**Example: Volume-aware trial transcript naming**

```json
{
  "filename": [
    {
      "id": "trial_with_volume",
      "when": {
        "hearing_type": "Trial",
        "volume": { "exists": true }
      },
      "template": "{{date|YYYY-MM-DD}}_{{projectInfo.case_number}}_Trial_Vol{{volume}}_{{witness_name|slug}}.pdf"
    },
    {
      "id": "trial_no_volume",
      "when": { "hearing_type": "Trial" },
      "template": "{{date|YYYY-MM-DD}}_{{projectInfo.case_number}}_Trial_{{witness_name|slug}}.pdf"
    },
    {
      "id": "default",
      "template": "{{date|YYYY-MM-DD}}_{{projectInfo.case_number}}_{{hearing_type|slug}}.pdf"
    }
  ]
}
```text

**Result Examples:**

- `2025-10-11_12-34567-FH_Trial_Vol3_jane-smith.pdf`

- `2025-10-11_12-34567-FH_Motion_suppress-evidence.pdf`

### Validation Patterns

Use `pattern` for regex validation.

```json
{
  "id": "case_no",
  "label": "Case Number",
  "type": "text",
  "pattern": "^``````[0-9]``````{2}-``````[0-9]``````{5}-``````[A-Z]``````{2}$",
  "help": "Format: XX-XXXXX-XX (e.g., 12-34567-FH)"
},
{
  "id": "phone",
  "label": "Phone Number",
  "type": "phone",
  "pattern": "^\\(``````[0-9]``````{3}\\) ``````[0-9]``````{3}-``````[0-9]``````{4}$",
  "help": "Format: (XXX) XXX-XXXX"
}
```text

### Complete Real-World Example

**Trial Transcript with all features:**

```json
{
  "id": "trial_transcript",
  "label": "Trial Transcript",
  "view": "dialogue",
  "fields": [
    {
      "id": "date",
      "label": "Transcript Date",
      "type": "date",
      "required": true
    },
    {
      "id": "case_number",
      "label": "Case Number",
      "type": "text",
      "default": "{{projectInfo.case_number}}",
      "required": true
    },
    {
      "id": "is_multi_volume",
      "label": "Multi-Volume Trial?",
      "type": "boolean"
    },
    {
      "id": "volume",
      "label": "Volume Number",
      "type": "number",
      "show_if": { "is_multi_volume": true },
      "required": true
    },
    {
      "id": "session",
      "label": "Session",
      "type": "select",
      "options": ``````["Morning", "Afternoon", "Full Day"]``````,
      "default": "Full Day"
    },
    {
      "id": "witness_testifying",
      "label": "Primary Witness",
      "type": "lookup",
      "source": "people",
      "role": "Witness",
      "help": "Main witness for this portion"
    },
    {
      "id": "page_range",
      "label": "Page Range",
      "type": "text",
      "pattern": "^``````[0-9]``````+-``````[0-9]``````+$",
      "help": "e.g., 1-50"
    }
  ],
  "logic": [
    {
      "set": { "view": "dialogue" },
      "when": { "witness_testifying": { "exists": true } }
    }
  ],
  "filename": [
    {
      "id": "multi_volume",
      "when": { "is_multi_volume": true },
      "template": "{{date|YYYY-MM-DD}}_{{case_number}}_Trial_Vol{{volume}}_{{witness_testifying|slug}}_p{{page_range}}.pdf"
    },
    {
      "id": "single",
      "template": "{{date|YYYY-MM-DD}}_{{case_number}}_Trial_{{session|slug}}_{{witness_testifying|slug}}.pdf"
    }
  ],
  "tags": ``````["trial", "transcript", "{{witness_testifying}}", "vol{{volume}}"]``````
}
```text

---

## Project Info Access

All wizards (sources, people, events) can reference **project-level case metadata** in filename templates and field defaults.

### Available Variables

The following variables are available from the **Project Info** panel (Settings → Project Information):

| Variable                           | Description           | Example                     |
| ---------------------------------- | --------------------- | --------------------------- |
| `{{projectInfo.case_number}}`      | Case number           | `12-34567-FH`               |
| `{{projectInfo.case_caption}}`     | Case caption          | `People v. Doe`             |
| `{{projectInfo.circuit_court}}`    | Circuit court name    | `Wayne Circuit Court`       |
| `{{projectInfo.district_court}}`   | District court name   | `36th District Court`       |
| `{{projectInfo.appeals_court}}`    | Appeals court name    | `Michigan Court of Appeals` |
| `{{projectInfo.trial_judge}}`      | Trial judge name      | `Hon. Jane Smith`           |
| `{{projectInfo.defendant}}`        | Defendant name        | `John Doe`                  |
| `{{projectInfo.prosecutor}}`       | Prosecutor name       | `Jane Prosecutor`           |
| `{{projectInfo.defense_attorney}}` | Defense attorney name | `Bob Attorney`              |
| `{{projectInfo.filing_date}}`      | Case filing date      | `2023-01-15`                |

### Example Usage in Sources Wizard

In `sources.wizard.json`:

```json
{
  "id": "transcript",
  "label": "Transcript",
  "fields": [
    {
      "id": "date",
      "label": "Date",
      "type": "date",
      "required": true
    },
    {
      "id": "hearing_type",
      "label": "Hearing Type",
      "type": "select",
      "options": ``````["Trial", "Motion", "Sentencing"]``````
    }
  ],
  "filename": [
    {
      "id": "default",
      "template": "{{date|YYYY-MM-DD}}_{{projectInfo.case_number}}_{{hearing_type|slug}}_Transcript.pdf"
    }
  ]
}
```text

**Result:** `2025-10-11_12-34567-FH_Trial_Transcript.pdf`

### Example Usage in People Wizard

In `people.wizard.json`:

```json
{
  "id": "witness",
  "label": "Witness",
  "fields": [
    {
      "id": "full_name",
      "label": "Full Name",
      "type": "text",
      "required": true
    },
    {
      "id": "case_relation",
      "label": "Relation to Case",
      "type": "text",
      "default": "Witness in {{projectInfo.case_caption}}"
    }
  ]
}
```text

**Result:** Field `case_relation` will be pre-filled with `"Witness in People v. Doe"`

### Example Usage in Events Wizard

In `events.wizard.json`:

```json
{
  "id": "hearing",
  "label": "Court Hearing",
  "fields": [
    {
      "id": "date",
      "label": "Date",
      "type": "date",
      "required": true
    },
    {
      "id": "court",
      "label": "Court",
      "type": "text",
      "default": "{{projectInfo.circuit_court}}"
    },
    {
      "id": "judge",
      "label": "Judge",
      "type": "text",
      "default": "{{projectInfo.trial_judge}}"
    }
  ],
  "title": [
    {
      "id": "default",
      "template": "{{date|YYYY-MM-DD}} Hearing - {{projectInfo.case_number}}"
    }
  ]
}
```text

**Result:** Event title will be `"2025-10-11 Hearing - 12-34567-FH"` and fields will be pre-filled with court and judge from project info.

---

## Registry Lookups

Wizards can use **shared registries** (agencies, courts, judges) for dropdown fields. These registries are managed globally with optional per-project overrides.

### Available Registry Types

- **`agencies`** — Law enforcement agencies (Detroit PD, MSP, FBI, etc.)

- **`courts`** — Courts (Wayne Circuit, Michigan COA, etc.)

- **`judges`** — Judges (Hon. Smith, Hon. Johnson, etc.)

### Using Registries in Wizards

```json
{
  "id": "agency",
  "label": "Agency",
  "type": "lookup",
  "source": "agencies"
}
```text

The dropdown will be populated from:

1. **App defaults:** `server/config/registries/agencies.json`

1. **Project overrides:** `<project>/config/registries/agencies.json`


Project overrides take precedence and are merged by ID.

### Example: Police Report Wizard

```json
{
  "id": "police_report",
  "label": "Police Report",
  "fields": [
    {
      "id": "date",
      "label": "Date",
      "type": "date",
      "required": true
    },
    {
      "id": "agency",
      "label": "Agency",
      "type": "lookup",
      "source": "agencies"
    },
    {
      "id": "report_no",
      "label": "Report Number",
      "type": "text"
    }
  ],
  "filename": [
    {
      "id": "default",
      "template": "{{date|YYYY-MM-DD}}_{{agency|slug}}_Report_{{report_no}}.pdf"
    }
  ]
}
```bash

**Result:** User selects "Detroit PD" from dropdown → filename becomes `2025-10-11_detroit-pd_Report_12345.pdf`

---

## Setting Project Info

To make project info available to all wizards:

1. Open **Settings** (⚙️ icon in sidebar)

1. Scroll to **Project Information** section

1. Click **Edit**

1. Fill in case metadata fields:

   - Case Number

   - Case Caption

   - Circuit Court

   - District Court

   - Trial Judge

   - Defendant

   - Prosecutor

   - Defense Attorney

   - Charges (one per line)

   - etc.

1. Click **Save**


Now all wizards in the project can access these values via `{{projectInfo.*}}` variables.

---

## Managing Registries

### App-Wide Defaults

Edit files in `server/config/registries/`:

- `agencies.json`

- `courts.json`

- `judges.json`

These apply to all projects unless overridden.

### Per-Project Overrides

Create files in `<project>/config/registries/`:

- `agencies.json`

- `courts.json`

- `judges.json`

These override app defaults by ID for the specific project only.

**Example:** Add a custom agency to your project:

`<project>/config/registries/agencies.json`:

```json
{
  "version": 1,
  "items": [
    {
      "id": "custom_pd",
      "label": "Custom PD",
      "full_name": "Custom Police Department"
    }
  ]
}
```text

This agency will now appear in the dropdown alongside app defaults.

---

## Template Filters

Variables support filters for formatting:

| Filter         | Description                     | Example                               |
| -------------- | ------------------------------- | ------------------------------------- |
| `\|YYYY-MM-DD` | Format date                     | `{{date\|YYYY-MM-DD}}` → `2025-10-11` |
| `\|slug`       | Slugify (lowercase, hyphens)    | `{{agency\|slug}}` → `detroit-pd`     |
| `\|upper`      | Uppercase                       | `{{court\|upper}}` → `WAYNE CIRCUIT`  |
| `\|abbr`       | Use abbreviation (from helpers) | `{{published\|abbr}}` → `PUB`         |

---

## Summary

- **Project Info** provides case-level metadata accessible via `{{projectInfo.*}}`

- **Registries** provide shared lookup lists (agencies, courts, judges)

- **All wizards** (Sources, People, Events) can use both in templates and defaults

- **Per-project overrides** allow customization without affecting other cases

For more information on wizard specs, see:

- `sources.wizard.json` — Source ingestion wizard

- `people.wizard.json` — People creation wizard

- `events.wizard.json` — Events creation wizard
