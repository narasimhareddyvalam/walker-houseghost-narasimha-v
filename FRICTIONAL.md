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
