---
description: Fetch a YouTube video transcript and save it as a note in 01 Raw Sources/.
argument-hint: YouTube URL or video ID
allowed-tools: Bash, Write
---

Fetch a YouTube video transcript and save it as a note. $ARGUMENTS: YouTube URL or video ID.

Extract the video ID from $ARGUMENTS (handle full URLs, short URLs, and bare IDs).

Run this Python script to fetch the transcript and video title:
```bash
"$HOME/.venvs/claude/Scripts/python.exe" -c "
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse

arg = '$ARGUMENTS'.strip()
# Extract video ID from various URL formats
if 'v=' in arg:
    vid = urllib.parse.parse_qs(urllib.parse.urlparse(arg).query).get('v', [arg])[0]
elif 'youtu.be/' in arg:
    vid = arg.split('youtu.be/')[-1].split('?')[0]
else:
    vid = arg

transcript = YouTubeTranscriptApi().fetch(vid)
lines = []
for e in transcript:
    m, s = divmod(int(e.start), 60)
    h, m = divmod(m, 60)
    ts = f'{h}:{m:02d}:{s:02d}' if h else f'{m}:{s:02d}'
    lines.append(f'[{ts}] {e.text}')
print(f'VIDEO_ID={vid}')
print('TRANSCRIPT_START')
print('\n'.join(lines))
"
```

If the script fails with ImportError, run `uv pip install youtube-transcript-api --python "$HOME/.venvs/claude/Scripts/python.exe"` first, then retry.

From the output:
- Extract the video ID after `VIDEO_ID=`
- Extract all lines after `TRANSCRIPT_START` as the transcript text

Create the note at `01 Raw Sources/YouTube - {VIDEO_ID}.md` with this content:
```
---
source: https://www.youtube.com/watch?v={VIDEO_ID}
type: youtube-transcript
---

## Transcript

{transcript lines}
```

Then open it:
```bash
obsidian open path="01 Raw Sources/YouTube - {VIDEO_ID}.md"
```

Confirm with one line: "Saved transcript for `{VIDEO_ID}` → [[YouTube - {VIDEO_ID}]]". If Obsidian CLI fails, report it. If the video has no transcript available, say so clearly.
