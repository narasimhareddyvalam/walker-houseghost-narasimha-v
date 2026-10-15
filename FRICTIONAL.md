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

## Entries

<!-- One entry per work session, newest last. -->

### 2026-10-14 — The folder was never a repository, and a tag is the reason that matters

- **Date and what I was working on:** 2026-10-14, the setup phase of Assignment 3. No modelling, and deliberately none: the brief puts the "Learn the window" session and a committed `CHANGE-BRIEF.md` before any prompting, so that the sizes I predict are informed guesses rather than blind ones.

- **I tried / expected:** I expected this to be a naming problem. The assignment wants a repository beginning `walker-`, I already had a folder called `walker-houseghost-narasimha-v` sitting on my disk, and I pushed back three separate times asking why we could not simply push it, remap it, or duplicate it into my account. It looked like a repository to me.

- **What happened:** It was never a repository. There is no `.git` inside that folder — it belongs to the course repo four levels above it, so a push from inside it would have sent all 349 MB of `csye-7270-building-virtual-environments`, every classmate's work included, with my game buried at `fall-2026/narasimha-v/assignment-2/`. Wrong name, wrong contents, wrong shape.

  The argument that actually decided it was not the name at all, and I had not thought of it. Assignment 3 is submitted as a **tag**, and tags are global to a repository rather than scoped to a branch. An `a3` tag pushed to the shared course repo would collide with every other student's `a3`. Since Assignments 3 through 10 all tag the same repository, this was the last moment the move would cost nothing.

  Two things went wrong on the way. Claude created the new repository under `narasimhareddyvalamm` because that was the account `gh` reported as active; it should have asked, and I deleted the empty repo myself. Then the split exposed a gap I did not know existed: the game folder's own `.gitignore` never excluded `*.wav`, because the *course* repository's root ignore file had quietly been doing that job the whole time. Standing alone, the game would have begun committing WAV audio immediately, and `.blend1` backups the moment Assignment 3 starts — which the brief explicitly says not to commit.

- **What I did:** I set the two constraints that shaped the session before anything ran: do not lose Assignment 2, and never commit the assignment prompt. I rejected the account Claude had chosen. And when it started executing a plan I had agreed to without restating what the command would do, I stopped it mid-action and made stating intent first the rule — an agreed plan is not a standing permission to act unannounced. `[TO FILL — anything else you pushed back on today]`

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

- **What I did:** I did not reach for `BLENDERMCP_ADDONS_DIR` or install `addon.py` by hand, which is what the error suggests. Both would have papered over a one-line cause. The fix is to open Blender once, which I have to do anyway for the "Learn the window" session, and then re-run the installer. `[TO FILL — your own reaction to the chapter's commands not working]`

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

  Bound to `127.0.0.1`, not `0.0.0.0` — reachable only from this machine. `[TO FILL — your own note on running an unauthenticated socket, and when you intend to switch the add-on off]`

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

- **What I did:** Set the commit identity explicitly rather than relying on a default, and only in this repository's local config so nothing else on the machine changes. I then had the five unpushed Assignment 3 commits rewritten onto the linked address, with a backup branch `backup/pre-author-rewrite` taken first. Only the author changed: the original timestamps were kept, and `git diff` against the backup is empty. The hashes did change, so the change brief committed before any building is now `722658f`, still at 17:48. `54a86c3` was left alone — it is already on `origin/main`, and fixing it would need a force-push to a published branch, which costs more than one unlinked commit does.

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

- **What I did:** Asked whether the plan was best practice before approving it, and approved it with two additions: smooth shading by angle, and the lid's origin on its hinge so it could swing open later. When asked whether the key needed to be larger and whether the back view mattered, I left the call to Claude: "whatever will help us add details to it more nicely." What it chose is the next entry.

- **What Claude or another person contributed:** Claude derived the lid thickness from the brief's own numbers, ran the full script headless into a scratch file before touching the live session so that any Blender 5.2 API difference would fail there instead, then sent one call per object, each followed by an independent `get_scene_info` reading. It flagged that the art shows the lid thrown wide open while the brief says ajar, and that the box in the art is nearly cubic. Both are recorded here, not changed.

- **What I understand now / still do not understand:** The interesting numbers were not the ones I chose. They came from my choices combining: the height the bevel cost, the gap at the hinge, and the width the key added. Still unverified: whether the colours, the smooth shading and the +Z-up orientation survive the glTF export, and whether the box reads at game scale in Godot. Nothing has been exported yet.

- **Evidence and next step:** Evidence: `tools/blender/build_musicbox.py` — the headless run (`blender -b --factory-startup -P`) and the six live calls printed identical numbers; `blender/musicbox.blend`; the four-view `look` image in material shading. The live calls sent each step without the script's `__main__` block, and the save step used a literal path where the script reads one from its arguments. Next step: build the lamp the same way.

### 2026-10-14 — The key was made larger, and the back view only partly improved

- **Date and what I was working on:** 2026-10-14, immediately after the music box was built. The open question from the last entry: whether the key was large enough to do its job.

- **I tried / expected:** I asked what the open marker wanted from me, then left the decision with Claude. It recommended enlarging the key and adding nothing else, expecting the larger key to help with the back view as well.

- **What happened:** The key went from a 35 × 25 mm bow to 50 × 40 mm, and the shaft from r 5 mm to r 6 mm. Both live and headless, the asset now measures **0.275 × 0.1754 × 0.1795 m at 252 triangles** — the same triangle count, because only the sizes changed. Re-running the two steps replaced `MB_KeyShaft` and `MB_KeyHandle` by name; no `.001` appeared. From directly behind, the key now shows in the silhouette, where before it did not. **From behind and to the left it still reads as a plain chest**, because the key is on the far side. That part was not fixed, and it was not claimed to be.

- **What I did:** Delegated the decision, quoted in the decisions table.

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

- **What I understand now / still do not understand:** After orbiting the rebuild in Blender: "yes lets go to next. i am happy with this one." `[TO FILL — optional: whether "realistic through lighting" is what you meant; this is judged again once the box is lit in Godot]`

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

- **What I did:** Approved the plan; set the instruction to follow all assignment requirements.

- **What Claude or another person contributed:** The design changes and their reasons; the catch on the one-light rule; the shared library, with a before/after diff proving it changed nothing; the session-file safeguard; finding and fixing both of its own check errors.

- **What I understand now / still do not understand:** After orbiting it in Blender: "i want more realsitc one, give me prompt to give to chatgpt." `[TO FILL — optional: what specifically looked unrealistic to you]`

- **Evidence and next step:** Evidence: `tools/blender/build_lamp.py` with its `LIVE_CALLS` log; `tools/blender/asset_lib.py`; `blender/lamp.blend`; `CHANGE-BRIEF.md` revision A3-3; the four-view `look` image including two views from below. Next step: the bookshelf.

### 2026-10-14 — The first lamp references came back too old-fashioned, so I regenerated them

- **Date and what I was working on:** 2026-10-14, the reference image for a more realistic lamp, generated in ChatGPT from the prompt Claude wrote.

- **I tried / expected:** I expected the prompt to give me a realistic lamp I could build from.

- **What happened:** In my words: "chatgpt didnt give me what i like, it gave me too old styles." The prompt described a gourd-shaped ceramic base, a brass neck and a cone shade — a traditional bedside lamp, because that is what the painting in `env_room_memory.png` shows — and the results read as dated rather than realistic. `[TO FILL — how many takes you rejected, and whether you kept any of them]`

- **What I did:** Rejected those results, kept generating in ChatGPT myself, and downloaded the one I liked. `[TO FILL — what you changed in the prompt to get away from the old style]`

- **What Claude or another person contributed:** Claude wrote the original prompt. The rejection, the regeneration and the choice of image were mine, done in ChatGPT outside this session. Claude has not seen the chosen image yet.

- **What I understand now / still do not understand:** `[TO FILL — what "realistic" means to you for this lamp, now that you have seen what you did not want]` Still open: the lamp in my painting is a traditional one, so a modern reference moves the 3D lamp away from the 2D art. That may be the right call, but it should be stated in revision A3-4 when the lamp is rebuilt.

- **Evidence and next step:** Evidence: the chosen image, to be added as `design/ref-lamp-chatgpt.png` with a `SOURCES.md` row REF-LAMP-3D. Next step: share the image, then Claude checks it against the six-shape and triangle limits and proposes revision A3-4 before building.

