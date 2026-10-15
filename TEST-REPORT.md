# TEST REPORT — HOUSEGHOST, Night 1 slice

**Engine:** Godot 4.7.2.stable.official.ed1daf0bf · **Platform:** macOS 26.x, Apple Silicon
**Source revision:** see the final commit on branch `narasimhaReddyValam`
**Project path:** `fall-2026/narasimha-v/assignment-2/walker-houseghost-narasimha-v/godot`

---

## 1. Startup and controls

Run from a clean checkout with:

```bash
godot --path godot
```

**Run it from a terminal rather than from the editor.** Godot keeps an open scene in memory, so an editor left running while the files change will play an older build. A terminal launch is also how a grader will run it.

**The fresh copy is the only honest version of this check.** Running from the working directory proves nothing about what a grader receives, because the working directory holds files the repository excludes. Cloning the pushed branch into a scratch directory and running it there caught a real fault the moment it was first tried: converting the audio to Ogg had left thirteen `.wav.import` stubs tracked in git, describing WAV files the course rule keeps out of the repository. On this machine the masters are still on disk so nothing complained; from a clean clone Godot reported three load failures. The automated suite passed in both cases, because the game reads the Ogg files and the stale records belong to nothing it asks for. Removed in `70974a7`, re-verified from a second clean clone: no errors, 13 checks passing.

**A correction worth recording.** A repeated report of "the character will not move" was twice attributed to that stale editor, and that diagnosis was wrong. The real cause was a race between two tween `finished` signals in the opening sequence: awaiting one that has already fired waits forever, and which of the two fired first depended on frame timing. The same build therefore handed over control on one machine and froze on another. It was found by putting the four relevant values on screen and asking for a single screenshot, after four rounds of reasoning had not found it.

| Check | Result |
|---|---|
| Project opens on Godot 4.7.2 with no missing resources | **Pass, verified from a fresh clone** of the pushed branch, not from the working copy: 39 art files, 11 effects, 2 music tracks and 6 storyboard panels all present, import clean, no load errors. This check first ran red — see below |
| Main scene loads and runs | Pass |
| Opening sequence plays and hands over control | Pass — each line waits for a key press, so the opening is read at the player's pace and cannot overrun |
| Read the story again (I) during play | Pass — holds the player still while open, returns control when closed |
| Move left and right | Pass |
| Jump | Pass |
| Flip the world | Pass |
| Contact a relic, tap and hold | Pass |
| Mute music (M) and effects (N) independently | Pass |
| Restart (R) | Pass |

## 2. The automated check

```bash
godot --headless --path godot --script tests/test_sound_triggers.gd
```

Twelve assertions, zero failures at the time of writing. It covers one sound per event under rapid repeats and held input, and the walking-versus-drifting contrast in both directions.

```
PASS  one flip produces exactly one flip sound
PASS  12 flip calls during a turn still produce one sound
PASS  two resolves inside the cooldown produce one contact sound
PASS  one frost sound per day torn
PASS  muted SFX still counts the event (state is unchanged by audio)
PASS  a held jump fires one jump sound
PASS  landing from that jump fires one land sound
PASS  walking in the memory produces footsteps
PASS  the ghost makes no real footsteps
PASS  but he keeps a rhythm of his own
PASS  the ghost displaces air while he moves
PASS  and the air stops when he stops
--- 12 checks, 0 failed ---
```

**What this check cannot do, stated plainly.** It verifies that an event fires exactly once and that muting changes no game state. It cannot hear, see, or understand. Every audio fault and every comprehension fault in this project was found by a person playing, while these assertions passed throughout.

It also cannot catch a timing race. Three runs of this check passed while a player could not move at all, because it drives input directly and never exercises the real frame timing of the opening sequence. Passing tests and a person who cannot play are not a contradiction; they are measuring different things. That is the single most useful thing this project taught about verification.

## 3. My own playtest

Played on 2026-10-07 from a terminal launch, with sound on and then with both music and effects muted.

| Check | Result |
|---|---|
| Plays through with sound on | Pass — movement, the flip, all three relics, the day cost, and the ending all behaved as designed |
| Plays through fully muted (M and N) | **Pass** — everything the slice communicates was still understandable with no audio at all |
| Music loop seam | **Pass.** Both tracks played past their wrap with no click or gap. This session is on the Ogg build, so the conversion is covered by it |
| Revised effects balance | **Pass.** The quieter footsteps sit under the story sounds and the mix reads as intended |

The muted result is the one that matters most here, because readability without sound is a scored criterion and the only honest way to establish it is to take the sound away and still be able to play. All four rows are a human result, not an engine one. The muted row matters most: readability without sound is a scored quality and the only honest way to establish it is to take the sound away and still be able to play.

## 4. Another person played it

A friend played the build without being told anything about the story or the controls. Her feedback, as reported to me:

> It's confusing. I didn't know what to do, or when to turn upside down, or why I was doing that.

This is recorded as given and was not solicited with leading questions. It is the most useful result in this report, because it isolates a failure I could not see: I already knew the story, so I could not tell that the game never conveyed it.

**What it exposed.** The slice had an opening that establishes *who the player is* — a boy who was erased, a family living in his house, a wish to be noticed — but nothing that teaches *what to do*. The central verb, turning the world over, was never taught at all. It appeared in a hint line at the bottom of the screen that listed every control at all times, which a player reads once and then stops seeing.

**What changed in response.**

- The permanent hint line is gone. In its place, a prompt appears beside the thing it refers to, only when it can be acted on, and stops appearing once it has been used.
- Arrow keys are shown until the player first moves.
- Standing below a relic that cannot be reached from the floor shows **F**, next to the relic itself.
- Once inverted and within reach, that becomes **E**.
- Once a relic has been taken, its prompt and its light both go out, so what remains lit is always what is left to do.

Verified in engine: before moving the cue reads the arrow keys; standing under the music box in the normal world it reads F; after flipping, in reach, it reads E; after the contact lands it fades out.

**Not yet retested with her.** The changes above are a response to her session, not a result she has confirmed. A second session with the same player, or a fresh one, is the honest next step and has not happened.

## 6. Storyboard against the slice

Each panel the slice covers, beside the same moment captured in engine.

| Storyboard panel | The same moment, in engine | Difference |
|---|---|---|
| **1 — Moving day**<br>![](design/storyboard/01-moving-day.png) | ![](evidence/A0-the-truth.png) | The slice opens on the stripped room with the child already present, which the panel does not show. Strengthened deliberately: the first thing the player sees is the room emptied, not a title |
| **2 — The flip**<br>![](design/storyboard/02-the-flip.png) | ![](evidence/B0-mid-dissolve.png) | The panel draws a 180° roll; the engine dissolves one room into the other while the camera stays level. The dissolve read far better in play and never disorients — recorded as a deliberate departure |
| **3 — The music box**<br>![](design/storyboard/03-music-box.png) | ![](evidence/D1-the-music-box.png) | Matches. The box sits on the bookshelf and is reachable only from the inverted side |
| **4 — She looks up**<br>![](design/storyboard/04-she-looks-up.png) | ![](evidence/D2-she-heard-that.png) | Matches in substance: her posture changes toward the room. The panel frames her from a high angle; the game camera stays at eye level, because the slice never moves the camera |
| **5 — The hallway is wrong**<br>![](design/storyboard/05-hallway-wrong.png) | *not covered* | Out of scope for the slice; semester work |
| **6 — The cellar door**<br>![](design/storyboard/06-cellar-door.png) | *not covered* | Out of scope for the slice; semester work |

## 7. Character against the sheet

| Sheet element | In engine |
|---|---|
| Idle, remembered — solid, grounded | ![](evidence/70-idle.png) |
| Walk, remembered — the eight-frame cycle | ![](evidence/71-walking.png) |
| Ghost, inverted — hanging from the ceiling | ![](evidence/22-ghost-on-the-ceiling.png) |
| Jump poses | ![](evidence/28-jump-poses.png) |
| One body size across every pose | ![](evidence/29-consistent-size.png) |
| Orientation follows input, left flipped at runtime | ![](evidence/25-continuous-walk.png) |
| Collision against the art | ![](design/character/collision.png) |

The size row is the one that took three attempts: height, shoulder width and head
width all failed across poses, and body area is what finally held. The screenshot
above is the check that settled it.

## 8. Sound

| Check | Result |
|---|---|
| Four events minimum, each firing once per occurrence | Pass — nine events, twelve assertions |
| Rapid repeats and held input do not double-fire | Pass |
| Music loops without an audible click | **Pass.** Verified two ways: in engine both tracks load as `AudioStreamOggVorbis`, 59.5 s and 61.9 s, with loop set in code because the importer defaults it to false; and by listening past the wrap on the Ogg build, where no click or gap is audible |
| Music behaviour on flip, failure, success and end | Pass — crossfade on the flip, long clean fade on either ending |
| Mute works for music and effects separately | Pass |
| Slice readable with all sound muted | **Pass, confirmed by a muted human playthrough** on 2026-10-07: played with both M and N muted, and everything the slice communicates was still legible. The visual carriers are the nights counter, the relic lights going out as each is answered, the contextual key cues, and the child's posture turning further toward the room |

## 9. Revision driven by observation

Several, all recorded in FRICTIONAL.md and CHANGE-BRIEF.md. The two most consequential:

**Sounds that fired and could not be heard.** Measurement showed `contact` audible for 19 % of its length, `correct` 15 %, `frost` 29 % — brief ticks surrounded by silence, lost under a score at full level. All were compressed to be dense rather than spiky (contact now 84 %, correct 77 %, flip 96 %) and the music now ducks 15 dB beneath each one. The automated check had passed the whole time.

**A level where nothing the player did mattered.** The floating platforms could be ignored entirely by walking on flat ground. They were removed and replaced with gaps in the floor that cost a night to fall through, and with obstacles that exist in only one world.

## 10. Honest limitations

- The three room tiles repeat; the middle one is mirrored to break the repetition, which puts two doors adjacent at the seam.
- The floor gaps exist in both worlds although the fiction says only the real house has been pulled apart.
- Three character-sheet poses are specified but not generated.
- The floorboard relic, the floor holes, the glow and the heartbeat are drawn or synthesised in code and satisfy no generative requirement; the asset log marks each as such.
- Storyboard panels 5 and 6 are not covered.
- A player who skips the opening can still take a few moments to work out what the game wants; the contextual cues are a response to that and have not been retested on a fresh player.
- Storyboard panel 2 reads closer to a diagonal division than a 180° roll.

## 11. The film

**The House Is a Witness.** — 3840x2160, in the [course media storage](https://northeastern-my.sharepoint.com/:f:/r/personal/valam_n_northeastern_edu/Documents/The%20House%20Is%20a%20Witness%20(Art%20%26%20Sound)?d=w4cd7a183ebfb445282e99594585c140b&csf=1&web=1&e=F2oHje),
identified by filename and SHA-256 in README.md and SUBMISSION.md.

The gameplay in it is a real engine capture, not a reconstruction: 32.63 s at native
4K, 1958 ticks at exactly 60 fps, driven by real key events against an isolated copy
with no teleporting and no seeded state, carrying the game's own audio. Every clip is
labelled on screen as a scripted-input capture, and the stretches that hold a final
frame say so. The capture's SHA-256 and the hash of every source file it displays are
in `youtube/claude-liam-houseghost-gamedev/`.

---

# Assignment 3 — first 3D assets

**Blender** 5.2.2 LTS · **Godot** 4.7.2.stable.official.ed1daf0bf (Compatibility renderer) · **MCP** `mcp-for-blender` 2.1.9 · macOS 26.6.2, Apple Silicon · branch `a3-first-3d-assets`

Every number below comes from a command run in this session; the raw outputs are in `evidence/a3-check-assets.txt` and `evidence/a3-inspect-glb.txt`.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Interface notes | **Done.** All six parts described in `BLENDER-NOTES.md`, with how I used each, and my own screenshot of my session with a part selected and the N sidebar's Item tab open | `BLENDER-NOTES.md`; `evidence/a3-blender-window.png` |
| 2 | Size | **Pass.** Brief, Blender and Godot agree to the millimetre for all three (table below) | `get_scene_info` after every object; `check_assets.gd` |
| 3 | Upright and scale | **Pass.** Height lies along Y for all three; every node's scale is 1, 1, 1 in Godot; no rotation or scale on any node in the `.glb` | `check_assets.gd`; `inspect_glb.py` |
| 4 | Origin | **Pass.** Lowest point y = 0.0000 for all three; in the render each stands on the floor with its contact shadow at its base | `check_assets.gd`; `evidence/a3-showcase.png` |
| 5 | Triangle count | **Pass.** 312 / 320, 406 / 420, 280 / 360 — all under the course's 500. Counted from mesh data and from the exported index buffers, which agree; not read from Blender's status bar | build-script output; `inspect_glb.py` |
| 6 | Imports and appears | **Pass.** `--import` exits 0 with no errors or warnings; the scene loads with all nine nodes and exactly one `Light3D`, and all three render | `evidence/a3-showcase.png` |
| 7 | HUMAN CHECK: look | **Done, by me, in the Godot editor.** From behind and below, the bookshelf reads clearly as a bookshelf and the lamp clearly as a lamp. **The music box reads only as a box from behind** — the key is too small to say "music box". No holes or missing faces from any angle; the colours looked right. Each asset was viewed beside the boy at game scale | `evidence/a3-orbit-*-own.png` (nine of my screenshots: rear, bottom and an angled view of each) |
| 8 | What Claude got wrong | Ten things, all caught before they shipped (list below) | `FRICTIONAL.md` |

### Size: three sources side by side (metres, W × D × H)

| Asset | Brief (as revised) | Blender | Godot bounding box (x × z × y) |
|---|---|---|---|
| MusicBox | 0.316 × 0.190 × 0.297 (A3-2) | 0.316 × 0.19 × 0.2968 | 0.3160 × 0.1900 × 0.2968 |
| BedsideLamp | 0.28 × 0.28 × 0.42 (A3-4) | 0.28 × 0.28 × 0.42 | 0.2800 × 0.2800 × 0.4200 |
| Bookshelf | 0.64 × 0.30 × 1.00 (A3-8) | 0.64 × 0.30 × 1.00 | 0.6400 × 0.3000 × 1.0000 |

### What the automated check does and does not show

`check_assets.gd` shows that each asset arrived at the size, orientation and scale measured in Blender, with its origin at its base. It was run against a deliberately wrong expected height and reported FAIL with exit 1, so it can fail. It does **not** show that anything looks right: colour on screen, shading, or whether an asset reads as what it is. "Lowest point at y = 0" is a property of the mesh bounds, not a test of contact with a floor. The first version of the check failed all three assets for a reason that had nothing to do with them (below), which is the clearest evidence that a check proves only what it measures.

### What Claude got wrong

1. Proposed a key bow at right angles to the shaft, like a T-handle; a butterfly key's bow lies in the plane of its shaft. Fixed in revision A3-2.
2. Its test for the music box's inner walls caught only the floor (`cavity faces 1`). Replaced with a bounds test (`cavity faces 5`) before the live build.
3. Its normals check assumed convex parts and would have failed the hollow box's correctly inward-facing walls. Replaced with consistent winding plus positive signed volume.
4. Its lamp-shade check read the wrong face as the cap ("cap normal z +0.20"), then miscounted sides (24 / 25) by comparing Blender faces by identity. Both fixed before the live build.
5. Proposed a light inside the lamp, which would have broken the scene's one-light rule. Withdrawn before building.
6. Logged the live calls only by reference at first; the assignment asks for every call body in the build script. Added verbatim, retroactively for the music box.
7. Its exporter guard read the glTF format list before export, which is always empty; the script stopped itself. Removed.
8. Its first Godot check used `global_transform` outside the scene tree and failed all nine assertions on correct assets. Rewritten to compose transforms itself.
9. Chose emission 1.0 for the lamp shade, which clipped to white in Godot. Lowered to 0.4 (A3-6).
10. Its first showcase light was too orange and its camera framed the assets badly. Retuned.
11. Its first filter for the bookshelf's corner edges also matched the edges running front-to-back across the top; its own assertion stopped the build before any geometry was made.
12. It bevelled the bookshelf's front edges before rounding the corners, so Blender's overlap clamp shrank the 3 cm rounding to about 3 mm and the corners came out square — with every numeric check still passing. Caught only by looking at the views; the corners are now rounded first, and a check asserts the front face stops at 0.97 m.

### Inspect-and-revise cycles driven by observation

- **The lamp shade (A3-6).** Observation: in the first render the shade was pure white and its cream was gone. Cause: emission plus lighting above white. Change: emission 1.0 → 0.4 in the shared library; lamp rebuilt, re-exported, re-imported. Result: the cream shows in the second render.
- **The brass.** Observation: the key, collar and finial read near-black. Cause: metal shows its colour by reflection and the sky was too dim to reflect. Change: sky reflection energy raised; the background stays dark. Result: the brass reads gold.
- **My hand edit (A3-8).** Observation, in my own screenshots: dragging two shelves had also moved them up to 1 cm sideways and backwards, into the side panel and through the back; duplicating a shelf had copied its parent and its material as `.001`, and made seven boards. Change: the shelves re-centred and evenly spaced at my heights, the copies renamed and merged back into the library, and the back panel removed to return to six. Result: 280 / 360 triangles, the check still passing. Before and after are `evidence/a3-hand-edit-before.png` and `evidence/a3-hand-edit-after.png`, from the same camera.
- **The bookshelf's corners (A3-7).** Observation: in the first views of the rebuild the side panels' top corners were square, though every numeric check passed. Cause: bevel order. Change: corners rounded first, plus a check that the front face stops 3 cm below the top. Result: rounded corners, front face top at 0.9700 m.
- **The music box's key (A3-1).** Observation in Blender: a 35 mm bow on a 268 mm box, about 9 px at game scale. Change: bow enlarged to 50 × 40 mm at no triangle cost.

### Honest limitations

- From behind, the music box reads only as a plain box: its identifying detail, the key, is too small at that distance. Found in my orbit check; not changed.
- Compatibility renderer: no ambient occlusion or screen-space reflections. The brighter sky lifts the woods slightly above their hex values.
- The music box's key is hidden from behind and to the left.
- No other person has looked at the scene; no viewer is invented here.

