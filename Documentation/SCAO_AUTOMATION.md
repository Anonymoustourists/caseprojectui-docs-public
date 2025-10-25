# SCAO Form Automation System

**Automated Michigan Court Form Detection & Field Extraction with AI**

Last Updated: October 15, 2025

---

## Overview

This system uses AI to analyze blank SCAO (State Court Administrative Office) forms and generate both detection patterns AND field structure templates. The goal is to enable intelligent form processing with machine-learning-based field extraction.

### System Capabilities

#### Phase 1: Form Detection ✅ COMPLETE
- **One-Time Training**: Downloaded all 227 SCAO forms, analyzed with GPT-4o-mini
- **Smart Detection**: AI identified unique text patterns that distinguish each form
- **Auto-Classification**: Filled forms automatically matched to correct form type
- **Files**: `config/detectors.wizard.json` (227 trained detectors)

#### Phase 2: Field Structure Extraction 🔄 IN PROGRESS
- **Field Templates**: AI extracts field definitions from blank forms
- **Structured Definitions**: Each form has field IDs, types, labels, hint texts
- **96 Priority Forms**: Selected high-value forms (criminal, judgments, probation)
- **Files**: `form_sources/field_templates/{CODE}_fields.json`

#### Phase 3: Wizard Integration 📋 PLANNED
- **Guided Labeling**: Wizard shows pre-defined field list from templates
- **User Training**: User clicks field → draws bbox on PDF → system learns
- **Progressive Learning**: After ~5 labeled documents, system auto-extracts new ones
- **Coordinate Storage**: Learned bbox coordinates stored per form type

#### Phase 4: Auto-Extraction 🎯 FUTURE
- **Pattern Matching**: Use learned coordinates to auto-populate wizard
- **Confidence Scores**: Show extraction confidence, allow user corrections
- **Continuous Learning**: Each correction improves future extractions

---

## Current Status (October 15, 2025)

### ✅ Completed
1. **Form Detection** - All 227 forms trained
   - `config/detectors.wizard.json` - Smart detection patterns
   - Upload filled PDF → system identifies form type
   
2. **Form Crawler** - 8 Michigan Courts URLs
   - `forms/manifest.json` - 227 form metadata
   - `form_sources/raw/` - All blank PDFs downloaded

3. **Field Template Extraction** - Running on 96 selected forms
   - `scripts/extract_selected_forms.mjs` - GPT-based field extractor
   - `SCAO_FORMS_CHECKLIST.csv` - User-selected priority forms
   - Output: `form_sources/field_templates/{CODE}_fields.json`

### 🔄 In Progress
- Extracting field structures from 96 priority forms
- Estimated completion: ~10 minutes
- Cost: ~$3-5

### 📋 Next Steps

#### Step 1: Complete Field Template Extraction
- Wait for current extraction to finish
- Review generated field templates
- Commit to repository

#### Step 2: Wizard Integration
Build UI components to use field templates:
```javascript
// Load field template for detected form
const template = await loadFieldTemplate(detectedFormCode);

// Display field checklist in wizard
<FieldChecklist fields={template.fields} />

// User clicks field → draws bbox → save coordinates
onFieldLabeled(fieldId, bbox);
```

#### Step 3: Coordinate Storage System
```json
{
  "formCode": "MC227",
  "learnedFields": {
    "defendant_name": {
      "bbox": {"x": 100, "y": 200, "w": 300, "h": 20},
      "confidence": 0.95,
      "sampleCount": 12
    }
  }
}
```

#### Step 4: Auto-Extraction Engine
- Match learned coordinates to new PDFs
- Extract text at those positions
- Pre-populate wizard fields
- User verifies/corrects

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Michigan Courts Website (8 URLs)                            │
└────────────────┬────────────────────────────────────────────┘
                 ↓ (one-time crawl)
┌─────────────────────────────────────────────────────────────┐
│ forms/manifest.json (227 forms)                             │
│ form_sources/raw/{CODE}/*.pdf (blank PDFs)                  │
└────────────────┬─────────────────┬──────────────────────────┘
                 ↓                 ↓
      (form detection)    (field extraction)
                 ↓                 ↓
┌────────────────────┐  ┌──────────────────────────────────┐
│ GPT-4o-mini        │  │ GPT-4o-mini                      │
│ "Find unique       │  │ "List all fields on this form"   │
│  patterns"         │  │                                  │
└────────────┬───────┘  └──────────┬───────────────────────┘
             ↓                     ↓
┌──────────────────────┐  ┌────────────────────────────────┐
│ detectors.wizard.json│  │ field_templates/{CODE}.json    │
│ (detection patterns) │  │ (field definitions)            │
└────────────┬─────────┘  └──────────┬─────────────────────┘
             ↓                       ↓
┌─────────────────────────────────────────────────────────────┐
│ User uploads filled PDF                                     │
└────────────────┬────────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────────────┐
│ 1. Auto-detect form type (MC227)                    ✅      │
│ 2. Load field template (96 fields defined)          ✅      │
│ 3. Show wizard with field checklist                 📋      │
│ 4. User labels fields → system learns coordinates   📋      │
│ 5. Next upload → auto-extract using learned coords  🎯      │
└─────────────────────────────────────────────────────────────┘
```

**The Vision:** One-time AI training → User labels a few examples → System learns → Auto-extraction forever.

---

## Quick Start

### 1. Initial Setup (One Time)

```bash
# Install dependencies
npm install

# Install Playwright browsers (required for JavaScript-rendered pages)
npx playwright install chromium

# Install poppler-utils for PDF text extraction
# macOS:
brew install poppler

# Linux:
apt-get install poppler-utils

# Ensure OpenAI API key is in .env.local
echo "OPENAI_API_KEY=your-key-here" >> .env.local
```

### 2. Download All SCAO Forms (One Time)

```bash
# Crawl all Michigan court forms (227+ forms)
node scripts/scao_sync.mjs --areas all

# This creates:
# - forms/manifest.json (metadata)
# - form_sources/raw/{CODE}/*.pdf (blank PDFs)
```

### 3. Train Form Detectors with AI (One Time) ✅ COMPLETE

```bash
# Train ALL forms (227 forms trained)
node scripts/train_form_detectors.mjs --all

# OR train in batches (if API rate limits hit)
node scripts/train_form_detectors.mjs --batch=50

# OR train single form for testing
node scripts/train_form_detectors.mjs MC227
```

**What this does:**
1. Reads each blank PDF
2. Sends to GPT-4o-mini: "Identify unique text patterns on this form"
3. GPT finds distinctive phrases, headers, form codes
4. Updates `config/detectors.wizard.json` with smart detection rules
5. System can now auto-detect this form when filled versions are uploaded

**Status:** ✅ All 227 forms trained (October 15, 2025)

### 4. Extract Field Structures (Priority Forms) 🔄 IN PROGRESS

```bash
# Extract field definitions from selected forms
node scripts/extract_selected_forms.mjs

# This reads SCAO_FORMS_CHECKLIST.csv (96 forms marked YES)
# Creates: form_sources/field_templates/{CODE}_fields.json
```

**What this does:**
1. Reads blank PDF for each selected form
2. Sends to GPT-4o-mini: "List all fields on this form"
3. GPT identifies field IDs, types, labels, hint texts
4. Saves field template JSON for wizard integration
5. Wizard can show pre-defined field checklist for guided labeling

**Status:** 🔄 Running on 96 priority forms (est. 10 min)
- 46 HIGH priority (criminal sentences, charges, judgments)
- 40 MED priority (probation, bonds, appeals)
- 10 LOW priority (administrative, fee waivers)

### 5. Regenerate Labels

```bash
# Generate labels.yml from trained detectors
node scripts/generate_labels_from_detectors.mjs
```

### 5. Test Detection

Upload a filled SCAO form to the Case Project UI. The system should automatically:
- Detect which form type it is (e.g., "MC227 - Judgment of Sentence")
- Set the detector type automatically
- Extract fields based on the learned patterns

---

## Maintenance

### When to Re-Sync

SCAO forms don't update frequently. Only re-run the sync when:
- Michigan Courts announces new forms
- You notice a form revision you don't have
- Approximately: Check quarterly or semi-annually

### Manual Re-Sync

```bash
# Download latest forms
node scripts/scao_sync.mjs --areas all --force

# Re-train only NEW forms
node scripts/train_form_detectors.mjs --all

# Regenerate labels
node scripts/generate_labels_from_detectors.mjs
```

---

## Scripts Reference

### scao_sync.mjs

Crawls Michigan court form indexes and downloads PDFs.

**Important:** Requires Playwright because the Michigan Courts website uses JavaScript rendering (React/Vue framework). Static HTML fetching returns an empty page. The script launches a Chromium browser to render the page and extract form listings from dynamically loaded div elements.

**Usage:**
```bash
node scripts/scao_sync.mjs [--areas=all,circuit,district] [--force]
```

**Options:**
- `--areas`: Comma-separated list of areas to sync (default: `all`)
  - `all`: Michigan Court Forms index (most comprehensive, 227+ forms)
  - `circuit`: Circuit Court forms
  - `district`: District Court forms
- `--force`: Re-download all PDFs even if unchanged

**Output:**
- `forms/manifest.json`: Form metadata (code, title, revised date, hash, etc.)
- `form_sources/raw/{CODE}/{CODE}_YYYY-MM.pdf`: Downloaded PDFs
- `tmp/scao_debug.html`: Rendered HTML for debugging (optional)

**Example:**
```bash
# Sync all forms
node scripts/scao_sync.mjs --areas all

# Force re-download circuit forms
node scripts/scao_sync.mjs --areas circuit --force
```

### build_form_registry.mjs

Generates form registry and auto-registers new forms as detectors.

**Usage:**
```bash
node scripts/build_form_registry.mjs
```

**Process:**
1. Reads `forms/manifest.json`
2. Generates `config/forms.registry.json` with clean mappings
3. Checks existing detectors in `config/detectors.wizard.json`
4. Auto-calls `add_form_detector.mjs` for new forms
5. Regenerates `config/labels.yml`

**Output:**
- `config/forms.registry.json`: Form code → name/category/pdf mappings

**Example Registry Entry:**
```json
{
  "MC227": {
    "name": "Application to Set Aside Conviction(s)",
    "category": "Criminal – Misdemeanor",
    "pdf": "form_sources/raw/MC227/MC227_2025-03.pdf",
    "revised": "2025-03",
    "citations": ["MCL 780.621"],
    "source": "https://www.courts.michigan.gov/siteassets/forms/scao-approved/mc227.pdf",
    "hash": "a3f5d2e8c1b4...",
    "lastChecked": "2025-10-15T07:00:00Z"
  }
}
```

### suggest_fields.mjs

Uses OpenAI GPT-4 to analyze PDF and suggest field names/locations.

**Usage:**
```bash
node scripts/suggest_fields.mjs [form-code] [pdf-path]
```

**Example:**
```bash
node scripts/suggest_fields.mjs MC227 form_sources/raw/MC227/MC227_2025-03.pdf
```

**Process:**
1. Extracts text from PDF page 1 using `pdftotext`
2. Calls OpenAI API with structured prompt
3. Parses JSON response with field suggestions
4. Saves to `form_sources/suggestions/{CODE}_suggestions.json`

**Output Format:**
```json
{
  "formCode": "MC227",
  "formName": "Application to Set Aside Conviction(s)",
  "generatedAt": "2025-10-15T...",
  "model": "gpt-4o-mini",
  "suggestions": [
    {
      "id": "defendant_name",
      "label": "Defendant Name",
      "type": "name",
      "hintTexts": ["Defendant", "Name of Defendant"]
    },
    {
      "id": "case_number",
      "label": "Case Number",
      "type": "case_number",
      "hintTexts": ["Case No.", "Case Number"]
    }
  ]
}
```

**Supported Field Types:**
- `text`: Generic text field
- `date`: Date fields (filing date, DOB, offense date)
- `case_number`: Case/docket/file numbers
- `name`: Person names (defendant, plaintiff, attorney, judge)
- `signature`: Signature areas
- `checkbox`: Checkboxes
- `number`: Numeric fields (amounts, counts, sentences)
- `address`: Address fields

---

## GitHub Actions Workflow

### Automated Nightly Sync

The workflow runs every night at 2 AM EST:

**File:** `.github/workflows/scao-sync.yml`

**Steps:**
1. Checkout repository
2. Install dependencies + poppler-utils
3. Run `scao_sync.mjs --areas all`
4. Run `build_form_registry.mjs`
5. Run `generate_labels_from_detectors.mjs`
6. Check for changes (git diff)
7. Generate changelog with summary
8. Create pull request if changes detected

**PR Contents:**
- Commit message with summary
- Changelog with new/updated forms
- Links to official "Recently Revised" page
- Workflow run link

### Manual Trigger

You can also trigger the workflow manually:

1. Go to GitHub Actions → "SCAO Forms Sync"
2. Click "Run workflow"
3. Choose areas to sync (`all`, `circuit`, `district`)
4. Optionally enable "Force re-download"

---

## Data Flow

### 1. Initial Crawl

```bash
node scripts/scao_sync.mjs --areas all
```

**What happens:**
- Fetches HTML from Michigan Courts indexes
- Parses tables to extract form metadata
- Downloads PDFs to `form_sources/raw/{CODE}/`
- Calculates SHA-256 hash for change detection
- Writes `forms/manifest.json`

### 2. Registry Build

```bash
node scripts/build_form_registry.mjs
```

**What happens:**
- Reads `forms/manifest.json`
- Generates clean registry with code → name mappings
- Compares against existing detectors
- Auto-registers new forms via `add_form_detector.mjs`
- Writes `config/forms.registry.json`

### 3. AI Field Suggestions

```bash
node scripts/suggest_fields.mjs MC227 form_sources/raw/MC227/MC227_2025-03.pdf
```

**What happens:**
- Extracts page-1 text with `pdftotext`
- Sends to OpenAI API with structured prompt
- Receives JSON with field suggestions
- Saves to `form_sources/suggestions/MC227_suggestions.json`

### 4. Manual Labeling

**In UI:**
1. Upload blank MC227 PDF
2. Select "MC227 - Application to Set Aside Conviction(s)" as Detector Type
3. Open PDF Label Mode
4. Refer to AI suggestions for field hints
5. Draw bounding boxes around each field
6. Assign labels (defendant_name, case_number, etc.)

**Behind the scenes:**
- Annotations save to `training/form_mc227/{docId}/annotations.jsonl`
- PDF copies to `training/form_mc227/{docId}/document.pdf`
- Metadata tracks label count

### 5. Template Export

```bash
node scripts/export_form_template.mjs 01K7MD367W9S740P65SVMZR5KR MC227
```

**What happens:**
- Reads training annotations
- Extracts bbox coordinates for each label
- Infers field types from label names
- Creates `form_templates/criminal_misdemeanor/MC227.json`
- Copies reference PDF

---

## File Structure

```
forms/
  manifest.json                   # Master form list with metadata

form_sources/
  raw/
    MC227/
      MC227_2025-03.pdf           # Downloaded blank forms
    MC220/
      MC220_2024-11.pdf
  suggestions/
    MC227_suggestions.json        # AI field suggestions
    MC220_suggestions.json

config/
  forms.registry.json             # Code → name/category mappings
  detectors.wizard.json           # Detector definitions (auto-updated)
  labels.yml                      # Label definitions (auto-generated)

training/
  form_mc227/
    01K7MD367.../
      document.pdf                # Labeled blank PDF
      annotations.jsonl           # Label events
      metadata.json               # Doc metadata
  form_mc220/
    ...

form_templates/
  criminal_misdemeanor/
    MC227.json                    # Field locations template
    MC227.pdf                     # Reference PDF
  criminal_felony/
    MC220.json
    MC220.pdf
```

---

## Configuration

### Environment Variables

**`.env.local`:**
```bash
VITE_API_BASE=http://localhost:5050
```env
# .env.local
OPENAI_API_KEY=your-openai-api-key-here
```

### Source URLs

**Defined in `scripts/scao_sync.mjs`:**
```javascript
const INDEXES = {
  all: 'https://www.courts.michigan.gov/SCAO-forms/Michigan-court-forms/',
  circuit: 'https://www.courts.michigan.gov/SCAO-forms/circuit-court-forms/',
  district: 'https://www.courts.michigan.gov/SCAO-forms/district-court-index/',
  revised: 'https://www.courts.michigan.gov/SCAO-forms/recently-revised-court-forms/'
};
```

---

## Field Template Structure

Each generated field template follows this structure:

```json
{
  "formCode": "MC227",
  "formTitle": "Judgment of Sentence",
  "category": "Criminal - Sentencing",
  "priority": "HIGH",
  "generatedAt": "2025-10-15T22:30:53.832Z",
  "model": "gpt-4o-mini",
  "fieldCount": 18,
  "fields": [
    {
      "id": "defendant_name",
      "label": "Defendant Full Name",
      "type": "name",
      "hintTexts": ["Defendant", "Name of Defendant", "Defendant's Name"],
      "required": true,
      "description": "Full legal name of the defendant"
    },
    {
      "id": "case_number",
      "label": "Case Number",
      "type": "case_number",
      "hintTexts": ["Case No.", "Case Number", "File No."],
      "required": true,
      "description": "Court-assigned case identifier"
    },
    {
      "id": "sentence_jail_days",
      "label": "Jail Sentence (Days)",
      "type": "number",
      "hintTexts": ["days in jail", "jail sentence", "term of"],
      "required": false,
      "description": "Number of days of jail time imposed"
    }
  ]
}
```

**Field Types:**
- `name` - Person names
- `text` - General text
- `date` - Dates
- `case_number` - Case identifiers
- `signature` - Signature fields
- `checkbox` - Checkboxes
- `number` - Numeric values
- `address` - Addresses
- `phone` - Phone numbers
- `email` - Email addresses
- `dropdown` - Dropdown selections

**How Fields Are Used:**
1. **Wizard UI**: Display field checklist for user
2. **Hint Texts**: Help user locate field on PDF
3. **Type Validation**: Enforce data type rules
4. **Learning**: Store bbox coordinates per field ID
5. **Auto-Extraction**: Use learned coordinates on new uploads

---

## Priority Form Selection

Forms were prioritized based on case management value:

### HIGH Priority (46 forms)
- Criminal sentences and judgments
- Felony/misdemeanor charges and complaints
- Probation violations and orders
- Key appeals and motions
- Traffic citations and DUI forms

### MED Priority (40 forms)
- Bond modifications and receipts
- Pretrial releases and continuances
- Attorney appointments
- Court appearances and notices
- Restitution orders

### LOW Priority (10 forms)
- Fee waivers and administrative forms
- Interpreter requests
- Media coverage requests
- Case inventory forms

**Selection File:** `SCAO_FORMS_CHECKLIST.csv`
- Edit "Include" column (YES/NO) to change selection
- Re-run extraction: `node scripts/extract_selected_forms.mjs`

---

## Troubleshooting

### Crawler Issues

**Problem:** HTML parsing fails  
**Solution:** Check if Michigan Courts changed their page structure. Update regex patterns in `parseFormsTable()` or `parseCategoryPage()`.

**Problem:** PDFs fail to download  
**Solution:** Check network connectivity. Verify URLs are still valid. Use `--force` to retry.

**Problem:** Form code extraction fails  
**Solution:** Check filename format. Update `extractFormCode()` regex if needed.

### AI Suggestions Issues

**Problem:** OpenAI API key not found  
**Solution:** Ensure `OPENAI_API_KEY` is set in `.env.local`.

**Problem:** pdftotext not found  
**Solution:** Install poppler-utils (`brew install poppler` on macOS).

**Problem:** Suggestions are inaccurate  
**Solution:** This is first-pass only. Use suggestions as hints, then manually adjust in UI.

**Problem:** JSON parsing fails  
**Solution:** GPT sometimes returns markdown. The script tries to extract JSON from code blocks, but check the raw response if it fails.

### GitHub Actions Issues

**Problem:** Workflow doesn't run  
**Solution:** Check cron syntax. Verify workflow file is in `.github/workflows/`. Check Actions are enabled for repo.

**Problem:** PR not created  
**Solution:** Ensure `GITHUB_TOKEN` has write permissions. Check if there are uncommitted changes.

**Problem:** Poppler install fails  
**Solution:** Add `sudo apt-get update` before install step.

---

## Future Enhancements

### Phase 2: Template Application

**Goal:** Auto-extract data from filled forms

**Plan:**
1. Detect form type from uploaded PDF (keyword matching)
2. Load matching template from `form_templates/`
3. OCR text from each bbox region
4. Populate structured JSON with extracted values
5. Present in UI for review/correction
6. Save to wizard/event/people pipelines

### Phase 3: Machine Learning

**Goal:** Improve field detection over time

**Plan:**
1. Collect user corrections as feedback
2. Fine-tune field type classifier
3. Improve bbox suggestions
4. Auto-adjust templates for form revisions

### Phase 4: Cross-Jurisdiction

**Goal:** Support forms from other states

**Plan:**
1. Add new crawlers for other state courts
2. Generalize registry structure
3. Support jurisdiction-specific categories
4. Share templates in community library

---

## API Reference

### OpenAI Field Suggestion Prompt

**System:**
```
You are an expert at analyzing legal forms and identifying data fields. Always return valid JSON.
```

**User Prompt Structure:**
```
You are analyzing a Michigan court form (MC227 - Application to Set Aside Conviction(s)).

Given the text extracted from page 1 of this form, suggest the most important fields...

For each field, provide:
1. A machine-readable ID (lowercase_with_underscores)
2. A human-readable label
3. The field type (text, date, case_number, name, signature, checkbox, number, address)
4. Text hints - phrases that appear near this field on the form

Focus on:
- Party names (defendant, plaintiff, attorney, judge)
- Case identifiers (case number, docket number, file number)
- Dates (filing date, hearing date, DOB, offense date)
- Signatures (judge, defendant, attorney)
- Court information (court name, county, jurisdiction)
- Form-specific key fields (sentence terms, plea, verdict, etc.)

Return a JSON array of field suggestions.

PDF Text:
[extracted text here]
```

**Model:** `gpt-4o-mini`  
**Temperature:** `0.3` (low for consistency)  
**Max Tokens:** `2000`

---

## Testing

### Test Crawler

```bash
# Test with small set
node scripts/scao_sync.mjs --areas circuit

# Check manifest
cat forms/manifest.json | jq '.MC227'

# Verify PDF downloaded
ls -lh form_sources/raw/MC227/
```

### Test Registry Build

```bash
# Build registry
node scripts/build_form_registry.mjs

# Check registry
cat config/forms.registry.json | jq '.MC227'

# Verify detector added
cat config/detectors.wizard.json | jq '.types[] | select(.id=="form_mc227")'
```

### Test AI Suggestions

```bash
# Get suggestions
node scripts/suggest_fields.mjs MC227 form_sources/raw/MC227/MC227_2025-03.pdf

# Check output
cat form_sources/suggestions/MC227_suggestions.json | jq '.suggestions'
```

---

## Maintenance

### Weekly Tasks

- Review "Recently Revised" PRs from GitHub Actions
- Merge approved form updates
- Check for failed syncs in Actions logs

### Monthly Tasks

- Review AI suggestion accuracy
- Update prompts if needed
- Archive old form versions
- Check disk usage in `form_sources/`

### Quarterly Tasks

- Review all templates for accuracy
- Update documentation
- Check for Michigan Courts website changes
- Audit form coverage (ensure all common forms have templates)

---

## Resources

- **Michigan Courts Forms**: https://www.courts.michigan.gov/SCAO-forms/
- **Recently Revised**: https://www.courts.michigan.gov/SCAO-forms/recently-revised-court-forms/
- **Explanation of Changes**: https://www.courts.michigan.gov/SCAO-forms/explanationofchanges-eoc/
- **Form Detection System**: `Documentation/TECHNICAL_REFERENCE.md#form-detection-system`
- **Template Creation Guide**: `form_templates/README.md`

---

**Questions or Issues?**  
Open an issue on GitHub or check existing PRs for form-related updates.
