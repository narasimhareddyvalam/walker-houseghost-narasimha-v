# HOUSEGHOST — Building Three Game Props with Claude, Blender MCP and Godot

**Film script — revised production draft** · `godot-gamedev walker` · Narrator: Liam, teardown register  
**Project:** HOUSEGHOST · **Developer:** Narasimha Reddy Valam  
**Tools shown:** Blender 5.2.2 LTS · `mcp-for-blender` 2.1.9 (add-on 1.8) · Godot 4.7.2.stable · Claude Code (Claude Opus 5.5)  
**Frame:** 3840 × 2160 landscape, 30 fps  
**Source revision:** Insert verified submitted source commit SHA at render time; show in Verdict.  
**Evidence rule:** Use only genuine screenshots, captured Blender MCP views, Godot renders and labelled reconstructions from the project. Do not depict reconstructed interaction as live footage. Do not imply a check proves more than it does.

---

## Film coverage map (production reference — not narrated)

| Required story element | Beat |
|---|---|
| Game, three props, purpose | B01–B02 |
| Original brief, dimensions, predictions | B03 |
| Real Blender session, MCP connection, prompt and result | B04–B05 |
| Model iterations and inspection | B06–B08 |
| Developer's own manual Blender edit | B09 |
| GLB export, headless measurements versus brief | B10 |
| Running Godot scene, human orbit and limits | B11 |
| What was checked, uncertainty, Claude's errors, roles, next step, source SHA | B12 |
| Walker opening/summary, Verdict → Your Turn → regular outro | Bookends, B12–B13, Outro |

---

## Bookend 1 — Claude composer

*Visual: Claude composer typing at readable speed. Label **Reconstruction**. No narration.*

> Use Walker to turn my HOUSEGHOST bedroom design into three simple 3D props: the wind-up music box, bedside lamp and memory-only bookshelf. Work in my running Blender session through the Blender MCP. Read my committed change brief first, propose each build before executing it, keep the geometry and material budgets, then export the assets to Godot and verify their dimensions, orientation and origins. Show me what the automated checks cannot establish.

---

## Bookend 2 — Hesitant-writer summary

*Visual: short text composing, with one revision shown.*

> Three objects from a remembered bedroom. Designed to a scale, built through a live Blender session, revised by eye, and tested in Godot. The numbers tell me whether they arrived correctly. ~~The numbers tell me whether they work.~~ **The scene tells me whether they read correctly.**

---

## B01 — Open on the result

*Visual: `a3-showcase.png` (**Godot render**). Slow, clean sequence of the three assets; then `env_room_memory.png` (**My A2 art**) showing their place in the room. Use genuine evidence; do not simulate new footage.*

**Liam:** “This is a small part of HOUSEGHOST: three objects from a bedroom that exists in two states. A music box, a lamp, and a bookshelf. They look ordinary. In this game, they are the difference between a room that has been emptied and a room that still remembers who lived there.”

“Rather than treat them as isolated models, I built them as game assets. Each has a visual job, a defined size, a geometry budget, an origin, and a path from Blender into Godot. This is how that path held up.”

---

## B02 — The game defines the props

*Visual: `env_room_memory.png`, then three finished assets individually. Label original art and Godot renders accurately.*

**Liam:** “HOUSEGHOST is a side-on 2D story about the ghost of a boy believed to have run away. In the empty bedroom, his belongings are gone. Turn the world over, and the remembered room comes back — warmer, lit, and full of objects with meaning.”

“The music box is the first relic. It calls from a place the player cannot reach directly and introduces the room’s logic. The lamp establishes the warmth of memory. The bookshelf exists as solid geometry only in the remembered state, so it matters to navigation, not just decoration.”

“The main game is 2D, but these props also live in a separate 3D Godot showcase. That lets me inspect their actual scale, orientation and materials without pretending they are already integrated into the side-scroller.”

---

## B03 — Define the target before modeling

*Visual: `CHANGE-BRIEF.md`, its scale table and prediction table. Show original commit `722658f` and timestamp from repository evidence. Label **Repository file**.*

**Liam:** “I started by fixing a scale instead of guessing by eye. The player's collision capsule is 250 pixels high, so I used 250 pixels per metre as the working conversion. That makes the bookshelf one metre tall — the height of the capsule that it blocks.”

“The illustration isn't perfectly consistent with that measurement. A later check showed the boy's standing drawing was 341 pixels, or 1.36 metres, rather than the 1.28 metres first quoted in the brief. The brief now records that correction; the collider-based scale did not change.”

“Before any model was built, I committed a brief with dimensions, materials, origins and triangle limits for all three objects. I also wrote down seven ways the process might fail: wrong orientation, wrong scale, misplaced origin, excess geometry, colour changes, a connected-but-unusable MCP, and an object that passes every numeric check but still looks wrong. Those predictions became the inspection plan.”

---

## B04 — Establish a real Blender connection

*Visual: own Blender screenshot showing the actual interface; briefly identify viewport, toolbar, Outliner, Properties, N-sidebar and mode selector using overlays based on `BLENDER-NOTES.md`. Then `get_scene_info` output, MCP panel, and `lsof` output. Label each source.*

**Liam:** “First, I learned the window I was about to direct: the viewport for looking, the Outliner for objects, Properties for materials and scene settings, the sidebar for exact transforms, the toolbar for interaction, and the mode selector for object-level versus mesh-level editing.”

“Then I checked the connection itself. A client saying ‘connected’ is not proof it can control Blender. I asked Claude to call `get_scene_info` before building anything. It returned the live default scene — cube, camera and light. That confirmed the MCP could read the running session.”

“The add-on was bound to localhost on port 9876, verified with `lsof`. I left remote model-download and generation services disabled. The geometry in this film was built locally from Blender shapes, not imported from an asset library.”

---

## B05 — Directing the build

*Visual: `a3-prompt-to-claude-own.png` (**My screenshot**), showing the real prompt and plan; `a3-prompt-result-bookshelf-a3-5.png` (**Captured in my Blender session via the MCP**). Keep the parts table legible.*

**Liam:** “Here is the collaboration in practice. I told Claude to go ahead with the bookshelf, and its first reply laid the build out in numbers: six boards, with dimensions, materials, bevels and a triangle estimate — 296 triangles against a 360-triangle target. For each redesign that followed, nothing ran until I had approved the plan.”

“Claude then created the pieces through `execute_blender_code`, one object at a time. After each operation it queried the scene again to read the resulting position, dimensions, rotation and scale. The geometry was built at its intended size, with identity object transforms.”

“Every executed call body is kept in `tools/blender`, alongside scripts that rebuild each source file from an empty scene. That means the final `.blend` files are not the only record of how the objects were made.”

---

## B06 — Music box: shape carries identity

*Visual: `stills/final-musicbox-4view.png` (**Captured in my Blender session via the MCP** — final version), `design/ref-musicbox-chatgpt.png` (**ChatGPT reference — image only**), a verbatim `tools/blender/build_musicbox.py` excerpt with path and line numbers, then `evidence/a3-stats-musicbox.png`. Earlier versions are narrated, not shown.*

**Liam:** “The first music box was within the limits: five basic shapes, 252 triangles, and a lid opened eighteen degrees. But it was too generic. It met the numbers without delivering the presence I wanted.”

“I used a generated image as a design reference, not as a mesh. Then we translated only the parts six shapes could build: a hollow body with a darker cavity, a raised plinth, an opened lid and a butterfly key whose bow aligns with its shaft.”

“The body uses an inset and extrusion to create twelve-millimetre walls and a ten-centimetre cavity. A small gap at the lid's hinge was closed, and the new silhouette checked. The finished model uses 312 triangles against a 320-triangle budget. Small bevels catch the light; face-weighted normals help the flat faces shade cleanly.”

---

## B07 — Lamp: light is a material decision

*Visual: `stills/final-lamp-4view.png` (**Captured in my Blender session via the MCP** — final version), `design/ref-lamp-chatgpt.png` (**ChatGPT reference — image only**), a verbatim `tools/blender/asset_lib.py` excerpt showing the final `"emission": 0.4`, then the final lamp in `evidence/a3-showcase.png` (**Godot render**). Earlier versions are narrated, not shown.*

**Liam:** “The first lamp followed the original painting: a traditional base and cone shade. I replaced it with a quieter modern silhouette — ceramic base, brass collar and broad drum shade. I revised its triangle budget from 340 to 420 before building, documenting why the curved base needed more geometry.”

“The showcase scene allows one light, so an internal lamp light was ruled out, and the lamp’s glow lives in its shade material instead.”

“The first Godot import exposed a problem the Blender numbers could not: emission at 1.0 pushed the cream shade to clipped white. We lowered the source emission to 0.4, rebuilt, re-exported and re-imported. The cream returned, and the source, export and rendered result agreed.”

---

## B08 — Bookshelf: the silhouette beats the spreadsheet

*Visual: `design/ref-bookshelf-chatgpt.png` (**ChatGPT reference — image only**), a verbatim `side_bm()` excerpt from `tools/blender/build_bookshelf.py` with line numbers, then `stills/final-bookshelf-4view.png` (**Captured in my Blender session via the MCP** — final version; the side view shows the rounded corners). The square-corner version is narrated, not shown.*

**Liam:** “The bookshelf was deliberately simple: six boards, warm wood, a modern profile with rounded top corners. Its first version passed the dimensional and transform checks. It still missed the feature that made the design recognizable: the upper corners were square.”

“The issue was the order of bevel operations. An earlier edge bevel caused Blender's overlap clamp to reduce the intended three-centimetre rounding to about three millimetres. Reordering the operations restored the shape.”

“Claude added an assertion for the corrected geometry. That check initially contained its own local-versus-world coordinate mistake, which was corrected too. A passing test is useful only when the test is measuring what I think it measures.”

---

## B09 — The edit I made directly in Blender

*Visual: `a3-hand-edit-before.png` (**MCP capture**); `a3-hand-edit-attempt-duplicate.png`, `a3-hand-edit-during-own.png`, `a3-hand-edit-third-shelf-own.png` (**My screenshots**); `a3-hand-edit-after.png` (**MCP capture**). Keep own screenshots on screen long enough to distinguish actual manual interaction.*

**Liam:** “I also changed the bookshelf myself in Blender's window. I duplicated a shelf and moved the new one toward the base, so the open space felt more deliberately divided.”

“That small edit taught me how precise the interface needs to be. My first duplication included the selected parent and created a second root. A free gizmo drag shifted the shelf sideways as well as vertically, and Blender made a duplicate material. Inspecting the Outliner and transforms showed each of those, and taught me that a free drag moves every axis at once, while the axis arrow keeps it to one.”

“The extra shelf took the model over six boards. I chose to remove the back panel rather than lose the new shelf, preserving the open-backed direction of the original brief. Claude then re-centred the shelves at my heights, cleaned up the duplicate objects and material, and brought the reproducible build script into agreement with the edited scene. The final bookshelf uses six boards and 280 triangles.”

---

## B10 — Export is a separate verification step

*Visual: `export_glb.py` reconstruction with `export_yup=True`; `inspect_glb.py` output; `check_assets.gd` reconstruction with file and line numbers. Then headless table beside original brief, explicitly **Headless check — not a visual check**.*

| Asset | Brief (metres: W × H × D) | Godot headless (metres: W × H × D) |
|---|---|---|
| MusicBox | 0.316 × 0.297 × 0.190 | 0.3160 × 0.2968 × 0.1900 |
| BedsideLamp | 0.28 × 0.42 × 0.28 | 0.2800 × 0.4200 × 0.2800 |
| Bookshelf | 0.64 × 1.00 × 0.30 | 0.6400 × 1.0000 × 0.3000 |

**Liam:** “A Blender model is not finished when it looks good in Blender. Each asset was exported as a binary `.glb` with plus-Y up. A separate reader inspected the exported files for colours, transforms and orientation before Godot loaded them.”

“Then a Godot headless script read each imported asset's bounding box, node scales, vertical axis and lowest point. Here are the results beside the original targets. All three fall within two millimetres of the specified dimensions, stand along Y, have unit scales and measure down to zero.”

“The first version of that script failed every correct asset because it asked for global transforms before the objects were in the scene tree. Claude corrected it to compose transforms explicitly, and it was tested against a deliberately wrong height, which it rejects. The output is a measurement, not a substitute for looking at the scene.”

---

## B11 — See the assets in Godot

*Visual: `a3-showcase.png` (**Godot render**), `a3-godot-editor-own.png`, `a3-godot-inspector-bookshelf-own.png` (**My screenshots**), then genuine rear/below/angled orbit screenshots for each asset. Show each asset clearly before introducing limitations.*

**Liam:** “This is the assembled showcase: a floor, one light, a camera and all three props together at game scale. I also placed the boy's sprite alongside them to judge proportion. His standing art reads 1.36 metres at the working scale, while his one-metre collision capsule is what matters for the bookshelf's gameplay height.”

“The scene uses Godot's Compatibility renderer, consistent with the main 2D project. The sky lighting was adjusted when the brass appeared almost black. That was a presentation issue the geometry checks would never catch.”

“Finally, I inspected each object from the front, behind, below and at an angle. The bookshelf reads correctly, and the lamp keeps its intended silhouette and colour. The music box has no missing faces, but from behind its small key disappears visually, so it can read as an ordinary box. That remains a real design limitation.”

---

## B12 — Verdict

*Visual: five concise panels: **Built**, **Verified**, **Revised**, **Still uncertain**, **Next**. Show exact submitted source SHA; label source footage and reconstructions correctly.*

**Liam:** “The result is three game-scale props, built in a live Blender workflow, exported as `.glb`, and visible together in Godot. Their final triangle counts are 312 for the music box, 406 for the lamp, and 280 for the bookshelf.”

“I verified the sizes, orientations, origins, object scales and colours across Blender, the exported files and Godot. I also inspected the actual renders and the assets from multiple angles. Those checks agree on the measurable properties; they cannot certify that an object reads correctly under every lighting condition.”

“The revisions were substantive. I redesigned a too-simple music box, replaced the lamp silhouette, fixed a shade that clipped to white, recovered the bookshelf's rounded corners, and cleaned up my manual shelf edit. Claude also made errors in geometry selection, normals logic, exporter validation and the Godot check itself. I kept the specific failures and corrections in the test report rather than presenting the final pass as if it happened on the first try.”

“My role was to define the game context and brief, choose and reject designs, approve builds, edit geometry in Blender, inspect the visual results and decide which tradeoffs to keep. Claude wrote and executed the modeling and checking code under that direction, with its outputs preserved for review.”

“What remains uncertain is how the props will read in the finished game's actual room lighting, whether the music box is identifiable from behind, and how another viewer would interpret the scene. My next step is to improve the music box's rear silhouette without exceeding six shapes or 320 triangles.”

“The demonstrated game source is commit **[INSERT VERIFIED SOURCE SHA]**, with the submitted revision identified in the accompanying source records.”

---

## B13 — Your Turn

*Visual: composer prompt typed. Label **Reconstruction**.*

> Use Walker to improve the music box's silhouette from behind. Keep the same six-shape and 320-triangle limits. Before editing, propose one specific geometry change and predict how it will read from behind and from the left in Godot. Build it through the Blender MCP, export the `.glb`, run `check_assets.gd`, and compare real editor views from both angles. Report what improved and what still does not read.

**Liam:** “Your turn. Find the place where the numbers pass but the design still needs work. Make one controlled change, predict the result, then test it twice: with measurements and with your own eyes. That's where the next iteration begins.”

---

## Outro — locked card

*Visual: `ClaudeTitleOutro` with exact title, @NikBearBrown and one mascot. Liam re-reads the title, then says “At Nik Bear Brown.” No jingle, game audio or additional narration.*

---

## Production and integrity notes (not narrated)

- Verify every filename, screenshot label, version, count, measurement, code line number and commit reference against the final repository before rendering. If the actual source differs, revise the narration and evidence rather than inventing a match.
- Keep **My screenshot**, **Captured in my Blender session via the MCP**, **Godot render**, **Repository file**, **Command output**, and **Reconstruction** visibly distinct. Do not fabricate mouse footage.
- In the actual film, make the manual Blender edit, one real Claude prompt/result, all three Godot assets, and the brief/headless table readable at normal playback speed.
- Include the required Walker opening and summary, Verdict → Your Turn → regular outro. Follow the installed Brutalist skill's native 4K landscape workflow and quality checks; watch the exported film.
- Do not claim the props are already integrated into the 2D gameplay. The 3D showcase is the demonstrated result.
- Preserve the honest unresolved rear-view music box issue and the distinction between headless and visual checks.
- Asset visuals show the **final versions only** (`stills/final-*-4view.png`, the Godot renders and my orbit screenshots). Earlier iterations are narrated, not shown — except where the story requires a before: the hand-edit sequence (B09) and the prompt-and-result bookshelf (B05).
- Before submission, separately verify the tagged clean clone, required documentation, matching GitHub/Canvas revision, film URL, filename, SHA-256 and reviewer access. These are source/submission requirements, not facts a narration can prove by itself.
