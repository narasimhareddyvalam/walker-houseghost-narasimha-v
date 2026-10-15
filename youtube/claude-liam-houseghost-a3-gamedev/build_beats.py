"""Build beat_sheet.json for the Assignment 3 film from SCRIPT.md.

Every narrated line is taken verbatim from SCRIPT.md (each paragraph of Liam's narration
becomes one beat), so the film cannot drift from the approved script. Visuals are real
repository evidence: screenshots, captures, renders and verbatim source excerpts.

    python3 youtube/claude-liam-houseghost-a3-gamedev/build_beats.py

Images used by Remotion compositions are read from
brutalist.art/runtime/remotion/public/houseghost-a3/ (copies of the files named below).
"""

import json, re, subprocess
from pathlib import Path

REEL = Path(__file__).resolve().parent
REPO = REEL.parent.parent
GODOT = REPO / "godot"
TITLE = "Building Three Game Props with Claude, Blender MCP and Godot"
SLUG = "claude-liam-houseghost-a3-gamedev"
IMG = "houseghost-a3/"
WPS = 2.6   # words per second, for estimates only; the measured audio is the clock


def script_paras():
    s = (REEL / "SCRIPT.md").read_text()
    out = {}
    for sec in re.split(r"\n## ", s)[1:]:
        key = sec.split(" ", 1)[0]
        out[key] = re.findall(r"“([^”]+)”", sec)
        out[key + ":quote"] = re.findall(r"^> (.+)$", sec, re.M)
    return out


def lines(path, start, end):
    text = (REPO / path).read_text().splitlines()
    return "\n".join(text[start - 1:end])


def find_lines(path, first, count):
    text = (REPO / path).read_text().splitlines()
    i = next(k for k, l in enumerate(text) if first in l)
    return i + 1, i + count, "\n".join(text[i:i + count])


P = script_paras()


def narr(key, i):
    return P[key][i]


def est(text):
    return round(max(4.0, len(text.split()) / WPS), 2)


def figure(title, status, image, label, source, cards, excerpt=""):
    return {"type": "GRAPHIC", "source": "remotion", "motion": "figure",
            "remotion": {"pattern": "GodotDesignFigure", "props": {
                "title": title, "status": status, "image": IMG + image, "imageLabel": label,
                "excerpt": excerpt, "source": source, "cards": cards}}}


def trace(title, source, output, path="", label="Command output", notes=None):
    """Lines in the workbench's large list panel; facts in the notes column beside it."""
    return {"type": "GRAPHIC", "source": "remotion", "motion": "code",
            "remotion": {"pattern": "GodotDevWorkbench", "props": {
                "mode": "trace", "title": title, "project": "HOUSEGHOST — Assignment 3",
                "path": path, "source": source, "treeLabel": label, "tree": output,
                "inspectorLabel": "What it shows", "notes": notes or []}}}


def clip(capture, label):
    return {"type": "source-cut", "source": "own", "capture": capture,
            "capture_kind": label, "show": [{"at": "0.00", "event": "label: " + label}],
            "evidence_media": None}


beats = []


def add(bid, act, text, shot, note=""):
    b = {"beat_id": bid, "act": act, "role_note": note, "narration_text": text,
         "shot": shot, "estimated_duration_s": est(text) if text else 9.0}
    beats.append(b)
    return b


# ---- Bookends -------------------------------------------------------------------
composer = " ".join(P["Bookend:quote"]) if "Bookend:quote" in P else ""
b00_cmd = re.search(r"## Bookend 1.*?\n> (.+?)\n", (REEL / "SCRIPT.md").read_text(), re.S).group(1)
b00 = add("B00", "ASK", "", {"type": "GRAPHIC", "source": "remotion", "motion": "type-on",
    "remotion": {"pattern": "ClaudeComposerAsk", "props": {
        "greeting": "Namaste, Liam", "topic": "CLAUDE CODE · BLENDER MCP · GODOT 4.7",
        "segment": "Building Three Game Props", "command": b00_cmd}}},
    "Reconstruction of the Claude composer; the opening prompt, typed, no narration")
b00["audio_policy"] = "silence"
b00["silent"] = True

add("B01", "ASK",
    "Three objects from a remembered bedroom. Designed to a scale, built through a live Blender "
    "session, revised by eye, and tested in Godot. The numbers tell me whether they arrived "
    "correctly. The scene tells me whether they read correctly.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "type-on",
     "remotion": {"pattern": "ClaudeVerdictArtifact", "props": {
         "artifactTitle": "What got built", "artifactHeading": "Three props from a remembered bedroom",
         "artifactLines": ["Designed to a scale, built through a live Blender session.",
                           "Revised by eye, and tested in Godot.",
                           "The numbers tell me whether they arrived correctly.",
                           "The scene tells me whether they read correctly."]}}},
    "Hesitant-writer summary, read aloud from SCRIPT.md Bookend 2 (its struck line omitted)")

# ---- B01 Open on the result --------------------------------------------------------
add("B02", "RESULT", narr("B01", 0), clip("capture/godot-showcase-orbit-4k.mp4",
    "Godot engine capture — scripted camera, native 4K"))
add("B03", "RESULT", narr("B01", 1), figure("Three props, one remembered room",
    "My A2 art — the room they come from", "env_room_memory.png", "env_room_memory.png",
    "godot/assets/art/env_room_memory.png", [{"label": "Music box", "text": "the first relic"},
    {"label": "Lamp", "text": "the warm light"}, {"label": "Bookshelf", "text": "solid only in memory"}]))

# ---- B02 The game defines the props ------------------------------------------------
add("B04", "GAME", narr("B02", 0), figure("A room in two states", "My A2 art",
    "env_room_memory.png", "the remembered bedroom", "godot/assets/art/env_room_memory.png",
    [{"label": "Game", "text": "side-on 2D, Godot 4.7"}, {"label": "Verb", "text": "turn the world over"}]))
add("B05", "GAME", narr("B02", 1), figure("Each prop has a job", "Captured in my Blender session via the MCP — final versions",
    "final-musicbox-4view.png", "final music box", "stills/final-musicbox-4view.png",
    [{"label": "Music box", "text": "calls from out of reach"}, {"label": "Lamp", "text": "warmth of memory"},
     {"label": "Bookshelf", "text": "blocks the way"}]))
add("B06", "GAME", narr("B02", 2), figure("A separate 3D showcase", "Godot render",
    "a3-showcase.png", "godot/scenes/AssetShowcase.tscn", "evidence/a3-showcase.png",
    [{"label": "Scene", "text": "floor, one light, camera"}, {"label": "Not claimed", "text": "integrated into the 2D game"}]))

# ---- B03 Define the target ---------------------------------------------------------
add("B07", "BRIEF", narr("B03", 0), trace("One metre is 250 pixels", "CHANGE-BRIEF.md — scale table (Repository file)",
    ["His collision capsule — 250 px — 1.00 m",
     "Bookshelf collider — 150 × 250 px — 0.60 × 1.00 m",
     "Floor to ceiling, interior — 800 px — 3.20 m",
     "The door — ~609 px — 2.44 m"], "CHANGE-BRIEF.md", "CHANGE-BRIEF.md — scale table",
    [{"label": "Scale", "value": "250 px = 1 m"}, {"label": "Anchor", "value": "the 1.00 m collider"}]))
add("B08", "BRIEF", narr("B03", 1), trace("The art disagrees with itself", "CHANGE-BRIEF.md — correction, 2026-10-15 (Repository file)",
    ["Brief, as written — sprite 320 px — 1.28 m",
     "Measured, standing — figure 341 px — 1.36 m (char_remembered.png)",
     "Walking frames — 303–317 px — about 1.27 m"], "CHANGE-BRIEF.md", "CHANGE-BRIEF.md — correction",
    [{"label": "Scale", "value": "unchanged"}, {"label": "Why", "value": "anchored on the collider, not the drawing"}]))
add("B09", "BRIEF", narr("B03", 2), trace("Seven predictions, committed first", "CHANGE-BRIEF.md — committed 722658f, 2026-10-14 17:48, before any build (Repository file)",
    ["1 — lying on its side", "2 — wrong by ×10 or ×100", "3 — origin in the middle", "4 — over-building",
     "5 — colour lost in export", "6 — MCP connects but cannot drive", "7 — right by every number, still wrong"],
    "CHANGE-BRIEF.md", "CHANGE-BRIEF.md — predicted failures",
    [{"label": "Committed", "value": "722658f · 2026-10-14 17:48"}, {"label": "Before", "value": "any model was built"}]))

# ---- B04 Real Blender connection ---------------------------------------------------
add("B10", "MCP", narr("B04", 0), figure("Learning the window first", "My screenshot",
    "a3-blender-window.png", "my Blender session, BS_Shelf_Mid selected", "evidence/a3-blender-window.png · BLENDER-NOTES.md",
    [{"label": "Viewport · Toolbar", "text": "look · interact"}, {"label": "Outliner", "text": "objects"},
     {"label": "Properties · Sidebar", "text": "materials · exact transforms"}, {"label": "Mode", "text": "object vs mesh"}]))
add("B11", "MCP", narr("B04", 1), trace("Connected is not controlling", "get_scene_info — first call, before any build (Command output)",
    ["Scene 'Scene' | 1 camera, 1 light, 1 mesh | active Cube | mode OBJECT",
     "(unsaved) | engine BLENDER_EEVEE | 1920x1080 | unit scale 1.0",
     "Cube   | mesh   | at (0.0, 0.0, 0.0)     | size 2.0x2.0x2.0",
     "Light  | light  | at (4.08, 1.01, 5.9)   | point 1000.0W",
     "Camera | camera | at (7.36, -6.93, 4.96) | rot (64, 0, 47)"], "", "get_scene_info",
    [{"label": "Proves", "value": "the MCP reads my live session"}, {"label": "When", "value": "before any build"}]))
add("B12", "MCP", narr("B04", 2), figure("Local only, generators off", "My screenshot",
    "a3-mcp-panel-own.png", "MCP for Blender: connected on port 9876; libraries and generators off",
    "evidence/a3-mcp-panel-own.png · lsof: Blender TCP 127.0.0.1:9876 (LISTEN)",
    [{"label": "Socket", "text": "127.0.0.1:9876"}, {"label": "Libraries", "text": "all off"},
     {"label": "Generators", "text": "all off"}]))

# ---- B05 Directing the build -------------------------------------------------------
add("B13", "BUILD", narr("B05", 0), figure("A prompt, and its plan", "My screenshot",
    "a3-prompt-to-claude-own.png", "“yes go ahead with the bookshelf”", "evidence/a3-prompt-to-claude-own.png",
    [{"label": "Plan", "text": "six boards"}, {"label": "Budget", "text": "296 / 360 tris"}]))
add("B14", "BUILD", narr("B05", 1), figure("What it built", "Captured in my Blender session via the MCP",
    "a3-prompt-result-bookshelf-a3-5.png", "the bookshelf that prompt produced (A3-5)",
    "evidence/a3-prompt-result-bookshelf-a3-5.png",
    [{"label": "Per object", "text": "one execute_blender_code call"}, {"label": "Then", "text": "get_scene_info reads it back"}]))
add("B15", "BUILD", narr("B05", 2), clip("capture/blender-bookshelf-turntable.mp4",
    "Capture of my Blender session — camera driven via the MCP"))

# ---- B06 Music box -----------------------------------------------------------------
add("B16", "MUSICBOX", narr("B06", 0), clip("capture/blender-musicbox-turntable.mp4",
    "Capture of my Blender session — camera driven via the MCP"))
add("B17", "MUSICBOX", narr("B06", 1), figure("A reference, not a mesh", "ChatGPT reference — image only",
    "ref-musicbox-chatgpt.png", "read for what six shapes can build", "design/ref-musicbox-chatgpt.png",
    [{"label": "Hollow body", "text": "darker cavity"}, {"label": "Plinth", "text": "the sixth shape"},
     {"label": "Key", "text": "bow in the shaft plane"}]))
s, e, _ = find_lines("tools/blender/build_musicbox.py", "inset = bmesh.ops.inset_individual", 4)
ex = "inset_individual(thickness=0.006) → extrude_face_region → translate(z −0.10)"
add("B18", "MUSICBOX", narr("B06", 2), figure("Twelve-millimetre walls", "Captured in my Blender session via the MCP",
    "a3-stats-musicbox.png", "Blender statistics: 124 / 312 triangles", f"abbreviated from tools/blender/build_musicbox.py lines {s}–{e}",
    [{"label": "Walls", "text": "12 mm"}, {"label": "Cavity", "text": "10 cm deep"}, {"label": "Triangles", "text": "312 / 320"}], ex))

# ---- B07 Lamp ----------------------------------------------------------------------
add("B19", "LAMP", narr("B07", 0), clip("capture/blender-lamp-turntable.mp4",
    "Capture of my Blender session — camera driven via the MCP"))
add("B20", "LAMP", narr("B07", 1), figure("One scene light", "ChatGPT reference — image only",
    "ref-lamp-chatgpt.png", "the modern reference", "design/ref-lamp-chatgpt.png",
    [{"label": "Scene", "text": "exactly one light"}, {"label": "Glow", "text": "in the shade material"}]))
s, e, _ = find_lines("tools/blender/asset_lib.py", '"M_Shade_Cream":', 2)
ex = '"M_Shade_Cream": {"hex": "#F0DCA8", …, "emission": 0.4}'
add("B21", "LAMP", narr("B07", 2), figure("Emission 1.0 → 0.4", "Godot render",
    "a3-showcase.png", "the final lamp, cream restored", f"abbreviated from tools/blender/asset_lib.py lines {s}–{e}",
    [{"label": "Before", "text": "clipped to white"}, {"label": "After", "text": "cream visible"}], ex))

# ---- B08 Bookshelf -----------------------------------------------------------------
add("B22", "BOOKSHELF", narr("B08", 0), figure("Six boards, rounded corners", "ChatGPT reference — image only",
    "ref-bookshelf-chatgpt.png", "the modern reference", "design/ref-bookshelf-chatgpt.png",
    [{"label": "Boards", "text": "six"}, {"label": "Detail", "text": "rounded top corners"}]))
s, e, _ = find_lines("tools/blender/build_bookshelf.py", "bmesh.ops.bevel(bm, geom=top_corners", 2)
ex = "bevel(top_corners, offset=0.03, segments=4) — before the front-edge bevel"
add("B23", "BOOKSHELF", narr("B08", 1), figure("Order of operations", "Captured in my Blender session via the MCP — final version",
    "final-bookshelf-4view.png", "side view: the rounded corners", f"abbreviated from tools/blender/build_bookshelf.py lines {s}–{e}",
    [{"label": "Cause", "text": "bevel order"}, {"label": "Fix", "text": "round the corners first"}], ex))
add("B24", "BOOKSHELF", narr("B08", 2), trace("A test that measures what it means", "tools/blender/build_bookshelf.py — side_bm() assertion (Command output)",
    ["rounded corners: 2 | front edges: 2 | front face top z = 0.9700 (expect 0.9700)",
     "first run: AssertionError — local height compared with world height",
     "fixed: world height = local z + 0.5"], "", "side_bm() — the rounding assertion",
    [{"label": "Asserts", "value": "front face stops 3 cm below the top"}]))

# ---- B09 Hand edit -----------------------------------------------------------------
add("B25", "HANDEDIT", narr("B09", 0), figure("Before my edit", "Captured in my Blender session via the MCP",
    "a3-hand-edit-before.png", "two shelves and a back panel — 248 triangles", "evidence/a3-hand-edit-before.png",
    [{"label": "Edit", "text": "by hand, with the mouse"}]))
add("B26", "HANDEDIT", narr("B09", 1), figure("What the edit taught me", "My screenshots",
    "hand-edit-own-trio.png", "duplicate with its parent · drift on every axis · a seventh board",
    "evidence/a3-hand-edit-attempt-duplicate.png · a3-hand-edit-during-own.png · a3-hand-edit-third-shelf-own.png",
    [{"label": "Shift+D", "text": "copies the parent too"}, {"label": "Free drag", "text": "moves every axis"},
     {"label": "Copies", "text": ".001 names and materials"}]))
add("B27", "HANDEDIT", narr("B09", 2), figure("After my edit", "Captured in my Blender session via the MCP — same camera",
    "a3-hand-edit-after.png", "three shelves, open back — 280 triangles", "evidence/a3-hand-edit-after.png",
    [{"label": "Boards", "text": "six"}, {"label": "Triangles", "text": "280 / 360"}]))

# ---- B10 Export and the headless check ---------------------------------------------
add("B28", "CHECK", narr("B10", 0), trace("Read the exported file itself", "python3 tools/inspect_glb.py — bookshelf.glb (Command output)",
    ["asset: Khronos glTF Blender I/O v5.2.40 | up axis: glTF is always +Y up",
     "node BS_Shelf_Bottom translation [0, 0.12, 0.0015] | no rotation, no scale",
     "size x 0.64 | y (up) 1.0 | z 0.3 | lowest point y = 0.0",
     "triangles 280",
     "material M_Wood_Dark base #4A2E19 · M_Wood_Warm base #6B4428"], "", "tools/inspect_glb.py — bookshelf.glb",
    [{"label": "Format", "value": "binary glTF, +Y up"}, {"label": "Reader", "value": "no Blender, no Godot"}]))
b10 = P["B10"][1]
cut = b10.index("Here are the results")
code_start, code_end = 82, 95
add("B29", "CHECK", b10[:cut].strip(), {"type": "GRAPHIC", "source": "remotion", "motion": "code",
    "remotion": {"pattern": "GodotDevWorkbench", "props": {
        "mode": "code", "title": "Compose the transforms yourself", "project": "HOUSEGHOST — Assignment 3",
        "path": f"godot/tests/check_assets.gd:{code_start}",
        "source": f"godot/tests/check_assets.gd lines {code_start}–{code_end} · verbatim · Reconstruction",
        "code": lines("godot/tests/check_assets.gd", code_start, code_end), "startLine": code_start,
        "codeFontSize": 28,
        "notes": [{"label": "Why", "value": "global_transform is identity outside the tree"},
                  {"label": "Checks", "value": "size · scale · up axis · lowest point"}]}}})
add("B30", "CHECK", b10[cut:].strip(), dict(trace("Headless check — not a visual check",
    "timeout 120 godot --headless --path godot --script res://tests/check_assets.gd (Command output)",
    ["MusicBox — brief 0.316 × 0.297 × 0.190 m — Godot 0.3160 × 0.2968 × 0.1900",
     "BedsideLamp — brief 0.28 × 0.42 × 0.28 m — Godot 0.2800 × 0.4200 × 0.2800",
     "Bookshelf — brief 0.64 × 1.00 × 0.30 m — Godot 0.6400 × 1.0000 × 0.3000",
     "every node scale 1, 1, 1 · height along Y · lowest point 0.0000",
     "RESULT: PASS (0 failures) · exit 0"], "", "Headless — W × H × D, metres",
    [{"label": "Tolerance", "value": "2 mm"}, {"label": "Not", "value": "a visual check"}]), evidence_media="media/B30.mp4"))
add("B31", "CHECK", narr("B10", 2), trace("A check must be able to fail", "check_assets.gd against a deliberately wrong height (Command output)",
    ["FAIL: Bookshelf: size differs from the brief by more than 2 mm",
     "FAIL: Bookshelf: height does not lie along Y (lying on its side?)",
     "RESULT: FAIL (2 failures) · exit 1",
     "What it cannot prove: how an asset looks · contact with a floor"], "", "check_assets.gd — negative test",
    [{"label": "Proves", "value": "the check can fail"}]))

# ---- B11 The assets in Godot -------------------------------------------------------
b11 = P["B11"][0]
cut = b11.index("I briefly placed")
add("B32", "GODOT", b11[:cut].strip(), {"type": "GRAPHIC", "source": "remotion", "motion": "code",
    "remotion": {"pattern": "GodotDevWorkbench", "props": {
        "mode": "code", "title": "The whole scene", "project": "HOUSEGHOST — Assignment 3",
        "path": "godot/scenes/AssetShowcase.tscn:44",
        "source": "godot/scenes/AssetShowcase.tscn lines 44–66 · verbatim · Reconstruction",
        "code": lines("godot/scenes/AssetShowcase.tscn", 44, 66), "startLine": 44, "codeFontSize": 24,
        "notes": [{"label": "Lights", "value": "exactly one"},
                  {"label": "Assets", "value": "three .glb instances"}]}}})
r = add("B33", "GODOT", b11[cut:].strip(), clip("capture/godot-showcase-orbit-4k.mp4",
    "Godot engine capture — scripted camera, native 4K"))
r["shot"]["evidence_media"] = "media/B33.mp4"
add("B34", "GODOT", narr("B11", 1), figure("Lit for the materials", "My screenshots",
    "a3-godot-editor-own.png", "the scene open in my Godot editor", "evidence/a3-godot-editor-own.png",
    [{"label": "Renderer", "text": "Compatibility"}, {"label": "Brass", "text": "needs a sky to reflect"}]))
add("B35", "GODOT", narr("B11", 2), figure("Behind, below, at an angle", "My screenshots",
    "orbit-own-grid.png", "my orbit check: rear · bottom · angled, for each asset", "evidence/a3-orbit-*-own.png",
    [{"label": "Bookshelf", "text": "reads correctly"}, {"label": "Lamp", "text": "reads correctly"},
     {"label": "Music box", "text": "from behind, a box"}]))

# ---- B12 Verdict ---------------------------------------------------------------------
verdict = [
    ("Built", "Three game-scale props", ["Music box — 312 triangles.", "Lamp — 406 triangles.", "Bookshelf — 280 triangles.", "Built live in Blender, exported as .glb, shown in Godot."]),
    ("Verified", "What the checks agree on", ["Size, orientation, origin, scale and colour.", "Across Blender, the exported files and Godot.", "Plus renders and my own look: behind, below, at an angle.", "Not certified: every lighting condition."]),
    ("Revised", "What changed, and why", ["A music box rebuilt with real presence.", "A lamp redesigned; its shade un-clipped.", "The bookshelf's rounded corners recovered.", "Claude's errors kept in the test report."]),
    ("Roles", "Who did what", ["Me: the brief, the designs, approvals, the hand edit,", "the visual judgement and the trade-offs.", "Claude: the modelling and checking code,", "run under that direction, outputs preserved."]),
    ("Still uncertain · Next", "What remains open", ["The props in the game's own room lighting.", "The music box from behind.", "Another viewer's reading of the scene.", "Next: a rear silhouette within six shapes."]),
    ("Source", "The demonstrated revision", ["Game source: commit d331a4a.", "Tag a3 on GitHub; SHA in SUBMISSION.md.", "Footage: CAPTURE.md, with SHA-256 per file."]),
]
for k, (title, heading, ls_) in enumerate(verdict):
    add(f"B{36 + k}", "VERDICT", P["B12"][k].replace("d331a4a", "d, 3, 3, 1, a, 4, a"), {"type": "GRAPHIC", "source": "remotion", "motion": "verdict-panel",
        "remotion": {"pattern": "ClaudeVerdictArtifact", "props": {
            "artifactTitle": title, "artifactHeading": heading, "artifactLines": ls_}}})

# ---- B13 Your Turn, Outro ----------------------------------------------------------
yt = re.search(r"## B13.*?\n> (.+?)\n", (REEL / "SCRIPT.md").read_text(), re.S).group(1)
add("B42", "YOUR_TURN", P["B13"][0], {"type": "GRAPHIC", "source": "remotion", "motion": "prompt-card",
    "remotion": {"pattern": "ClaudeComposerAsk", "props": {
        "greeting": "Your turn.", "topic": "ONE BOUNDED CHANGE", "segment": "Predict First, Then Test",
        "command": yt}}})
o = add("B43", "OUTRO", f"{TITLE}. At Nik Bear Brown.", {"type": "GRAPHIC", "source": "remotion",
    "component": "ClaudeTitleOutro", "remotion": {"pattern": "ClaudeTitleOutro", "props": {
        "title": TITLE, "slug": SLUG}}})
o["kind"] = "outro_voice"

# Source clips: compile reads media/<beat>.mp4, prepared by prepare_clips.py.
for b in beats:
    if b["shot"]["type"] == "source-cut":
        b["shot"]["evidence_media"] = f"media/{b['beat_id']}.mp4"

sheet = {"metadata": {
    "title": TITLE, "slug": SLUG,
    "topic": "Three 3D props for HOUSEGHOST, built with Claude through the Blender MCP and checked in Godot",
    "kind": "godot-gamedev", "mode": "walker", "brand": "claude", "audience": "developers and game design students",
    "register": "teardown", "engine": "kokoro", "voice": "am_onyx", "voice_kokoro": "am_onyx",
    "aspect_ratio": "16:9", "captions": False, "channel_title": "Nik Bear Brown", "channel": "@NikBearBrown",
    "presenter": "Liam", "persona": "liam-in-for-bear", "author": "Narasimha Reddy Valam",
    "game": "HOUSEGHOST — Assignment 3 props", "godot_version": "4.7.2.stable.official.ed1daf0bf",
    "blender_version": "5.2.2 LTS", "mcp": "mcp-for-blender 2.1.9 (add-on 1.8)",
    "teaching_contract": "code-then-result-v1", "script": "SCRIPT.md"}, "beats": beats}
# Keep measured narration when a beat's words are unchanged: the audio is the clock, and
# regenerating identical speech would only churn the files.
old_path = REEL / "beat_sheet.json"
if old_path.exists():
    prev = {b["beat_id"]: b for b in json.loads(old_path.read_text())["beats"]}
    for b in beats:
        o = prev.get(b["beat_id"])
        if o and o.get("narration_text") == b["narration_text"]:
            for k in ("actual_duration_s", "audio_file", "voice", "audio_sha256"):
                if k in o:
                    b[k] = o[k]
        # Likewise keep the renderer's stamp while the composition it rendered is unchanged.
        ro, rn = (o or {}).get("shot", {}).get("remotion"), b["shot"].get("remotion")
        if ro and rn and "rendered" in ro and {k: v for k, v in ro.items() if k != "rendered"} == rn:
            rn["rendered"] = ro["rendered"]
old_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
words = sum(len(b["narration_text"].split()) for b in beats)
print(f"{len(beats)} beats · {words} narrated words · ~{words / WPS / 60:.1f} min estimated")
