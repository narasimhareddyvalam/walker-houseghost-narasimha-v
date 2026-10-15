"""Fit each recorded clip onto a 3840x2160 canvas with its evidence label, as media/<beat>.mp4.

The compiler would otherwise crop non-16:9 footage to fill the frame, cutting off the top and
bottom of the 2940x1846 Blender window recordings. Here each clip is scaled to fit whole,
centred on the film's cream ground, with its label in a strip underneath. Nothing inside the
recorded frame is altered. The compiler then retimes each clip to its narration.

    python3 youtube/claude-liam-houseghost-a3-gamedev/prepare_clips.py
"""

import json, subprocess
from pathlib import Path

REEL = Path(__file__).resolve().parent
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
W, H, LABEL_H = 3840, 2160, 150

from PIL import Image, ImageDraw, ImageFont

sheet = json.loads((REEL / "beat_sheet.json").read_text())
(REEL / "media").mkdir(exist_ok=True)
(REEL / "media" / "_labels").mkdir(exist_ok=True)
font = ImageFont.truetype(FONT, 58)
for b in sheet["beats"]:
    shot = b["shot"]
    if shot["type"] != "source-cut":
        continue
    src, label = REEL / shot["capture"], shot["capture_kind"]
    out = REEL / shot["evidence_media"]
    strip = Image.new("RGB", (W, LABEL_H), (0xF3, 0xEB, 0xDD))
    d = ImageDraw.Draw(strip)
    tw = d.textlength(label, font=font)
    d.text(((W - tw) / 2, (LABEL_H - 58) / 2 - 6), label, font=font, fill=(0x3B, 0x2E, 0x25))
    lab = REEL / "media" / "_labels" / f"{b['beat_id']}.png"
    strip.save(lab)
    fc = (f"[0:v]scale={W}:{H - LABEL_H}:force_original_aspect_ratio=decrease,"
          f"pad={W}:{H - LABEL_H}:(ow-iw)/2:(oh-ih)/2:color=0xF3EBDD,"
          f"pad={W}:{H}:0:0:color=0xF3EBDD[v];[v][1:v]overlay=0:{H - LABEL_H}[o]")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(src), "-i", str(lab),
                    "-filter_complex", fc, "-map", "[o]", "-an", "-c:v", "libx264", "-crf", "14",
                    "-pix_fmt", "yuv420p", "-preset", "slow", str(out)], check=True)
    print(b["beat_id"], "←", shot["capture"], "→", shot["evidence_media"])
