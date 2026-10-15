# HOUSEGHOST — Three 3D Props with Claude, the Blender MCP and Blender

**Film script, DRAFT for review** · `godot-gamedev walker` · Narrator: Liam, Teardown register
**Course:** CSYE 7270 Assignment 3 · **Author:** Narasimha Reddy Valam
**Tools shown:** Blender 5.2.2 LTS · `mcp-for-blender` 2.1.9 (add-on 1.8) · Godot 4.7.2.stable · Claude Code (Claude Opus 5.5)
**Frame:** 3840×2160 landscape, 30 fps
**Source revision shown:** filled at render time from the submitted commit, and shown on screen in the Verdict

Every claim below is drawn from the repository, a recorded command output or one of the
screenshots in `evidence/`. Every image on screen carries one of four labels:
**"My screenshot"** (taken by me), **"Captured in my Blender session via the MCP"**,
**"Godot render"**, or **"Reconstruction"** (an editor or composer view rebuilt for teaching,
with its source file and line numbers). Nothing is presented as live footage that is not.

---

## Assignment requirements → where the film meets them

| Requirement (Assignment 3, §4) | Beat |
|---|---|
| Identifies the game, the three assets and why the game needs each | B01, B02 |
| Shows my real Blender session — my own screenshots, labelled | B03, B04, B08, throughout |
| Shows at least one prompt to Claude and what it built | B04 |
| Shows my own hand edit | B08 |
| Shows the three assets in the running Godot scene | B10 |
| Shows the headless numbers beside my brief, labelled as headless | B09 |
| States what I checked, what remains uncertain, what Claude got wrong, one next step, the human and AI contributions, and the source revision shown | B11 |
| Walker opening / summary, then Verdict → Your Turn → regular outro | Bookends 1–2, B11, B12, outro |

---

## Bookend 1 — Claude composer

*Visual: the Claude composer, typing at reading speed. Labelled **Reconstruction**. No narration.*

> Please use Walker to convert my game design document about HOUSEGHOST into three 3D props
> for its remembered bedroom — the wind-up music box that is the first relic, the bedside lamp
> that makes the room feel safe, and the bookshelf that is solid only in the memory. Build them
> from Blender primitives through the Blender MCP, at true scale against the boy, export them to
> Godot, and check that they arrived the size, the way up and the scale I specified.

---

## Bookend 2 — Hesitant-writer summary

*Visual: plain text composing, one word corrected in place.*

> Three props for a 2D ghost story, built from primitives in Blender and verified in Godot —
> by script, by the numbers, and by ~~hand~~ **eye**.

---

## B01 — The game, and why it needs three 3D props

*Visual: my A2 art, `env_room_memory.png`, the music box on its shelf and the lamp beside the bed
highlighted in turn. Then the three finished assets, side by side. Labelled **Godot render**.*

**Liam:** "HOUSEGHOST is a side-on 2D Godot game. You play the ghost of a boy the world believes
ran away, in the bedroom a new family has emptied out. Turn the room over and it becomes the room
he remembers — warm, lamplit, his things back where they were."

"This assignment adds three objects from that remembered room, as real 3D models a Godot 3D scene
can use. Each one is chosen because the game already depends on it."

"The **music box** is the first relic: visible from the spawn point, out of reach from the floor,
calling every few seconds. It is the whole of the slice's tutorial. The **bedside lamp** is the
warm light that makes the remembered world read as safe. And the **bookshelf** is solid only in
the memory — in the stripped room it is not there — so it is one half of the mechanic that forces
you to turn the world over."

---

## B02 — The scale, and a brief written before anything was built

*Visual: `CHANGE-BRIEF.md`, the scale table, then the seven-prediction table, with the commit
hash and time beside it. Labelled **Repository file**.*

**Liam:** "A 2D game has no metres, so the first decision was a scale. The brief anchors it on the
player: his collision capsule is 250 pixels tall, so 250 pixels is one metre. That makes the
in-game bookshelf collider exactly one metre — the height of the capsule, which is why it stops him."

"The art does not fully agree with itself. The door implies closer to 300 pixels a metre, and when
we later placed the boy in the 3D scene, measuring his standing drawing showed it is 341 pixels —
1.36 metres, not the 1.28 the brief had quoted. The scale held, because it was anchored on the
collider, not the drawing. The brief now carries that correction."

"The brief was committed at commit `722658f` before Claude built anything, with seven predicted
failure cases and the check for each — lying on its side, wrong by a factor of ten, origin in the
middle, over-building, colour lost in export, an MCP that connects but cannot drive Blender, and
assets that are right by every number and still look wrong. All seven now have an outcome recorded
against them, whatever it was."

---

## B03 — Does the MCP actually drive Blender?

*Visual: the `get_scene_info` output from the first call — the unsaved default scene, cube, light,
camera at their default positions. Then the add-on panel and the `lsof` line showing
`127.0.0.1:9876`. Labelled **Command output** and **Repository file** (`FRICTIONAL.md`).*

**Liam:** "Prediction six was the one that would have stopped everything: the client reports
'connected' the moment a process starts, which says nothing about whether it can reach a running
Blender. So the first call was not a build. It was `get_scene_info`, and it came back with the
unsaved default scene — a two-metre cube at the origin, the light and camera at their stock
positions. Only a live session reports that."

"The add-on listens on 127.0.0.1, port 9876 — localhost only, checked with `lsof` rather than
taken from the panel, because the socket has no authentication. Every download and generation
service stayed off. No model in this film was generated, downloaded or imported."

---

## B04 — A prompt to Claude, and what it built

*Visual, phase 1: `a3-prompt-to-claude-own.png` — the prompt "yes go ahead with the bookshelf" and
Claude's build plan. Labelled **My screenshot**. Hold long enough to read the parts table.*
*Visual, phase 2: `a3-prompt-result-bookshelf-a3-5.png` — the four views of that build. Labelled
**Captured in my Blender session via the MCP**.*

**Liam:** "This is the working loop. Claude proposes a build in numbers — here, six boards, each
with its size, bevel, material and triangle count, totalling 296 of a 360 budget — and nothing
runs until it is approved."

"Then one `execute_blender_code` call per object, and after every one, `get_scene_info` reads
back the location, size, rotation and scale. Every mesh is built at its final size and angle in
`bmesh`, so no object ever carries a rotation or scale that needs applying."

"Every call body is kept, verbatim, at the end of the asset's build script in `tools/blender`. And
each script rebuilds its asset headless from an empty scene, so the `.blend` file is reproducible,
not just saved."

---

## B05 — The music box: from too simple to a hollow box on a plinth

*Visual, phase 1: the first build — five shapes, the lid ajar at 18°. Labelled **Captured in my
Blender session via the MCP**. Then `design/ref-musicbox-chatgpt.png`, labelled **ChatGPT
reference (image only)**.*

**Liam:** "The first music box met its brief exactly: five primitives, 252 triangles, the lid ajar at
eighteen degrees. I wanted more from it — something that would read as realistic."

"Within the assignment's rules — flat colour, no painted textures, at most six shapes and 500
triangles — realism has to come from shape and from light. So I generated a reference image in
ChatGPT and we read it for exactly what six primitives can build."

*Visual, phase 2: `build_musicbox.py`, `step_body`, the inset-and-extrude lines highlighted.
Labelled **Reconstruction** with file path and line numbers. Then `a3-stats-musicbox.png`.*

"The body became hollow: its top face inset to leave twelve-millimetre walls and pushed ten
centimetres down, the cavity in the darker wood. A plinth took the sixth shape. The lid opened to
seventy degrees and sits flush on its hinge. The key's bow was turned into the plane of its shaft, the way
a real butterfly key is made. 312 triangles, against a budget of 320."

"Face-weighted normals are baked into every flat-faced part, so a one-segment bevel catches light
like a rounded edge at no triangle cost."

---

## B06 — The lamp: one light, and a shade that clipped to white

*Visual, phase 1: the traditional A3-3 lamp, then `design/ref-lamp-chatgpt.png` (labelled
**ChatGPT reference (image only)**), then the modern A3-4 lamp. Labelled **Captured in my Blender
session via the MCP**.*

**Liam:** "The lamp was developed through two designs. The first followed the painting — a gourd base and
a cone shade. I chose a modern direction instead: a pill-shaped ceramic base, a brass collar and a
wide drum shade open underneath, in six shapes."

"The budget was raised from 340 triangles to 420 — before building, with the reason written into the
brief — because the rounded base alone costs 140. The neck runs fifteen millimetres through the top
of the shade and becomes the finial, so the finial costs no seventh shape."

"The scene is allowed exactly one light, so the lamp's glow comes from emission on the shade's
material, not from a second light."

*Visual, phase 2: `asset_lib.py`, the `M_Shade_Cream` entry, `"emission": 1.0` highlighted. Then the
first Godot render — the shade pure white. Then the edit to `0.4`. Then the second render, the cream
visible. Labelled **Reconstruction** and **Godot render**.*

"Godot's first render is where this was tuned. At emission 1.0 the lit cream exceeded white and the
tonemapper clipped it — exactly the kind of colour shift prediction five was written to catch. Lowering
it to 0.4 at the source restored the cream, and the lamp was rebuilt from its script and re-exported,
so the file, the script and the export stay in step."

---

## B07 — The bookshelf: every check passed, and the corners were square

*Visual, phase 1: `design/ref-bookshelf-chatgpt.png`. Labelled **ChatGPT reference (image only)**.
Then the first A3-7 views — square corners. Labelled **Captured in my Blender session via the MCP**.*

**Liam:** "The bookshelf's reference was modern and buildable: thick sides with rounded top corners,
rising above a top board set between them. Six boards."

"Every numeric check passed on the first build — and the visual review still caught that the
rounded corners had not formed. It is the reason this project checks with pictures as well as numbers."

*Visual, phase 2: `side_bm()` in `build_bookshelf.py`, the two bevel calls, reordered, and the new
assertion highlighted. Labelled **Reconstruction**. Then the rounded side profile.*

"The fix was the order of two operations: rounding the corners before softening the edges. A new
assertion now proves the rounding exists — the front face must stop at 0.97 metres — so it can never
silently disappear again."

---

## B08 — My hand edit: a third shelf

*Visual, in sequence, each labelled: `a3-hand-edit-before.png` (**Captured in my Blender session via
the MCP**), `a3-hand-edit-attempt-duplicate.png`, `a3-hand-edit-during-own.png`,
`a3-hand-edit-third-shelf-own.png` (each **My screenshot**), `a3-hand-edit-after.png` (**Captured in
my Blender session via the MCP**, same camera as "before").*

**Liam:** "One change had to be made by hand, with the mouse, in Blender's own window. I added a
third shelf: duplicate a shelf, drag the copy down to just above the floor."

"Doing it by hand taught me how Blender actually behaves. Duplicating with the parent selected
copies the parent too. Dragging the centre of the move gizmo moves on all three axes at once. And every
copy is named `.001` — objects, meshes, even materials. My screenshots record each of those, and each
one was then put right."

"A third shelf made seven boards against a limit of six, so I made the design trade: the back panel
came out, and the bookshelf is open-backed — which is what the brief first specified. The shelves sit at
my heights in even bays, in dark wood against the warm frame. The build script was updated to match, and
its headless rebuild equals the edited file object for object. 280 triangles."

---

## B09 — Export, and a check that failed every correct asset

*Visual, phase 1: `export_glb.py`, the exporter call with `export_yup=True` highlighted. Then
`inspect_glb.py` output: nodes with no rotation or scale, height on +Y, colours as hex. Labelled
**Reconstruction** and **Command output**.*

**Liam:** "Each asset exports as binary glTF with plus-Y up, headless, with `--python-exit-code 1`, so
any error stops the pipeline instead of passing silently."

"A small reader parses the exported files directly, with no Blender and no Godot. Every base colour
reads back as the exact hex in the brief, every node has no rotation and no scale, and height lies
on plus-Y."

*Visual, phase 2: `check_assets.gd`, the `_walk` function, labelled **Reconstruction**. Then the
headless output beside the brief, in a table titled **Headless check — not a visual check**:*

| Asset | Brief (m) | Godot, headless (m) |
|---|---|---|
| MusicBox | 0.316 × 0.297 × 0.190 | 0.3160 × 0.2968 × 0.1900 |
| BedsideLamp | 0.28 × 0.42 × 0.28 | 0.2800 × 0.4200 × 0.2800 |
| Bookshelf | 0.64 × 1.00 × 0.30 | 0.6400 × 1.0000 × 0.3000 |

"In Godot, a headless script loads each asset and prints its bounding box, every node's scale, the
axis its height lies along and its lowest point. The check itself was tested too: it composes each
part's transform explicitly, because Godot's `global_transform` is not valid before a node is in the
scene tree. It passes — all three within two millimetres of the brief, height along Y, lowest point at
zero, every scale one — and run against a deliberately wrong height, it fails, which proves it can."

"And what it does not prove is written at the top of the file: nothing about how an asset looks, and
nothing about contact with a floor."

---

## B10 — The running scene, and the check that had to be human

*Visual: `a3-showcase.png` (**Godot render**). Then `a3-godot-editor-own.png` and
`a3-godot-inspector-bookshelf-own.png` (**My screenshot**). Then the nine orbit screenshots,
rear / below / angled for each asset (**My screenshot**).*

**Liam:** "The scene is what the assignment asks for — a floor, one light, a camera, the three assets
side by side at game scale — with the boy himself beside them: his own sprite, at 250 pixels a metre,
1.36 metres tall, turning to face the camera. He is taller than the bookshelf that stops him, because
in the game it is his one-metre collider, not his drawing, that collides."

"The scene uses Godot's Compatibility renderer, matching the 2D game, and is lit for the materials:
a sky the brass and the glossy ceramic can reflect, soft shadows and filmic tonemapping."

"Then the check no script can run. I orbited every asset in the editor, from behind and from below.
The bookshelf reads as a bookshelf and the lamp as a lamp from every side. No holes, no missing faces,
and every colour right. The one improvement my review identified is the music box from directly behind,
where its key is small — recorded as my next step."

---

## B11 — Verdict

*Visual: five panels in turn, each a short list. The submitted commit hash on screen.*

**Liam:** "What was checked. Size, orientation, scale and origin — in Blender, in the exported files
and in Godot, and the three agree. Triangle counts in Blender's own statistics: 312, 406 and 280.
Imports without errors. And a human orbit of every asset."

"What remains open. How the props read inside the game's own lit room rather than a showcase, and a
review by someone other than me."

"What Claude got wrong: twelve issues, every one caught by our own checks before export and listed in
the test report — the most instructive being a bevel order that squared the bookshelf's corners, and a
Godot check that needed to compose its own transforms."

"One next step: give the music box a detail that reads from behind, inside the same six shapes."

"Who did what. I set the rules, chose the account the work is credited to, pushed the music box and the
lamp beyond their first versions, chose all three references, raised the lamp's budget, made the hand edit, chose
an open back over a seventh board, and made the orbit judgement. Claude wrote the build scripts and the
checks, drafted the prompts and the documents, and ran every step after I approved it. The source shown
is commit [submitted SHA], tagged `a3`."

---

## B12 — Your Turn

*Visual: the composer, `greeting: "Your turn."`, the prompt typed in. Labelled **Reconstruction**.*

> Please use Walker to make my music box read as a music box from behind. Propose one change that stays
> within six shapes and 320 triangles. Before building, predict whether it will read from behind and to
> the left in Godot. Then build it through the MCP, export it, run `check_assets.gd`, and orbit it.

**Liam:** "Your turn. Take one weakness your own eyes found, make one bounded change, and write down what
you expect before you run anything. Then check it the same two ways — with a script, and by looking.
That's it from me."

---

## Outro — locked card

*Visual: `ClaudeTitleOutro` — the exact title, @NikBearBrown, one mascot. Liam re-reads the title, then
"At Nik Bear Brown." No jingle, no game sound, no further narration.*

---

*Narration: roughly 1,800 words, about 11–12 minutes at Liam's pace; the final length follows the
measured audio.*
