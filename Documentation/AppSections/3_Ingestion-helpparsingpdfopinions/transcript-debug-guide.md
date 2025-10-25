<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Transcript Ingestion Debugging Guide](#transcript-ingestion-debugging-guide)
  - [Quick Diagnosis](#quick-diagnosis)
    - [Check what the PDF extractor is seeing](#check-what-the-pdf-extractor-is-seeing)
  - [Watch Live Ingestion](#watch-live-ingestion)
    - [Option 1: Server Logs (Terminal)](#option-1-server-logs-terminal)
    - [Option 2: Python Script with Logging](#option-2-python-script-with-logging)
  - [Common Issues with Transcripts](#common-issues-with-transcripts)
    - [Issue 1: Line Numbers Treated as Paragraphs](#issue-1-line-numbers-treated-as-paragraphs)
    - [Issue 2: Speaker Names Not Detected](#issue-2-speaker-names-not-detected)
    - [Issue 3: Q/A Not Detected](#issue-3-qa-not-detected)
  - [Real-Time Monitoring Script](#real-time-monitoring-script)
  - [Quick Fixes to Try](#quick-fixes-to-try)
    - [1. Filter Line Numbers](#1-filter-line-numbers)
    - [2. Better Speaker Detection](#2-better-speaker-detection)
    - [3. Merge Line-Wrapped Text](#3-merge-line-wrapped-text)
  - [Test Your Changes](#test-your-changes)
  - [Next Steps](#next-steps)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Transcript Ingestion Debugging Guide

## Quick Diagnosis

### Check what the PDF extractor is seeing

```bash
# Activate Python environment
source .venv/bin/activate

# Run debug mode on your problem transcript
python tools/ingest/ingest_pdf_debug.py \
  --pdf "server/~/Desktop/casefolder/sources/2025-10-14_TrialTranscript_Dunning_Witness.pdf" \
  --output /tmp/debug-output \
  --mode transcript \
  --doc-id TEST123 \
  --source-path sources/test.pdf \
  --source-file test.pdf
```

This will show you:

1. **First 3 pages** of extracted blocks with their text
2. Detection status for each block (SPEAKER, Q/A, HEADING, LINE NUMBER)
3. First 10 segments after processing
4. Markdown preview of output
5. Block structure

## Watch Live Ingestion

### Option 1: Server Logs (Terminal)

```bash
# In one terminal, watch the server logs
cd server
npm run dev | tee ingestion.log
```

Then upload a PDF in the UI and watch the terminal output.

### Option 2: Python Script with Logging

Add `--verbose` flag support to see real-time processing:

```bash
# Edit tools/ingest/ingest_pdf_advanced.py to add verbose logging
# Then run server with DEBUG env var
DEBUG=pdf-ingest npm run dev
```

## Common Issues with Transcripts

### Issue 1: Line Numbers Treated as Paragraphs

**Symptom:** Output shows "1", "2", "3" as separate blocks

**Cause:** PDF has line numbers in separate text blocks

**Fix:** Filter out blocks that are only digits

```python
# In extract_segments(), after getting text:
if re.match(r'^\d+\s*$', text):
    continue  # Skip line numbers
```

### Issue 2: Speaker Names Not Detected

**Symptom:** No speaker attribution in output

**Debug:** Check if speaker pattern matches your format:

- Current pattern: `[A-Z][A-Z\s.]+?:`
- Matches: "MR. SMITH:", "THE COURT:", "MS. JONES:"
- Doesn't match: "Mr. Smith:", "Smith:", "SMITH" (no colon)

### Issue 3: Q/A Not Detected

**Current pattern:** `^(Q|A)[:.]?\s+(.+)$`

- Matches: "Q: What happened?", "A. I saw him.", "Q What time?"
- Doesn't match: "Q-1. What...", "Question:"

## Real-Time Monitoring Script

```bash
#!/bin/bash
# Save as tools/watch-ingestion.sh

# Watch for new canonical docs
fswatch -0 server/~/Desktop/casefolder/canonical | while read -d "" event
do
  if [[ $event == *.md ]]; then
    echo "New MD: $event"
    head -50 "$event"
  elif [[ $event == *.index.json ]]; then
    echo "New index: $event"
    jq '.blocks[:5]' "$event"
  fi
done
```

## Quick Fixes to Try

### 1. Filter Line Numbers

Add to `extract_segments()` after `text = clean_text(raw_text)`:

```python
# Skip line numbers (common in court transcripts)
if re.match(r'^\d+\s*$', text):
    continue
```

### 2. Better Speaker Detection

```python
# Allow lowercase after first letter
speaker_pattern = r'^([A-Z][A-Za-z\s.]+?):\s*(.*)$'

# Or be more specific for court transcripts
court_speaker_pattern = r'^(THE COURT|MR\. \w+|MS\. \w+|BY [A-Z\s.]+):\s*(.*)$'
```

### 3. Merge Line-Wrapped Text

The current code should already handle this via `_flush_buffer()`, but if it's not working:

```python
# In _split_transcript_block, accumulate lines until next speaker
```

## Test Your Changes

```bash
# After editing ingest_pdf_advanced.py:
npm run test tests/ingest/pdf-real.spec.ts

# Full verification
npm run lint
npm run test
npm run build
```

## Next Steps

Based on what you see in the debug output, I can:

1. **Add line number filtering** (if that's the issue)
2. **Improve speaker detection** (if names aren't being caught)
3. **Better text merging** (if Q/A are fragmented)
4. **Add logging to server** (to see what's passed to Python)

Run the debug script and share the first 50 lines of output!
