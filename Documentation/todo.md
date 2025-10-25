<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Structure](#structure)
- [UI Generally](#ui-generally)
  - [Future](#future)
- [Project Info](#project-info)
- [Sources](#sources)
  - [Ingest a/v](#ingest-av)
    - [Next-Diarizer Ideas](#next-diarizer-ideas)
  - [Transcripts Section](#transcripts-section)
  - [More Info Panel](#more-info-panel)
  - [Dialogue](#dialogue)
- [Events](#events)
  - [Events Metadata](#events-metadata)
  - [Events Section](#events-section)
- [Notebooks](#notebooks)
  - [Basic](#basic)
  - [Note Editor UI](#note-editor-ui)
  - [CITEs Notebook](#cites-notebook)
  - [Templates](#templates)
    - [Brief Template](#brief-template)
    - [Witness Outline Template](#witness-outline-template)
- [People](#people)
- [Export](#export)
- [Locations](#locations)
  - [For events, sources, people, etc. allow user to add a location (with autocomplete from Google Maps API or something else) and then show that location on a map view of the case](#for-events-sources-people-etc-allow-user-to-add-a-location-with-autocomplete-from-google-maps-api-or-something-else-and-then-show-that-location-on-a-map-view-of-the-case)
  - [Location / Timeline Mapping](#location--timeline-mapping)
  - [Cellular Tower Mapping](#cellular-tower-mapping)
- [Future](#future-1)
  - [Integrate with larger legal database (OpinionUI) to allow user to auto-add boilerplate, case cites, etc. to briefs and other documents](#integrate-with-larger-legal-database-opinionui-to-allow-user-to-auto-add-boilerplate-case-cites-etc-to-briefs-and-other-documents)
  - [Integrate with guidelines calculator](#integrate-with-guidelines-calculator)
  - [Self-Contained App (no backend)](#self-contained-app-no-backend)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Structure

# UI Generally

## Future

-- Dark mode support
-- Two Screen support (need to be able to view source and type notes at the same time)

# Project Info

# Sources

## Ingest a/v
### Next-Diarizer Ideas

Generate MFCC embeddings (e.g., via meyda or a lightweight WASM backend) and cluster with cosine distance to reduce label swaps.
Add an energy-based VAD pass so silence gaps are learned from the waveform instead of the transcript timing, improving segment boundaries.
Expose a pluggable adapter layer that can handshake with WhisperX or Pyannote when GPU resources are available, falling back to the current heuristic otherwise.


## Transcripts Section
Incorporate tables of contents used in transcripts to auto-generate different sections that can be navigated to more easily, and to assign witness for certain pages to "A. " durning page-ranges where they are the witness.


## More Info Panel

there should be a button in the top right corner of the source view that opens a panel that allows user to edit metadata about the source, rename the source, rescan the source using another OCR method, delete the source, and require the source to show the PDF rather than the OCR'ed text by default.

## Dialogue


# Events

## Events Metadata

- allow connected events, begin YYYY-MM-DD, end YYYY-MM-DD, location, notes
  
## Events Section

- Allows user to filter by event type (e.g. arrests, searches, interviews, PEOPLE, etc.)
- Some better visual for thing where give people testify at trial, maybe symbols for things like verdict, bindover, offense date, birthdays, stuff like that
-  

# Notebooks

## Basic

## Note Editor UI

- ✅ Single-pane WYSIWYG editor renders formatting (bold, italics, headings, lists) inline while typing (Oct 2025)
- ✅ Inline cite chips stay editable via toolbar + cite picker (Oct 2025)
- Follow-up: extend serializer to cover nested lists, blockquotes, code blocks so round-tripping markdown ↔ editor stays lossless
- Follow-up: evaluate migrating from `document.execCommand` to Slate/Tiptap (or similar) for long-term stability & richer formatting APIs

## CITEs Notebook

## Templates

### Brief Template

### Witness Outline Template

# People
- Create and show connections. Edit person + add connection > PEOPLE selector w/relationship label (i.e., "sibling," "alleged accomplice," "spouse," etc.)
- People view - show list of people, their roles, and connections
- Ability to search names on OTIS, 


# Export

# Locations 

## For events, sources, people, etc. allow user to add a location (with autocomplete from Google Maps API or something else) and then show that location on a map view of the case

## Location / Timeline Mapping
- allow user to see events on map view and timeline view
- allow user to filter events by location on map view and timeline view
- 

## Cellular Tower Mapping 
- Create larger database of cell towers (location, carrier, etc.) for specific times
- Allow user to upload cell tower dumps (from carrier or from phone) and get map of tower locations and times




# Future 

## Integrate with larger legal database (OpinionUI) to allow user to auto-add boilerplate, case cites, etc. to briefs and other documents

## Integrate with guidelines calculator 


## Self-Contained App (no backend)
