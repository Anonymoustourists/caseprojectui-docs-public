# Technical Reference Guide

**Case Project UI** — Complete technical documentation for developers

**Last Updated**: November 10, 2025  
**Version**: 0.1.0

---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Overview](#overview)
  - [Tech Stack](#tech-stack)
- [Architecture](#architecture)
  - [High-Level Design](#high-level-design)
  - [Directory Structure](#directory-structure)
- [Data Model](#data-model)
  - [Core Entities](#core-entities)
    - [1. **Source** (Document)](#1-source-document)
    - [2. **Block** (Canonical Content)](#2-block-canonical-content)
    - [3. **Cite** (Citation/Annotation)](#3-cite-citationannotation)
    - [4. **Event**](#4-event)
    - [5. **Person**](#5-person)
    - [6. **Note**](#6-note)
    - [7. **FeedbackEvent**](#7-feedbackevent)
    - [8. **SplitSession & SplitManifest**](#8-splitsession--splitmanifest)
- [Frontend Architecture](#frontend-architecture)
  - [App.jsx — Main Component](#appjsx--main-component)
  - [State Management](#state-management)
    - [Zustand Stores](#zustand-stores)
  - [API Layer (`src/api.js`)](#api-layer-srcapijs)
  - [Key Components](#key-components)
    - [DocumentViewer (`src/pages/DocumentViewer.jsx`)](#documentviewer-srcpagesdocumentviewerjsx)
    - [SourceMetadataEditor (`src/components/sources/SourceMetadataEditor.tsx`)](#sourcemetadataeditor-srccomponentssourcessourcemetadataeditortsx)
    - [Source display helpers (`src/lib/sources/display.ts`)](#source-display-helpers-srclibsourcesdisplayts)
    - [NotesViewer (`src/pages/NotesViewer/`)](#notesviewer-srcpagesnotesviewer)
    - [EventsViewer (`src/pages/EventsViewer/`)](#eventsviewer-srcpageseventsviewer)
    - [PeopleViewer (`src/pages/PeopleViewer.jsx`)](#peopleviewer-srcpagespeopleviewerjsx)
    - [LocationsViewer (`src/pages/LocationsViewer.tsx`)](#locationsviewer-srcpageslocationsviewertsx)
    - [ImageViewer (`src/components/sources/ImageViewer.tsx`)](#imageviewer-srccomponentssourcesimageviewertsx)
    - [SelectionActionPopover (`src/components/SelectionActionPopover.jsx`)](#selectionactionpopover-srccomponentsselectionactionpopoverjsx)
    - [FeedbackProvider (`src/components/feedback/FeedbackProvider.tsx`)](#feedbackprovider-srccomponentsfeedbackfeedbackprovidertsx)
    - [Feedback UI Components](#feedback-ui-components)
    - [SplitReview Workspace (`src/views/SplitReview/`)](#splitreview-workspace-srcviewssplitreview)
- [Backend Architecture](#backend-architecture)
  - [Server Entry Point (`server/src/index.ts`)](#server-entry-point-serversrcindexts)
  - [Key Route Handlers](#key-route-handlers)
    - [Canonical Routes](#canonical-routes)
    - [GET /api/canonical/docs](#get-apicanonicaldocs)
    - [GET /api/canonical/docs/:docId](#get-apicanonicaldocsdocid)
    - [GET /api/canonical/docs/:docId/blocks](#get-apicanonicaldocsdocidblocks)
    - [GET /api/canonical/docs/:docId/cites](#get-apicanonicaldocsdocidcites)
    - [POST /api/canonical/docs/:docId/cites](#post-apicanonicaldocsdocidcites)
    - [PUT /api/canonical/docs/:docId/blocks/:blockId](#put-apicanonicaldocsdocidblocksblockid)
    - [Ingestion Routes](#ingestion-routes)
    - [POST /ingest/pdf](#post-ingestpdf)
    - [POST /ingest/av](#post-ingestav)
    - [Event Routes](#event-routes)
    - [GET /api/events](#get-apievents)
    - [POST /api/events](#post-apievents)
    - [POST /api/events/createFromSelection](#post-apieventscreatefromselection)
    - [People Routes](#people-routes)
    - [GET /api/people](#get-apipeople)
    - [POST /api/people](#post-apipeople)
    - [Feedback Routes](#feedback-routes)
    - [POST /api/feedback/append](#post-apifeedbackappend)
    - [Batch Upload Routes (PR91)](#batch-upload-routes-pr91)
    - [POST /api/sources/batch](#post-apisourcesbatch)
    - [GET /api/sources/pending](#get-apisourcespending)
    - [POST /api/sources/:id/name](#post-apisourcesidname)
- [Ingestion Pipeline](#ingestion-pipeline)
  - [Overview](#overview-1)
  - [Pipeline Flow](#pipeline-flow)
  - [Transcript Pipeline](#transcript-pipeline)
  - [Transcript Witness Sections & Phase Navigator (PR 86)](#transcript-witness-sections--phase-navigator-pr-86)
  - [Narrative Pipeline](#narrative-pipeline)
  - [Exhibit/Appendix Pipeline (PR96)](#exhibitappendix-pipeline-pr96)
  - [A/V Pipeline](#av-pipeline)
  - [Image Pipeline](#image-pipeline)
  - [Dual Extractor (Native + Docling)](#dual-extractor-native--docling)
  - [Mega PDF Splitter](#mega-pdf-splitter)
  - [Auto-Event Creation](#auto-event-creation)
- [Feedback and Learning Profiles](#feedback-and-learning-profiles)
  - [Overview](#overview-2)
  - [Label Catalog](#label-catalog)
  - [Client Workflow](#client-workflow)
  - [Storage Conventions](#storage-conventions)
  - [Profile Loading](#profile-loading)
  - [Profile Compilation](#profile-compilation)
  - [Detector Integration](#detector-integration)
  - [Backend Requirements](#backend-requirements)
- [Wizard System](#wizard-system)
  - [Purpose](#purpose)
  - [Wizard Specification Format](#wizard-specification-format)
  - [Wizard Components](#wizard-components)
  - [Field Types](#field-types)
  - [Conditional Logic](#conditional-logic)
  - [Title Generation](#title-generation)
- [Form Detection System](#form-detection-system)
  - [Purpose](#purpose-1)
  - [Architecture](#architecture-1)
  - [Detector Structure](#detector-structure)
  - [Adding a New Form Type](#adding-a-new-form-type)
  - [Training Data Collection](#training-data-collection)
  - [Template Export](#template-export)
  - [Label Generation](#label-generation)
  - [Training Statistics](#training-statistics)
  - [Future: Template Application](#future-template-application)
  - [SCAO Form Automation](#scao-form-automation)
- [Data Contracts](#data-contracts)
  - [Golden Invariants](#golden-invariants)
  - [Validation Layers](#validation-layers)
- [Testing Strategy](#testing-strategy)
  - [Unit Tests (`tests/`)](#unit-tests-tests)
  - [E2E Tests (`tests/e2e/`)](#e2e-tests-testse2e)
  - [Verification Gates](#verification-gates)
- [Performance Considerations](#performance-considerations)
  - [Bundle Size](#bundle-size)
  - [Database Strategy](#database-strategy)
  - [Ingestion Performance](#ingestion-performance)
- [Development Workflow](#development-workflow)
  - [Adding a New Feature](#adding-a-new-feature)
  - [Modifying Data Structures](#modifying-data-structures)
  - [Adding a New Wizard](#adding-a-new-wizard)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
  - [Debug Tools](#debug-tools)
- [API Reference](#api-reference)
  - [Complete Endpoint List](#complete-endpoint-list)
- [Future Enhancements](#future-enhancements)
  - [Planned Features](#planned-features)
  - [Technical Debt](#technical-debt)
- [Contributing](#contributing)
  - [Code Style](#code-style)
  - [Commit Messages](#commit-messages)
  - [PR Guidelines](#pr-guidelines)
- [Resources](#resources)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Overview

Case Project is a legal case management application for organizing, annotating, and analyzing evidence. This guide covers the complete technical architecture, data flows, APIs, and implementation details.

### Tech Stack

**Frontend**:

- React 18 + TypeScript
- Vite (build tool)
- Zustand (state management)
- TailwindCSS (styling)
- Lucide React (icons)

**Backend**:

- Node.js + Express
- TypeScript
- File-based storage (no database)

**Ingestion Pipeline**:

- Python (PDFPlumber, faster-whisper)
- TypeScript adapters
- YAML-based document type detection

---

## Architecture

### High-Level Design

```text
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (React)                      │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐  ┌────────────┐ │
│  │  Sources │  │   Notes   │  │  Events  │  │   People   │ │
│  │  Viewer  │  │  Viewer   │  │  Viewer  │  │   Viewer   │ │
│  └──────────┘  └───────────┘  └──────────┘  └────────────┘ │
│         │              │              │             │        │
│         └──────────────┴──────────────┴─────────────┘        │
│                          │                                   │
│                   ┌──────▼──────┐                           │
│                   │   API Layer  │                           │
│                   │   (axios)    │                           │
│                   └──────┬──────┘                           │
└──────────────────────────┼────────────────────────────────────┘
                           │ HTTP/REST
┌──────────────────────────▼────────────────────────────────────┐
│                    Backend (Express)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  Canonical   │  │   Ingestion  │  │    Registries    │   │
│  │  API Routes  │  │   Pipeline   │  │    (Events,      │   │
│  │              │  │              │  │     People)      │   │
│  └──────┬───────┘  └──────┬───────┘  └────────┬─────────┘   │
│         │                 │                     │             │
└─────────┼─────────────────┼─────────────────────┼─────────────┘
          │                 │                     │
          ▼                 ▼                     ▼
┌─────────────────────────────────────────────────────────────┐
│              File System Storage                             │
│  ┌────────────┐  ┌────────────┐  ┌───────────────────────┐ │
│  │ canonical/ │  │  sources/  │  │  project-registries/  │ │
│  │  (blocks)  │  │  (originals│  │   (events/people)     │ │
│  └────────────┘  └────────────┘  └───────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Directory Structure

```text

case-project-ui/
├── src/                          # Frontend React application
│   ├── App.jsx                   # Main app component, routing
│   ├── api.js                    # Axios instance with project context
│   ├── components/               # Reusable components
│   │   ├── DocumentViewer/       # PDF/Text viewer components
│   │   ├── feedback/             # FeedbackProvider, chips, PDF label overlay
│   │   ├── sources/              # Source upload/wizard
│   │   ├── people/               # People management
│   │   ├── events/               # Event management
│   │   ├── viewer/               # Inline chips, selection UX
│   │   └── wizard/               # JSON-driven wizard framework
│   ├── pages/                    # Main view components
│   │   ├── DocumentViewer.jsx    # Document viewing/annotation
│   │   ├── NotesViewer/          # Rich text notes editor
│   │   ├── EventsViewer/         # Events list/details
│   │   ├── PeopleViewer.jsx      # People management
│   │   └── SplitReview/          # Split session review workspace (beta)
│   ├── state/                    # Zustand stores
│   ├── stores/                   # Additional stores
│   └── lib/                      # Utilities (detection, docket parsing, etc.)
│
├── server/                       # Backend Express server
│   ├── src/
│   │   ├── index.ts              # Main server + all routes
│   │   ├── routes/               # API route handlers
│   │   │   ├── canonical.ts      # Document CRUD
│   │   │   ├── events.ts         # Event CRUD
│   │   │   ├── people.ts         # People CRUD
│   │   │   ├── wizard.ts         # Wizard spec serving
│   │   │   └── registries.ts     # Registry management
│   │   └── lib/                  # Server utilities
│   └── config/
│       └── wizards/              # JSON wizard specifications
│
├── tools/                        # Python tooling
│   ├── ingest/                   # Legacy ingestion entry points
│   │   ├── ingest_controller.py
│   │   ├── ingest_transcript.py
│   │   ├── ingest_doc.py
│   │   └── ingest_av.py
│   ├── extractors/               # PR-71 adapters (docling/native)
│   ├── mappers/                  # Canon output helpers
│   ├── detectors/                # Quality detectors (title/ToC/speaker)
│   ├── splitter/                 # Mega-PDF splitter CLI + heuristics
│   ├── profiles/                 # Feedback profile compiler
│   ├── schemas/                  # JSON schema definitions
│   └── utils/                    # Shared helpers (ULIDs, text normalization)
│
├── canonical/                    # Canonical document storage
│   ├── manifest.json             # Document registry
│   └── {docId}/
│       ├── blocks.jsonl          # Document content blocks
│       ├── manifest.json         # Document metadata
│       └── source.md             # Human-readable version
│
├── sources/                      # Original uploaded files + feedback
│   ├── {sourceId}/
│   │   ├── document.md           # Canon markdown (generated)
│   │   ├── document.index.json   # Canon index (generated)
│   │   └── feedback.jsonl        # Append-only feedback events
│
├── project-registries/           # Project-specific data
│   └── {projectSlug}/
│       ├── events.json           # Events registry
│       └── people.json           # People registry
│
├── annotations/                  # User annotations
│   └── {docId}/
│       └── cites.json            # Citations for document
│
├── public/profiles/              # Detection profiles (default + learned)
├── config/                       # Runtime configuration (extraction, split, labels)
├── requirements_minimal.txt      # Optional dependencies (docling, ulid-py)
└── Documentation/                # Project documentation
    ├── README.md                 # Documentation overview
    ├── index.md                  # PR tracker & work categories
    ├── TECHNICAL_REFERENCE.md    # This file
    ├── USER_GUIDE.md             # User-facing guide
    ├── PRs/                      # PR designs & runlogs
    └── Standards/                # Data contracts & standards

```

---

## Data Model

### Core Entities

#### 1. **Source** (Document)

Original uploaded files (PDFs, audio, video) that get processed into canonical blocks.

```typescript
type SourceManifest = {
  docId: string; // ULID
  docKey: string; // Human-friendly key
  type: string; // "Document" | "Transcript" | etc.
  source: {
    originalFilename: string;
    path: string; // Relative path to file
  };
  filename: {
    templateKey: string;
    current: string;
    history: string[];
  };
  dates?: {
    source?: string; // YYYY-MM-DD from document
    upload?: string; // ISO 8601 upload timestamp
  };
  createdAt: string; // ISO 8601
  updatedAt: string; // ISO 8601
  meta?: Record<string, any>;
};
```

**Storage**:

- Original file: `sources/{type}/{filename}`
- Manifest: `canonical/{docId}/manifest.json`
- Processed blocks: `canonical/{docId}/blocks.jsonl`

#### 2. **Block** (Canonical Content)

Atomic units of content extracted from sources. All blocks have a unique ID and source reference.

```typescript
type SourceRef = {
  kind: "pdf" | "av" | "image" | "text";
  sourceId: string; // Path to source file
  page?: number; // For PDFs
  startMs?: number; // For A/V
  endMs?: number; // For A/V
};

type Block = {
  id: string; // ULID
  type: "paragraph" | "heading" | "dialogue" | "section";
  text: string;
  sourceRef: SourceRef;
  speaker?: {
    label: string; // Display name
    personId?: string; // Link to Person entity
  };
  sequence: number; // Order in document
  createdAt: string;
  updatedAt: string;
};
```

**Storage**: `canonical/{docId}/blocks.jsonl` (one JSON object per line)

#### 3. **Cite** (Citation/Annotation)

User-created citations that reference specific spans of text within blocks.

```typescript
type Cite = {
  id: string; // ULID
  docId: string; // Parent document
  blockId: string; // Block being cited
  startOffset: number; // Character offset in block.text
  endOffset: number; // Character offset in block.text
  selectedText: string; // Exact text quoted
  label?: string; // User label
  eventIds?: string[]; // Linked events
  tags?: string[]; // User tags
  createdAt: string;
  updatedAt: string;
};
```

**Storage**: `annotations/{docId}/cites.json`

#### 4. **Event**

Represents legal or factual events (hearings, filings, interviews, etc.).

```typescript
type EventCategory = "legal" | "factual" | "investigatory";

type EventItem = {
  id: string; // ULID
  title: string; // System-generated title
  customTitle?: string; // User override
  category: EventCategory;
  date?: string; // YYYY-MM-DD
  datetime?: string; // ISO 8601
  location?: Location; // Geographic location (PR78)
  wizard?: {
    entity: "events";
    type: string; // Wizard template type
    answers: Record<string, any>;
    template_id: string;
    spec_version: number;
  };
  data: Record<string, any>; // Wizard answers
  sourceId?: string; // Linked source document
  sourceType?: string; // Type of linked source
  citeIds?: string[]; // Linked citations
  participants?: Participation[];
  createdFrom?: "wizard" | "selection" | "source_upload";
  createdAt: string;
  updatedAt: string;
};

type Participation = {
  personId: string;
  role: string; // "speaker" | "witness" | "defendant" | etc.
  note?: string;
  addedAt?: string;
};
```

**Storage**: `project-registries/{projectSlug}/events.json`

**Golden Invariant**: Auto-create one event on source upload (category determined by source type).

#### 5. **Person**

Individuals mentioned in the case (witnesses, attorneys, defendants, etc.).

```typescript
type PersonItem = {
  id: string; // ULID
  name: string;
  aliases?: string[];
  role?: string; // Primary role
  wizard?: {
    entity: "people";
    type: string;
    answers: Record<string, any>;
    template_id: string;
    spec_version: number;
  };
  data: Record<string, any>;
  location?: Location; // Geographic location (address)
  locationNote?: string; // Context note (e.g., "primary residence")
  appearances?: Array<{
    // Where person appears
    sourceId: string;
    eventId?: string;
    role?: string;
    note?: string;
  }>;
  createdAt: string;
  updatedAt: string;
};
```

**Storage**: `project-registries/{projectSlug}/people.json`

**Location Support** (PR78):

```typescript
type Location = {
  lat: number;
  lon: number;
  label: string; // Display name (e.g., "123 Main St, Detroit, MI")
  source: "user" | "geocode" | "revgeocode";
  address?: Address;
  zoomHint?: number; // Suggested zoom level for map
};

type Address = {
  raw: string;
  houseNumber?: string;
  road?: string;
  city?: string;
  county?: string;
  state?: string;
  postcode?: string;
  country?: string;
};
```

#### 6. **Note**

Rich text notes with cite embeds.

```typescript
type Note = {
  id: string; // ULID
  title: string;
  content: string; // Markdown with cite macros
  tags?: string[];
  createdAt: string;
  updatedAt: string;
};
```

**Cite Macro Format**: `[[CITE:citeId|displayText]]`

**Storage**: `notes/{noteId}.md` (with YAML frontmatter)

#### 7. **FeedbackEvent**

Structured observation emitted whenever a user labels a span or PDF region.

```typescript
type FeedbackEvent = {
  ts: string;
  user: string;
  kind: "span" | "region";
  sourceId: string;
  label: string;
  payload:
    | {
        blockId: string;
        charStart: number;
        charEnd: number;
        text: string;
      }
    | {
        page: number;
        bbox: [number, number, number, number];
        nearestText?: string;
      };
  note?: string;
};
```

**Storage**: `sources/{sourceId}/feedback.jsonl` (append-only JSONL feed)

#### 8. **SplitSession & SplitManifest**

Intermediate artifacts produced by the mega-PDF splitter.

```typescript
type SplitSegment = {
  index: number;
  startPage: number;
  endPage: number;
  title: string;
  confidence: number;
  docket?: {
    id?: string;
    title?: string;
    confidence?: number;
  };
};

type SplitSession = {
  pdf: string;
  generatedAt: string;
  segments: SplitSegment[];
};

type SplitManifestEntry = {
  folder: string;
  start_page: number;
  end_page: number;
  title: string;
  docket_entry?: string | null;
  confidence: number;
  docket_confidence: number;
};
```

**Storage**:

- `projects/<slug>/split_sessions/*.session.json` (staged review files)
- `projects/<slug>/sources/*/` (finalized child sources + `<pdf>.split_manifest.json`)

---

## Frontend Architecture

### App.jsx — Main Component

**Responsibilities**:

- Manages current view state (`sources`, `notebooks`, `people`, `events`, `tags`, `settings`)
- Renders sidebar navigation
- Handles overlay/modal state
- Provides project context to child components

**Key State**:

```javascript
const [currentView, setCurrentView] = useState("sources");
const [mainSidebarCollapsed, setMainSidebarCollapsed] = useState(false);
const [selectedDocId, setSelectedDocId] = useState(null);
const [selectedNoteId, setSelectedNoteId] = useState(null);
```

**View Routing**:

```javascript
{
  currentView === "sources" && <SourcesSpreadsheet />;
}
{
  currentView === "notebooks" && <NotesViewer />;
}
{
  currentView === "people" && <PeopleViewer />;
}
{
  currentView === "events" && <EventsViewer />;
}
{
  currentView === "locations" && <LocationsViewer />;
}
{
  currentView === "tags" && <TagsViewer />;
}
{
  currentView === "settings" && <Settings />;
}
```

### State Management

#### Zustand Stores

**useCanonicalDocs** (`src/state/useCanonicalDocs.js`):

```javascript
const useCanonicalDocs = create((set, get) => ({
  docs: [], // Array of documents
  loaded: false,
  loading: false,

  loadDocs: async () => {
    /* Fetch all docs */
  },
  getDoc: (docId) => {
    /* Get single doc */
  },
  createDoc: async (manifest) => {
    /* Create doc */
  },
  updateDoc: async (docId, updates) => {
    /* Update doc */
  },
  deleteDoc: async (docId) => {
    /* Delete doc */
  },
}));
```

**ProjectContext** (`src/state/ProjectContext.jsx`):

```javascript
const ProjectContext = createContext({
  active: null, // Current project
  projects: [], // All projects
  selectProject: (slug) => {
    /* Switch project */
  },
});
```

### API Layer (`src/api.js`)

Axios instance with automatic project context injection:

```javascript
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:3001",
});

// Add project slug to all requests
api.interceptors.request.use((config) => {
  const project = getActiveProject();
  if (project?.slug) {
    config.params = { ...config.params, project: project.slug };
  }
  return config;
});
```

### Key Components

#### DocumentViewer (`src/pages/DocumentViewer.jsx`)

**Purpose**: Display and annotate documents (PDF or text)

**Features**:

- PDF.js integration for PDF rendering
- Text view with synchronized pagination
- Text selection → CITE/TAG/EVENT popup
- Block-level editing (narrative mode)
- Speaker association (dialogue mode)
- Source header with icon/emoji, formatted date, short cite badge, and a collapsed **More** panel that reveals advanced controls (detector selector, metadata editor shortcut, native/Docling toggles)
- Dispatches a global `edit-source` event when the user clicks **Edit Metadata** so the Sources viewer can open `SourceMetadataEditor`

**Advanced Controls Toggle**:

- Header shows only core fields by default (name, date, type, short cite)
- Clicking **More ▾** expands detector selection, metadata button, Docling controls, and the dev mode chip
- Toggle automatically resets to collapsed when `docId` changes so new documents always start in the simplified state

**Props**:

```typescript
type DocumentViewerProps = {
  docId: string;
  onNavigateBack?: () => void;
  previousScreen?: string;
};
```

**Key State**:

```javascript
const [viewMode, setViewMode] = useState<"pdf" | "text">("text");
const [blocks, setBlocks] = useState<Block[]>([]);
const [cites, setCites] = useState<Cite[]>([]);
const [currentPage, setCurrentPage] = useState(1);
```

**Data Flow**:

1. Load blocks from `/api/canonical/docs/{docId}/blocks`
2. Load cites from `/api/canonical/docs/{docId}/cites`
3. Render blocks with cite highlights
4. On selection → show `SelectionActionPopover`
5. On cite create → POST to `/api/canonical/docs/{docId}/cites`

#### SourceMetadataEditor (`src/components/sources/SourceMetadataEditor.tsx`)

**Purpose**: Unified editor for source manifest metadata using the wizard infrastructure.

**Highlights**:

- Fetches the current manifest via `/api/canonical/docs/:docId/manifest` and keeps filename history intact when users rename the source
- Provides dedicated inputs for **Source Name**, **Citation Name**, and **Short Cite Name** before rendering the standard wizard form; empty values fall back to wizard-generated defaults
- Persists updates through `PUT /api/canonical/docs/:docId/manifest` and rehydrates the canonical docs store so the active document reflects changes immediately
- Emits the same wizard payload structure (`wizard.answers._emoji`, `_iconPath`, etc.) so downstream consumers remain compatible

**Integration Touchpoints**:

- `DocumentsViewer` listens for a global `edit-source` event (fired from the document header and sidebar) to mount this editor inline in the main content pane
- Inline cite selectors and event linkers read `manifest.meta.citeName`/`shortCite`, so the editor keeps those fields authoritative

#### Source display helpers (`src/lib/sources/display.ts`)

- `resolveSourceEmoji(manifest)` / `resolveSourceIcon(manifest)` — prefer explicit metadata, fall back to wizard defaults, then to a type-to-icon map
- `formatSourceDate(value)` — human readable `MMM DD, YYYY`, preserves original string if parsing fails
- `formatSourceType(type, subtype)` — user-facing label with capitalization and optional subtype

Used by `DocumentViewer`, `DocumentsViewer`, and other list views to keep iconography/date presentation consistent.

#### NotesViewer (`src/pages/NotesViewer/`)

**Purpose**: Rich text note-taking with live formatting and cite embedding

**Features**:

- Single-pane contentEditable surface with inline formatting + cite chips
- Markdown↔HTML round-tripping via `markdownUtils.js` and `editorConversions.js`
- Cite insertion that preserves caret position and renders non-editable chips
- Table of contents sidebar fed by live heading extraction
- Note organization (folders, tags)

**Components**:

- `NotesViewer.jsx` — Main container, editor, cite toolbar, TOC + CITES tab switcher
- `editorConversions.js` — Serializes between DOM HTML and stored markdown
- `markdownUtils.js` — Markdown → HTML helper with heading slugging
- `FormattingToolbar.jsx` — Bold/italic/heading buttons
- `TableOfContents.jsx` — Auto-generated TOC from current markdown
- `CitationsNotebook.jsx` — Aggregated citation grid per project

**Cite Insertion Flow**:

1. User clicks "Insert Cite" button or quote shortcut
2. Opens `CitePicker` modal
3. User selects cite (doc block + quote metadata)
4. Editor injects a non-editable cite chip span at current cursor and appends a space for continued typing

#### EventsViewer (`src/pages/EventsViewer/`)

**Purpose**: Manage events and link to sources

**Features**:

- List view with category filters
- Detail view with source linking
- Participant management
- Duplicate event creation
- Source → Event auto-linking

**Components**:

- `EventsViewer.jsx` — List view
- `EventDetailsDrawer.tsx` — Detail panel
- `EventWizard.tsx` — Create/edit wizard

**Key APIs**:

- `GET /api/events` — List events
- `POST /api/events` — Create event
- `PUT /api/events/:id` — Update event
- `PUT /api/events/:id/source` — Link source
- `POST /api/events/:id/duplicate` — Duplicate event

#### PeopleViewer (`src/pages/PeopleViewer.jsx`)

**Purpose**: Manage people and their appearances

**Features**:

- List view with search
- Create person via wizard
- Link to events/sources
- Track appearances across documents

**Key APIs**:

- `GET /api/people` — List people
- `POST /api/people` — Create person
- `PUT /api/people/:id` — Update person
- `DELETE /api/people/:id` — Delete person

#### LocationsViewer (`src/pages/LocationsViewer.tsx`)

**Purpose**: Centralized view of all geographic locations from People and Events

**Features**:

- **Sidebar list** with search and filters
- **Spreadsheet view** with sortable columns
- **Map view** with interactive markers and auto-zoom
- **Filtering**: by type (people/events), search query, date range
- **Clustering**: automatic grouping of nearby locations (>= 10 locations)
- **Location selection**: click marker or row to highlight

**Map Integration** (PR78):

- MapLibre GL for vector maps
- Photon API for address autocomplete
- Nominatim API for geocoding and reverse geocoding
- Environment-driven configuration (`.env.local`)
- Michigan-focused defaults

**Components**:

- `LocationsViewer.tsx` — Main container with sidebar + view switcher
- `LocationsMapView.tsx` — Map component with clustering
- `LocationSelector.tsx` — Autocomplete + map for selecting locations
- `MichiganMap.tsx` — Base map component

**Key APIs**:

- `GET /api/people` — Fetch people with locations
- `GET /api/events` — Fetch events with locations
- Map services (via CORS proxy):
  - `/autocomplete` — Photon address search
  - `/geocode` — Nominatim forward geocoding
  - `/reverse` — Nominatim reverse geocoding

**Data Types**:

```typescript
interface Location {
  lat: number;
  lon: number;
  label: string;
  source: "user" | "geocode" | "revgeocode";
  address?: Address;
  zoomHint?: number;
}

interface Address {
  raw: string;
  houseNumber?: string;
  road?: string;
  city?: string;
  county?: string;
  state?: string;
  postcode?: string;
  country?: string;
}
```

**Configuration** (`.env.local`):

```env
VITE_MAPS_BASE_URL=https://mxpsxrvxr.stevenhelton.com
VITE_MAP_STYLE_PATH=/styles/bright/style.json
VITE_AUTOCOMPLETE_PATH=/autocomplete
VITE_GEOCODE_PATH=/geocode
VITE_REVERSE_PATH=/reverse
VITE_FEATURE_MAPS=1
```

**Clustering**:

- Uses Supercluster library (60px radius, max zoom 16)
- Green cluster markers show count
- Click to expand and zoom in
- Toggle button to enable/disable
- Dynamic updates on map movement

#### ImageViewer (`src/components/sources/ImageViewer.tsx`)

**Purpose**: Display image sources with zoom and lightbox capabilities

**Features**:

- **Zoom controls**: In/out/reset buttons
- **Pan**: Drag to pan when zoomed in
- **Lightbox mode**: Click image to view full-screen overlay
- **Close on click**: Click lightbox background to exit
- **Responsive**: Fits to container, respects max dimensions

**Props**:

```typescript
interface ImageViewerProps {
  imageUrl: string; // Image source URL
  imageName: string; // Display name for alt text
  onClose?: () => void; // Optional close handler
}
```

**State**:

```javascript
const [zoom, setZoom] = useState(1.0); // Current zoom level (1.0 = 100%)
const [lightbox, setLightbox] = useState(false); // Lightbox open/closed
```

**Interactions**:

- Zoom in: +20% (max 300%)
- Zoom out: -20% (min 50%)
- Reset: Return to 100%
- Lightbox: Click image → full screen overlay
- Close: Click overlay background or press Esc

**Usage**: Automatically rendered by DocumentViewer when `source.type === 'image'`.

#### SelectionActionPopover (`src/components/SelectionActionPopover.jsx`)

**Purpose**: Context menu for text selection

**Triggers**:

- Text selection in DocumentViewer
- Text selection in NotesViewer

**Actions**:

1. **CITE** — Create citation
2. **TAG** — Add tags (future)
3. **EVENT** — Create event from selection

**Data Flow**:

```text
1. User selects text
2. Parent component calls:
   onSelectionChange({
     text, blockId, startOffset, endOffset
   })
3. Popover renders at selection position
4. User clicks action:
   - CITE → createCite({ blockId, startOffset, endOffset, text })
   - EVENT → createEventFromSelection({ blockId, text })
```

#### FeedbackProvider (`src/components/feedback/FeedbackProvider.tsx`)

**Purpose**: Queue and persist structured feedback events to `/api/feedback/append` (or a project-specific file writer).

**Behavior**:

- Validates outgoing events with Zod (`FeedbackEventSchema`).
- Maintains an in-memory queue; failed requests are retried with exponential backoff and survive transient offline states.
- Exposes `pending` and `lastError` so the UI can surface status indicators.

**Integration**: Wrap the document viewer tree in `<FeedbackProvider>` and call `useFeedback().append(event)` whenever the user labels a span or region.

#### Feedback UI Components

- `LabelMenu.tsx`: Context menu grouping label definitions from `config/labels.yml`, displaying optional hotkeys.
- `PdfLabelLayer.tsx`: Absolute overlay that captures drag gestures, emits normalized bounding boxes, and calls the feedback provider.
- `HeaderChips.tsx`: Renders detection results (auto or user-confirmed) with quick jump and inline correction affordances.

These components are optional building blocks—you can compose them differently if the host app already has custom viewers.

#### SplitReview Workspace (`src/views/SplitReview/`)

**Purpose**: Let reviewers confirm or adjust proposed segments before creating canonical child sources.

**Hooks & Components**:

- `useSplitSession.ts`: Local session state with selection + rename helpers; designed to load JSON generated by `tools/splitter/split_cli.py`.
- `SegmentList.tsx`: Left rail listing segments with confidence scores and docket hints.
- `PageStrip.tsx`: Lightweight thumbnail placeholders (pluggable with real page snapshots).
- `SplitReview.tsx`: Two-pane layout that wires the list and page strip together and surfaces a `Finalize` callback.

To integrate with production data, hydrate the hook with the CLI session JSON, render `<SplitReview initialSegments={...} onFinalize={...} />`, and persist any adjustments prior to calling `tools/splitter/make_sources.write_sources`.

---

## Backend Architecture

### Server Entry Point (`server/src/index.ts`)

Single file containing all routes and logic (~4000 lines). Routes organized by domain:

**Binding & proxy coordination**:

- The Express server listens on `HOST` (default `127.0.0.1`) and `PORT` (`5050`) as written to `server/.env.local`.
- `scripts/dev.py` also exports `CASE_PROXY_TARGET` to Vite so `/api/*` requests proxy to the same host/port combination.
- Override with `HOST=0.0.0.0` (server) and/or `CASE_PROXY_HOST=0.0.0.0` (dev runner) when you need LAN access.

**Canonical API** (`/api/canonical/*`):

- Document CRUD
- Block CRUD
- Cite CRUD

**Ingestion API** (`/ingest/*`):

- PDF ingestion
- A/V ingestion
- Auto-event creation

**Registry API** (`/api/*`):

- Events CRUD
- People CRUD
- Tags CRUD

**Wizard API** (`/api/wizard/*`):

- Serve wizard specs
- Evaluate wizard rules

**Project API** (`/api/project/*`):

- Project info CRUD
- Registry management

**Feedback API**:

- `POST /api/feedback/append` — Append a single JSONL event to `sources/{sourceId}/feedback.jsonl`
- `GET /api/profiles` (optional) — Serve merged YAML profiles from `public/profiles/`

### Key Route Handlers

#### Canonical Routes

#### GET /api/canonical/docs

```typescript
// List all documents for project
// Query: ?project={slug}
// Response: { docs: SourceManifest[] }
```

#### GET /api/canonical/docs/:docId

```typescript
// Get document manifest
// Response: SourceManifest
```

#### GET /api/canonical/docs/:docId/blocks

```typescript
// Get document blocks
// Response: { blocks: Block[] }
```

#### GET /api/canonical/docs/:docId/cites

```typescript
// Get document citations
// Response: { cites: Cite[] }
```

#### POST /api/canonical/docs/:docId/cites

```typescript
// Create citation
// Body: { blockId, startOffset, endOffset, selectedText }
// Response: { cite: Cite }
```

#### PUT /api/canonical/docs/:docId/blocks/:blockId

```typescript
// Update block text
// Body: { text: string }
// Response: { block: Block }
```

#### Ingestion Routes

#### POST /ingest/pdf

```typescript
// Upload and ingest PDF
// Body (multipart): file, type, citeName, dates
// Process:
//   1. Save file to sources/pdf/
//   2. Create manifest in canonical/{docId}/
//   3. Run Python ingestion pipeline
//   4. Auto-create event (if applicable)
// Response: { docId, basename, manifest }
```

#### POST /ingest/av

```typescript
// Upload and ingest audio/video
// Body (multipart): file, type, citeName
// Process:
//   1. Save file to sources/av/
//   2. Create manifest
//   3. Run faster-whisper transcription
//   4. Convert to blocks
//   5. Auto-create event
// Response: { docId, basename, manifest, transcript }
```

#### Event Routes

#### GET /api/events

```typescript
// List events for project
// Query: ?project={slug}&category={legal|factual|investigatory}
// Response: EventItem[]
```

#### POST /api/events

```typescript
// Create event
// Body: EventItem (partial)
// Response: EventItem
```

**PUT /api/events/:id**

```typescript
// Update event
// Body: Partial<EventItem>
// Response: EventItem
```

**PUT /api/events/:id/source**

```typescript
// Link source to event
// Body: { sourceId: string, sourceType: string }
// Response: EventItem
```

#### POST /api/events/createFromSelection

```typescript
// Create event from text selection
// Body: { docId, blockId, selectedText, category }
// Process:
//   1. Create event
//   2. Create cite
//   3. Link cite to event
// Response: { event: EventItem, cite: Cite }
```

#### People Routes

#### GET /api/people

```typescript
// List people for project
// Query: ?project={slug}
// Response: PersonItem[]
```

#### POST /api/people

```typescript
// Create person
// Body: PersonItem (partial)
// Response: PersonItem
```

**PUT /api/people/:id**

```typescript
// Update person
// Body: Partial<PersonItem>
// Response: PersonItem
```

#### Feedback Routes

#### POST /api/feedback/append

```typescript
// Append feedback event to JSONL file
// Body: FeedbackEvent (see Data Model)
// Response: { ok: true }
```

Implementation tip: resolve `sources/{sourceId}/feedback.jsonl` within the active project, open in append mode, write the serialized JSON plus `\n`, and flush immediately. The client's retry loop assumes idempotent append semantics.

#### Batch Upload Routes (PR91)

#### POST /api/sources/batch

```typescript
// Upload multiple files simultaneously
// Body: FormData with files[] field (up to 20 files)
// Query: ?project={slug}
// Process:
//   1. Save files temporarily
//   2. Detect source type from extension
//   3. Create SourceItem with status:"pending_name", requiresName:true
//   4. Create draft EventItem (draft:true) to satisfy 1:1 invariant
//   5. Draft events excluded from indexes until published
// Response: { ok: true, created: Array<{sourceId, eventId, detectedType, tempName}> }
```

#### GET /api/sources/pending

```typescript
// Fetch list of sources awaiting user-provided names
// Query: ?project={slug}
// Response: { pending: SourceItem[] }
// Only returns sources with requiresName:true
```

#### POST /api/sources/:id/name

```typescript
// Finalize a pending source by providing name and optional citation fields
// Params: :id = sourceId
// Query: ?project={slug}
// Body: { name: string, citationName?: string, shortCiteName?: string }
// Process:
//   1. Update source: name, metadata, requiresName:false, status:"ready"
//   2. Update linked event: title, draft:false
//   3. Trigger index updates (onEventWrite)
// Response: { ok: true, source: SourceItem }
```

---

## Ingestion Pipeline

### Overview

The ingestion pipeline converts uploaded files (PDF, audio, video) into canonical blocks that can be viewed, searched, and annotated.

### Pipeline Flow

```text
┌─────────────┐
│   Upload    │
│   (File)    │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Auto-Detect Source Type            │
│  (detect_source_type.py)            │
│  • Transcript (Q&A format)          │
│  • Narrative (paragraphs)           │
│  • A/V Recording (audio/video)      │
└──────┬──────────────────────────────┘
       │
       ├───────────────┬───────────────────┐
       ▼               ▼                   ▼
┌──────────────┐ ┌──────────────┐  ┌─────────────┐
│ Transcript   │ │  Narrative   │  │   A/V       │
│  Pipeline    │ │   Pipeline   │  │  Pipeline   │
│              │ │              │  │             │
│ ingest_      │ │ ingest_      │  │ ingest_     │
│ transcript   │ │ doc.py       │  │ av.py       │
│ .py          │ │              │  │             │
└──────┬───────┘ └──────┬───────┘  └──────┬──────┘
       │                │                  │
       │                │                  │
       └────────────────┴──────────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Canonical Output │
              │  • blocks.jsonl  │
              │  • source.md     │
              │  • source.index  │
              │  • manifest.json │
              └──────┬───────────┘
                     │
                     ▼
              ┌──────────────┐
              │ Auto-Create  │
              │    Event     │
              │ (based on    │
              │ source type) │
              └──────────────┘
```

### Transcript Pipeline

**Input**: PDF with Q&A format (court transcripts, depositions)

**Process** (`tools/ingest/ingest_transcript.py`):

1. Extract text per page using PyMuPDF
2. Detect speaker labels (Q:, A:, MR. SMITH:, etc.)
3. Parse dialogue blocks with page anchors
4. Normalize speaker labels
5. Write blocks.jsonl

**Output Block**:

```json
{
  "id": "01HZYD...",
  "type": "dialogue",
  "text": "I was at the scene around 3 PM.",
  "speaker": {
    "label": "WITNESS JONES",
    "personId": null
  },
  "sourceRef": {
    "kind": "pdf",
    "sourceId": "sources/pdf/deposition.pdf",
    "page": 42
  },
  "sequence": 127,
  "createdAt": "2025-10-14T..."
}
```

### Transcript Witness Sections & Phase Navigator (PR 86)

- **Data shape:** `SourceItem.metadata.transcript.sections` mirrors to `projects/<project>/sources/<sourceId>/transcript_sections.json` for fast reads. Each section stores `displayName`, optional `personId`, `[pageStart,pageEnd]`, and nested `phases[]` (`type: "direct" | "cross" | "redirect" | "recross"`, optional `examiner`).
- **API:** `GET/PUT /api/sources/:sourceId/transcript/sections?project=<slug>` (implemented in `server/src/routes/transcriptSections.ts`). Writes happen when the reviewer edits or accepts proposals; reads happen whenever DocumentViewer loads a transcript source.
- **Detector / suggestion:** `src/tools/transcript/sectionizer.ts` consumes `{ page, text }[]` and emits `{ sections, detector }`, combining TOC headings (`WITNESS JANE SMITH ... 123`) with regex cues (`DIRECT EXAMINATION`, `BY MR. JOHNSON:`). UI surfaces this behind a “Suggest Sections” button—no auto-run.
- **Viewer components:** `WitnessNavigator` injects a `Jump…` select (labels like `Jane Smith — Cross (by Ms. Patel)`), while `PhaseHeadingsProvider` overlays virtual headings and exposes smart Q/A relabeling (A. → `WITNESS [NAME]:`, Q. → `MR./MS. [EXAMINER]:`). Toggle lives in the viewer header; the underlying transcript text stays untouched.

### Narrative Pipeline

**Input**: PDF with paragraph format (reports, exhibits, opinions)

**Process** (`tools/ingest/ingest_doc.py`):

1. Extract text per page
2. Detect headings (ALL CAPS, short lines)
3. Split paragraphs (deterministic chunking)
4. Create heading/paragraph blocks
5. Write blocks.jsonl

**Output Block**:

```json
{
  "id": "01HZYF...",
  "type": "paragraph",
  "text": "The incident occurred on Main Street near the intersection with Oak Avenue...",
  "sourceRef": {
    "kind": "pdf",
    "sourceId": "sources/pdf/police-report.pdf",
    "page": 3
  },
  "sequence": 8,
  "createdAt": "2025-10-14T..."
}
```

### Exhibit/Appendix Pipeline (PR96)

**Input**: Any file type (PDF, image, document) designated as Exhibit or Appendix

**Process**: Exhibits bypass specialized ingestion (no transcript parsing, no text extraction). They are stored as opaque sources with rich metadata.

**Metadata Structure** (`ExhibitMetadata`):

```typescript
{
  kind: "exhibit" | "appendix",
  numberOrLetter?: string,        // "A", "1", "23-B"
  titleOrDescription?: string,    // "Medical Records"
  offeredBy?: "prosecution" | "defense" | "other",
  connectedTo: {
    mode: "proceeding" | "filing",
    proceeding?: {
      type: "prelim" | "pretrial" | "trial" | "other",
      note?: string                // "Motion Hearing"
    }
  }
}
```

**Validation**: Zod schema requires **at least one** of `numberOrLetter` or `titleOrDescription`.

**Filename Auto-Detection** (`server/src/lib/exhibitFilenameParser.ts`):
- Detects `offeredBy` from patterns: "D's Exhibit", "P's Exhibit", "Defense Exhibit"
- Extracts number/letter from delimiters: "Exhibit-A.pdf" → "A"
- Extracts title from filename: "Def-1-Medical-Records.pdf" → number=1, title="Medical Records"

**Auto-Event**: Creates "Exhibit / Appendix" event (legal category) with title combining kind + number + description.

**No Blocks**: Exhibits don't generate canonical blocks—they're viewed as whole documents via PDF viewer or image viewer.

### A/V Pipeline

**Input**: Audio or video file (.mp3, .wav, .mp4, .mov, etc.)

**Process** (`tools/ingest/ingest_av.py`):

1. Run faster-whisper transcription
2. Get timestamped segments
3. Detect speakers (if applicable)
4. Create dialogue blocks with time anchors
5. Write blocks.jsonl

**Output Block**:

```json
{
  "id": "01HZYG...",
  "type": "dialogue",
  "text": "Can you describe what you saw?",
  "speaker": {
    "label": "INTERVIEWER",
    "personId": null
  },
  "sourceRef": {
    "kind": "av",
    "sourceId": "sources/av/interview.mp4",
    "startMs": 45320,
    "endMs": 47890
  },
  "sequence": 12,
  "createdAt": "2025-10-14T..."
}
```

### Image Pipeline

**Input**: Image file (.jpg, .jpeg, .png, .gif, .tiff, .tif, .bmp, .webp)

**Process**: Zero-metadata extraction (no OCR, no EXIF parsing)

1. File extension detected → `sourceKind = "image"`
2. User selects actual source TYPE (e.g., "police-report", "court-filing")
3. Single placeholder block created with image reference
4. No text extraction or classification
5. Auto-Event created based on selected source type (not "Photograph")

**Key Concept**: Images are a **format** (kind), not a source type. Any document type can be an image:
- Police report that's a photograph
- Court filing that's a scanned/photographed document
- 911 call transcript that's a screenshot

**Output Block**:

```json
{
  "id": "01HZYH...",
  "type": "note",
  "text": "Reference file: police-report_2024-08-27.jpg",
  "sourceRef": {
    "kind": "image",
    "sourceId": "sources/police-report/crime-scene.jpg"
  },
  "sequence": 1,
  "createdAt": "2025-10-14T..."
}
```

**Viewer**: `ImageViewer` component provides:

- Pan and zoom controls
- Lightbox mode (click to expand)
- Zoom in/out/reset buttons
- Drag to pan in zoomed state

**DocumentViewer Integration**: Automatically detects `sourceRef.kind === "image"` and renders `ImageViewer` instead of text/PDF view.

**Upload**: Images bypass all text classifiers and transcript section detection. User selects actual document type in SourcesWizard.

### Dual Extractor (Native + Docling)

**Purpose**: Run the legacy PDF pipeline and Docling in parallel, emit two canonical sources, and score quality detectors for fast side-by-side comparison.

**Entry Point**: `tools/ingest/dual_ingest.py`

**Config**: `config/extraction.yml`

- `run_sequence`: ordered list of extractors (`native`, `docling`, etc.).
- `detectors`: thresholds for title page, table of contents, and speaker segmentation.
- `naming.suffixes`: appended to the output folder names.

**Extractors**:

- `tools/extractors/native_wrapper.py` → wraps `ingest_pdf_advanced` in a temp directory, copies `document.md` and `document.index.json`.
- `tools/extractors/docling_wrapper.py` → calls Docling, maps headings/paragraphs/tables/images into the canon format via `tools/mappers/canon_mapper.py`.

**Detectors**:

- `tools/detectors/titlepage_detector.py`
- `tools/detectors/toc_detector.py`
- `tools/detectors/speaker_detector.py`

**Workflow**:

1. User drops PDFs into `inbox/` and runs `python tools/ingest/dual_ingest.py --in inbox --out projects/<slug>/sources --reports projects/<slug>/reports`.
2. Script emits sibling folders `<stem>-native` and `<stem>-docling` with canonical assets.
3. PASS/FAIL summaries live in `reports/<stem>.report.md`.
4. UI simply exposes both sources; the reviewer deletes the weaker one.

**Dependencies**: optional `requirements_minimal.txt` (`docling`, `ulid-py`).

### Mega PDF Splitter

**Purpose**: Break large court filings or multi-incident police PDFs into discrete sources, optionally aligned against a docket CSV.

**Modules**:

- `tools/splitter/page_features.py` — Extracts header/body text per page.
- `tools/splitter/split_rules.py` — Heuristics for segment boundaries (headings, stamps, incident numbers).
- `tools/splitter/docket_align.py` — Fuzzy title/date matching against docket rows.
- `tools/splitter/police_header.py` — Dedicated regex extractor for incident metadata.
- `tools/splitter/make_sources.py` — Emits placeholder sources + manifest from reviewed segments.
- `tools/splitter/split_cli.py` — CLI glue orchestrating the pipeline.

**Supporting Config**:

- `config/split.yml` — Thresholds, naming templates, and docket tolerances.
- `public/profiles/split_patterns.yml` — Regex hints (augmented by feedback profiles).

**Workflow**:

1. Run the CLI with `--pdf`, optional `--docket`, and output targets (`--session`, `--report`, `--out`).
2. Reviewers load the generated session JSON in the Split Review UI, adjust segments, and finalize.
3. Finalization writes canonical child sources plus `<pdf>.split_manifest.json` that maps original pages to children for auditing.

**Integration Hooks**:

- Segment detections reuse the same profile infrastructure described in [Feedback & Profiles](#feedback-and-learning-profiles) so user-labeled headings immediately improve split accuracy.

### Auto-Event Creation

**Trigger**: Successful source ingestion

**Mapping Table** (from `json_data_contract_bible.md`):

| source.type   | event.type    | category      |
| ------------- | ------------- | ------------- |
| transcript    | Court Hearing | legal         |
| court-filing  | Court Filing  | legal         |
| opinion       | Court Filing  | legal         |
| police-report | Police Report | investigatory |
| av-interview  | A/V Interview | investigatory |
| bodycam       | Body Camera   | investigatory |
| dashcam       | Dash Camera   | investigatory |
| 911-call      | 911 Call      | investigatory |
| image         | Photograph    | investigatory |

**Process**:

1. Ingest completes successfully
2. Determine event type from source type
3. Create event with:
   - `title` = event type
   - `category` = from mapping table
   - `sourceId` = uploaded source
   - `sourceType` = source.type
   - `createdFrom` = "source_upload"
4. Save to events.json

---

## Feedback and Learning Profiles

### Overview

The feedback system lets reviewers label spans or PDF regions while reading. Events stream to JSONL, and recurring patterns graduate into reusable detection profiles that feed auto-detections, split heuristics, and UI chips.

### Label Catalog

- Source: `config/labels.yml`
- Fields: `key`, `title`, `hotkey`, `kind` (`span`, `region`, or both)
- The UI reads this catalog to populate context menus and hotkeys.

### Client Workflow

1. `<FeedbackProvider>` validates and enqueues `FeedbackEvent`s.
2. POST to `/api/feedback/append` (or equivalent file writer) per event.
3. UI surfaces chips via detections; corrections are also logged as feedback.

### Storage Conventions

- Each source directory contains `feedback.jsonl` (append-only, UTF-8).
- Schema documented at `tools/schemas/feedback_event.schema.json` and mirrored in TypeScript (`src/components/feedback/types.ts`).
- Keep writes idempotent: the client may retry the same payload on transient failures.

### Profile Loading

- Loader: `src/lib/detection/profileLoader.ts` fetches YAML from `/profiles/*.yml`, merges `default` + doc-type-specific profiles.
- Structures: `sections` (regex patterns for spans) and `regions` (bbox templates + optional text anchors).

### Profile Compilation

- CLI: `python tools/profiles/compile_profiles.py --sources projects/<slug>/sources --out public/profiles --name transcripts`
- Logic: scan JSONL files, aggregate hits per label, promote patterns seen in ≥ `--min-hits` sources.
- Output: YAML saved beside defaults so the loader automatically picks them up on the next reload.

### Detector Integration

- `src/lib/detection/detectors.ts` tries profile patterns first, then falls back to legacy heuristics.
- Dual extractor reports reuse the same detectors for scoring.
- Splitter heuristics pull cue patterns from `public/profiles/split_patterns.yml` (seeded defaults + compiled additions).

### Backend Requirements

- Implement `POST /api/feedback/append` (append to JSONL) and optionally expose `GET /api/profiles` if profiles can't be served statically.
- Provide a lightweight cron or manual workflow to run the compiler and deploy updated YAMLs as they stabilize.

---

## Wizard System

### Purpose

JSON-driven forms for creating structured entities (sources, events, people). Allows dynamic form generation without code changes.

### Wizard Specification Format

**Location**: `server/config/wizards/{entity}/{type}.json`

**Example** (`server/config/wizards/events/hearing.json`):

```json
{
  "entity": "events",
  "type": "hearing",
  "label": "Court Hearing",
  "category": "legal",
  "description": "Create a record for a court hearing",
  "steps": [
    {
      "id": "basic",
      "title": "Basic Information",
      "fields": [
        {
          "id": "hearing_type",
          "type": "select",
          "label": "Hearing Type",
          "required": true,
          "options": [
            { "value": "arraignment", "label": "Arraignment" },
            { "value": "preliminary", "label": "Preliminary Hearing" },
            { "value": "motion", "label": "Motion Hearing" },
            { "value": "trial", "label": "Trial" }
          ]
        },
        {
          "id": "date",
          "type": "date",
          "label": "Hearing Date",
          "required": true
        },
        {
          "id": "judge",
          "type": "text",
          "label": "Judge",
          "required": false
        }
      ]
    }
  ],
  "titleTemplate": "{hearing_type} - {date}"
}
```

### Wizard Components

**Frontend** (`src/components/wizard/`):

- `DynamicWizard.tsx` — Main wizard renderer
- `WizardStep.tsx` — Single step renderer
- `FieldRenderer.tsx` — Field type renderer
- `ValidationEngine.ts` — Rule evaluation

**Backend** (`server/src/routes/wizard.ts`):

- `GET /api/wizard/:entity` — Get wizard spec for entity type
- `POST /api/wizard/:entity/evaluate` — Evaluate conditional rules

### Field Types

- `text` — Single-line text input
- `textarea` — Multi-line text
- `select` — Dropdown
- `date` — Date picker
- `time` — Time picker
- `datetime` — Date + time picker
- `checkbox` — Boolean
- `radio` — Radio buttons
- `person-select` — Person picker (autocomplete)
- `source-select` — Source picker (autocomplete)

### Conditional Logic

Fields can have `showIf` rules:

```json
{
  "id": "trial_verdict",
  "type": "select",
  "label": "Verdict",
  "showIf": {
    "field": "hearing_type",
    "equals": "trial"
  },
  "options": [
    { "value": "guilty", "label": "Guilty" },
    { "value": "not_guilty", "label": "Not Guilty" }
  ]
}
```

### Title Generation

Wizard specs include `titleTemplate` with placeholder syntax:

```json
"titleTemplate": "{hearing_type} - {date}"
```

Backend replaces placeholders with user answers:

```javascript
const title = titleTemplate.replace(/{(\w+)}/g, (_, key) => {
  return answers[key] || "";
});
```

---

## Form Detection System

### Purpose

The form detection system enables document-type-specific labeling and template creation for standardized forms (e.g., Michigan court forms MC227, MC220, etc.). Each form type is registered as a detector, allowing:

- Form-specific label organization in training data
- Template creation from labeled blank forms
- Auto-application of templates to filled forms (future)

### Architecture

**Configuration Files**:

- `config/detectors.wizard.json` — Hierarchical detector definitions
- `config/labels.yml` — Auto-generated labels (synced from detectors)
- `training/{detector-type}/{doc-id}/` — Training data organized by form type

**Key Scripts**:

- `scripts/add_form_detector.mjs` — Add new form type as detector
- `scripts/setup_common_forms.mjs` — Batch-add 11 common Michigan forms
- `scripts/generate_labels_from_detectors.mjs` — Sync labels.yml from detectors
- `scripts/export_form_template.mjs` — Convert labeled doc to reusable template
- `scripts/download_michigan_forms.mjs` — Download blank forms from Michigan courts

### Detector Structure

**Example** (`config/detectors.wizard.json`):

```json
{
  "id": "form_mc227",
  "label": "MC227 - Judgment of Sentence",
  "description": "Michigan SCAO Form MC227: Judgment of Sentence",
  "detectors": [
    {
      "id": "form_number",
      "label": "Form Number",
      "type": "keyword_match",
      "require_keywords": ["MC227", "MC 227"],
      "search_area": "first_10_lines",
      "min_hits": 1
    },
    {
      "id": "scao_header",
      "label": "SCAO Header",
      "type": "keyword_match",
      "require_any": ["STATE COURT ADMINISTRATIVE OFFICE", "SCAO"],
      "search_area": "first_15_lines",
      "min_hits": 1
    }
  ]
}
```

### Adding a New Form Type

**Single Form**:

```bash
node scripts/add_form_detector.mjs MC227 "Judgment of Sentence"
```

**What it does**:

1. Creates detector in `detectors.wizard.json` with ID `form_mc227`
2. Adds basic detectors (form number, SCAO header)
3. Auto-regenerates `labels.yml` with form-specific labels
4. Makes form available in "Detector Type" dropdown in UI

**Batch Setup (11 Common Forms)**:

```bash
node scripts/setup_common_forms.mjs
```

Adds:

- Criminal Disposition: MC227, MC228, MC229
- Criminal Felony: MC220, MC221, MC260
- Criminal Misdemeanor: MC10, MC11, MC12
- Appeals: MC51, MC52

### Training Data Collection

**Workflow**:

1. **Upload blank form** with detector type selected (e.g., "MC227 - Judgment of Sentence")
2. **Label PDF** — Draw boxes around all fields (defendant_name, case_number, etc.)
3. **Auto-save** — Annotations save to `training/form_mc227/{doc-id}/`

**Training Directory Structure**:

```text
training/
  form_mc227/
    01K7MD367W9S740P65SVMZR5KR/
      document.pdf          # Copy of original PDF
      annotations.jsonl     # Label events (bbox + label)
      metadata.json         # Doc info, label count
  form_mc220/
    ...
```

**Backend Implementation** (`server/src/index.ts`):

```typescript
POST / api / feedback / append;
// When kind === "region" and manifest.detectorType exists:
// 1. Append to sources/{sourceId}/feedback.jsonl
// 2. Copy to training/{detectorType}/{docId}/annotations.jsonl
// 3. Copy PDF to training/{detectorType}/{docId}/document.pdf
// 4. Update metadata.json with label count
```

### Template Export

**Export labeled form as template**:

```bash
node scripts/export_form_template.mjs [doc-id] MC227
```

**Output** (`form_templates/criminal_disposition/MC227.json`):

```json
{
  "formCode": "MC227",
  "formName": "Judgment of Sentence",
  "category": "criminal_disposition",
  "version": "2023",
  "fields": [
    {
      "id": "defendant_name",
      "label": "Defendant Name",
      "type": "text",
      "bbox": [120, 180, 400, 200],
      "page": 1
    },
    {
      "id": "case_number",
      "label": "Case Number",
      "type": "case_number",
      "bbox": [450, 180, 550, 200],
      "page": 1
    }
  ],
  "referenceDoc": "01K7MD367W9S740P65SVMZR5KR",
  "createdAt": "2025-10-15T..."
}
```

**Field Types** (auto-inferred from label names):

- `date` — Contains "date", "dob", "filed"
- `case_number` — Contains "case", "docket", "file_number"
- `name` — Contains "name", "defendant", "plaintiff", "attorney"
- `signature` — Contains "signature", "signed", "judge"
- `number` — Contains "count", "amount", "fine", "sentence"
- `address` — Contains "address", "street", "city", "zip"
- `checkbox` — Contains "check", "box", "select"
- `text` — Default

### Label Generation

**Auto-sync from detectors**:

```bash
node scripts/generate_labels_from_detectors.mjs
```

**What it does**:

1. Reads all detector IDs from `detectors.wizard.json` (recursively)
2. Creates label entries with `doc_types` filtering
3. Sections get `kind: ["region"]`, others get `["region", "span"]`
4. Writes to `config/labels.yml` and `public/static/config/labels.yml`

**Example Output**:

```yaml
labels:
  - key: form_mc227
    title: MC227 - Judgment of Sentence
    kind:
      - region
      - span
    doc_types:
      - form_mc227

  - key: form_number
    title: Form Number
    kind:
      - region
      - span
    doc_types:
      - form_mc227
```

### Training Statistics

**View progress**:

```bash
node scripts/training_stats.mjs
```

**Output**:

```text
📊 Training Data Statistics

Documents per detector type:
  form_mc227:  5 docs
  form_mc220:  3 docs
  form_mc10:   2 docs

Labels per detector:
  form_mc227:
    defendant_name:    5 ████████████████
    case_number:       5 ████████████████
    judge_signature:   4 █████████████
    sentence_min:      5 ████████████████
```

### Future: Template Application

**Planned workflow** (not yet implemented):

1. User uploads filled MC227 form
2. System detects form type (keyword matching)
3. Loads template `form_templates/criminal_disposition/MC227.json`
4. Applies bounding boxes to extract values
5. Populates structured data with extracted text
6. User reviews/corrects in UI

**Benefits**:

- One-time labeling per form type
- Automatic field extraction for all filled instances
- Structured data export (JSON, CSV)
- Quality validation (missing fields, format errors)

### SCAO Form Automation

**Purpose**: Automatically crawl, download, and manage Michigan SCAO forms with AI-assisted field labeling.

**Architecture**:

```text
Michigan Courts → Crawler → forms/manifest.json
                             ↓
                  Registry Builder → config/forms.registry.json
                             ↓
                  Auto-Register → config/detectors.wizard.json
                             ↓
                  AI Suggestions → form_sources/suggestions/
                             ↓
                  Manual Labeling → training/{form_type}/
                             ↓
                  Template Export → form_templates/
```

**Key Scripts**:

- `scripts/scao_sync.mjs` — Crawl Michigan Courts indexes and download PDFs
- `scripts/build_form_registry.mjs` — Generate registry and auto-register detectors
- `scripts/suggest_fields.mjs` — Use OpenAI to suggest field locations
- `.github/workflows/scao-sync.yml` — Nightly automated sync with PR creation

**Data Sources**:

- Michigan Court Forms index (primary, has all metadata)
- Circuit Court forms
- District Court forms
- Recently Revised forms (for change tracking)

**Workflow**:

1. **Nightly Sync** (GitHub Actions):
   - Crawls form indexes
   - Downloads new/updated PDFs to `form_sources/raw/`
   - Generates `forms/manifest.json` with metadata
   - Creates PR if changes detected

2. **Registry Build**:
   - Reads manifest
   - Generates `config/forms.registry.json` (code → name mappings)
   - Auto-calls `add_form_detector.mjs` for new forms
   - Regenerates labels

3. **AI Field Suggestions**:
   - Extracts PDF page-1 text with `pdftotext`
   - Calls OpenAI API (gpt-4o-mini) with structured prompt
   - Returns field suggestions: `{id, label, type, hintTexts}`
   - Saves to `form_sources/suggestions/`

4. **Manual Refinement**:
   - User uploads blank form with detector type selected
   - Refers to AI suggestions for quick labeling
   - Draws bounding boxes in PDF Label Mode
   - System saves to training directory

5. **Template Export**:
   - Converts labeled form to reusable template
   - Includes bbox coordinates and field types
   - Saves to `form_templates/{category}/`

**Configuration**:

```env
# .env.local
OPENAI_API_KEY=your-openai-api-key-here
```

**See**: `Documentation/SCAO_AUTOMATION.md` for complete guide

---

## Data Contracts

### Golden Invariants

From `Documentation/Standards/json_data_contract_bible.md`:

1. **Stable IDs**: All entities use ULIDs that never change
2. **Event Categories**: Must be `"legal"`, `"factual"`, or `"investigatory"`
3. **Auto-Event on Upload**: Every source upload creates exactly one event
4. **Events Without Sources**: Allowed, but UI nudges to link if category="legal"
5. **Participation Links**: People can attach to events/sources with roles
6. **Cites Are Read-Through**: Always resolvable to block + source
7. **Touched-Only Indexing**: No global rebuilds, only update changed items

### Validation Layers

**Shape Validation** (Zod schemas):

- Applied at API boundaries
- Ensures required fields present
- Type checking

**Index Validation**:

- After create/update/delete operations
- Runs `npm run validate:touched`
- Checks cross-references valid

**UI Guarantees**:

- EventDetailsView shows linked source chip
- Non-blocking legal tip for unlinked legal events
- People participation visible in UI

---

## Testing Strategy

### Unit Tests (`tests/`)

**Framework**: Vitest + Testing Library

**Coverage**:

- Block parsing logic
- Cite creation/validation
- Event creation/linking
- Wizard field rendering
- API utilities

**Example**:

```javascript
// tests/api/cites.spec.ts
describe("Cite API", () => {
  it("creates cite with valid block reference", async () => {
    const cite = await createCite({
      docId: "test-doc",
      blockId: "test-block",
      startOffset: 0,
      endOffset: 10,
      selectedText: "test text",
    });

    expect(cite.id).toBeDefined();
    expect(cite.selectedText).toBe("test text");
  });
});
```

### E2E Tests (`tests/e2e/`)

**Framework**: Playwright

**Coverage**:

- Full ingestion flow (upload → blocks → event)
- Document viewing and annotation
- Event creation from selection
- Notes with cite embeds

**Example**:

```javascript
// tests/e2e/ingestion.spec.ts
test("PDF upload creates document and event", async ({ page }) => {
  await page.goto("/");
  await page.click("text=Upload Source");
  await page.setInputFiles('input[type="file"]', "test.pdf");
  await page.fill('input[name="citeName"]', "Test Doc");
  await page.click("text=Upload");

  // Verify document created
  await expect(page.locator("text=Test Doc")).toBeVisible();

  // Verify event auto-created
  await page.click("text=Events");
  await expect(page.locator("text=Police Report")).toBeVisible();
});
```

### Verification Gates

**Required before PR merge**:

1. `npm run lint` — 0 errors
2. `npm run test` — All pass
3. `npm run build` — Successful
4. `npm run e2e` — All pass
5. Manual smoke test — No console errors

---

## Performance Considerations

### Bundle Size

**Current**: 142.55 KB gzipped (main bundle)

**Optimizations**:

- Tree-shaking unused dependencies
- Code splitting by route
- Lazy loading heavy components (PDF.js)

**Budget**: 250 KB (enforced via size-limit)

### Database Strategy

**Current**: File-based storage (no database)

**Why**:

- Simplicity for prototype
- Version control friendly
- Portable projects

**Limitations**:

- No complex queries
- No concurrent write handling
- File system I/O overhead

**Future**: Consider SQLite for production

### Ingestion Performance

**PDF Processing**: ~1-2 seconds per page
**A/V Transcription**: Real-time (1x speed with base model)

**Optimizations**:

- Background processing (async)
- Progress reporting via WebSocket
- Batch ingestion support

---

## Development Workflow

### Adding a New Feature

1. **Check** `Documentation/index.md` for existing PR
2. **Create PR triplet**:
   - `Documentation/PRs/pr{N}.md` — Design
   - `Documentation/PRs/pr{N}-manifest.json` — Changes
   - `Documentation/PRs/runlog-PR{N}.md` — Evidence
3. **Implement** following data contracts
4. **Test** (unit + e2e + manual)
5. **Document** changes in manifest
6. **Verify** gates pass
7. **Update** index.md (move to Completed)

### Modifying Data Structures

**CRITICAL**: Check `Documentation/Standards/json_data_contract_bible.md`

**Steps**:

1. Verify change doesn't violate Golden Invariants
2. Update Zod schemas if needed
3. Write migration script if breaking change
4. Update all affected components
5. Add tests for new structure
6. Document in PR manifest

### Adding a New Wizard

1. **Create spec**: `server/config/wizards/{entity}/{type}.json`
2. **Define fields**: Use standard field types
3. **Add title template**: With placeholder syntax
4. **Test in UI**: Verify all fields render
5. **Document**: Add to wizard README

---

## Troubleshooting

### Common Issues

**Issue**: "Project not found" error
**Solution**: Ensure project slug in API requests (check ProjectContext)

**Issue**: UI Settings page shows `net::ERR_CONNECTION_REFUSED`
**Solution**: Confirm the dev server is running and that `HOST`/`CASE_PROXY_HOST` are aligned. Run `CASE_PROXY_HOST=127.0.0.1 ./start` to force IPv4 loopback; use `HOST=0.0.0.0` if you need LAN access.

**Issue**: Blocks not loading
**Solution**: Check `canonical/{docId}/blocks.jsonl` exists and is valid JSONL

**Issue**: PDF not rendering
**Solution**: Verify PDF.js worker loaded, check browser console

**Issue**: Transcription fails
**Solution**: Check faster-whisper installed, verify audio file format supported

**Issue**: Event not auto-created
**Solution**: Check source type mapping table, verify ingestion completed

### Debug Tools

**Server logs**:

```bash
# Check ingestion logs
tail -f server/logs/ingestion.log

# Check API logs
tail -f server/logs/api.log
```

**Frontend debug**:

```javascript
// Enable debug mode
localStorage.setItem("DEBUG", "true");

// Check store state
console.log(useCanonicalDocs.getState());
console.log(useProject.getState());
```

**Validate data**:

```bash
# Check manifest integrity
node scripts/check_manifests.mjs

# Validate JSON files
find canonical -name "*.json" -exec jq empty {} \;

# Check for orphaned files
npm run sweep:orphans
```

---

## API Reference

### Complete Endpoint List

**Canonical API**:

- `GET /api/canonical/docs` — List documents
- `GET /api/canonical/docs/:docId` — Get document
- `GET /api/canonical/docs/:docId/blocks` — Get blocks
- `POST /api/canonical/docs/:docId/blocks` — Create block
- `PUT /api/canonical/docs/:docId/blocks/:blockId` — Update block
- `DELETE /api/canonical/docs/:docId/blocks/:blockId` — Delete block
- `GET /api/canonical/docs/:docId/cites` — Get cites
- `POST /api/canonical/docs/:docId/cites` — Create cite
- `PUT /api/canonical/docs/:docId/cites/:citeId` — Update cite
- `DELETE /api/canonical/docs/:docId/cites/:citeId` — Delete cite

**Ingestion API**:

- `POST /ingest/pdf` — Upload PDF
- `POST /ingest/av` — Upload audio/video

**Events API**:

- `GET /api/events` — List events
- `GET /api/events/:id` — Get event
- `POST /api/events` — Create event
- `POST /api/events/createFromSelection` — Create from selection
- `PUT /api/events/:id` — Update event
- `PUT /api/events/:id/source` — Link source
- `POST /api/events/:id/duplicate` — Duplicate event
- `DELETE /api/events/:id` — Delete event
- `GET /api/events/by-source/:sourceId` — Get events for source

**People API**:

- `GET /api/people` — List people
- `GET /api/people/:id` — Get person
- `POST /api/people` — Create person
- `PUT /api/people/:id` — Update person
- `DELETE /api/people/:id` — Delete person

**Wizard API**:

- `GET /api/wizard/:entity` — Get wizard specs
- `GET /api/wizard/:entity/:type` — Get specific wizard
- `POST /api/wizard/:entity/evaluate` — Evaluate rules

**Project API**:

- `GET /api/project` — Get project info
- `PUT /api/project` — Update project info
- `GET /api/registries/:type` — Get registry (events/people)
- `PUT /api/registries/:type` — Update registry

**Files API**:

- `GET /api/files/:docId/source` — Get source file
- `GET /api/files/:docId/pdf` — Get PDF
- `GET /api/files/:docId/blocks` — Get blocks file

---

## Future Enhancements

### Planned Features

1. **Real-time Collaboration**: WebSocket for multi-user editing
2. **Advanced Search**: Full-text search across all content
3. **Export Formats**: Word, PDF, HTML export
4. **Timeline View**: Chronological event visualization
5. **Evidence Board**: Visual case organization
6. **Mobile App**: React Native companion app
7. **AI Assistants**: Summarization, entity extraction
8. **Database Migration**: Move from files to SQLite/PostgreSQL

### Technical Debt

1. **Refactor server**: Split monolithic index.ts into modules
2. **Type Safety**: Complete TypeScript migration
3. **Error Handling**: Centralized error handling + logging
4. **State Management**: Consider Redux for complex state
5. **Testing**: Increase coverage to 80%+
6. **Documentation**: Auto-generate API docs from code

---

## Contributing

### Code Style

- **Frontend**: ESLint + Prettier
- **Backend**: ESLint + TypeScript strict mode
- **Python**: Black + isort + mypy

### Commit Messages

Format: `type(scope): description`

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Example: `feat(events): add duplicate event functionality`

### PR Guidelines

1. Follow PR workflow in `Documentation/index.md`
2. Include manifest + runlog
3. Pass all verification gates
4. Update relevant documentation
5. Add tests for new features

---

## Resources

- **Main README**: `/README.md`
- **User Guide**: `/Documentation/USER_GUIDE.md`
- **Data Contracts**: `/Documentation/Standards/json_data_contract_bible.md`
- **PR Index**: `/Documentation/index.md`
- **Quick Reference**: `/Documentation/QUICK_REFERENCE.md`

---

**Questions?** Check the PR history in `Documentation/PRs/` or create a new issue.
