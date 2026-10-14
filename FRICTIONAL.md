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

- **What I did:** Quit Blender and reopened it. `[TO FILL — whether it then enabled cleanly, and anything the MCP panel showed]`

- **What Claude or another person contributed:** Claude refused to act on the plausible explanation. It queried `bpy.utils.script_paths(subdir='addons')` to establish where Blender looks before arguing about whether the path was wrong, then ran `addon_utils.enable()` in a headless Blender to separate "the add-on is broken" from "my session is stale". Two commands, and the answer came back unambiguous. The decision to stop and check rather than start moving files was its call, and the right one.

- **What I understand now / still do not understand:** This is the same fault I had in Assignment 2 with the Godot editor — it kept the open scene in memory and happily played a build that no longer existed, and I lost real time to it twice before we found it. **A running editor is a cache, and installing something underneath one proves nothing.** It is the second time this project has cost me an hour to that, and the general rule I should have carried over is: when a tool says something does not exist, check whether the tool has looked since it changed.

  The second thing is narrower and worth keeping. "No module named X" reads like a path problem and invites you to start moving files, which would have left me with the add-on installed in two places and no idea which one loaded. The cheap test — can a *fresh* process load it — answers the real question and changes nothing on disk.

  Still unresolved: whether the server, once started from the add-on's panel, can actually be driven from Claude Code. Everything so far has tested the client and the add-on separately; nothing has yet connected the two.

- **Evidence and next step:** Evidence: the Preferences error quoted exactly; `ADDON DIRS` and `EXTENSIONS` output; the headless `addon_utils.enable()` result showing "BlenderMCP addon registered". Next step: enable the add-on in the restarted Blender, start the server from the `N`-panel's MCP tab with every download and generation option left off, restart Claude Code so it sees the server, and call `get_scene_info` as the first real test of the connection.
