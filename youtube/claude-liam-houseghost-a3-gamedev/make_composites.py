"""Build the film's three composite stills from existing evidence images, into stills/ and the
Remotion public folder. Nothing inside any source image is altered; each is scaled and placed
with a caption saying what it is.

    python3 youtube/claude-liam-houseghost-a3-gamedev/make_composites.py
"""

import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REEL = Path(__file__).resolve().parent
REPO = REEL.parent.parent
PUBLIC = Path.home() / "Desktop/brutalist.art/runtime/remotion/public/houseghost-a3"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CREAM, INK, GAP = (243, 235, 221), (59, 46, 37), 24


def caption(img, text, size=44):
    f = ImageFont.truetype(FONT, size)
    strip = Image.new("RGB", (img.width, int(size * 2)), CREAM)
    d = ImageDraw.Draw(strip)
    d.text(((img.width - d.textlength(text, font=f)) / 2, size * 0.45), text, font=f, fill=INK)
    out = Image.new("RGB", (img.width, img.height + strip.height), CREAM)
    out.paste(img, (0, 0)); out.paste(strip, (0, img.height))
    return out


def side_by_side(left, right, h=1000):
    tiles = [caption(im.convert("RGB").resize((round(im.width * h / im.height), h), Image.LANCZOS), t)
             for im, t in (left, right)]
    out = Image.new("RGB", (sum(t.width for t in tiles) + GAP, tiles[0].height), CREAM)
    out.paste(tiles[0], (0, 0)); out.paste(tiles[1], (tiles[0].width + GAP, 0))
    return out


def save(img, name):
    (REEL / "stills").mkdir(exist_ok=True)
    img.save(REEL / "stills" / name)
    shutil.copy(REEL / "stills" / name, PUBLIC / name)
    print(name, img.size)


save(side_by_side((Image.open(REPO / "evidence/a3-prompt-result-bookshelf-a3-5.png"), "What this prompt built (A3-5)"),
                  (Image.open(REEL / "stills/final-bookshelf-4view.png"), "The approved final (A3-8)")),
     "compare-bookshelf.png")
save(side_by_side((Image.open(REPO / "design/ref-musicbox-chatgpt.png"), "ChatGPT reference — image only"),
                  (Image.open(REEL / "stills/final-musicbox-4view.png"), "My final build in Blender")),
     "compare-musicbox.png")

# Orbit check: each of my nine Godot screenshots cropped to the middle of its 3D viewport.
f = ImageFont.truetype(FONT, 40)
W, H = 1120, 520
grid = Image.new("RGB", (W * 3 + GAP * 2, H * 3 + GAP * 2), CREAM)
for i, (a, v) in enumerate((a, v) for a in ("bookshelf", "lamp", "musicbox") for v in ("rear", "bottom", "angled")):
    t = Image.open(REPO / f"evidence/a3-orbit-{a}-{v}-own.png").convert("RGB").crop((480, 380, 480 + W, 380 + H))
    d = ImageDraw.Draw(t)
    label = f"{'Music box' if a == 'musicbox' else a.capitalize()} selected · {v}"
    d.rectangle((0, 0, d.textlength(label, font=f) + 36, 64), fill=CREAM)
    d.text((18, 10), label, font=f, fill=INK)
    grid.paste(t, ((i % 3) * (W + GAP), (i // 3) * (H + GAP)))
save(grid, "orbit-own-grid.png")
