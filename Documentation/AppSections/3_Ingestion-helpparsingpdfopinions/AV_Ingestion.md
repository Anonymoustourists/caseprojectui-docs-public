<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A/V Ingestion & UI Guide](#av-ingestion--ui-guide)
  - [Overview](#overview)
  - [Setup](#setup)
    - [Python Dependencies](#python-dependencies)
  - [Upload & Transcription Flow](#upload--transcription-flow)
    - [Supported File Types](#supported-file-types)
    - [Upload (Frontend)](#upload-frontend)
    - [Server (Backend)](#server-backend)
    - [Transcript Output](#transcript-output)
  - [UI Integration](#ui-integration)
    - [Components](#components)
    - [Playback Flow](#playback-flow)
    - [Current Limitations](#current-limitations)
  - [Testing](#testing)
    - [Quick Start](#quick-start)
    - [Scenarios](#scenarios)
  - [Troubleshooting](#troubleshooting)
  - [Model Sizes](#model-sizes)
  - [Future Enhancements](#future-enhancements)
  - [History](#history)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A/V Ingestion & UI Guide

This document consolidates all guidance for ingesting, transcribing, and integrating audio/video (A/V) materials into the system. It merges prior guides and fix notes into a single authoritative reference.

---

## Overview

A/V ingestion converts raw audio or video into searchable, timestamped transcripts (Markdown + JSON sidecar) that integrate seamlessly with the UI for playback, navigation, and editing.

**Pipeline:**

1. Upload `.mp4`, `.wav`, or similar file.
2. Server saves original to `library/sources/`.
3. Placeholder transcript created in `library/texts/av-transcripts/`.
4. Background transcription runs using **faster-whisper**.
5. Output = Markdown transcript + `.index.json` sidecar.
6. UI displays transcript blocks with Play/Stop buttons linked to timestamps.

---

## Setup

### Python Dependencies

```bash
cd tools/ingest
pip install -e ".[av]"
```

This installs:

- `faster-whisper` (speech-to-text)
- `ffmpeg` (video processing, must be installed separately)
- `pymupdf`, `pydantic`, `pyyaml` (support libraries)

**Verify:**

```bash
python3 -m tools.ingest.ingest_av --help
```

---

## Upload & Transcription Flow

### Supported File Types

- **Audio:** `.wav`, `.mp3`, `.m4a`, `.aac`, `.flac`, `.ogg`
- **Video:** `.mp4`, `.mov`, `.avi`, `.mkv`

### Upload (Frontend)

1. Navigate to **Upload → Add Source**.
2. Select audio/video file.
3. Enter metadata (cite name, date, type).
4. Click **Upload**.

### Server (Backend)

- Saves file → `library/sources/`.
- Creates placeholder transcript:

  ```markdown
  ---
  id: src_abc123
  type: AV
  cite_name: "Interview"
  narration_date: 2024-01-01
  source_file: ../../../library/sources/interview.mp4
  ---

  Transcription in progress...
  ```

- Launches background transcription.
- On success: replaces placeholder with full Markdown transcript + `.index.json` sidecar.

### Transcript Output

```markdown
<!-- [[t:00:00:00-00:00:15]] SPEAKER -->

▶ Play (00:00:00)
SPEAKER: Can you tell me what happened?
```

Sidecar JSON:

```json
{
  "t_start": 0.0,
  "t_end": 15.0,
  "speaker_raw": "SPEAKER",
  "text": "Can you tell me what happened?"
}
```

---

## UI Integration

### Components

- **Media streaming endpoint:** `/media?src=…` (supports HTTP 206 partial requests).
- **MediaManager:** ensures only one `<audio>`/`<video>` element per source, auto-stops at `t_end`.
- **BlockRenderer:** renders each transcript block with Play/Stop button + timestamp.
- **DocumentViewer:** page that loads transcript Markdown + sidecar and maps into blocks.

### Playback Flow

1. User clicks **Play** on a block.
2. MediaManager seeks to `t_start`, plays until `t_end`.
3. Auto-stop at `t_end`.
4. UI updates button state (`▶ Play` ↔ `⏸ Stop`).

### Current Limitations

- Must refresh Sources screen after transcription completes.
- No progress indicator (planned).
- Single-speaker output (diarization planned).

---

## Testing

### Quick Start

```bash
export CASE_ROOT="/absolute/path/to/case-project-ui"
export PORT=5050
./scripts/dev_all.sh
open http://localhost:5173
```

### Scenarios

**1. Playback test**

- Navigate to Viewer.
- Open sample transcript (`McFadden-Miranda.md`).
- ✅ Play button starts audio, auto-stops at `t_end`.
- ✅ Only one block plays at a time.

**2. Network verification**

- Open browser DevTools → Network.
- ✅ Media requests show `206 Partial Content` with `Content-Range`.

**3. Multiple segments**

- ✅ Playing different blocks stops previous playback.
- ✅ No memory leaks (check Elements tab for `<audio>` count).

---

## Troubleshooting

**Issue: "Failed to load markdown"**

- Likely CASE_ROOT misconfigured.
- Check path: `echo $CASE_ROOT`.

**Issue: Audio doesn’t play**

- Check Network tab → `/media` request must succeed.
- Ensure ffmpeg installed.

**Issue: Playback doesn’t stop at t_end**

- Check `mediaManager.playSegment()` attaches `timeupdate` listener.

**Issue: Placeholder never updates**

- Check server logs for Python errors.
- Verify venv activated + `faster-whisper` installed.

---

## Model Sizes

Whisper model tradeoffs:

| Model  | Speed     | Accuracy | Use Case       |
| ------ | --------- | -------- | -------------- |
| tiny   | Fast      | Low      | Quick tests    |
| base   | Med       | Good     | Default        |
| small  | Slower    | Better   | Higher quality |
| medium | Slow      | Best     | Legal use      |
| large  | Very slow | Best     | Archival       |

---

## Future Enhancements

- Progress API (status + percent complete).
- UI progress indicator.
- Multi-speaker diarization.
- Batch uploads + job queue.
- Retry + error recovery.
- Subtitle export (`.srt`, `.vtt`).

---

## History

This guide consolidates and supersedes:

- `AV_TESTING_GUIDE.md`
- `AV_TRANSCRIPTION_AND_VIEW_FIX.md`
- `AV_UI_INTEGRATION_FIX.md`
- `AV_UI_INTEGRATION.md`
- `AV_UPLOAD_TRANSCRIPTION.md`

Older files may be archived under `docs/devnotes/` for reference.

---

**Status:** ✅ Core A/V ingestion and playback pipeline complete. Ready for production with future enhancements pending.
