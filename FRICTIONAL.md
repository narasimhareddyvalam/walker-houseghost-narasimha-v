# FRICTIONAL — HOUSEGHOST

## How this log works

The method is the one I set on the first day of Assignment 2 and have not changed: **Claude proposes, I attack, and whatever survives is the game.** I ask it to argue back rather than agree, because an assistant that agrees with everything is worth nothing on a project I have to defend myself.

Entries are dated and in order, written as the work happened. Nothing is rewritten after the fact; where a decision is reversed later, the reversal is its own entry rather than an edit to the original. Claude drafts the factual spine of an entry from the session it was present for; the judgements are mine, and anything still marked `[TO FILL]` is a gap I have not closed rather than a claim I am making.

**Assignment 2's log** stays in the course repository at `fall-2026/narasimha-v/assignment-2/FRICTIONAL.md`. It did not travel when this game moved into its own repository on 2026-10-14. This file begins at Assignment 3.

## Decisions, and where each of us overruled the other

### Assignment 3

| What was on the table | Claude's position | Mine | What happened |
|---|---|---|---|
| Where Assignment 3 lives | A new repository named `walker-houseghost-narasimha-v` | Asked three times whether the folder already sitting on my disk could just be pushed, remapped or duplicated | **It held its position and was right.** The folder had no `.git` of its own, so a push from inside it pushes the entire 349 MB course repository under the wrong name. What actually settled it was tags: `a3` is repo-global, not per-branch, so on the shared course repo it collides with every classmate's `a3` |
| How to seed the new repository | Offered both — `cp -R` plus `git init` for one clean commit, or `git subtree split` to carry all 73 | Did not overrule | Took the split. The cumulative-game rule only means something if Assignment 3 continues a history instead of landing on top of a blank slate |
| Which GitHub account | Used whichever account `gh` had marked active, `narasimhareddyvalamm` | `narasimhareddyvalam`, single m | **I overruled it,** after it had already created the repository. I deleted the empty one myself. "Active account" is not the same as "the right account", and that is a question, not an assumption |
| Risk to Assignment 2 | — | "Make sure to not lose anything in that repo, that is connected to my Assignment 2" | **A constraint I set before anything ran.** It took a 432 MB bundle of the whole course repo first, used only read-only operations against it, pushed nowhere but the new repo, and then verified the A2 branch, folder and submitted commit were untouched |
| Assignment prompts in the repo | — | "Never commit assignment requirements to the repo" | **A standing instruction.** The prompt lives as `ASSIGNMENT-3-REQUIREMENTS.md` and is gitignored in both repositories |
| Narrating the work | Began running a command whose name I had already agreed to | "Tell what you are doing first" | **I overruled it.** Agreeing to a branch name is not agreeing to the moment it gets created. Intent is now stated before the action, not reported after it |
| Which three assets | The music box, a bedside lamp and the bookshelf — one collectible, one prop, one piece of environment, at three different scales | *Open* | *Undecided as this is written.* Its other candidate was the three relics, which it then argued against itself: shoes and a floorboard lying nearly flat will not read as what they are when they are built from six boxes |
| Which scale the metre is | 250 px per metre, anchored on the boy, because the brief says to justify sizes against the player | *Open* | *Undecided.* See the entry below — my own art does not agree with itself about this |
| Which identity commits carry | Had been committing with whatever Git defaulted to, which on this machine was a hostname address | "Commit to GitHub under only `narasimhareddyvalam`, not `narasimhareddyvalamm`" | **A standing instruction.** Checking it is what exposed the hostname address — see the entry below. The repo's local config now sets `valam.n@northeastern.edu`, which GitHub resolves to the single-m account |
| How the music box's meshes are made | `bmesh` primitives built at final size and angle, bevels as real geometry, instead of `bpy.ops` primitives with modifiers | Approved the plan | **Accepted.** Rotation and scale never exist on the objects, so there is nothing to apply and nothing to forget. Triangle counts are exact rather than estimated, and the script runs headless without a viewport |
| Smooth-shading threshold | Proposed 30°, then changed it to 40° before running, and said so | Did not overrule | A 12-sided shaft has exactly 30° between faces, so 30° left the result to rounding. At 40° the shaft is smooth and the 45° bevels and 90° caps stay crisp |
| Where the `.blend` lives | `blender/musicbox.blend`, outside `godot/` | Did not overrule | Godot 4 tries to import any `.blend` inside its project folder; only the `.glb` belongs there |
| The music box's key, and its back view | Enlarge the key at no triangle cost; add nothing to the back, because extra parts are the over-building that prediction 4 exists to catch | Left it to Claude: "whatever will help us add details to it more nicely" | **Its call, taken.** Recorded as revision A3-1 in `CHANGE-BRIEF.md`, not as an edit to the original spec. The key now shows from directly behind; from behind-left it still does not |
| "Realistic graphics" for the music box | The brief forbids painted textures and allows six flat-colour shapes, so realism has to come from lighting and material response — environment reflections, shadows, ambient occlusion, tonemapping in Godot — plus a plinth, softer bevels and proportions closer to the painting | "It's too simple, I want it to be more visually appealing", then "it should be realistic graphics". Offered three routes — realism through light, a second textured variant outside the rules, or breaking the limits on the graded asset — **I chose realism through light** | **My choice, inside the rules.** A ChatGPT reference image is to be generated from a prompt that asks for a realistically lit render of a buildable object, not a textured one; it becomes revision A3-2 and a `SOURCES.md` row when it arrives |
| What to take from the ChatGPT image | The hollow box, wide lid, plinth, round key bow and dark interior; not the hinges (shapes 7 and 8), the tray lid (triangles) or the redder wood (palette) | "Follow assignment requirements and follow best practices and they should be realistic and creative to get me full marks" | **Accepted as proposed.** Recorded as revision A3-2 |
| Hollowing the body | Two edit operations on one cube; not sculpting; within "built mainly from basic shapes" | Accepted | **A judgement call, stated in the brief so it can be disputed** |
| How the live calls carry the code | Each call `exec`s the saved build script and runs one step from it, instead of pasting a copy | Did not overrule | The code that ran in Blender is the file, so rule 8 is proven rather than asserted |
| The lamp's design | Five shapes: add a foot and a bulb, open the shade underneath, brass neck, glowing shade, rounder base — each change with its reason | "Yes go ahead. Make sure we are following all assignment requirements" | **Accepted.** Recorded as revision A3-3 |
| A light inside the lamp in Godot | Proposed it at first, then withdrew it after re-reading the assignment: the showcase scene is "floor, one light, a camera" | Asked that every requirement be followed | **Claude corrected its own proposal before building.** The glow comes from emission on the material, which is not a light |
| Logging the call bodies | Each build script now ends with `LIVE_CALLS`, every `execute_blender_code` body verbatim, including the music box's, added retroactively | Same instruction | The assignment says to copy every body into the build script. Calls that ran the file itself already proved the code; the log also satisfies the rule as written |
| One shared library | Moved the five materials and helpers into `tools/blender/asset_lib.py` | Approved | Verified harmless: the music box's headless geometry report is identical before and after |
| Making the lamp more realistic | Same route as the music box: a ChatGPT prompt asking for a realistically lit render of a lamp built from at most six spheres, cylinders and cones in flat colours — a larger base and a short neck as in the painting, a view from below, the lamp switched on — so the result stays buildable | After orbiting the built lamp in Blender: "i want more realsitc one, give me prompt to give to chatgpt" | **My decision; the outcome is pending.** The reference image is to be recorded as REF-LAMP-3D and any changes as revision A3-4, proposed before building |
| Which lamp reference to use | Wrote the first ChatGPT prompt: a realistically lit lamp from at most six simple shapes, flat colours | "chatgpt didnt give me what i like, it gave me too old styles" — **I rejected those results, regenerated it myself, and chose the one I liked** | **My call, made outside this session.** The chosen image becomes REF-LAMP-3D once it is in the repository; the rejected takes are recorded as rejected, as the A2 asset log does |
| The lamp's triangle budget | The modern design needs ~406; offered raising the budget to 420 before building, or fitting 340 by dropping the collar and the rounding | **Raise to 420** | **My choice.** Declared in revision A3-4 before building, with the reason; still under the course limit of 500 |
| Committing the ChatGPT screenshot | Recorded the two follow-up prompts from it as text, and did not commit the image | — | It shows unrelated personal browser tabs and chat titles; the prompts are what `SOURCES.md` needs |
| The bookshelf's sixth shape | A back panel, reading the art's dark interior as a back in shadow; the brief had kept the spare for a plinth | "Yes go ahead with the bookshelf" | **Approved.** Recorded as revision A3-5; the brief's size is kept exactly |
| Fixing the white-out shade | Lower the emission at the source and rebuild, rather than override the material in Godot | — | So the `.blend`, its build script and the `.glb` still agree. Revision A3-6 |
| Renderer for the showcase | Leave the project on Godot's Compatibility renderer, which has no SSAO or screen-space reflections | — | Changing it would change the whole 2D game. The realism comes from sky reflections, shadows and tonemapping instead; recorded as a limitation |
| How the Blender-window screenshot was taken | macOS refused a terminal capture (no Screen Recording permission), so the shot was taken inside my own running session with Blender's own Window › Save Screenshot operator, `bpy.ops.screen.screenshot`, after selecting `BS_Shelf_Mid` | Asked for it to be taken for me | **Recorded as taken through the MCP, in my session**, and kept as `evidence/a3-blender-window-mcp.png`. I then took my own screenshot with the N sidebar open on its Item tab showing the shelf's dimensions; that one is `evidence/a3-blender-window.png`. The hand edit and the orbit check are kept for the end, by my choice |
| A more realistic bookshelf | A ChatGPT prompt for a modern piece built from exactly six boards, then a follow-up asking for small realistic details within that limit | "I want more realistic, let's generate a photo", then "tell it to add small realistic details unique style, modern" | **My direction.** I sent the follow-up and chose the image |
| The bookshelf's design | Thick sides rising above an inset top, rounded corners, shelves at a third and two-thirds, open bottom bay, inset back — all six boards, 248 triangles | "Yes, build it" | **Approved.** Revision A3-7; the overall size and the 1.00 m height are unchanged |
| Writing `BLENDER-NOTES.md` | Asked how I had used each of the six parts, then wrote the note from my answers, saying only what I said I did | "Do the blender notes" | **My usage, Claude's sentences.** Orbit, select and Material Preview in the viewport; the Outliner for the hierarchy and for selecting; the N sidebar's Item tab for every number; Object Mode throughout, with a brief look at Edit Mode |
| My hand edit | Suggested moving one shelf, then a two-tone recolour for something more visible on video | "I think the easiest thing I can do is to add a third shelf" | **My edit, made with the mouse.** Revision A3-8 |
| Seven boards | Laid out the choices: drop the back panel, undo the shelf, or keep seven and break the limit | First asked for the back slab as well, then: "keep how it is now without back its fine" | **My decision.** Open-backed, six boards |
| Tidying the edit | Re-centred the shelves at my heights in even bays, renamed the copies, merged the `.001` material back, made the shelves dark wood | Accepted | **Claude's tidy-up of my edit**, logged as such, in one recorded call |
| The 1 m cube and the capsule in the showcase | They were not required — the assignment asks for a floor, one light, a camera and the three assets; they came from my own plan. Proposed replacing both with the boy's own sprite at game scale | "I don't like them … remove them … or change them to something related to our game and more in detail" | **My call, Claude's proposal.** The boy now stands beside his props at 1.36 m; measuring him corrected the brief's 1.28 m |
| The boy's texture after it appeared in 3D | Godot's "detect 3D" re-imported `char_remembered.png` with lossy VRAM compression and mipmaps — the same file the 2D game draws. Restored the lossless import and turned detect-3D off for that one texture | — | **A side-effect of using a 2D sprite in 3D, caught in `git status` before commit.** The A2 slice's own test then passed 13 / 13 |
| Blender's own triangle counts | The assignment says "Blender shows scene statistics"; until now the counts came from code. Opened each `.blend` in my session and saved a screenshot with the statistics overlay | "Alright, let's do it" | **Closed.** 312, 406 and 280 in Blender's overlay, matching the code. `evidence/a3-stats-musicbox.png`, `a3-stats-lamp.png` |
| Reviewing every image before the film and the push | — | "Before the film stop … I want to review all the images we are submitting before assignment submission and pushing to GitHub" | **My rule.** Nothing goes to GitHub or into the film until I have looked at every image |
| The 24 images for submission | Listed every A3 image with what it shows, which requirement it serves and who captured it; opened them in Preview | Reviewed them: "photos are good i guess" | **Approved by me** for the repository and the film, before any push |
| One hand edit or three | One meets the requirement ("at least one change by hand"); more earns nothing and costs a re-export and re-check per asset | Asked whether all three assets needed one | **One — the third shelf.** The music box's weak back view stays a recorded limitation |
| A prompt to Claude, and what it built | My terminal screenshot of "yes go ahead with the bookshelf" and Claude's build plan, paired with Blender's four-view image of the bookshelf that prompt produced (A3-5, before my rebuild and hand edit) | Took the screenshot myself | **For the film's prompt-and-result beat.** `evidence/a3-prompt-to-claude-own.png`, `evidence/a3-prompt-result-bookshelf-a3-5.png` |
| The film's script, before any video | Drafted `SCRIPT.md` against the assignment's film requirements, with a requirement-to-beat table, every image labelled by who made it, and every claim traced to a file or command | "Before generating the video, I want the video script … professional and technical and add our work properly" | **My review gate.** No narration or render until I approve the script |
| The film's tone | Recast each problem as a short caught-and-fixed moment and kept every required statement (what is uncertain, what Claude got wrong, one next step) to one line each; nothing omitted or made untrue, since the rubric requires defensible claims | "Make sure the video looks like we are doing everything correct and … not give out too many negative things about us" | **My direction, within the rubric.** The full detail stays in `TEST-REPORT.md` and this log |
| The production script | Adopted my revised script as `SCRIPT.md`. Every number, file, version and label in it checked out against the repository; 16 lines were changed where they credited me with work Claude did under my direction (the lid gap, the corner assertion, the emission change, the Godot check fix, the sky, the hand-edit clean-up) or misstated the bookshelf approval | Wrote it myself and asked for it to be the production script, "accurately acknowledging Claude's contributions" | **My script, fact-checked.** Claude's first draft kept as `SCRIPT-draft-v1.md` |
| What the film shows of each asset | Proposed a re-render of the old emission 1.0 lamp for a before/after; the difference proved subtle. Then captured fresh four-view images of all three final assets from the committed `.blend` files | "Use only assets I generated, I mean my final versions … for doing before and all it's fine maybe" | **Final versions only.** The re-render and the earlier-version stills were deleted; earlier versions are narrated, not shown, except the hand edit and the prompt-and-result pair |
| Screen recordings for the film | Explained that I could not record the screen without permission; offered my own recordings, an engine capture, or granting VS Code the permission | "You do all the screen recordings for me" — granted VS Code Screen Recording and restarted | **Recorded.** Blender turntables of all three final assets captured from inside my session, a native 4K Godot engine orbit, hashes in `CAPTURE.md` |
| The boy in the showcase | Advised against generating him in 3D: an AI-generated mesh does not count and the generators must stay off, and a primitive figure would look worse; he is not required, because my character is 2D | "The character is not 3D and it looks bad … we don't need it in assignment requirements?" | **Removed.** The scene is now exactly the assignment's minimum; `char_remembered.png.import` restored byte-for-byte to its A2 original |
| Retaking the orbit screenshots without the boy | Keep them: they are the genuine record of the check I did, the assets they judge did not change, and the docs already say the boy was present then and removed after; the film opens B11 on the clean 4K orbit | Asked whether to retake them, then: "alright keep the originals" | **Kept as taken.** Eight of my Godot screenshots show the boy; the record is the check as it happened |

## Entries

<!-- One entry per work session, newest last. -->

### 2026-10-14 — The folder was never a repository, and a tag is the reason that matters

- **Date and what I was working on:** 2026-10-14, the setup phase of Assignment 3. No modelling, and deliberately none: the brief puts the "Learn the window" session and a committed `CHANGE-BRIEF.md` before any prompting, so that the sizes I predict are informed guesses rather than blind ones.

- **I tried / expected:** I expected this to be a naming problem. The assignment wants a repository beginning `walker-`, I already had a folder called `walker-houseghost-narasimha-v` sitting on my disk, and I pushed back three separate times asking why we could not simply push it, remap it, or duplicate it into my account. It looked like a repository to me.

- **What happened:** It was never a repository. There is no `.git` inside that folder — it belongs to the course repo four levels above it, so a push from inside it would have sent all 349 MB of `csye-7270-building-virtual-environments`, every classmate's work included, with my game buried at `fall-2026/narasimha-v/assignment-2/`. Wrong name, wrong contents, wrong shape.

  The argument that actually decided it was not the name at all, and I had not thought of it. Assignment 3 is submitted as a **tag**, and tags are global to a repository rather than scoped to a branch. An `a3` tag pushed to the shared course repo would collide with every other student's `a3`. Since Assignments 3 through 10 all tag the same repository, this was the last moment the move would cost nothing.

  Two things went wrong on the way. Claude created the new repository under `narasimhareddyvalamm` because that was the account `gh` reported as active; it should have asked, and I deleted the empty repo myself. Then the split exposed a gap I did not know existed: the game folder's own `.gitignore` never excluded `*.wav`, because the *course* repository's root ignore file had quietly been doing that job the whole time. Standing alone, the game would have begun committing WAV audio immediately, and `.blend1` backups the moment Assignment 3 starts — which the brief explicitly says not to commit.

- **What I did:** I set the two constraints that shaped the session before anything ran: do not lose Assignment 2, and never commit the assignment prompt. I rejected the account Claude had chosen. And when it started executing a plan I had agreed to without restating what the command would do, I stopped it mid-action and made stating intent first the rule — an agreed plan is not a standing permission to act unannounced. Nothing else: those were all the points I pushed back on that day.

- **What Claude or another person contributed:** Claude found the tag-collision argument, which is the reason the move was necessary rather than merely tidy. It offered both seeding routes with the trade-off stated and recommended `git subtree split`, which carried all 73 commits across with the game at the root. It took the 432 MB backup bundle unprompted once I raised the risk, used read-only operations throughout, pushed only to the new repository, and verified afterwards that the course repo was untouched. It caught the `*.wav` and `*.blend1` ignore gap. It read the Assignment 2 Godot project to recover the scale anchors below. And it argued itself out of its own first instinct on the asset list. The constraints, the account correction and the acceptances were mine.

- **What I understand now / still do not understand:** Two things, and the second matters more. The first is that the tag, not the repository name, is the real constraint — I had been reading the `walker-` rule as bookkeeping, when the thing that genuinely breaks is a label that has to be unique inside one repository and cannot be when thirty people share it.

  The second is a fault in my own game that Assignment 3 forced into the open. **My art does not agree with itself about scale.** Anchored on the boy's 320 px sprite it is roughly 250 pixels per metre; anchored on the door in `env_room_memory.png` at a standard two metres it is roughly 300. At 250 the ceiling reads 3.2 m and the door 2.44 m; at 300 the boy reads 1.07 m, short for the eight-year-old he is supposed to be. Both cannot be true, and every dimension in `CHANGE-BRIEF.md` has to be justified against one of them. A consequence falls straight out of it: at 250 px/m the music box sprite would be a 0.79 m object, so the relic art was drawn oversized for legibility on screen and was never to scale. Nothing in Assignment 2 ever made me measure it, because nothing in a 2D game does.

  Still unresolved: which of the two scales I commit to, which three assets I build, and whether the MCP will connect on this machine at all.

- **Evidence and next step:** Evidence: the new repository at `github.com/narasimhareddyvalam/walker-houseghost-narasimha-v`, 73 commits, game at the root; commit `54a86c3` adding the ignore rules; the backup bundle at `~/Desktop/csye-7270-backup-20261014.bundle`; the course repo verified afterwards still on `narasimhaReddyValam` at `a3fbb48` with the A2 folder intact and nothing pushed to `origin`. Next step: the "Learn the window" session in Blender, then settle the scale and the three assets and commit `CHANGE-BRIEF.md` before Claude builds anything.

- **Versions on this machine, 2026-10-14:** Blender **5.2.2 LTS** (build date 2026-09-15) — the chapter ran 5.1.2, so I am a version ahead, and anything that differs from the behaviour the brief describes gets recorded here rather than assumed to be my mistake. Godot **4.7.2.stable.official.ed1daf0bf**, matching the chapter. `uv` **0.13.1** via Homebrew. GNU `coreutils` for `timeout`. macOS **26.6.2**, Apple Silicon.

### 2026-10-14 — Both setup lines from the chapter failed, and neither failure was the MCP's fault

- **Date and what I was working on:** 2026-10-14, immediately after the repository move: the two command-line steps that register the MCP server and install the Blender add-on. The brief says to treat each line as a claim to check and to write down what differs on my machine, so this entry is that.

- **I tried / expected:** I expected two copy-paste commands and a connected server. The chapter prints both lines exactly, and I had no reason to think either would need editing.

- **What happened:** Both failed, for unrelated reasons, and neither was a problem with the MCP project.

  **First line, verbatim from the chapter:**

  ```
  claude mcp add -e DISABLE_TELEMETRY=true blender -- uvx mcp-for-blender
  ```
  ```
  Invalid environment variable format: blender, environment variables should be
  added as: -e KEY1=value1 -e KEY2=value2
  ```

  `claude mcp add --help` gives the signature as `claude mcp add [options] <name> <commandOrUrl> [args...]`, and documents `-e, --env <env...>` as **variadic**. Because `-e` accepts a list, putting it before the server name made it swallow `blender` as a second environment variable, leaving no name for the server. The chapter's own note says this combination is "the chapter's adaptation, not a README line", which is consistent with it never having been run. Moving the name in front of the flag works:

  ```
  claude mcp add blender -e DISABLE_TELEMETRY=true --scope user -- uvx mcp-for-blender
  ```

  I added `--scope user` on top of the fix, so the server is registered for every project directory rather than only the one the session happened to start in. `claude mcp get blender` then reports `Status: ✔ Connected`, which I am treating as "the stdio process launches", not as "it can reach Blender" — Blender is not running yet, so that claim is untested.

  **Second line, verbatim from the chapter:**

  ```
  uvx mcp-for-blender install-addon
  ```
  ```
  Could not find a Blender user addons directory. Set BLENDERMCP_ADDONS_DIR to your
  Blender scripts/addons path, or install addon.py manually from the repo.
  ```

  The cause is mine, not the tool's: I had installed Blender an hour earlier and never opened it. `~/Library/Application Support/Blender/` does not exist, because Blender creates its user directory on first launch. The installer is looking for something that cannot exist yet.

  Worth recording separately: **that command exited 0.** It printed a failure and reported success to the shell. The brief warns about exactly this shape of trap with Blender's `--python-exit-code 1`, and it turns out to apply here too — a script that chained these steps would have carried on as though the add-on were installed.

- **What I did:** I did not reach for `BLENDERMCP_ADDONS_DIR` or install `addon.py` by hand, which is what the error suggests. Both would have papered over a one-line cause. The fix is to open Blender once, which I have to do anyway for the "Learn the window" session, and then re-run the installer. I was not surprised. Tools change between versions, and I expected some of the chapter's setup to break on a newer machine than the one it was written on.

- **What Claude or another person contributed:** Claude ran both commands, read `claude mcp add --help` rather than guessing at the syntax, diagnosed the variadic `-e` as the cause of the first failure, checked for the Blender user directory rather than assuming the add-on installer was broken, and noticed the exit-0 behaviour. The decision not to force the add-on path manually was mine.

- **What I understand now / still do not understand:** A documented command is a claim about a version, not a fact. Both of these lines are probably correct for the versions the chapter ran against; neither is correct here, and one of them the chapter admits it assembled rather than copied. The second lesson is the one I will carry further: a tool that prints an error and exits 0 is worse than one that crashes, because every check downstream of it keeps passing. Still unresolved: whether the add-on installs cleanly once Blender has a user directory, and whether the server can actually drive a running Blender — everything so far has tested the client side only.

- **Evidence and next step:** Evidence: the two error strings above, quoted exactly; `claude mcp get blender` output; the absence of `~/Library/Application Support/Blender/`. Next step: open Blender for the first time and do the "Learn the window" session, then re-run `uvx mcp-for-blender install-addon` and enable the add-on in Preferences.

### 2026-10-14 — The add-on was never broken; Blender was holding a stale list

- **Date and what I was working on:** 2026-10-14, straight after the installer finally succeeded. Opening Blender for the first time created `~/Library/Application Support/Blender/5.2/`, and re-running `uvx mcp-for-blender install-addon` wrote the file:

  ```
  Installed MCP for Blender addon to /Users/narasimhareddyvalam/Library/Application
  Support/Blender/5.2/scripts/addons/blender_mcp.py
  ```

- **I tried / expected:** I went to Edit → Preferences → Add-ons expecting to tick one box and be done. The file was on disk, in the directory the installer named, and nothing about that looked ambiguous.

- **What happened:** Enabling it failed, in the Preferences window and again in the status bar:

  ```
  Add-on not loaded: "blender_mcp", cause: No module named 'blender_mcp'
  ```

  The obvious reading is that Blender 5.2 has stopped looking in `scripts/addons` — 4.2 introduced the extensions system, and the brief has already warned me twice that this version is ahead of the one the chapter ran. That reading was wrong, and it would have cost me an afternoon.

  Rather than guess, Claude asked Blender where it actually looks:

  ```
  ADDON DIRS: ['/Users/.../Blender/5.2/scripts/addons']
  EXTENSIONS: /Users/.../Blender/5.2/extensions
  ```

  The file was in a directory Blender scans. So the next question was not "is the path right" but "can Blender load this file at all", which is a different test — and one that can be run headless, away from my session:

  ```
  blender_mcp in list: True
  BlenderMCP addon registered
  ENABLE RESULT: <module 'blender_mcp' from '.../scripts/addons/blender_mcp.py'>
  ```

  It loads and registers without complaint. **Nothing was wrong with the add-on, the path, or Blender 5.2.** The only broken thing was the Blender I had open: it scans that directory when it starts, and it had been running since before the file existed at 15:47. It was reporting, accurately, that it knew of no such module.

- **What I did:** Quit Blender and reopened it. The add-on enabled on the first tick with no error, which settles it. Four things I then recorded from the `N`-panel rather than assumed:

  - It reports **"Connected on port 9876"**, and while connected the button reads **"Disconnect"**. That is a *fourth* name for this control: the brief already notes the README says "Start MCP Server" in one place and "Connect to Claude" in another, while the add-on code says "Connect to MCP server".
  - The add-on is listed as plain **"MCP for Blender"**, not "Interface: MCP for Blender" as the brief has it.
  - Every remote service is off, as required and as shipped: Poly Haven, Sketchfab, Poly Pizza, Hyper3D Rodin and Tencent Hunyuan 3D all unchecked, with "No API keys?" shown beside the generation section.
  - The panel reports **Addon 1.8 · up to date**, which is not a version the brief mentions at all. The installed package is **`mcp-for-blender` 2.1.9**, which is the version whose nine-tool list the brief describes, and the server log line `Blender addon on disk is current (protocol 13)` is the check that actually matters between the two. The add-on carries its own version number; 1.8 and 2.1.9 are not in conflict.

  I also had the socket checked rather than trusting the panel, because the brief is specific that this thing has no authentication and should stay on localhost:

  ```
  COMMAND   PID    USER                FD  TYPE  NAME
  Blender   79619  narasimhareddyvalam 8u  IPv4  TCP 127.0.0.1:9876 (LISTEN)
  ```

  Bound to `127.0.0.1`, not `0.0.0.0` — reachable only from this machine. I will switch the add-on off in Preferences at the end of every session, as the brief's safety note advises, and turn it on again only when I am working with Claude in Blender.

- **What Claude or another person contributed:** Claude refused to act on the plausible explanation. It queried `bpy.utils.script_paths(subdir='addons')` to establish where Blender looks before arguing about whether the path was wrong, then ran `addon_utils.enable()` in a headless Blender to separate "the add-on is broken" from "my session is stale". Two commands, and the answer came back unambiguous. The decision to stop and check rather than start moving files was its call, and the right one.

- **What I understand now / still do not understand:** This is the same fault I had in Assignment 2 with the Godot editor — it kept the open scene in memory and happily played a build that no longer existed, and I lost real time to it twice before we found it. **A running editor is a cache, and installing something underneath one proves nothing.** It is the second time this project has cost me an hour to that, and the general rule I should have carried over is: when a tool says something does not exist, check whether the tool has looked since it changed.

  The second thing is narrower and worth keeping. "No module named X" reads like a path problem and invites you to start moving files, which would have left me with the add-on installed in two places and no idea which one loaded. The cheap test — can a *fresh* process load it — answers the real question and changes nothing on disk.

  Still unresolved: whether the server, once started from the add-on's panel, can actually be driven from Claude Code. Everything so far has tested the client and the add-on separately; nothing has yet connected the two.

- **Evidence and next step:** Evidence: the Preferences error quoted exactly; `ADDON DIRS` and `EXTENSIONS` output; the headless `addon_utils.enable()` result showing "BlenderMCP addon registered". Next step: enable the add-on in the restarted Blender, start the server from the `N`-panel's MCP tab with every download and generation option left off, restart Claude Code so it sees the server, and call `get_scene_info` as the first real test of the connection.

### 2026-10-14 — The MCP reads my real scene; my commits were signed by nobody

- **Date and what I was working on:** 2026-10-14, the first call after the add-on connected — the test the brief names as predicted failure case 6, before any build is approved. Followed straight away by a check I asked for on which GitHub account my commits land under.

- **I tried / expected:** The brief's worry was that "Connected" only proves a process launched. I expected `get_scene_info` either to fail outright or to return my open scene. On the commits, I expected everything to be under `narasimhareddyvalam` already, since that is the account the repository lives on.

- **What happened:** The connection works end to end. `get_scene_info` returned Blender's actual default scene, unsaved, with values that only a live session could report:

  ```
  Scene 'Scene' | 1 camera, 1 light, 1 mesh | active Cube | selected Cube | mode OBJECT
  (unsaved) | engine BLENDER_EEVEE | frames 1-250 (now 1) at 24 fps | 1920x1080 | camera Camera | HDRI none | unit scale 1.0
  Cube   | mesh   | at (0.0, 0.0, 0.0)   | size 2.0x2.0x2.0 | 6 faces | mat Material
  Light  | light  | at (4.08, 1.01, 5.9) | point 1000.0W
  Camera | camera | at (7.36, -6.93, 4.96) | rot (64, 0, 47)
  ```

  The commit check found something real. This repository had no `user.email` set, locally or globally, so Git fell back to `narasimhareddyvalam@Narasimhas-MacBook-Air.local`, built from the machine's hostname. Six commits carry it — `54a86c3` and all five Assignment 3 commits. GitHub links that address to **no account at all**, single m or double. The 73 commits carried over from Assignment 2 use `valam.n@northeastern.edu`, and the GitHub API resolves one of them (`7fead95`) to `narasimhareddyvalam`.

- **What I did:** Required every commit to be credited to my own GitHub account, `narasimhareddyvalam`, and had the identity checked rather than assumed — which is what exposed the problem. It is now set explicitly, in this repository's local config only, so nothing else on the machine changes. I then had the five unpushed Assignment 3 commits rewritten onto the linked address, with a backup branch `backup/pre-author-rewrite` taken first. Only the author changed: the original timestamps were kept, and `git diff` against the backup is empty. The hashes did change, so the change brief committed before any building is now `722658f`, still at 17:48. `54a86c3` was left alone — it is already on `origin/main`, and fixing it would need a force-push to a published branch, which costs more than one unlinked commit does.

- **What Claude or another person contributed:** Claude ran `get_scene_info` before proposing any geometry, as the brief requires. On the identity, it read `git config` and `gh auth status` instead of assuming, noticed the hostname address in the log, and confirmed through the GitHub API which account the university address belongs to. The instruction to check, and the account it had to be, were mine.

- **What I understand now / still do not understand:** Case 6 is answered for reading; it is not yet answered for writing, and nothing has been built. On the commits: an unset identity is not an error Git reports. It quietly signs with a made-up address, and the work looks fine locally while appearing on GitHub under nobody. Still unresolved: whether `execute_blender_code` changes the live scene as reliably as `get_scene_info` reads it.

- **Evidence and next step:** Evidence: the `get_scene_info` output above; `git log --format='%h %ae'` showing the six hostname-address commits; `gh api repos/narasimhareddyvalam/walker-houseghost-narasimha-v/commits/7fead95 --jq .author.login` returning `narasimhareddyvalam`; `git config --local user.email` now reading `valam.n@northeastern.edu`. Next step: approve the music-box build plan, then one `execute_blender_code` call per object.

### 2026-10-14 — The music box, built in six calls

- **Date and what I was working on:** 2026-10-14, the first asset. Five primitives under a `MusicBox` root empty, as specified in the change brief.

- **I tried / expected:** I expected the brief's numbers back from Blender, and a triangle count near the 274 I had estimated.

- **What happened:** It built as specified, and the numbers match in both Claude's own report and `get_scene_info`'s independent one:

  ```
  asset min [-0.12, -0.0885, 0.0] max [0.148, 0.0869, 0.1795] size [0.268, 0.1754, 0.1795]
  tris 252 / 320 | objects 5 / 5
  every object: rot (0,0,0) scale (1,1,1) non-manifold 0 inward-facing 0
  meshes:    MB_Body MB_Clasp MB_KeyHandle MB_KeyShaft MB_Lid
  materials: M_Brass M_Wood_Dark M_Wood_Warm
  ```

  The body is exactly 0.24 × 0.17 × 0.12. Four things differ from the brief, and none was hidden:
  - **The height with the lid ajar is 0.1795 m, not 0.180.** The lid's 2 mm bevel rounds its front-top corner, which is the highest point.
  - **The lid sits about 0.6 mm above the body at the hinge**, because the same bevel pulls the lid's back-bottom edge in off the hinge line. It is invisible at game scale, but it is a gap.
  - **The asset is 0.268 wide, not 0.24.** The key sticks out of the right side. The brief's 0.24 is the body, and prediction 2's three-way comparison has to use the same thing in all three places.
  - **252 triangles, not the 274 estimated.** A 2-segment bevelled cube is 108, not ~130. The estimate was wrong; the budget held.

  The lid thickness of 0.008 m was not stated in the brief. It is the only thickness that makes 0.18 m overall possible at 18°.

  In the viewport it reads as a music box from the front and the three-quarter view. **From behind it reads as a closed chest**, because the key is out of sight and nothing else says "music box". The key's bow is 35 mm on a 268 mm box, smaller in proportion than in `relic_musicbox.png`. Both were noted before any export, and they are what predicted failure 7 is for.

- **What I did:** Held the plan to a best-practice review before approving anything, which brought in two improvements — smooth shading by angle, and the lid's origin on its hinge so it could swing open later — and approved it with both. When asked whether the key needed to be larger and whether the back view mattered, I left the call to Claude: "whatever will help us add details to it more nicely." What it chose is the next entry.

- **What Claude or another person contributed:** Claude derived the lid thickness from the brief's own numbers, ran the full script headless into a scratch file before touching the live session so that any Blender 5.2 API difference would fail there instead, then sent one call per object, each followed by an independent `get_scene_info` reading. It flagged that the art shows the lid thrown wide open while the brief says ajar, and that the box in the art is nearly cubic. Both are recorded here, not changed.

- **What I understand now / still do not understand:** The interesting numbers were not the ones I chose. They came from my choices combining: the height the bevel cost, the gap at the hinge, and the width the key added. Still unverified: whether the colours, the smooth shading and the +Z-up orientation survive the glTF export, and whether the box reads at game scale in Godot. Nothing has been exported yet.

- **Evidence and next step:** Evidence: `tools/blender/build_musicbox.py` — the headless run (`blender -b --factory-startup -P`) and the six live calls printed identical numbers; `blender/musicbox.blend`; the four-view `look` image in material shading. The live calls sent each step without the script's `__main__` block, and the save step used a literal path where the script reads one from its arguments. Next step: build the lamp the same way.

### 2026-10-14 — The key was made larger, and the back view only partly improved

- **Date and what I was working on:** 2026-10-14, immediately after the music box was built. The open question from the last entry: whether the key was large enough to do its job.

- **I tried / expected:** I asked what the open marker wanted from me, then left the decision with Claude. It recommended enlarging the key and adding nothing else, expecting the larger key to help with the back view as well.

- **What happened:** The key went from a 35 × 25 mm bow to 50 × 40 mm, and the shaft from r 5 mm to r 6 mm. Both live and headless, the asset now measures **0.275 × 0.1754 × 0.1795 m at 252 triangles** — the same triangle count, because only the sizes changed. Re-running the two steps replaced `MB_KeyShaft` and `MB_KeyHandle` by name; no `.001` appeared. From directly behind, the key now shows in the silhouette, where before it did not. **From behind and to the left it still reads as a plain chest**, because the key is on the far side. That part was not fixed, and it was not claimed to be.

- **What I did:** Set the goal — the box should read better without breaking the brief — and delegated the specific change within it, then reviewed the result from four angles before moving on. The instruction is quoted in the decisions table.

- **What Claude or another person contributed:** The recommendation and its reasoning: the key is the brief's own named identifier, it was about 9 px tall at game scale, and enlarging it cost nothing, while adding parts to the back would have been over-building against the brief. It recorded the change as a dated revision rather than editing the specification, and it confirmed the result in two independent runs.

- **What I understand now / still do not understand:** The decision changed proportion, not structure, which is why it cost nothing. Whether 50 mm is enough is still a guess until the box is seen at game scale in Godot.

- **Evidence and next step:** Evidence: `CHANGE-BRIEF.md` revision A3-1; `tools/blender/build_musicbox.py` steps 3 and 4 with the revision noted inline; the second four-view `look` image (front, three-quarter, back, behind-left). Next step: the bedside lamp.

### 2026-10-14 — The music box rebuilt: hollow, on a plinth, six shapes

- **Date and what I was working on:** 2026-10-14. After seeing the first music box in Blender I said it was "too simple" and that I wanted it "more visually appealing" and "realistic graphics".

- **I tried / expected:** I wanted to generate a reference in ChatGPT and have Claude build from it. My first instinct was realism in the textured sense.

- **What happened:** Claude pointed out that the assignment requires flat colour and no painted textures, at most six shapes and 500 triangles, and offered three routes. I chose realism through lighting and shape. ChatGPT produced `design/ref-musicbox-chatgpt.png` from a prompt Claude wrote for exactly that. The rebuild came out at:

  ```
  asset min [-0.13, -0.095, 0.0] max [0.186, 0.095, 0.2968] size [0.316, 0.19, 0.2968]
  tris 312 / 320 | objects 6 / 6
  every part: rot (0,0,0) scale (1,1,1) non-manifold 0 inconsistent-winding 0 signed volume outward
  ```

  The hinge gap from the first build is gone: the lid's lowest point is at exactly 0.135 m, the top of the rim. The key is visible from the front, from the three-quarter view and from directly behind. From behind and to the left it is still hidden.

  **Two things went wrong on the way and were caught before anything ran live.** The first headless run reported `cavity faces 1`: only the floor of the box took the dark material, because Claude's test for which faces were inner walls was wrong. It was replaced with a plain bounds test and re-run (`cavity faces 5`). Separately, the original normals check — "does each face point away from the object's centre" — is only valid for convex parts; the inner walls of a hollow box correctly point *toward* the centre, so it would have reported a false failure. It was replaced with two checks that hold for any closed mesh: every edge consistently wound, and a positive signed volume.

  One rendered `look` came back almost black. That was not a fault: the build deletes the scene's light so the `.blend` holds only the asset, and Rendered mode uses scene lights. Material Preview was used instead.

- **What I did:** Rejected the first build as too plain; generated the reference image; chose the inside-the-rules route to realism; set the goal as following the assignment requirements and best practice while being realistic and creative.

- **What Claude or another person contributed:** Claude identified that "realistic" in the textured sense would break the flat-colour rule, wrote both ChatGPT prompts, chose what to take from the image and what to leave and why, proposed baking weighted normals for rounded-edge shading at no triangle cost, corrected its own key-bow orientation (the first bow was at right angles to the shaft, like a T-handle), and found and fixed both of its own check errors before the live build. The judgement that the first build was too plain was mine.

- **What I understand now / still do not understand:** After orbiting the rebuild in Blender: "yes lets go to next. i am happy with this one." Realism through lighting and shape, inside the rules, is what I meant. I will judge it again once the box is lit in Godot.

- **Evidence and next step:** Evidence: `design/ref-musicbox-chatgpt.png`; `CHANGE-BRIEF.md` revision A3-2; `SOURCES.md` row REF-MUSICBOX-3D; `tools/blender/build_musicbox.py`, which the live calls executed directly; `blender/musicbox.blend`. Next step: the bedside lamp.

### 2026-10-14 — The bedside lamp, built and seen from below

- **Date and what I was working on:** 2026-10-14, the second asset, straight after approving the music box.

- **I tried / expected:** I approved the five-shape plan and asked that every assignment requirement be followed.

- **What happened:** It built at exactly the brief's size, and every part checks:

  ```
  asset min [-0.1, -0.1, 0.0] max [0.1, 0.1, 0.42] size [0.2, 0.2, 0.42]
  tris 326 / 340 | objects 5 / 6
  every part: rot (0,0,0) scale (1,1,1) non-manifold 0 inconsistent-winding 0
  closed parts: signed volume outward | LP_Shade: 24 open edges (its open bottom, intended)
  shade: sides facing outward 24 / 24 | cap normal z +1.00 | double-sided True
  ```

  Seen from below, the open shade shows its lit inside, the bulb and the neck — the reason it was left open. Two things are noted rather than fixed: the visible neck is longer and thinner than in the painting, and the 12-segment base shows facets close up.

  **Re-reading the assignment before building changed the plan.** The showcase scene is specified as "floor, one light, a camera", and Claude had proposed a light inside the lamp. It withdrew that before anything ran; the glow comes from the material instead. The same reading showed that the assignment asks for every call *body* to be copied into the build script, so both scripts now end with a verbatim log.

  **Claude's own check was wrong twice, both caught in the headless run.** It reported "cap normal z +0.20" — a side face, because it had taken the last face to be the cap — and then "24 / 25" sides, because Blender makes a new Python object for a face each time it is read, so an identity comparison never matches. Both were fixed and re-run before the live build, so the claim that the cap faces up was tested, not assumed.

  Step 0 saved the emptied session as `blender/lamp.blend` immediately, because the session had been `musicbox.blend`; `git status` confirmed the music box file untouched.

- **What I did:** Approved the plan on the condition that every assignment requirement was followed. That condition prompted a full re-read of the assignment before building, which caught the one-light rule and the call-body rule while they were still cheap to fix.

- **What Claude or another person contributed:** The design changes and their reasons; the catch on the one-light rule; the shared library, with a before/after diff proving it changed nothing; the session-file safeguard; finding and fixing both of its own check errors.

- **What I understand now / still do not understand:** After orbiting it in Blender: "i want more realsitc one, give me prompt to give to chatgpt." It looked old-fashioned, and too plain — closer to a game placeholder than to a real lamp.

- **Evidence and next step:** Evidence: `tools/blender/build_lamp.py` with its `LIVE_CALLS` log; `tools/blender/asset_lib.py`; `blender/lamp.blend`; `CHANGE-BRIEF.md` revision A3-3; the four-view `look` image including two views from below. Next step: the bookshelf.

### 2026-10-14 — The first lamp references came back too old-fashioned, so I regenerated them

- **Date and what I was working on:** 2026-10-14, the reference image for a more realistic lamp, generated in ChatGPT from the prompt Claude wrote.

- **I tried / expected:** I expected the prompt to give me a realistic lamp I could build from.

- **What happened:** In my words: "chatgpt didnt give me what i like, it gave me too old styles." The prompt described a gourd-shaped ceramic base, a brass neck and a cone shade — a traditional bedside lamp, because that is what the painting in `env_room_memory.png` shows — and the results read as dated rather than realistic. Two rounds were rejected before the one I chose: the result of the first prompt, and an 18-lamp grid from the follow-up "give more diff shapes". I kept neither; the only image downloaded is the one used.

- **What I did:** Rejected those results, kept generating in ChatGPT myself, and downloaded the one I liked. Two follow-ups, verbatim from the ChatGPT conversation: "give more diff shapes", which returned an 18-lamp grid of traditional shapes, then "give me modern, realistic one", which returned the image I chose.

- **What Claude or another person contributed:** Claude wrote the original prompt. The rejection, the regeneration and the choice of image were mine, done in ChatGPT outside this session. Claude has not seen the chosen image yet.

- **What I understand now / still do not understand:** Both things together: a shape that looks like a lamp you could buy today, and light that falls on it convincingly. Still open: the lamp in my painting is a traditional one, so a modern reference moves the 3D lamp away from the 2D art. That may be the right call, but it should be stated in revision A3-4 when the lamp is rebuilt.

- **Evidence and next step:** Evidence: the chosen image, to be added as `design/ref-lamp-chatgpt.png` with a `SOURCES.md` row REF-LAMP-3D. Next step: share the image, then Claude checks it against the six-shape and triangle limits and proposes revision A3-4 before building.

### 2026-10-14 — The lamp rebuilt as a modern ceramic lamp

- **Date and what I was working on:** 2026-10-14, rebuilding the lamp from the modern reference I chose.

- **I tried / expected:** A lamp that looks like `design/ref-lamp-chatgpt.png`: a glossy pill-shaped ceramic base, a wide drum shade, brass details.

- **What happened:** Built in seven calls after `get_scene_info`, and it checks:

  ```
  asset min [-0.14, -0.14, 0.0] max [0.14, 0.14, 0.42] size [0.28, 0.28, 0.42]
  tris 406 / 420 | objects 6 / 6
  every part: rot (0,0,0) scale (1,1,1) non-manifold 0 inconsistent-winding 0
  closed parts: signed volume outward | LP_Shade: 24 open edges (open bottom, intended)
  base: rim edges bevelled 24 (expect 24) | shade: 24 / 24 sides outward, cap +1.00, double-sided
  ```

  It follows the reference closely from the front and three-quarter views, and from below the bulb and neck show inside the shade. The neck passes 15 mm through the shade's top and becomes the finial, so the six-shape limit held. The shade's top is closed where the reference's is open on a wire fitter, which six shapes cannot build. At close range the 12-sided base shows facets on its outline, and the glossy ceramic only reads properly once something is there to reflect, which is Godot's job.

  Before clearing the A3-3 lamp, Claude checked whether I had hand-edited it — the hand edit is one of my deliverables and clearing the scene would have destroyed it. Every value matched the saved build; the "unsaved changes" flag came from view and selection changes.

  The lamp is now 0.28 m wide rather than the original brief's 0.20, and modern rather than the traditional lamp in my painting. Both are stated in revision A3-4.

- **What I did:** Chose the modern reference, raised the budget to 420 before building, and provided the ChatGPT conversation so the prompts could be recorded.

- **What Claude or another person contributed:** Read the reference into six buildable shapes, used the neck as the finial to stay within six, priced the rounded base and offered the two budget options, kept the screenshot out of the repository, and checked for a hand edit before clearing the scene.

- **What I understand now / still do not understand:** I am happy with it. It matches the reference well enough to move on.

- **Evidence and next step:** Evidence: `design/ref-lamp-chatgpt.png`; `SOURCES.md` rows REF-LAMP-3D-01, -02 and REF-LAMP-3D; `CHANGE-BRIEF.md` revision A3-4; `tools/blender/build_lamp.py` with its call log; `blender/lamp.blend`. Next step: the bookshelf.

### 2026-10-14 — The bookshelf, built to the brief's exact size

- **Date and what I was working on:** 2026-10-14, the third and last asset.

- **I tried / expected:** The bookshelf from my own A2 art at the brief's size, with the same standard as the music box and lamp.

- **What happened:** It built cleanly, first time, at exactly the specified size:

  ```
  asset min [-0.32, -0.15, 0.0] max [0.32, 0.15, 1.0] size [0.64, 0.3, 1.0]
  tris 296 / 360 | objects 6 / 6
  every part: rot (0,0,0) scale (1,1,1) non-manifold 0 inconsistent-winding 0 signed volume outward
  coplanar faces between parts: 11, all facing each other (hidden joints), 0 facing the same way
  ```

  Two things in the first images looked like faults and were checked rather than assumed. A zig-zag along the low shelf's front edge was the image being scaled down — close up the edge is clean. Lighter rectangles on the back panel were Material Preview's reflections. A scan of every pair of faces found no two in the same plane facing the same way, which is what z-fighting needs.

- **What I did:** Approved the build with a back panel as the sixth shape, holding it to the same checks as the other two assets.

- **What Claude or another person contributed:** Claude read the art's dark interior as a back panel and proposed it, built the six boards, checked for a hand edit before clearing the lamp, and wrote the coplanar-face scan to rule out z-fighting.

- **What I understand now / still do not understand:** All three assets are now built. What none of the Blender checks can show is how they look at game scale beside each other and lit — that is the Godot scene.

- **Evidence and next step:** Evidence: `tools/blender/build_bookshelf.py` with its call log; `blender/bookshelf.blend`; `CHANGE-BRIEF.md` revision A3-5; the four-view `look` image. Next step: export all three as binary glTF.

### 2026-10-14 — Export, import and the showcase scene: one wrong check, two real findings

- **Date and what I was working on:** 2026-10-14, exporting the three assets, importing them into Godot and placing them side by side with a 1 m cube and the boy's 1.00 m capsule.

- **I tried / expected:** Clean exports, a clean import, a passing check, and a scene that shows the assets as realistic as flat colour allows.

- **What happened:** Four things, in order.

  1. **The first export failed, on purpose-built safety.** The exporter script read the list of valid formats before exporting, and the glTF exporter only fills that list in at call time, so it read empty and the script stopped itself. `--python-exit-code 1` turned that into exit code 1 and nothing was written — exactly what the assignment says the flag is for. The guard was removed; all three exported with exit 0.

  2. **The exports were verified from the files themselves**, with a stdlib reader (`tools/inspect_glb.py`) independent of both Blender and Godot. Every base colour reads back as the exact hex in the brief, triangle counts match (312, 406, 296), height lies on +Y, the lowest point is at y = 0, and no node carries rotation or scale.

  3. **The first Godot check failed all nine assertions, and the check was wrong, not the assets.** It measured each part with `global_transform` while the instance was not yet inside the scene tree; Godot then returns an identity transform without failing, so every part was measured at the origin — the bookshelf's "lowest point" came out at −0.4875 m, exactly half a side panel. Rewritten to compose transforms itself, it passes: all three match the brief within 2 mm, height along Y, lowest point 0, every node scale 1. **It was then run against a deliberately wrong expected height to prove it can fail** — it reported FAIL and exited 1.

  4. **The first render showed two real problems.** The lamp shade clipped to pure white, losing its cream (emission 1.0 plus lighting exceeds white), and the brass read near-black, because fully metallic brass shows its colour only by reflecting its surroundings and the sky was too dim. The emission was lowered to 0.4 at the source (revision A3-6) and the sky's reflection energy raised. After both, the cream and the brass read correctly. The trade-off: the brighter sky also lifts the ambient light, so the woods read a little lighter than their hex values.

- **What I did:** Required every step to follow the assignment's process, including the script route's exit-code flag and an honest account of what the check does not prove.

- **What Claude or another person contributed:** The exporter and inspector scripts, the check and its fix, the negative test, the showcase scene and its two render passes. Every number above comes from a command run in this session and saved in `evidence/`.

- **What I understand now / still do not understand:** A check that passes proves only what it measures, and this one nearly proved the opposite of the truth. What it cannot show at all is whether the assets read as what they are from behind and below; that is the orbit check, still to be done in the editor.

- **Evidence and next step:** Evidence: `evidence/a3-inspect-glb.txt`, `evidence/a3-check-assets.txt`, `evidence/a3-showcase.png`; `godot/tests/check_assets.gd`; `godot/scenes/AssetShowcase.tscn`; `CHANGE-BRIEF.md` revision A3-6. Next step: the test report and the remaining documents.

### 2026-10-14 — The bookshelf rebuilt as a modern piece: a passing check that was still wrong

- **Date and what I was working on:** 2026-10-14, the third asset, rebuilt from a modern reference to match the standard of the other two.

- **I tried / expected:** A bookshelf like `design/ref-bookshelf-chatgpt.png`: thick sides with rounded top corners rising above the top board, two shelves, an open bottom bay, a darker inset back.

- **What happened:** The final build matches it:

  ```
  asset min [-0.32, -0.15, 0.0] max [0.32, 0.15, 1.0] size [0.64, 0.3, 1.0]
  tris 248 / 360 | objects 6 / 6
  every part: rot (0,0,0) scale (1,1,1) non-manifold 0 inconsistent-winding 0 signed volume outward
  side panels: rounded corners 2, front edges 2, front face top z = 0.9700 (expect 0.9700)
  Godot: bbox (0.6400, 1.0000, 0.3000), height along Y, lowest point 0.0000 — RESULT: PASS
  ```

  Getting there took three corrections, all Claude's, all caught before the result was accepted. Its first filter for the corner edges matched the wrong edges, and its own assertion stopped the build. Then the first live build **passed every numeric check with square corners** — the signature detail of the reference was missing, and only the views showed it. The cause was bevel order: softening the front edges first let Blender's overlap clamp shrink the 3 cm rounding to about 3 mm. With the corners rounded first, a new check asserts the front face stops 3 cm below the top; on its first run that check failed on its own arithmetic (it compared a centred mesh's local height with a world height), and was corrected to read 0.9700 m.

- **What I did:** Asked for a more realistic bookshelf, directed the reference toward small realistic details and a unique modern style within six boards, and approved the design.

- **What Claude or another person contributed:** Both ChatGPT prompts; reading the reference into six boards; the build; the three fixes; the export, the re-check in Godot and the new showcase render.

- **What I understand now / still do not understand:** This is the clearest case so far of a check proving less than it seems to. Size, scale, orientation and normals were all correct, and the asset was still not the one specified. Looking at it is a check in its own right.

- **Evidence and next step:** Evidence: `design/ref-bookshelf-chatgpt.png`; `SOURCES.md` row REF-BOOKSHELF-3D; `CHANGE-BRIEF.md` revision A3-7; `tools/blender/build_bookshelf.py` and its call log; `blender/bookshelf.blend`; `godot/assets/models/bookshelf.glb`; `evidence/a3-check-assets.txt`, `evidence/a3-inspect-glb.txt`, `evidence/a3-showcase.png`.

### 2026-10-15 — My hand edit: a third shelf, and what dragging in the viewport actually does

- **Date and what I was working on:** 2026-10-15, the hand edit the assignment asks for — one change made with the mouse in Blender's own window.

- **I tried / expected:** I wanted a change that would be visible in the film, so I added a third shelf: I duplicated a shelf and dragged the copy down to just above the floor. I expected a clean new shelf.

- **What happened:** It worked visibly and was messy underneath, which my own screenshots record (`evidence/a3-hand-edit-attempt-duplicate.png`, `a3-hand-edit-during-own.png`, `a3-hand-edit-third-shelf-own.png`):
  - My first attempt duplicated the shelf **together with its parent**, so a second root, `Bookshelf.001`, appeared, and I undid it.
  - Dragging moved the shelves on **all three axes**: up to 1 cm sideways and backwards as well as up or down, which pushed them into the side panel and through the back.
  - The final duplicate again came with its parent, ended about 7 cm proud of the front, and brought a **copy of its material**, `M_Wood_Warm.001` — a sixth material outside the library.
  - The bookshelf now had **seven boards**, one over the course limit.

  I asked for the back panel to stay as well, then decided to keep it open-backed rather than break the limit. Claude tidied the edit in one recorded call: the copy re-parented and renamed `BS_Shelf_Bottom`, the duplicate root and material deleted, the shelves re-centred at my heights rounded to even 26 cm bays (0.12 / 0.40 / 0.68 m), made dark wood against the warm frame, and the back panel removed. Result: six boards, 280 / 360 triangles, no `.001` anywhere, the Godot check still passing. The build script was updated to match, and its headless rebuild equals the edited `.blend` object for object.

- **What I did:** Made the edit with the mouse, took my own screenshots during it, chose to keep three shelves and drop the back panel.

- **What Claude or another person contributed:** Read the scene after each of my changes and reported exactly what had moved; laid out the options for the seventh board; did the tidy-up, the before and after screenshots from one camera, the script update, the export and the re-check.

- **What I understand now / still do not understand:** Four things. Dragging the white circle of the Move gizmo moves an object freely on every axis; the arrow, or pressing Z after Shift+D, locks it to one. Shift+D copies whatever is selected, so with the parent selected it copied the whole parent. Blender names every copy `.001` silently — objects, meshes and even materials — which is exactly what the brief's naming rule exists to catch. And a fixed limit forces trade-offs: a third shelf cost me the back panel.

- **Evidence and next step:** Evidence: `evidence/a3-hand-edit-before.png` and `evidence/a3-hand-edit-after.png` (same camera), my three screenshots above, `CHANGE-BRIEF.md` revision A3-8, `tools/blender/build_bookshelf.py`, `blender/bookshelf.blend`, `evidence/a3-check-assets.txt`. Next step: the orbit check in Godot.

### 2026-10-15 — The boy in the showcase, and his real height

- **Date and what I was working on:** 2026-10-15, before the orbit check: the showcase scene's two reference objects, a grey 1 m cube and a 1.00 m capsule.

- **I tried / expected:** I did not like them in the scene and asked whether they were required. I expected they were.

- **What happened:** They were not. The assignment asks for "a floor, one light, a camera, and your three assets side by side at game scale"; the cube and capsule came from my own plan. Claude proposed replacing both with the boy himself — my game's own sprite, `char_remembered.png`, as a flat figure at 250 px per metre that turns to face the camera — which answers the orbit check's "at game size, beside your character" more directly than either did.

  Placing him exposed an error in my brief. The scale table says his sprite is 320 px, 1.28 m. Measured, his standing figure is **341 px — 1.36 m**; 320 was his walking height (303–317 px). A throwaway headless probe put his feet at y = 0.0000 and his head at 1.3640 m, and the scene still has exactly one light. In the render he stands beside his props and is visibly taller than the 1.00 m bookshelf — consistent with the game, where his 1.00 m collision capsule, not his drawing, is what the bookshelf stops.

- **What I did:** Asked whether the references were required, and chose to replace them with something from my game.

- **What Claude or another person contributed:** Checked the assignment text, proposed the boy sprite, measured the figure inside its canvas rather than trusting the brief, placed him with his feet on the floor, and recorded the correction to the brief.

- **What I understand now / still do not understand:** The number I anchored the whole scale on was the walking height, not the standing one. It did not change the scale, because the anchor is the collision capsule, but I had been quoting 1.28 m for a pose he never stands in.

- **Evidence and next step:** Evidence: `godot/scenes/AssetShowcase.tscn`; `evidence/a3-showcase.png`; the correction at the end of `CHANGE-BRIEF.md`. Next step: the orbit check, by me, in the editor.

### 2026-10-15 — The orbit check: two assets pass, the music box reads only as a box

- **Date and what I was working on:** 2026-10-15, the human check the rubric reserves for me — walking the camera around each asset in the Godot editor, from behind and below, beside the boy at game scale.

- **I tried / expected:** I had not used Godot's 3D view before. On an Apple Magic Mouse there is no middle button, and swiping its surface zooms rather than orbits, so the usual "middle-drag to orbit" did not work. What worked: selecting each asset in the Scene panel, pressing F to follow it, the Perspective menu's Rear and Bottom views, and dragging the axis gizmo for angled views.

- **What happened:** My verdict, from looking:
  - **Bookshelf:** reads clearly as a bookshelf from behind and below — the open back shows the shelves.
  - **Lamp:** reads clearly as a lamp from behind and below.
  - **Music box: reads only as a box from behind.** The key, the detail my brief named as what makes it a music box, is too small to carry from that distance.
  - No holes or missing faces from any angle, and the colours looked right.

  Claude's own reading of the same screenshots: the undersides render near-black from below, because the scene's one light comes from above — lighting rather than missing faces, since nothing could be seen through — and the boy, a flat sprite, turns to face the camera even from behind. The Godot tab showed unsaved changes throughout; nothing was saved, and `git status` confirmed the scene file on disk unchanged.

- **What I did:** Orbited all three, took nine screenshots, and judged each.

- **What Claude or another person contributed:** Small step-by-step instructions, adjusted for the Magic Mouse once the first ones did not work; reading each screenshot back to me; recording my verdict.

- **What I understand now / still do not understand:** This is the result the brief predicted in failure 7, and it only showed up by looking: every automated check passes for the music box. The key was already enlarged once (revision A3-1) for the same reason, and it is still not enough from behind. I have left it as a limitation rather than change the asset after the checks.

- **Evidence and next step:** Evidence: `evidence/a3-orbit-bookshelf-*-own.png`, `a3-orbit-lamp-*-own.png`, `a3-orbit-musicbox-*-own.png`, `a3-godot-editor-own.png`, `a3-godot-inspector-bookshelf-own.png`; `TEST-REPORT.md` check 7; `CHANGE-BRIEF.md` prediction 7. Next step: the film.

### 2026-10-15 — Recording the film footage: a crash, a lost setting, and a 4K workaround

- **Date and what I was working on:** 2026-10-15, real footage for the film — my Blender session and the Godot scene in motion, instead of stills.

- **I tried / expected:** I gave VS Code Screen Recording permission so the recordings could be made for me, expecting a straightforward desktop recording.

- **What happened:** Four things.
  1. **A desktop recording would not work,** even with permission: my VS Code was full-screen in its own macOS Space, and macOS 26 would not bring Blender in front of it from a script. The Blender footage was captured from inside Blender instead — its own *Save Screenshot* operator, frame by frame, while the view turned 360°. Those are Blender's own renders of its window, labelled as a capture driven via the MCP.
  2. **Blender crashed once, and the cause was Claude's code.** One call opened the music box file and then, in the same call, changed a viewport setting through a reference to the window layout that the file load had just replaced. The crash report pointed at that exact line. Nothing on disk was affected; from then on each file was opened in its own call.
  3. **After the restart the MCP add-on was gone,** because enabling it on the 14th had never been saved to my Blender preferences. I re-enabled it, saved the preferences and reconnected; every download and generation service stayed off.
  4. **Godot's Movie Maker recorded only 1920×1080,** because it records at the window's size and macOS will not open a window larger than the screen. A capture script now renders the scene into a 3840×2160 off-screen viewport and saves every frame the engine draws; its first run logged an error from aiming the camera before the scene was in the tree, so it was fixed and re-run cleanly.

  Watching the orbit, I found the boy's flat sprite looked wrong as the camera moved round it. He was not required, so he was removed and the three assets were re-spaced; the headless check still passes.

- **What I did:** Granted the permission, restarted VS Code, re-enabled and reconnected the add-on, judged the footage and decided to remove the boy.

- **What Claude or another person contributed:** The capture method for both programs, diagnosing the crash from Blender's crash report and the missing add-on from my saved preferences, the 4K workaround, the capture record with hashes, and the scene and document updates.

- **What I understand now / still do not understand:** A setting that is not saved lasts exactly as long as the program stays open — the same lesson as the stale Blender session on the 14th, from the other side. And a flat character in a 3D scene works only from the one angle it was drawn for.

- **Evidence and next step:** Evidence: `youtube/claude-liam-houseghost-a3-gamedev/CAPTURE.md` (four recordings, formats, SHA-256); `godot/tests/capture_orbit.gd`; the crash report's Python line, which matched the call; `godot/scenes/AssetShowcase.tscn`; `evidence/a3-showcase.png`, `evidence/a3-check-assets.txt`. Next step: the beat sheet and narration.

