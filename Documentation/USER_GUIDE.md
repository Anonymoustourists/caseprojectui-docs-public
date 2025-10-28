# User Guide

**Case Project** — Your complete guide to managing legal cases

**Last Updated**: October 14, 2025  
**Version**: 0.1.0

---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Welcome to Case Project](#welcome-to-case-project)
  - [What Can You Do?](#what-can-you-do)
- [Getting Started](#getting-started)
  - [First Launch](#first-launch)
  - [Navigation Basics](#navigation-basics)
- [Working with Projects](#working-with-projects)
  - [What is a Project?](#what-is-a-project)
  - [Creating a Project](#creating-a-project)
  - [Switching Projects](#switching-projects)
- [Uploading Sources](#uploading-sources)
  - [What is a Source?](#what-is-a-source)
  - [Upload Process](#upload-process)
  - [What Happens Next?](#what-happens-next)
- [Viewing and Annotating Documents](#viewing-and-annotating-documents)
  - [Opening a Source](#opening-a-source)
  - [View Modes](#view-modes)
  - [Creating a Citation](#creating-a-citation)
  - [Viewing Your Cites](#viewing-your-cites)
- [Taking Notes](#taking-notes)
  - [What are Notes?](#what-are-notes)
  - [Creating a Note](#creating-a-note)
  - [Formatting Your Notes](#formatting-your-notes)
  - [Embedding Citations in Notes](#embedding-citations-in-notes)
  - [Organizing Notes](#organizing-notes)
- [Managing Events](#managing-events)
  - [What is an Event?](#what-is-an-event)
  - [Viewing Events](#viewing-events)
  - [Auto-Created Events](#auto-created-events)
  - [Creating an Event Manually](#creating-an-event-manually)
  - [Event Details](#event-details)
  - [Linking a Source to an Event](#linking-a-source-to-an-event)
- [Managing People](#managing-people)
  - [What is a Person?](#what-is-a-person)
  - [Creating a Person](#creating-a-person)
  - [Linking People to Sources and Events](#linking-people-to-sources-and-events)
  - [Viewing a Person's Appearances](#viewing-a-persons-appearances)
- [Search and Filters](#search-and-filters)
  - [Searching Sources](#searching-sources)
  - [Filtering Events](#filtering-events)
  - [Finding Citations](#finding-citations)
- [Working with Transcripts and Dialogue](#working-with-transcripts-and-dialogue)
  - [Understanding Dialogue View](#understanding-dialogue-view)
  - [Selecting Across Multiple Speakers](#selecting-across-multiple-speakers)
  - [Associating Speakers with People](#associating-speakers-with-people)
- [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Global Shortcuts](#global-shortcuts)
  - [Document Viewer Shortcuts](#document-viewer-shortcuts)
  - [Note Editor Shortcuts](#note-editor-shortcuts)
- [Tips and Best Practices](#tips-and-best-practices)
  - [Organization Tips](#organization-tips)
  - [Workflow Suggestions](#workflow-suggestions)
  - [Common Mistakes to Avoid](#common-mistakes-to-avoid)
- [Troubleshooting](#troubleshooting)
  - [Upload Issues](#upload-issues)
  - [Viewing Issues](#viewing-issues)
  - [Citation Issues](#citation-issues)
  - [Performance Issues](#performance-issues)
- [Export and Backup](#export-and-backup)
  - [Exporting Notes (Future Feature)](#exporting-notes-future-feature)
  - [Backing Up Your Project](#backing-up-your-project)
- [Getting Help](#getting-help)
  - [In-App Help](#in-app-help)
  - [Documentation](#documentation)
  - [Support](#support)
- [FAQ](#faq)
- [Appendix: Document Types](#appendix-document-types)
  - [Source Document Types](#source-document-types)
  - [Event Categories](#event-categories)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Welcome to Case Project

Case Project is a powerful tool for organizing, annotating, and analyzing legal evidence. Whether you're managing court transcripts, police reports, witness interviews, or other case materials, Case Project helps you stay organized and find what you need quickly.

### What Can You Do?

- 📁 **Upload and organize** documents, audio, and video files
- 📝 **Annotate sources** by creating citations with notes
- 📕 **Take rich notes** with embedded citations
- 📅 **Track events** (hearings, filings, interviews, etc.)
- 👥 **Manage people** (witnesses, attorneys, defendants, etc.)
- 🔍 **Search and filter** across all your case materials
- 📤 **Export** your work to various formats

---

## Getting Started

### First Launch

When you first open Case Project, you'll see the main interface with a sidebar on the left:

```
┌─────────────────────────────────────────┐
│  🗂️  Sources      [Sidebar]             │
│  📕  Notebooks                           │
│  👥  People                              │
│  📅  Events                              │
│  🗺️  Locations                           │
│  🏷️  Tags                                │
│  ⚙️  Settings                            │
│                                          │
│  [Main Content Area]                    │
│                                          │
└─────────────────────────────────────────┘
```

### Navigation Basics

- **Click icons** in the left sidebar to switch between sections
- **Click the << button** at the top to collapse/expand the sidebar
- **Use the back button** (when visible) to return to previous screens

---

## Working with Projects

### What is a Project?

A project is a container for all materials related to one case. Each project has its own:

- Sources (documents, audio, video)
- Events (hearings, filings, etc.)
- People (witnesses, attorneys, etc.)
- Notes

### Creating a Project

1. Click **⚙️ Settings** in the sidebar
2. Click **"Create New Project"**
3. Enter:
   - **Project Name** (e.g., "State v. Smith")
   - **Project Slug** (e.g., "state-v-smith") — used for file organization
   - **Description** (optional)
4. Click **"Create"**

### Switching Projects

1. Click **⚙️ Settings**
2. In the **"Active Project"** section, select a different project from the dropdown
3. Click **"Switch Project"**

> **Tip**: All your work is automatically saved to the active project. Make sure you're in the right project before uploading or creating content!

---

## Uploading Sources

### What is a Source?

A "source" is any original document, audio file, or video file that contains case-related information. Examples:

- Court transcripts (PDF)
- Police reports (PDF)
- Witness interviews (MP3, MP4)
- Body camera footage (MP4)
- 911 calls (WAV)
- Legal filings (PDF)

### Upload Process

1. Click **🗂️ Sources** in the sidebar
2. Click the **"Upload Source"** button (usually a + icon or "Upload" button)
3. **Select your file**:
   - Click **"Choose File"** and select from your computer
   - Or drag and drop a file onto the upload area
4. **Fill in the wizard form**:

   **Step 1: File Information**
   - **Document Type**: Select the type (Court Transcript, Police Report, etc.)
   - **Citation Name**: Short name for referencing (e.g., "Tr v1", "PR 2023-456")
   - **Date**: Date of the document (auto-detected from filename if possible)

   **Step 2: Additional Details** (varies by document type)
   - For transcripts: Judge, case number, witnesses
   - For police reports: Agency, officer, incident number
   - For interviews: Interviewer, interviewee, location

5. Click **"Next"** through each step
6. Click **"Upload"** to finish

### What Happens Next?

After upload, Case Project automatically:

1. **Saves the original file** to your project folder
2. **Extracts the text** (for PDFs) or **transcribes the audio** (for A/V files)
3. **Creates an event** linked to this source (e.g., "Court Hearing" for a transcript)
4. **Makes the content searchable** and ready for annotation

> **Processing Time**: PDFs process in seconds. Audio/video transcription takes about as long as the recording (a 1-hour interview takes ~1 hour to process).

### Running the Dual Extractor (Native + Docling)

Case Project can now keep two extractions for every PDF so you can pick the cleanest result.

1. Install the optional dependencies once:

   ```bash
   pip install -r requirements_minimal.txt
   ```

2. Drop the PDFs you want to batch into an `inbox/` folder.
3. Run the helper script from the repository root:

   ```bash
   python tools/ingest/dual_ingest.py --in inbox --out projects/<Project>/sources --reports projects/<Project>/reports
   ```

4. Open your project. Each PDF becomes two sibling sources ending in `-native` and `-docling`.
5. Open both, skim the title page, table of contents, and speaker formatting, then archive whichever version reads worse.
6. Optional: review the generated `reports/<name>.report.md` for PASS/FAIL summaries of the automated detectors.

To temporarily stick with a single extractor, edit `config/extraction.yml` and update the `run_sequence` list.

### Split Review for Mega PDFs

Use the splitter when a single PDF contains many filings or incident reports.

1. Place the combined PDF in `inbox/`. If available, export its Register of Actions to CSV with columns such as `id,title,date,pages`.
2. Run:

   ```bash
   python tools/splitter/split_cli.py \
     --pdf inbox/All_Filings_2024.pdf \
     --docket data/dockets/All_Filings_2024.csv \
     --session projects/<Project>/split_sessions/All_Filings_2024.session.json \
     --report projects/<Project>/reports/All_Filings_2024.split.md \
     --out projects/<Project>/sources
   ```

3. Open the new **Split Review** view (beta) to inspect each proposed segment, drag pages between segments, merge or split, and rename titles.
4. Click **Finalize** to write canonical child sources plus an audit manifest. If you are not ready to finalize yet, keep the generated session JSON so you can resume later.

Split suggestions reuse your feedback labels, so every correction sharpens the next split run.

---

## Viewing and Annotating Documents

### Opening a Source

1. Go to **🗂️ Sources**
2. Each row now shows the source’s emoji/icon, stored date, and a short cite badge (if set) so you can skim quickly
3. Click on any source to open it in the document viewer

### View Modes

**For PDFs**, you can switch between two views:

- **Text View** (default): Shows extracted text, easy to select and annotate
- **PDF View**: Shows the original PDF with original formatting

Toggle between views using the **PDF/Text button** at the top.

**For Audio/Video**, you see:

- **Transcript**: Time-stamped dialogue
- **Media Player**: Play/pause controls with synchronized highlighting

### Editing Source Metadata

Need to rename a document or tweak its wizard answers? Edit metadata right inside the viewer.

1. Open the source. Click **More ▾** in the header to reveal advanced controls (detector selector, metadata shortcut, Docling toggles, dev-mode chip).
   - Click **Less ▴** to collapse the extras. The toggle resets whenever you switch to another source.
2. Choose **Edit Metadata**. The main pane swaps to the metadata editor.
3. Update the dedicated fields at the top:
   - **Source Name** — Overrides the generated filename shown in lists and headers (history is preserved automatically).
   - **Citation Name** — Becomes the default label used in cite pickers and event links. Leave blank to fall back to the source name.
   - **Short Cite Name** — Optional shorthand (e.g., “Tr Vol. I”). Displayed as a badge in the header and source list.
4. Scroll through the wizard form to adjust type-specific answers, emoji/icon selection, and other metadata.
5. Click **Save Source**. The sidebar, header, and cite pickers refresh immediately.

> **Tip:** You can also open the editor from the Sources list by hovering a row and clicking the pencil icon.

### Creating a Citation

A "citation" (or "cite") is a highlighted excerpt from a source that you want to reference or annotate.

**To create a cite**:

1. **Select text** by clicking and dragging in the document
2. A popup appears with three options:
   - **CITE** — Create citation
   - **TAG** — Add tags (future feature)
   - **EVENT** — Create event from selection
3. Click **"CITE"**
4. _(Optional)_ Add a label or note in the dialog that appears
5. Click **"Create"**

**Your cite is now saved!** It will appear:

- As a highlight in the document
- In the "Citations" list for this document
- Available for embedding in notes

### Viewing Your Cites

**In the document**:

- Highlighted text shows your citations
- Hover over highlights to see cite details
- Click highlights to view/edit

**In the sidebar** (when viewing a document):

- See a list of all cites for the current document
- Click to jump to that location
- Edit or delete cites

---

## Taking Notes

### What are Notes?

Notes are your personal workspace for organizing thoughts, outlining arguments, and building your case narrative. Think of them like a word processor, but with special powers:

- **Embed citations** directly into your text
- **Organize with headings** (auto table of contents)
- **Rich formatting** (bold, italic, lists, etc.)
- **Link to events and people**

### Creating a Note

1. Click **📕 Notebooks** in the sidebar
2. Click **"New Note"** button
3. Enter a **title** (e.g., "Witness Credibility Analysis")
4. Start typing in the editor

### Formatting Your Notes

The note editor formats text inline — no preview pane required. Use the toolbar at the top of the editor or keyboard shortcuts:

| Control          | Function                                                     |
| ---------------- | ------------------------------------------------------------ |
| **H1–H5**        | Apply heading levels (auto-builds the outline sidebar)       |
| **Bold**         | Toggle bold (`Cmd/Ctrl + B`)                                 |
| **Italic**       | Toggle italics (`Cmd/Ctrl + I`)                              |
| **Insert Cite**  | Drop the cite chip for the currently selected source segment |
| **Insert Quote** | Insert the cite plus quoted text pulled from the source      |

> Tip: You can still type Markdown if you prefer (e.g., `#` + space), but the editor immediately converts it to styled text.

### Embedding Citations in Notes

Citations appear as inline chips (📎 + label) so you can see exactly what’s linked.

**Method 1: Insert Cite Button**

1. Place the cursor where you want to add a cite
2. Click **Insert Cite**
3. Choose the document segment in the picker dialog
4. The cite chip is inserted in-line, and the cursor moves after it so you can keep typing

**Method 2: Insert Quote Button**

1. Place the cursor where the quote should go
2. Click **Insert Quote**
3. Pick a cite segment that includes captured text
4. The editor drops the quoted passage followed by the cite chip

**Managing cites inside notes**

- Click the ✕ button on a chip to remove it
- Hover to see the quote or page/time metadata
- Use the All Citations tab to audit every cite across the project

### Organizing Notes

**Folders** (future feature):

- Group related notes into folders
- Example: "Witness Statements", "Motion to Suppress", "Trial Prep"

**Tags**:

- Add tags like `#credibility`, `#timeline`, `#evidence`
- Filter notes by tag

**Table of Contents**:

- Automatically generated from your headings
- Click to jump to sections
- Appears in the sidebar when viewing a note

---

## Managing Events

### What is an Event?

An event represents something that happened in your case. Events help you build a timeline and understand the sequence of activities.

**Event Types**:

- **Legal Events**: Court hearings, filings, rulings, trials
- **Factual Events**: Incidents, observations, statements
- **Investigatory Events**: Interviews, evidence collection, police actions

### Viewing Events

1. Click **📅 Events** in the sidebar
2. See a list of all events in your case
3. Filter by category:
   - **Legal** — Court activities
   - **Factual** — Real-world occurrences
   - **Investigatory** — Investigation activities

### Auto-Created Events

When you upload a source, Case Project automatically creates a related event:

| Source Type         | Auto-Created Event |
| ------------------- | ------------------ |
| Court Transcript    | Court Hearing      |
| Police Report       | Police Report      |
| 911 Call            | 911 Call           |
| Body Camera         | Body Camera        |
| Interview Recording | A/V Interview      |

You can edit these auto-created events to add more details.

### Creating an Event Manually

**Method 1: From Event List**

1. Go to **📅 Events**
2. Click **"Create Event"** button
3. Select **event type** (hearing, filing, interview, etc.)
4. Fill in the wizard form with event details
5. Click **"Create"**

**Method 2: From a Selection in a Document**
Sometimes while reading a document, you come across a description of an event. You can create an event directly from that text!

1. Open a source document
2. **Select the text** describing the event
3. The popup appears — click **"EVENT"**
4. A pre-filled event form opens with:
   - The selected text as a note
   - A citation linking back to this location
5. Fill in additional details
6. Click **"Create"**

**Result**: The event is created and automatically linked to the source document and citation.

### Event Details

Click any event in the list to see its details:

**Information Shown**:

- Event title and category
- Date and time (if applicable)
- Linked source document (if any)
- Linked citations
- Participants (people involved)
- Custom fields (based on event type)

**Actions You Can Take**:

- **Edit**: Modify event details
- **Link Source**: Associate a document with this event
- **Add Participants**: Link people to this event with roles
- **Duplicate**: Create a copy (useful for recurring events)
- **Delete**: Remove the event

### Linking a Source to an Event

If you have an event without a source document (or want to link additional sources):

1. Open the event details
2. Click **"Link Source"** button
3. Select a source from your list
4. Click **"Link"**

Now when you view this event, you can quickly navigate to the related document.

---

## Managing People

### What is a Person?

The People section tracks individuals involved in your case: witnesses, attorneys, defendants, complainants, officers, judges, etc.

### Creating a Person

1. Click **👥 People** in the sidebar
2. Click **"Create Person"** button
3. Fill in the wizard form:
   - **Name**: Full name
   - **Role**: Primary role (witness, attorney, defendant, etc.)
   - **Aliases**: Other names they go by (optional)
   - **Additional details**: Contact info, notes, etc. (varies by role)
4. Click **"Create"**

### Linking People to Sources and Events

Once a person is created, you can associate them with specific sources and events.

**Linking to an Event**:

1. Open an event's detail view
2. In the **Participants** section, click **"Add Participant"**
3. Select the person
4. Choose their role in this event (witness, interviewer, defendant, etc.)
5. Click **"Add"**

**Linking to a Source**:

1. Open a source document
2. If it's a transcript/interview with speakers, click **"Associate Speaker"**
3. Select the person from your list
4. Click **"Link"**

Now when you see that person's name in the transcript, it's linked to their profile!

### Viewing a Person's Appearances

Click any person in the People list to see:

- All events they're involved in
- All sources where they appear
- Their role in each context
- Notes about their participation

---

## Managing Locations

### What is a Location?

Locations represent geographic places associated with people and events in your case. Case Project provides a centralized locations view with mapping capabilities.

### Viewing Locations

1. Click **🗺️ Locations** in the sidebar
2. See all locations from people and events in one place

**View Modes**:

- **List View** — Compact sidebar list with details
- **Spreadsheet View** — Table with all location data
- **Map View** — Interactive map with pins

### Filtering Locations

Use the filter controls in the sidebar:

**Search Box**: Find locations by name, city, county, or note

**Type Filter**:

- **All Types** — Show both people and events
- **People Only** — Only show person locations
- **Events Only** — Only show event locations

**Date Range** (for events):

- Set start and end dates to filter events by when they occurred

**Clear Filters**: Click the "Clear Filters" button to reset

### Using the Map View

1. Click the **map icon** in the sidebar header
2. The map displays all locations as colored pins:
   - **Blue pins** — People locations
   - **Purple pins** — Event locations
   - **Green clusters** — Groups of nearby locations

**Map Interactions**:

- **Click a pin** — View details in popup
- **Click a cluster** — Zoom in to see individual pins
- **Pan and zoom** — Navigate the map freely
- **Toggle clustering** — Use the button to enable/disable grouping

**Auto-Zoom**: The map automatically adjusts to show all locations

### Adding Locations to People

When creating or editing a person:

1. In the person wizard, find the **Location** field
2. Type an address in the search box
3. Select from autocomplete suggestions OR
4. Click on the map to place a pin
5. Add an optional location note (e.g., "primary residence", "last known address")

### Adding Locations to Events

When creating or editing an event:

1. In the event wizard, find the **Location** field (for incident-related events)
2. Type an address or place name
3. Select from suggestions
4. The location is saved with the event

### Location Spreadsheet View

Click the **expand button** in the sidebar to see all locations as a table:

| Column          | Description                        |
| --------------- | ---------------------------------- |
| **Type**        | Person or Event                    |
| **Name**        | Person name or event title         |
| **Address**     | Street address                     |
| **City**        | City name                          |
| **County**      | County name                        |
| **Date/Note**   | Event date or person location note |
| **Coordinates** | Latitude, longitude                |

Click any row to select that location (highlights on map).

---

## Search and Filters

### Searching Sources

1. Go to **🗂️ Sources**
2. Use the **search box** at the top
3. Type keywords (searches filenames, document types, dates)
4. Results filter in real-time

### Filtering Events

1. Go to **📅 Events**
2. Use the **category filter** buttons:
   - **All** — Show everything
   - **Legal** — Court activities only
   - **Factual** — Real-world events only
   - **Investigatory** — Investigation activities only
3. Use the **search box** to find specific events by name

### Finding Citations

**In a Source Document**:

- All cites are highlighted
- Use the cites sidebar to see a list
- Click to jump to location

**In Notes**:

- Click the **"Insert Cite"** button to browse all cites
- Use the search box to find specific quotes
- Filter by source

---

## Working with Transcripts and Dialogue

### Understanding Dialogue View

When you view a court transcript or interview, content is organized by speaker:

```
┌─────────────────────────────────────────┐
│ ATTORNEY JOHNSON:                       │
│ Can you describe what you saw?          │
├─────────────────────────────────────────┤
│ WITNESS SMITH:                          │
│ I was walking down Main Street around   │
│ 3 PM when I heard a loud noise.         │
├─────────────────────────────────────────┤
│ ATTORNEY JOHNSON:                       │
│ What did you do next?                   │
└─────────────────────────────────────────┘
```

### Selecting Across Multiple Speakers

You can select text that spans multiple dialogue turns:

1. Click at the start of your selection (in any speaker's turn)
2. Drag down across multiple turns
3. Release to select
4. The popup appears — create a cite or event

### Associating Speakers with People

If you've created a Person entry for a speaker:

1. Click the speaker's name in the dialogue
2. Select **"Associate Speaker"** from the menu
3. Choose the person from your list
4. Click **"Link"**

Now that speaker is linked to the person profile, and you can see all their testimony across documents.

### Jumping to Witnesses & Phases

When a transcript has defined witness sections, a **Jump…** dropdown appears in the viewer header:

1. Open the transcript in Text or PDF mode.
2. Use the dropdown to choose `Witness — Phase` (example: `Jane Smith — Cross (by Ms. Patel)`).
3. The PDF view jumps to that page, and (if you're in Text mode) the reader scrolls to the first matching block.

Need suggestions? Click **Suggest Sections** in the header. The sectionizer scans the table of contents plus standard cues (`DIRECT/CROSS/REDIRECT/RECROSS`, `BY MR./MS.`) and previews the proposed ranges before saving.

### Smart Q/A Labels

Enable **Smart Q/A Labels** in the header to make long transcripts easier to skim:

- `A.` lines render as `WITNESS [NAME]: …` when the current witness is known.
- `Q.` lines render as `MR./MS. [Examiner]: …` (falls back to `QUESTION:` if no examiner is recorded).
- Toggle off at any time to see the original literal `Q.`/`A.` prefixes.

These relabelings are presentation-only; the underlying transcript text and citations stay unchanged.

### Using Feedback Labels to Improve Detection

Teach the system where important sections live while you review:

1. **Label spans**: highlight text in the Markdown pane, right-click, and choose **Label as…** (for example, “Questions Presented” or “Table of Contents”).
2. **Label regions**: toggle **PDF Label Mode** in the viewer toolbar, drag a rectangle over the relevant area (sentencing grids, exhibits), and assign the matching region label.
3. The footer badge shows pending submissions. The app retries automatically if you lose connectivity, so you can keep reading.
4. Labeled sections appear as chips at the top of the document. Click a chip to jump back, or choose the ✎ icon to correct a mistake—the correction is logged as feedback too.
5. When you want the system to learn from your work, run:

   ```bash
   python tools/profiles/compile_profiles.py --sources projects/<Project>/sources --out public/profiles
   ```

   The compiler promotes repeated patterns into reusable detection profiles for future documents.

Every piece of feedback is appended to `sources/<sourceId>/feedback.jsonl`, giving you a full audit trail.

---

## Working with Form Templates

### What are Form Templates?

Many legal cases involve standardized forms (court filings, judgments, citations, etc.) that share the same structure. Instead of manually extracting data from every form, you can:

1. **Label a blank form once** — Mark all fields (defendant name, case number, dates, etc.)
2. **Export as a template** — Save the field locations
3. **Apply to filled forms** (future) — Automatically extract data from all similar forms

**Currently Supported**: Michigan court forms (MC227, MC220, MC10, etc.)

### Creating a Form Template

**Step 1: Set Up Form Detector**

Before labeling, each form type must be registered:

```bash
node scripts/add_form_detector.mjs MC227 "Judgment of Sentence"
```

This adds the form type to the system and makes it available in the "Detector Type" dropdown.

**For common forms** (11 Michigan forms), use the batch script:

```bash
node scripts/setup_common_forms.mjs
```

**Step 2: Download Blank Form**

Get a blank copy of the form from Michigan Courts website or use:

```bash
node scripts/download_michigan_forms.mjs
```

**Step 3: Upload and Select Detector Type**

1. Go to **🗂️ Sources**
2. Click **"Upload Source"**
3. Select the blank form PDF
4. **Important**: Set "Detector Type" dropdown to the form (e.g., "MC227 - Judgment of Sentence")
5. Complete the wizard and upload

**Step 4: Label All Fields**

1. Open the uploaded blank form
2. Toggle to **PDF View**
3. Click **"Label PDF"** button (top toolbar)
4. Draw boxes around each field:
   - Click and drag to create rectangle
   - Release mouse
   - Select label from menu (e.g., "defendant_name", "case_number")
   - Box turns green when saved
5. Label all fields on all pages
6. Click **"Done"** when finished

**Common Field Labels**:

- `defendant_name` — Defendant's name
- `plaintiff_name` — Plaintiff's name
- `case_number` — Case/docket number
- `judge_name` — Judge name
- `judge_signature` — Judge signature area
- `attorney_name` — Attorney name
- `date_filed` — Filing date
- `date_signed` — Signature date
- `court_name` — Court name
- `sentence_min_years` — Minimum sentence
- `sentence_max_years` — Maximum sentence

**Step 5: Export Template**

After labeling, find your document ID in the Sources list, then:

```bash
node scripts/export_form_template.mjs [doc-id] MC227
```

This creates:

- `form_templates/criminal_disposition/MC227.json` — Field definitions
- `form_templates/criminal_disposition/MC227.pdf` — Reference PDF

### View Training Progress

See how many forms you've labeled:

```bash
node scripts/training_stats.mjs
```

**Output shows**:

- Documents labeled per form type
- Fields labeled per form
- Visual progress bars

### Tips for Form Labeling

**Accuracy**:

- Draw boxes tight around field boundaries (not too big or small)
- Include the entire field area where text will appear
- Don't overlap boxes unless fields genuinely overlap

**Consistency**:

- Use the same label names across all similar fields
- Follow naming conventions (e.g., `defendant_name` not `def_name`)
- Label all instances (if a form has multiple defendant fields, label all)

**Efficiency**:

- Label blank forms first (cleaner, easier to see fields)
- Focus on important fields first (names, dates, case numbers)
- Optional fields can be added later

**Organization**:

- Each form type needs its own detector before labeling
- Training data auto-saves to `training/{form-type}/{doc-id}/`
- Export templates when labeling is complete

### Future: Auto-Extraction

Once templates are created, the system will (future feature):

1. **Auto-detect form type** when you upload a filled form
2. **Load matching template** with field locations
3. **Extract text** from each labeled region
4. **Present structured data** for review
5. **Export to spreadsheet** or database

This will save hours of manual data entry for cases with many similar forms!

---

## Keyboard Shortcuts

### Global Shortcuts

| Shortcut       | Action                |
| -------------- | --------------------- |
| `Ctrl/Cmd + K` | Quick search (future) |
| `Ctrl/Cmd + N` | New note              |
| `Ctrl/Cmd + S` | Save current item     |
| `Esc`          | Close modal/dialog    |

### Document Viewer Shortcuts

| Shortcut           | Action                    |
| ------------------ | ------------------------- |
| `Ctrl/Cmd + F`     | Find in document (future) |
| `→` or `Page Down` | Next page                 |
| `←` or `Page Up`   | Previous page             |
| `Home`             | First page                |
| `End`              | Last page                 |

### Note Editor Shortcuts

| Shortcut               | Action               |
| ---------------------- | -------------------- |
| `Ctrl/Cmd + B`         | Bold                 |
| `Ctrl/Cmd + I`         | Italic               |
| `Ctrl/Cmd + K`         | Insert link (future) |
| `Ctrl/Cmd + Shift + C` | Insert cite          |
| `Ctrl/Cmd + Z`         | Undo                 |
| `Ctrl/Cmd + Shift + Z` | Redo                 |

---

## Tips and Best Practices

### Organization Tips

1. **Use descriptive citation names**: Instead of "Tr v1", use "Smith Deposition 2023-03-15"
2. **Create events as you go**: Don't wait until you've uploaded everything
3. **Link people early**: Associate speakers with Person profiles for easier tracking
4. **Use headings in notes**: Generates automatic table of contents
5. **Tag consistently**: Use the same tags across notes for easier filtering

### Workflow Suggestions

**For Transcript Review**:

1. Upload transcript
2. Open in document viewer
3. Read through, creating cites for important testimony
4. Associate speakers with Person profiles
5. Create a note called "[Witness Name] — Key Points"
6. Insert cites into the note with your analysis

**For Event Timeline**:

1. Create all events manually or via source uploads
2. Ensure every event has a date
3. Go to **📅 Events** and sort by date
4. Review chronological sequence
5. Create a note called "Timeline" with embedded event references

**For Evidence Organization**:

1. Upload all sources first
2. Tag each source by topic (e.g., #physical-evidence, #witness-statements)
3. Create events for key incidents
4. Create cites for relevant excerpts
5. Build notes organized by legal issues
6. Embed cites in notes under appropriate headings

### Common Mistakes to Avoid

❌ **Uploading without completing the wizard**: Always fill in document details — it helps later!

❌ **Forgetting to switch projects**: Check active project before uploading

❌ **Not creating cites**: Highlights disappear; cites are permanent

❌ **Skipping event linking**: Events are more useful when linked to sources

❌ **Not using headings in notes**: Headings create structure and navigation

---

## Troubleshooting

### Upload Issues

**Problem**: "Upload failed" error  
**Solution**:

- Check file size (very large files may time out)
- Verify file format is supported (PDF, MP3, MP4, WAV, etc.)
- Try again — temporary network issue

**Problem**: "Processing stuck" — upload succeeded but document won't open  
**Solution**:

- For PDFs: Check that PDF contains selectable text (not just images)
- For A/V: Transcription takes time (1x speed) — wait and refresh
- Check Settings → Dev Tools for processing status

### Viewing Issues

**Problem**: PDF shows blank pages  
**Solution**:

- Try switching to **Text View**
- Refresh the browser
- Check browser console for errors (F12)

**Problem**: Text is garbled or wrong language  
**Solution**:

- PDF extraction quality depends on original PDF
- Try re-uploading with better quality PDF
- Use PDF View to see original formatting

### Citation Issues

**Problem**: Can't select text  
**Solution**:

- Make sure you're in **Text View** (not PDF view)
- Text must be in a block (not headings or margins)
- Try selecting smaller sections

**Problem**: Cite doesn't appear in notes  
**Solution**:

- Check the cite ID is correct in your `[[CITE:id|text]]` syntax
- Refresh the note
- Verify the cite exists in the source document

### Performance Issues

**Problem**: App running slowly  
**Solution**:

- Large projects can slow down — consider archiving old cases
- Close unused browser tabs
- Clear browser cache

**Problem**: Search not finding results  
**Solution**:

- Search looks in filenames and metadata (full-text search coming soon)
- Try different keywords
- Check spelling

---

## Export and Backup

### Exporting Notes (Future Feature)

Will support:

- Export to Microsoft Word (.docx)
- Export to PDF
- Export to Markdown
- Include embedded citations as footnotes

### Backing Up Your Project

**Current Setup**:

- All project data is stored in the project folder
- You can manually backup the entire folder
- Recommended: Regular backups to external drive or cloud storage

**Future**:

- Built-in backup/export functionality
- Cloud sync options
- Project templates

---

## Getting Help

### In-App Help

- Click **⚙️ Settings** → **Help** for in-app documentation
- Look for **?** icons throughout the app for context-sensitive help

### Documentation

- **This User Guide**: Overview of all features
- **Technical Reference** (`TECHNICAL_REFERENCE.md`): For developers
- **Quick Reference** (`QUICK_REFERENCE.md`): Command cheat sheet

### Support

- Check the **Issues** section on GitHub
- Review **Session logs** in `Documentation/SESSIONS/`
- Consult **PR documentation** in `Documentation/PRs/` for specific features

---

## FAQ

**Q: What file types can I upload?**  
A: PDFs, MP3, WAV, M4A, AAC, FLAC, OGG, MP4, MOV, AVI, MKV

**Q: How long does transcription take?**  
A: Approximately the same length as the audio/video (1-hour recording = ~1 hour processing)

**Q: Can I edit the extracted text?**  
A: Yes! In dialogue/narrative mode, click on any block to edit. Changes are saved to the canonical version.

**Q: What's the difference between a source and an event?**  
A: A **source** is the physical document/recording. An **event** is what happened (hearing, incident, etc.). Sources document events.

**Q: Can I work on multiple cases at once?**  
A: Yes! Create separate projects for each case and switch between them in Settings.

**Q: Where is my data stored?**  
A: On your local machine in the project folder. Nothing is uploaded to the cloud (currently).

**Q: How do I share my work with colleagues?**  
A: Export individual notes (future), or share the entire project folder. Multi-user collaboration coming soon!

**Q: Can I import existing notes or documents?**  
A: Upload PDFs normally. For existing notes, copy/paste text into new notes. Bulk import coming soon!

**Q: What happens if I delete a source?**  
A: The source, its blocks, cites, and auto-created event are removed. Notes with embedded cites will show broken references.

**Q: Can I customize the wizard forms?**  
A: Developers can edit wizard specifications in `server/config/wizards/`. User-customizable wizards coming soon!

---

## Appendix: Document Types

### Source Document Types

| Type                 | Description                                              | Auto-Event                    |
| -------------------- | -------------------------------------------------------- | ----------------------------- |
| **Court Transcript** | Record of court proceedings (hearing, trial, deposition) | Court Hearing (legal)         |
| **Court Filing**     | Motion, brief, complaint, answer, etc.                   | Court Filing (legal)          |
| **Court Opinion**    | Judge's written decision                                 | Court Filing (legal)          |
| **Police Report**    | Incident report, arrest report, investigation report     | Police Report (investigatory) |
| **A/V Interview**    | Recorded interview (suspect, witness, etc.)              | A/V Interview (investigatory) |
| **Body Camera**      | Body-worn camera footage                                 | Body Camera (investigatory)   |
| **Dash Camera**      | Dashboard camera footage                                 | Dash Camera (investigatory)   |
| **911 Call**         | Emergency call recording                                 | 911 Call (investigatory)      |
| **Evidence Photo**   | Photograph of physical evidence                          | N/A (manual event)            |
| **Document**         | Generic document (email, letter, report, etc.)           | N/A (manual event)            |

### Event Categories

**Legal**: Court activities, filings, hearings, trials, rulings  
**Factual**: Real-world events (incidents, observations, statements)  
**Investigatory**: Investigation activities (interviews, evidence collection, police actions)

---

**Thank you for using Case Project!** We hope this tool makes your case management easier and more efficient.

**Questions or feedback?** Check `Documentation/` for developer resources or submit an issue on GitHub.

---

**Document Version**: 1.0  
**Last Updated**: October 14, 2025  
**Compatible with**: Case Project v0.1.0
