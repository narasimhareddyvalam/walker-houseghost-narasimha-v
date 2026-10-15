# HOUSEGHOST — Change brief (Assignment 2 slice)

## Asset list

**Status 2026-10-06.** Built means the asset exists and is in the running slice.

| ID | Asset | Panel | Status |
|---|---|---|---|
| CHAR-REF / CHAR-SHEET | Turnaround and eight-view model sheet, both states | all | Built — `design/character/model-sheet-8-views.png` |
| CHAR-GHOST | Idle drift, ghost state | 1, 4 | Built — `assets/art/char_ghost.png` |
| CHAR-REMEMBERED | Idle, remembered state | 2, 3 | Built — `assets/art/char_remembered.png` |
| CHAR-WALK-01..04 | Walk cycle, remembered state | 3 | Built — `assets/art/char_walk_1..4.png` |
| ENV-ROOM-EMPTY | The bedroom, stripped (upright world) | 1, 4 | Built — `assets/art/env_room_empty.png` |
| ENV-ROOM-MEMORY | The same bedroom, remembered (inverted world) | 2, 3 | Built — `assets/art/env_room_memory.png` |
| UI-GLOW | Marker for an available contact | 3 | Built — code-drawn, not a generated asset |
| PROP-SHELF | His bookshelf: blocks the memory, absent from the truth | 1–4 | Built — lifted from `env_room_memory.png` |
| PROP-BOXES | The new family's moving boxes: block the truth, absent from the memory | 1–4 | Built — lifted from `env_room_empty.png` |
| ENV-FLOOR-HOLE | A hole where the floorboards have been pulled up | 1–4 | Built — drawn in code |
| CHAR-CHILD | The new family's daughter, three poses: playing, hearing, seeing | 1, 4 | Built — `child_1..3.png` |
| RELIC-SHOES | His shoes, still by the door | 3 | Built — lifted from `env_room_memory.png` |
| RELIC-BOARD | A floorboard lifted at one end, something pale beneath | 6 | Built — drawn in code |
| SFX-STEP / SFX-GHOSTSTEP | A footstep in the memory; displaced air as the ghost | all | Built |
| SFX-DRIFT | The ghost's continuous moving air | all | Built |
| SFX-FALL | Dropping through the floor | 5 | Built — derived from SFX-CORRECT |
| SFX-HEART | The night running out, from four nights onward | 6 | Built — synthesised in code |
| SFX-FLIP | World flip (held breath, reversed swell) | 2 | Wired, file pending |
| SFX-CONTACT | Contact (music-box chime with a paper tear inside) | 4 | Wired, file pending |
| SFX-FROST | A day tearing off (crystalline crackle) | 4 | Wired, file pending |
| SFX-CORRECT | The house reacting to a loud contact (wood groan, de-tuned note) | 4 | Wired, file pending |
| MUS-UPRIGHT | Tense arpeggiated score, upright world | 1, 4 | Built — `assets/music/mus_upright.wav` |
| MUS-MEMORY | Music-box lullaby over an afro-polyrhythmic groove, inverted world | 2, 3 | Built — `assets/music/mus_memory.wav` |
| CHAR-GHOST-REACH, CHAR-GHOST-SCARE, CHAR-GHOST-HURT | Contact, scare and dispersed poses | 3, 5 | Specified, not generated — the slice shows these states by image swap and engine motion |
| CHAR-CHILD-PLAY, CHAR-CHILD-LOOKUP | The child, playing and looking up | 1, 4 | Specified, not in the slice |
| CHAR-FATHER-BACK, CHAR-HOLLOW-GLIMPSE | The father at the cellar door, the Hollow glimpsed | 5, 6 | Specified, semester work |
| ENV-HALL-MEMORY, ENV-HALL-CORRECTED, ENV-CELLAR-DOOR | Hallway and cellar door | 5, 6 | Specified, semester work — panels 5 and 6 are outside this slice |
| PROP-MUSICBOX, PROP-CALENDAR | Music box and wall calendar as drawn props | 3, 4, 6 | Not separately generated; the music box is marked by UI-GLOW and the calendar is the HUD counter |

## Event-to-sound map

**Revision 2026-10-06 — as built.** The original plan is kept below the table; the differences are named, because the slice was built before the audio existed and the wiring is what the sounds will attach to.

| Sound | File | Exact trigger in the built slice | Double-trigger prevention |
|---|---|---|---|
| SFX-FLIP | `assets/sfx/sfx_flip.ogg` | `world.gd` `flip()` — played immediately after `is_inverted` is changed and `world_flipped` is emitted | A `_flipping` guard rejects any further call until the 0.6 s tween finishes, so a held or mashed key cannot flip or sound twice. Verified: twelve calls during one turn produce one sound |
| SFX-CONTACT | `assets/sfx/sfx_contact.ogg` | `contact_point.gd` `_resolve()` via the `contact_landed` signal, on key release, after the tap-or-hold has been decided | The contact arms on `just_pressed` and resolves on release, never on `pressed`; a 1.2 s cooldown is enforced inside `_resolve` itself, so a second resolve is refused regardless of who calls it. Verified: two resolves inside the cooldown produce one sound |
| SFX-FROST | `assets/sfx/sfx_frost.ogg` | `meters.gd` emits `day_torn` once per day removed; `world.gd` plays one sound per emission | One tear, one sound, by construction — the loop that decrements the calendar is the same loop that emits. Verified: a two-day cost produces exactly two sounds |
| SFX-CORRECT | `assets/sfx/sfx_correct.ogg` | A **scary** contact only: the loud way to be seen also wakes the house | Rides the same single `contact_landed` emission as SFX-CONTACT, so it inherits that cooldown |

**Changed from the plan:** SFX-CORRECT was planned for a hallway trigger in a room that the slice does not include, so it now fires on the scary contact, which is the slice's equivalent beat — the loud choice disturbing the house. SFX-FLIP's guard is 0.6 s rather than the estimated 0.8 s, matching the tween actually used.

**Rule, enforced in code:** sound never decides state. Every trigger above is played *after* the game has already changed state and emitted a signal. An automated assertion covers this directly: with sound effects muted, a flip still counts as having happened, because the audio layer only observes. The slice also runs with all five audio files absent — it prints a notice and plays silently.

## Music behaviour

**Revision 2026-10-06 — as built.** The plan had one track for the inverted world and silence upright; there are now two tracks, one per world.

- **Plays:** MUS-UPRIGHT from the moment the slice starts and whenever the world is upright; MUS-MEMORY whenever it is inverted. Never both.
- **On the flip:** a hard cut, not a crossfade — the abruptness is what makes the flip feel like a threshold. The two tracks share key and tempo so the cut does not lurch.
- **Failure (the anniversary arrives first):** the current track fades out over 2.5 s and stops.
- **Success (the child sees you):** the same clean fade — the only musical resolution in the slice, reserved for endings.
- **Mute:** M stops both tracks; unmuting resumes the track belonging to the world the player is currently in. N mutes effects independently. Neither changes any game state.
- **Looping:** each file is a 32 s body with two seconds of its own tail crossfaded equal-power back over its head, so the seam is inaudible wherever the playhead wraps. `loop_mode` is set in code with an explicit `loop_end`; enabling the mode alone produces a zero-length loop that stops instantly.

## Predicted failure cases, the checks, and what actually happened

1. **Generated poses drift in proportion from the reference.** Check: compare each accepted image against the model sheet; reject anything whose head height or proportions drift. **Outcome: this happened repeatedly and was the main cause of rejection.** Five character references were rejected before one was accepted (asset log CHAR-REF-01 to 05). The accepted walk cycle held proportions well enough to use, and was additionally normalised to a common height and canvas so the figure does not jitter between frames.
2. **The character disappears against a room.** Check: screenshot at game resolution and confirm the character reads; if not, adjust the art, not the room. **Outcome: partly failed and not yet fixed.** Green was reserved for the character and excluded from both rooms, which works in the remembered world. In the upright world the ghost is pale on grey and reads faint — visible in `evidence/01-upright-ghost.png`. The planned fix is a rim light on the ghost sprite; it is an open limitation, recorded in the README.
3. **The music loop clicks at the seam.** Check: cut at a bar boundary, listen to repetitions, and set the loop flag so the engine loops rather than a script timer. **Outcome: solved differently, and a new failure was found.** Rather than relying on cutting exactly on a bar line, each track is cut with two seconds of its own tail crossfaded back over its head, which makes the seam inaudible wherever it wraps. The unpredicted failure: setting Godot's `loop_mode` alone stopped playback instantly, because `loop_end` defaults to zero and produced a zero-length loop. Verified in engine — the loop wraps from 31.4 s to 0.8 s still playing. Human listening confirmation is still outstanding.
4. **A sound fires twice on one event.** Check: an automated script asserts one sound per event under mashing and held input. **Outcome: a real defect was caught.** The contact cooldown guarded only the input path, so the resolve function could still fire twice when called directly; the guard now lives inside the function. The check also caught a flaw in itself — it measured waits in frames, and headless frames are not real time. Five assertions now pass.
5. **The slice is unreadable muted.** Check: play it with all audio off and confirm the cost is still legible. **Outcome: designed for and visible in the captures, but the human playtest is still outstanding.** The calendar counter jolts when a day is torn, recognition pips fill, and a frost vignette deepens as the anniversary nears — none of which depend on sound. The slice currently runs silent by necessity, which has made this easy to observe but does not substitute for a real playtest with the audio present and then muted.

### Found while building and while playing, not predicted

6. **The core verb was unreachable** — the relic sat where the player could never touch it.
7. **The collision shape did not match the art**, having been specified before any art existed.
8. **The capsule was teleported into the floor on the first flip**, squeezing the player out through the bottom of the room.
9. **A blocker sat on the floor when the route it guards runs along the ceiling.**
10. **The movement read as teleporting:** the walk cycle only ran in one state and the stride was too long to read as walking.
11. **Three different ways of measuring the character's size were wrong.** Height fails across poses; shoulder width fails when the arms are raised; head width fails on the rising pose because the topmost pixels there are his raised hands. Body area is what finally worked.
12. **The idle textures were never rebuilt** when the frame sets were unified, so he changed size and height the moment he stopped walking. Later solved properly by making the idle the walk cycle's own legs-together frame: the standing drawing is 340 px where the walk frames are 303–317, and no amount of scaling reconciles a pose that stands straighter than walking ever does.
13. **He turned pale when he moved** — the walk and jump sheets were graded 30 percent brighter and cooler than the idle.
14. **The sounds could not be heard even though they fired.** Measured, `contact` was audible for 19 percent of its length, `correct` 15, `frost` 29: brief ticks surrounded by silence, which vanishes under a score at full level. The automated check had passed throughout, because counting that an event fired proves nothing about whether a person hears it.
15. **The player had no idea what to do**, solved without instruction by moving a relic into view, lighting it permanently and having it call across the level.
16. **The platforms were decoration** — the whole level could be walked on flat ground, so nothing the player did mattered.
17. **Gaps in the ceiling were tried and abandoned:** under reversed gravity crossing one means jumping downward, which no player will intuit.
18. **The first gap width was unfair,** leaving a 35 px window to take off in against a jump covering 275 px.
19. **The gaps were invisible,** which made them a trap rather than an obstacle.
20. **Twenty-four orphaned nodes** were left behind when the decorative platforms were deleted, drawing a stray rectangle on screen.
21. **The heartbeat was audible from the first second,** which made it wallpaper rather than information. Silent now until four nights remain.
22. **Taking the ghost's footsteps away entirely read as broken rather than weightless.** He keeps a stride rhythm in both worlds; what changes is what the rhythm is made of.
23. **Reaching the end and finding nothing there.** One relic in a three-room level meant two thirds of it existed for no reason.
24. **The slice never said who the player was.** No opening, no context, no reason to want anything. The single largest fault found, and the last one found, because it is invisible to anyone who already knows the story.
25. **Adding the opening broke five of the twelve automated assertions**, which began driving input while the player is deliberately held still. The checks were wrong, not the game.
26. **He appeared not to be moving while moving at full speed:** the camera follows him and all three room tiles were identical, so the background repeated exactly.
27. **The child was absent from the opening,** because her visibility was driven by a signal the opening sets up without emitting — so the image the entire opening exists to deliver was missing from it.
28. **The central verb was never taught.** An external playtester finished a session without learning that the world could be turned over. It had only ever appeared in a hint line listing every control at all times, which is read once and then stops being seen. Replaced with prompts that appear beside the object they refer to, only while actionable, and stop once used.
29. **The opening held control for eleven seconds with no way out.** A player pressing keys and getting nothing concludes the game is broken, not that a cutscene is running. Shortened, made skippable by any key press, and given a ten-second safety timer that hands over control regardless of what the sequence is doing.
30. **The relics called from the first frame of the opening,** before the player could act on them. A sound with no available response is a noise rather than a signal; nothing calls now until control has been handed across.
31. **The opening lines did not explain themselves.** "I need one of them to see me" never said what being seen would achieve. Rewritten so each line carries one idea and the last connects the goal to its reason.
32. **The first cue was positioned with a world coordinate inside a screen-space layer,** so it drifted off the side of the view as soon as the camera started following the player.
33. **The opening text could not be read.** Lines advanced on a timer set by someone who already knew the words, and a key press was wired to skip rather than to advance. Each line now waits for a key and says so, and I reopens the story at any point.
34. **The opening stranded the player, and it was a race rather than a stale editor.** The sequence awaited several tweens in turn; the player's fade-in was created before the room dissolve was awaited and both last about nine tenths of a second. Whichever finished first depended on frame timing, and awaiting a `finished` signal that has already fired waits forever. The identical build therefore worked on one machine and froze on another, and three automated runs passed while a person could not move — the checks drive input directly and never exercise the real timing path. The dissolve now runs from one clock on plain timers. **This had twice been attributed to a stale editor, which was wrong.**
35. **The loudest sound in the game was the one nobody chose.** The effects were asked to come down a little. Measuring them first showed why they felt hot: `step`, `ghoststep` and `fall` were absent from the mix table, so they played at full level while the comment above it claimed footsteps were deliberately quiet. Normalising every file to the same *peak* is not the same as to the same loudness, and the dense footstep sample measured 5 dB above the flip by RMS — on the sound that fires most often in the game. All levels came down 3 dB and the three missing entries were given real ones.

## Music behaviour, stated for all four cases

The brief asks for pause, failure, success and the end of the slice. All four are
answered here, including the one that turned out to be a design decision rather than
a behaviour.

| Case | Behaviour | Why |
|---|---|---|
| **Pause** | **The slice has no pause state.** Nothing in Night 1 stops the clock: the calendar moves only when the player spends a night, so there is nothing to suspend. This is recorded rather than left blank, because the absence is a choice. The nearest equivalent is the story overlay on **I**, which holds the player still and leaves the music playing at level — the words are his, and the room has not changed |
| **Failure** | Falling through a gap spends a night. `sfx_fall` fires and the score ducks 15 dB beneath it, then returns. The music does not stop: the night is still running, which is the point |
| **Success** | A contact ducks the score 15 dB, then holds a deliberate 1.8 s hush (`_audio.hush`). It is the only moment in the slice where the game goes quiet on purpose — being noticed should not sound like a reward |
| **End of the slice** | A single clean 2.5 s fade to silence on either ending, *seen* or *anniversary* (`finish_music`). It is the only full musical resolution in the slice, reserved for endings |

Verified in engine: the duck is `DUCK_DB = -15.0` in `scripts/audio.gd`, the hush is
called from `_on_contact_landed` in `scripts/world.gd`, and the ending fade is
`finish_music()`. The captured run shows the duck at the flip (−23.0 dBFS) and the
post-contact hush holding at −23 dBFS while the rest of the run sits near −17.

---

# HOUSEGHOST — Change brief (Assignment 3: first 3D assets)

**Written and committed 2026-10-14, before Claude was asked to build anything.** The
Assignment 2 brief above is kept exactly as it was. Nothing in this section is edited
later to make a prediction look right; corrections are appended as dated revisions, and
the outcome of every predicted failure is recorded in the last table whatever it turns
out to be.

## The scale this brief is written in

**1 metre = 250 pixels**, anchored on the player, which is what the assignment asks for
("justified against something in your game — the player's height, a tile, a door").

| Thing in the game | Pixels | Metres at 250 px/m |
|---|---|---|
| The boy's sprite, full height | 320 | **1.28** — correct for the eight-year-old he is |
| His collision capsule | 250 | **1.00** |
| Floor to ceiling, interior | 800 | 3.20 |
| The door in `env_room_memory.png` | ~609 | 2.44 |

**The known problem with this anchor, stated up front.** My own art does not agree with
itself. Anchored on the boy it is 250 px/m; anchored on the door at a standard two metres
it is ~300 px/m. I have taken 250 because the assignment names the player's height first
and because it makes the character correct, which matters more than the door does. The
cost is a 2.44 m door and a 3.2 m ceiling — tall, though not impossible in an old house.
Nothing in Assignment 2 ever required me to measure this, because nothing in a 2D game does.

A consequence worth naming: at 250 px/m the music-box sprite would be a **0.79 m** object.
The relic art was drawn oversized so that it reads on screen, not to scale. **The 3D assets
are built true to life rather than to the sprite dimensions**, and the gap between the two
is expected rather than an error.

## Reference

The reference for all three is **my own Assignment 2 art**, in this repository:
`godot/assets/art/env_room_memory.png`, `relic_musicbox.png` and `prop_shelf.png`. No
downloaded model, no generated mesh, no third-party reference.

Colours were sampled out of those PNGs with Pillow and then **lifted to albedo**, because
the paintings are lit by a single warm lamp and a flat material carries no lighting. The
bookshelf samples at `#0F0A06`, near black, which is what that wood looks like in that
room rather than what the wood is. Both values are recorded.

| Material | Shipped (albedo) | Sampled from art | Used on |
|---|---|---|---|
| `M_Wood_Warm` | `#6B4428` | `#61402A` music-box body | music-box body, bookshelf carcass |
| `M_Wood_Dark` | `#4A2E19` | `#402411` bookshelf side panel | music-box lid, shelves |
| `M_Brass` | `#9A7B3F` | — chosen; the key sits in shadow in the art | wind-up key, clasp |
| `M_Ceramic_Amber` | `#A15A26` | `#88441A` lamp base | lamp base and neck |
| `M_Shade_Cream` | `#F0DCA8` | `#FAE098` lit shade | lamp shade |

Palette rules carried over from `CHARACTER-SHEET.md` and respected here: **no green**, which
belongs to the boy alone, and nothing at the child's `#E9C846`. `#F0DCA8` is a pale cream
kept deliberately clear of that yellow.

## The three assets

Each is built around Blender's world origin with its base on the floor at that point, and
**each lives in its own `.blend` file**, because that origin is where Godot will place it.

### 1. MusicBox — `build_musicbox.py` → `musicbox.blend` → `musicbox.glb`

- **What it is in the game:** the first relic. Visible from the spawn point, out of reach
  from the floor, calling every few seconds with its own chime — it is the whole of the
  slice's tutorial. `relic_musicbox.png`, the `MusicBox` node at (1548, 470).
- **Size:** body **0.24 W × 0.17 D × 0.12 H m**; **0.18 m** overall with the lid ajar.
  Justified as roughly a seventh of the boy's 1.28 m — an object he holds in two hands.
- **Origin:** centre of the underside. It stands on a shelf, so that is the point I want to
  place and the point that should sit flush.
- **Shape — 5 primitives:** cube body; cube lid, hinged open about 18°; cylinder key shaft;
  cube key handle; small cube clasp on the front. The art shows a ballerina inside, which is
  organic and cannot be made from primitives within budget, so it is deliberately omitted.
  **The wind-up key is what makes this read as a music box rather than a chest**, which is
  also why the lid is ajar rather than closed.
- **Colours:** `M_Wood_Warm` body, `M_Wood_Dark` lid, `M_Brass` key and clasp.
- **Budget: 320 triangles.** Estimated 274 — a 2-segment bevel on the body (~130), 1-segment
  bevels on lid and handle (~44 each), a 12-vertex key shaft (44), unbevelled clasp (12).
  The margin is there in case the edges read too sharp and the bevel has to go up.

### 2. BedsideLamp — `build_lamp.py` → `lamp.blend` → `lamp.glb`

- **What it is in the game:** the warm light beside the bed in the remembered room — the
  reason that world looks safe. Painted into `env_room_memory.png`. **Unlike the other two
  it is not a separate node in `Bedroom.tscn`**, and I am stating that rather than implying
  all three are equally present. The assignment asks for assets the game *could* use, and
  gives "a lantern" as its own example.
- **Size:** **0.20 W × 0.20 D × 0.42 H m**. Justified as about a third of the boy's 1.28 m,
  standing on a bedside table; in the art the shade sits a little above the mattress.
- **Origin:** centre of the underside of the base.
- **Shape — 3 primitives:** UV sphere squashed to 0.6 on Z for the bulbous ceramic base; a
  thin cylinder neck; a truncated cone shade **wider at the bottom** (r1 0.10, r2 0.065),
  which is the proportion the painting actually shows and the thing that makes it read as a
  bedside lamp rather than a desk lamp.
- **Colours:** `M_Ceramic_Amber` base and neck, `M_Shade_Cream` shade.
- **Budget: 340 triangles.** Estimated 280 — sphere at 12 segments × 6 rings (144), 12-vertex
  neck (44), 24-vertex cone (92). The shade carries 24 segments because a faceted lampshade
  is the most obvious tell of a cheap model; the rest is made cheaper to pay for it.

### 3. Bookshelf — `build_bookshelf.py` → `bookshelf.blend` → `bookshelf.glb`

- **What it is in the game:** his bookshelf. Solid only in the memory and absent from the
  truth — one half of the mechanic that forces you to turn the world over. `Memory0` at
  (2200, 815) and `Memory1` at (4600, 815), collider 150 × 250 px.
- **Size:** **0.64 W × 0.30 D × 1.00 H m** overall; the carcass is 0.60 wide and the top slab
  overhangs 0.02 each side. Justified directly by the in-game collider: 150 × 250 px at
  250 px/m is 0.60 × 1.00 m, and **1.00 m is exactly the height of the boy's collision
  capsule**, which is why it stops him.
- **Origin:** centre of the underside. It stands on the floor, and the Godot check places it
  at y = 0 to see whether it sits or floats.
- **Shape — 5 primitives:** top slab (overhanging), two side panels, two interior shelves.
  **The overhang is the detail that makes it furniture rather than a box** — it is the first
  thing visible in `prop_shelf.png`. Open-backed, as the art shows a dark interior. One shape
  is left spare against the six-shape limit, deliberately, in case the viewport review wants
  a plinth.
- **Colours:** `M_Wood_Warm` carcass and top, `M_Wood_Dark` shelves.
- **Budget: 360 triangles.** Estimated 306 — a 2-segment bevel on the top slab (~130) because
  it is the most-seen edge, 1-segment bevels on the four panels (~44 each).

## Rules every asset is held to

1. Built around the world origin, base on the floor at that point, one `.blend` each.
2. Rotation and scale applied before export; Godot must read node scale `1, 1, 1`.
3. Every object, mesh and material named — no `Cube.001` anywhere.
4. One shared five-material library across all three, not fifteen unrelated colours.
5. Segment counts set deliberately and stated above; Blender's default 32 is never used.
6. Normals recalculated outside before export.
7. Exported as binary glTF with +Y Up.
8. Every line of code Claude runs is saved to `tools/blender/build_<asset>.py`, and each
   must rebuild its asset headless from an empty scene.

## Predicted failure cases, the checks, and what actually happened

**Predicted 2026-10-14, before building.** The last column is filled in as each is tested,
whatever the result.

| # | What could go wrong | How I will check it | What actually happened |
|---|---|---|---|
| 1 | An asset arrives lying on its side. Blender is Z-up and glTF is Y-up, and the exporter's +Y Up conversion is the only thing standing between the two. | The headless Godot script prints the standing axis and bounding-box extents per asset; in Blender the `N` sidebar must read rotation 0,0,0 before export. | **Did not happen.** Every object was built with rotation 0, 0, 0, and the exporter's +Y Up conversion did its job: in the `.glb` files height lies on +Y (`tools/inspect_glb.py`), and the Godot check reports each asset's height along Y. Blender's front (−Y) arrives as glTF +Z, facing a default Godot camera. |
| 2 | Wrong by a factor of ten or a hundred — a metres/centimetres slip, or a scale left unapplied. | Three numbers side by side for every asset: this brief, Blender's `N` sidebar Dimensions, and Godot's bounding box. All three must agree. | **Did not happen.** The three sources agree to the millimetre for all three assets — the brief as revised, Blender (`get_scene_info` and object dimensions, the values the `N` sidebar shows), and Godot's bounding box: music box 0.316 × 0.190 × 0.297, lamp 0.28 × 0.28 × 0.42, bookshelf 0.64 × 0.30 × 1.00 m. No scale was ever set, so none needed applying. |
| 3 | The origin ends up in the middle, so the asset sinks half under the floor or floats above it. Blender creates every primitive centred, so this is the default outcome rather than bad luck. | Place each asset at y = 0 in the Godot scene and look at whether it sits or hovers. The lamp and the bookshelf are the obvious tells. | **Prevented by construction, and confirmed.** Each mesh was translated so its base sits at z = 0 before it was finished, so the origin is the centre of the underside. Godot measures the lowest point of all three at y = 0.0000, and in the showcase render each stands on the floor with its contact shadow at its base. The check measures bounds, not floor contact; there is no collider involved. |
| 4 | Claude over-builds — more detail, more primitives or more triangles than asked, so the asset stops being the thing this brief describes. | Scene Statistics in Blender's status bar after every object, against the per-asset budget above, and primitive count against the stated shape list. Over budget means rebuild the asset, not rewrite the budget. | **It partly happened, by my choice and in the open.** Nothing was over-built unasked, but all three grew past this brief through dated revisions I approved: the music box from 5 to 6 shapes (252 → 312 triangles), the lamp from 3 to 6 shapes with its budget raised from 340 to 420 before building, and the bookshelf from 5 to 6 shapes. All stay within the course limits of six shapes and 500 triangles: 312 / 320, 406 / 420, 296 / 360 (248 / 360 after revision A3-7). Counts were taken from the mesh data and the exported index buffers, not read from Blender's status bar. |
| 5 | A colour does not survive the export. glTF carries base colour rather than viewport colour, and a material left on Blender's default grey exports as grey. | Orbit each asset in the Godot scene and compare it against the five hex values in the material table. | **The export kept every colour; the scene lost two, and both were fixed.** Read back from the `.glb` files, every base colour is the exact hex in the table above. In the first Godot render the lamp shade clipped to pure white (emission 1.0 plus lighting exceeds white — fixed at the source, revision A3-6) and the brass read near-black, because fully metallic brass shows its colour only by reflecting its surroundings (fixed with stronger sky reflections in the scene). Remaining: the woods read slightly lighter than their hex under the brighter sky. |
| 6 | The MCP registers but never actually drives Blender. The client reports "Connected" when the stdio process launches, which says nothing about whether it can reach a running Blender. | `get_scene_info` must return the real contents of my open scene before any build is approved. Every error string recorded verbatim in `FRICTIONAL.md`. Two-hour time box, then the script route. | **Did not happen.** `get_scene_info` returned the real contents of my open Blender before anything was approved — the unsaved default scene, with the camera and light at their default positions — and every asset was then built through `execute_blender_code` in that session. No error string was needed; the time box was never used. |
| 7 | The assets are correct and still look wrong — right size, right way up, and reading as three grey boxes beside the painted room they came out of. | The human check the rubric reserves for me: orbit each one in Godot from behind and below, at game scale, and judge whether it reads as what it is. No headless check can answer this. | **Not yet tested — this is my orbit check.** At the fixed showcase camera all three read as what they are; that is a single viewpoint, not the check the rubric reserves for me, which is orbiting each asset from behind and below in the editor. |

## Revisions

Appended after building began. The specification above is left as it was written.

**A3-1 — 2026-10-14, MusicBox: the wind-up key enlarged.** Shaft r 0.005 × 0.025 m → r 0.006 × 0.030 m; handle 0.006 × 0.035 × 0.025 m → 0.008 × 0.050 × 0.040 m. **Why:** as built to the original numbers the bow was 35 mm on a 268 mm box, about 9 px tall at 250 px/m, and smaller in proportion than in `relic_musicbox.png`. This brief names the key as the detail that makes the object read as a music box, and at that size it could not do that job. **Cost:** none in triangles (still 252 / 320) and none in primitives (still 5). The overall width grows from 0.268 m to 0.275 m; the body is unchanged at 0.24 × 0.17 × 0.12 m. **What it did not fix:** seen from behind and to the left, the key is on the far side and the box still reads as a plain chest. That is left for the Godot orbit check (prediction 7), not solved by adding parts.

**A3-2 — 2026-10-14, MusicBox: rebuilt from a second reference, six shapes.** I judged the
first build "too simple" and asked for it to look more realistic. Realistic textures are
outside the assignment (flat colour, no painted textures, at most six basic shapes and 500
triangles), so the realism is to come from lighting and material response in Godot, and the
geometry was revised against a ChatGPT reference image, `design/ref-musicbox-chatgpt.png`
(asset log row REF-MUSICBOX-3D). **This changes the Reference section above:** my A2 art is
no longer the only reference for this asset.

| | Original spec | A3-2 |
|---|---|---|
| Shapes | 5: body, lid, key shaft, key handle, clasp | **6**: adds `MB_Plinth`; the handle becomes `MB_KeyBow` |
| Plinth | — | 0.26 × 0.19 × 0.015 m, 1 cm overhang, chamfered, `M_Wood_Dark` |
| Body | Solid, 0.24 × 0.17 × 0.12 m | Same size, **hollowed**: 12 mm walls, 20 mm floor, cavity in `M_Wood_Dark` |
| Lid | 0.008 m thick, open ~18° | **0.012 m** thick, open **70°**, hinge at y = 0.079, flush on the rim |
| Key bow | Box, at right angles to the shaft | **Upright oval disc** 0.040 × 0.056 × 0.005 m, in the plane of the shaft as on a real butterfly key |
| Overall size | 0.24 × 0.17 × 0.18 m (body + lid) | **0.316 × 0.19 × 0.297 m** with plinth, key and open lid |
| Origin | Centre of the body's underside | Centre of the **plinth's** underside — still the point that sits on the shelf |
| Triangles | 252 built (estimate 274), budget 320 | **312**, budget unchanged at 320 |

**Two judgement calls, stated so they can be disputed.** Hollowing the body is two edit
operations (inset, push down) on one cube. It goes beyond "moved, scaled and combined", but
it is not sculpting, and I read it as within "built mainly from basic shapes". Face-area
weighted normals are baked into every mesh, so the 1-segment bevels shade as rounded edges
while the large faces stay flat; this costs no triangles and is a standard low-poly technique.

**What A3-2 leaves for later.** Seen from behind and to the left, the key is still on the far
side. Whether the box reads as a music box from there, and whether the colours survive
export, are predictions 7 and 5 and are tested in Godot.

**A3-3 — 2026-10-14, BedsideLamp: five shapes, a foot, and a lit shade.** Proposed before
building and approved. The overall size is unchanged at **0.20 × 0.20 × 0.42 m**; the
reference stays my own `env_room_memory.png`.

| | Original spec | A3-3 | Why |
|---|---|---|---|
| Shapes | 3: base, neck, shade | **5**: adds `LP_Foot` and `LP_Bulb` | — |
| Foot | — | 12-sided disc, r 0.055 × 0.012 m, `M_Wood_Dark` | A sphere touches the floor at one point; prediction 3 would be judged at a pole. The painting shows a foot |
| Base | UV sphere 12 × 6, squashed to 0.6 | Same sphere, r 0.07, squashed to **0.8**: 0.14 wide × 0.112 tall, seated 8 mm into the foot | The painted base is rounder, and narrower than the shade |
| Neck | Ceramic | **`M_Brass`**, r 0.008, rising to 1 mm under the shade's cap | Lamp hardware is metal; it repeats the music box's brass |
| Bulb | — | UV sphere 8 × 4, r 0.028, inside the shade | Seen from below, which the Godot orbit check looks from |
| Shade | Truncated cone, closed | Same cone (24 sides, r 0.10 → 0.065, 0.17 tall), **open at the bottom**, closed at the top; double-sided material | A closed cone shows a flat lid from below |
| Glow | — | `M_Shade_Cream` gains emission strength 1.0, on the shade and bulb only | Reads as lit **without a second light**: the Godot scene is allowed only one |
| Triangles | Estimate 280, budget 340 | **326**, budget unchanged | — |

**The library now has emission on one material.** It is still the five-material library
(rule 4); `M_Shade_Cream` is used only by the lamp. The library moved into
`tools/blender/asset_lib.py`, shared by every build script, so the rule is enforced in code.

**Noted, not changed:** the visible neck (0.116 to 0.25 m) is longer and thinner than in the
painting, and the 12-segment base shows facets at close range.

**A3-4 — 2026-10-14, BedsideLamp: rebuilt as a modern lamp, six shapes, budget raised to 420.**
After the A3-3 lamp I wanted it more realistic. The first ChatGPT references read as old-fashioned,
and the one I chose (`design/ref-lamp-chatgpt.png`, row REF-LAMP-3D) is a modern ceramic table
lamp. **This moves the 3D lamp away from my own painting**, which shows a traditional one; the
painting stays the reference for colour, not for shape.

| | A3-3 | A3-4 |
|---|---|---|
| Shapes | 5 | **6**: foot, base, `LP_Collar` (new), neck, bulb, shade |
| Foot | 12-sided, r 0.055 × 0.012 | **16-sided**, r 0.078 × 0.018, walnut (`M_Wood_Dark`) |
| Base | UV sphere 12 × 6, squashed | **12-sided drum r 0.07 × 0.14 with both rims rounded** (2-segment, 25 mm bevel): the glossy pill shape |
| Collar | — | Brass disc, r 0.032 × 0.008, on top of the base |
| Neck | r 0.008, ends under the shade's cap | r 0.009, **runs 15 mm through the cap to form the finial**, so the finial costs no seventh shape |
| Bulb | r 0.028 | r 0.032 |
| Shade | Cone r 0.10 → 0.065, 0.17 tall | **Drum** r 0.14 → 0.13, 0.16 tall, z 0.245 → 0.405; still open at the bottom and closed on top |
| Overall size | 0.20 × 0.20 × 0.42 m | **0.28 × 0.28 × 0.42 m** — a drum shade this wide is what makes it read as modern, and 28 cm is an ordinary bedside lamp |
| Triangles | 326 / 340 | **406 / 420** |

**The budget change, stated plainly.** The rounded base costs 140 triangles on its own, and the
design does not fit 340. I chose to raise the budget to 420 **before building**, with this reason
recorded, rather than drop the collar and the rounding to stay under it. It remains under the
course limit of 500. This is a design revision, not the overshoot that prediction 4 is about.

**A3-5 — 2026-10-14, Bookshelf: built to the brief's size, with a back panel as the sixth shape.**
The overall size is exactly as specified, **0.64 × 0.30 × 1.00 m**, and the height is still the
boy's 1.00 m collision capsule. The reference stays my own `prop_shelf.png`.

| | Original spec | A3-5 | Why |
|---|---|---|---|
| Shapes | 5, open-backed, one spare | **6**: top, two sides, two shelves, **`BS_Back`** | The "dark interior" in the art is a back panel in shadow. A back also makes it read as furniture from behind, which is where the Godot orbit check looks from |
| Top | 0.64 wide, 2 cm overhang each side | Same, plus 1 cm front and back; 0.025 thick, 2-segment bevel | The most-seen edge |
| Sides | — | 0.02 × 0.28 × 0.975 m, standing on the floor | Their lower ends are the legs |
| Shelves | Two interior shelves | 0.56 × 0.264 × 0.02 m at **6 cm** and **50 cm**, set back 1 cm, `M_Wood_Dark` | The art shows the lowest shelf raised off the floor on the sides |
| Triangles | Estimate 306, budget 360 | **296**, budget unchanged | — |

Where boards meet, their faces touch exactly; a check over every face of every part found
eleven such contacts, all facing each other and hidden inside the joints, and no two faces
in the same plane facing the same way — so nothing can z-fight.

**A3-6 — 2026-10-14, BedsideLamp: shade emission lowered from 1.0 to 0.4, found in Godot.**
In the first showcase render the shade and bulb clipped to pure white: emission at strength
1.0 on a cream that is also lit adds up to more than white, and the tonemapper clips it, so the
`#F0DCA8` cream was lost — predicted failure 5 in a form the prediction did not name. Lowered in
`tools/blender/asset_lib.py`, the lamp rebuilt headless from its script, re-exported and
re-imported; the cream now shows. Geometry is unchanged (406 triangles, 0.28 × 0.28 × 0.42 m).

**A3-7 — 2026-10-14, Bookshelf: rebuilt from a modern reference, still six boards at the
brief's exact size.** I wanted the bookshelf as realistic as the other two. The reference
(`design/ref-bookshelf-chatgpt.png`, row REF-BOOKSHELF-3D) is a modern open bookshelf whose
character comes entirely from how six boards are shaped and set — so it is buildable without
a seventh shape.

| | A3-5 | A3-7 |
|---|---|---|
| Sides | 0.02 thick, 0.975 tall, under the top | **0.03 thick, full 1.00 m height, rising 2.5 cm above the top, top front and back corners rounded (r 0.03, 4 segments), front edges softened** |
| Top | 0.64 wide, overhanging the sides | **0.58 wide, set between the sides**, top surface at 0.975 |
| Shelves | At 6 cm and 50 cm, `M_Wood_Dark` | **At 0.36 and 0.65 m** — a third and two-thirds — in **`M_Wood_Warm`**, as in the reference; the bottom bay is open, the sides standing as legs |
| Back | 0.006 thick, flush | **0.008 thick, set in 5 mm** from the back edge, stopping 10 cm above the floor |
| Triangles | 296 / 360 | **248 / 360** |

The overall size, 0.64 × 0.30 × 1.00 m, and the 1.00 m height that matches the boy's capsule
are unchanged. This moves the bookshelf away from `prop_shelf.png`, which has a shelf near
the floor; the painting stays the reference for colour.

