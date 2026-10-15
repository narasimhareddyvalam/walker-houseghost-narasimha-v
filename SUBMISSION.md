# SUBMISSION — Assignment 3

**Assignment:** Assignment 3 - Your First 3D Game Assets with Claude, the Blender MCP, and Blender
**Student:** Narasimha Reddy Valam
**Project name:** walker-houseghost-narasimha-v (HOUSEGHOST)

**GitHub repository URL:** https://github.com/narasimhareddyvalam/walker-houseghost-narasimha-v

**Git tag and submitted commit SHA:** tag `a3`. The submitted commit's SHA is given in the Canvas note, since a commit cannot contain its own SHA.

**Game-source revision shown in the film:** `d331a4adc0d70385116278e16e7058132bb525ee` — the last commit that touches `godot/`, `blender/` or `tools/`. Every later commit changes documentation and film records only; `git diff d331a4a a3 -- godot blender tools` is empty.

**Godot version, Blender version, and operating system:** Godot 4.7.2.stable.official.ed1daf0bf (Compatibility renderer) · Blender 5.2.2 LTS · macOS 26.6.2, Apple Silicon

**The three assets and what each is for:**

| Asset | For | Size (m, W × D × H) | Triangles |
|---|---|---|---|
| MusicBox | The first relic — visible from spawn, calling across the level | 0.316 × 0.190 × 0.297 | 312 / 320 |
| BedsideLamp | The warm light that makes the remembered room look safe | 0.28 × 0.28 × 0.42 | 406 / 420 |
| Bookshelf | Solid only in the memory — the half of the mechanic that forces the flip | 0.64 × 0.30 × 1.00 | 280 / 360 |

**MCP project and version, or "script route":** MCP route for all three assets: `mcp-for-blender` 2.1.9 (add-on 1.8, protocol 13), connected to my live Blender on 127.0.0.1:9876, every download and generation service off. Every live call body is logged verbatim at the end of `tools/blender/build_<asset>.py`; the same scripts rebuild each asset headless, and `tools/blender/export_glb.py` exports it.

**My hand edit in Blender:** On the bookshelf (revision A3-8), with the mouse in my own session: I duplicated a shelf and moved it down to make a third shelf, and decided to drop the back panel to stay at six boards. Claude then tidied the edit in one recorded call (re-centred the shelves, removed the `.001` copies, darkened the shelves). Before and after: `evidence/a3-hand-edit-before.png`, `evidence/a3-hand-edit-after.png`; the full account is in `BLENDER-NOTES.md` and `FRICTIONAL.md`.

**Checks run (command and result):**
- `godot --headless --path godot --import` — exit 0, no errors or warnings.
- `timeout 120 godot --headless --path godot --script res://tests/check_assets.gd --fixed-fps 60` — `RESULT: PASS (0 failures)`, exit 0: all three within 2 mm of the brief, height along Y, every node scale 1, lowest point 0 (`evidence/a3-check-assets.txt`). Run once against a deliberately wrong height: FAIL, exit 1.
- `python3 tools/inspect_glb.py godot/assets/models/*.glb` — nodes, bounds, triangles 312 / 406 / 280 and colours as sRGB hex (`evidence/a3-inspect-glb.txt`).
- Blender's statistics overlay — 312, 406 and 280 triangles (`evidence/a3-stats-*.png`, `evidence/a3-hand-edit-after.png`).
- My own look in the Godot editor from behind, below and at an angle — the bookshelf and lamp read clearly; the music box reads only as a box from behind (`evidence/a3-orbit-*-own.png`).

**Final film URL and filename:** added with the final export.
**Final film SHA-256:** added with the final export.

**Summary of my changes:** Three props from the game's remembered bedroom, built from Blender primitives through the MCP and exported as binary glTF: `blender/` (one `.blend` per asset), `tools/blender/` (build scripts, material library, exporter), `godot/assets/models/` (three `.glb` with `.import` files), `godot/scenes/AssetShowcase.tscn` (floor, one light, camera, the three props at game scale), `godot/tests/check_assets.gd`, `CHANGE-BRIEF.md`, `BLENDER-NOTES.md`, the Assignment 3 sections of `TEST-REPORT.md`, `FRICTIONAL.md`, `SOURCES.md` and `README.md`, and the film's records in `youtube/claude-liam-houseghost-a3-gamedev/`. The 2D game from Assignment 2 is unchanged.

**Known limitations:** From behind, the music box reads only as a plain box (the key is too small at that distance). The lamp is modern, while the lamp in my 2D painting is traditional. The Compatibility renderer has no ambient occlusion or screen-space reflections, and the brighter sky lifts the woods slightly above their hex values. The 12-sided lamp base shows facets close up. The 3D scene is not yet connected to the 2D game, as the assignment allows.

**Changed games since Assignment 2:** no.

---

# SUBMISSION — Assignment 2

**Assignment:** Assignment 2 — Generate Art, Sound, and Music for Your Game
**Student:** Narasimha Reddy Valam
**Project name:** walker-houseghost-narasimha-v

**Game concept in one sentence:** You play the ghost of a boy the world believes ran
away, haunting the bedroom a new family has moved into, and one key turns the world
between the room as he remembers it and the room as it really is.

**GitHub repository/folder URL:**
https://github.com/nikbearbrown/csye-7270-building-virtual-environments/tree/narasimhaReddyValam/fall-2026/narasimha-v/assignment-2/walker-houseghost-narasimha-v

**Started from:** an empty Godot 4 project. The world-inversion verb is carried
forward as an idea from my Assignment 1 game, walker-jumpman-narasimha-v; no code,
scenes or assets are reused.

**Source revision (the slice, and what the film demonstrates):** `268b44166f5a32e81da44dc7c8faab69b781ae43`
This commit contains the complete Godot project, every generated asset, and all
design and verification documents. The film's evidence ledger
(`youtube/claude-liam-houseghost-gamedev/gamedev-evidence.json`) hashes each source
file it displays against this revision.

**Submitted commit SHA:** the branch tip on `narasimhaReddyValam`, which is the
commit that adds this line and the film's checksum. Per the brief, that final commit
is documentation only — it touches `SUBMISSION.md` and `README.md` and changes no
source, asset, scene or script. The two revisions therefore demonstrate identical
work, and the ZIP submitted to Canvas is built from the tip.

**Godot version and operating system:** Godot 4.7.2.stable.official.ed1daf0bf · macOS 26.x, Apple Silicon

**Generative models used:**

| Model | Where run | Used for | Licence / terms |
|---|---|---|---|
| ChatGPT image model | chatgpt.com, free tier | Character art, both rooms, relics, 6 storyboard panels | OpenAI Terms of Use |
| Suno v6-mini | suno.com, free tier | Both music loops | Non-commercial, attribution, 7-download lifetime cap |
| ElevenLabs Sound Effects | elevenlabs.io, free tier | All event sounds | ElevenLabs ToS, free-tier output usable for coursework |
| Google Gemini (image) | gemini.google.com, free tier | Character reference attempts — **all rejected, nothing used** | Google ToS + generative-AI terms |
| Kokoro-82M (`am_onyx`) | local, offline | Film narration only | Apache 2.0 |

**Final film URL:** https://northeastern-my.sharepoint.com/:f:/r/personal/valam_n_northeastern_edu/Documents/The%20House%20Is%20a%20Witness%20(Art%20%26%20Sound)?d=w4cd7a183ebfb445282e99594585c140b&csf=1&web=1&e=F2oHje
**Final film filename:** `houseghost-the-house-is-a-witness-narasimha-v-4k.mp4`
**Final film SHA-256:** published in `CHECKSUM.txt` beside the film in the media folder linked above.

## Summary of my work

A Night 1 slice of HOUSEGHOST, built in Godot 4. One bedroom exists in two versions:
upright is the stripped room the new family moved into and you are the ghost;
inverted is the room as he remembers it and he looks like a living boy. Flipping
reverses gravity — the camera never rotates. Touching the three relics that were his
is the only way to be noticed, and every contact raises recognition while tearing a
day off the calendar toward the anniversary. A child in the doorway is the
recognition meter: her posture turns further toward the room with each relic.

Designed on paper first — concept, six storyboard panels, and a character sheet with
a silhouette test, collision overlay, palette and consistency rules — all committed
before the first generation. Every generation kept or seriously considered is logged
in SOURCES.md with its prompt, model, outcome and edits, including the rejections and
the one model dropped entirely.

## Known limitations

- The hallway that rearranges itself and the cellar door (storyboard panels 5 and 6)
  are drawn and belong to later nights; the slice does not cover them.
- Three character-sheet poses are specified and not generated; the slice never calls
  for them.
- Storyboard panel 2 reads closer to a diagonal division than a 180° roll.
- The contextual relic cues were written in response to a playtester's confusion and
  have not yet been retested on a fresh player.
- The three room tiles repeat; the middle one is mirrored, which puts two doors
  adjacent at the seam.
- Some art is drawn in code (the glow, the floor holes, the floorboard relic) and is
  marked in the asset log as satisfying no generative requirement.

## Verification

- 13 automated assertions (`tests/test_sound_triggers.gd`), all passing.
- Run from a **fresh clone** of the submitted revision, which is how a grader
  receives it — this check caught orphaned import records that the working copy hid.
- Human playthrough with sound on and then fully muted; the slice stays readable with
  no audio at all.
- An external playtester's confusion is recorded verbatim in TEST-REPORT.md, along
  with what changed because of it.

The most useful thing the project taught is in TEST-REPORT §2: the automated checks
stayed green through every real fault — a movement bug, three inaudible sounds, and a
clean clone that printed load errors. Passing tests and a broken game are not a
contradiction; they measure different things.
