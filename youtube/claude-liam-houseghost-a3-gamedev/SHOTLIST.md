# SHOTLIST — Building Three Game Props with Claude, Blender MCP and Godot

Generated from `beat_sheet.json`. Every visual is a real repository file, a recorded clip
(`CAPTURE.md`), a Godot render, or a labelled reconstruction. Durations are measured narration
seconds (B00 is a silent composer opening).

| Beat | Act | Visual | On-screen label | Source | Seconds |
|---|---|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | Reconstruction (Claude composer) | `SCRIPT.md` | 9.0 |
| B01 | ASK | ClaudeVerdictArtifact | What got built | `SCRIPT.md` | 13.06 |
| B02 | RESULT | recorded clip | Godot engine capture — scripted camera, native 4K | `capture/godot-showcase-orbit-4k.mp4` | 13.95 |
| B03 | RESULT | GodotDesignFigure | My A2 art — the room they come from | `godot/assets/art/env_room_memory.png` | 12.82 |
| B04 | GAME | GodotDesignFigure | My A2 art | `godot/assets/art/env_room_memory.png` | 13.18 |
| B05 | GAME | GodotDesignFigure | Captured in my Blender session via the MCP — final versions | `stills/final-musicbox-4view.png` | 16.32 |
| B06 | GAME | GodotDesignFigure | Godot render | `evidence/a3-showcase.png` | 13.06 |
| B07 | BRIEF | GodotDevWorkbench (trace) | CHANGE-BRIEF.md — scale table | `CHANGE-BRIEF.md — scale table (Repository file)` | 14.89 |
| B08 | BRIEF | GodotDevWorkbench (trace) | CHANGE-BRIEF.md — correction | `CHANGE-BRIEF.md — correction, 2026-10-15 (Repository file)` | 17.17 |
| B09 | BRIEF | GodotDevWorkbench (trace) | CHANGE-BRIEF.md — predicted failures | `CHANGE-BRIEF.md — committed 722658f, 2026-10-14 17:48, before any build (Repository file)` | 22.38 |
| B10 | MCP | GodotDesignFigure | My screenshot | `evidence/a3-blender-window.png · BLENDER-NOTES.md` | 14.98 |
| B11 | MCP | GodotDevWorkbench (trace) | get_scene_info | `get_scene_info — first call, before any build (Command output)` | 15.02 |
| B12 | MCP | GodotDesignFigure | My screenshot | `evidence/a3-mcp-panel-own.png · lsof: Blender TCP 127.0.0.1:9876 (LISTEN)` | 15.55 |
| B13 | BUILD | GodotDesignFigure | My screenshot | `evidence/a3-prompt-to-claude-own.png` | 18.97 |
| B14 | BUILD | GodotDesignFigure | Captured in my Blender session via the MCP | `evidence/a3-prompt-result-bookshelf-a3-5.png` | 15.64 |
| B15 | BUILD | recorded clip | Capture of my Blender session — camera driven via the MCP | `capture/blender-bookshelf-turntable.mp4` | 12.61 |
| B16 | MUSICBOX | recorded clip | Capture of my Blender session — camera driven via the MCP | `capture/blender-musicbox-turntable.mp4` | 11.86 |
| B17 | MUSICBOX | GodotDesignFigure | ChatGPT reference — image only | `design/ref-musicbox-chatgpt.png` | 13.95 |
| B18 | MUSICBOX | GodotDesignFigure | Captured in my Blender session via the MCP | `abbreviated from tools/blender/build_musicbox.py lines 61–64` | 18.69 |
| B19 | LAMP | recorded clip | Capture of my Blender session — camera driven via the MCP | `capture/blender-lamp-turntable.mp4` | 17.92 |
| B20 | LAMP | GodotDesignFigure | ChatGPT reference — image only | `design/ref-lamp-chatgpt.png` | 7.72 |
| B21 | LAMP | GodotDesignFigure | Godot render | `abbreviated from tools/blender/asset_lib.py lines 23–24` | 16.17 |
| B22 | BOOKSHELF | GodotDesignFigure | ChatGPT reference — image only | `design/ref-bookshelf-chatgpt.png` | 14.36 |
| B23 | BOOKSHELF | GodotDesignFigure | Captured in my Blender session via the MCP — final version | `abbreviated from tools/blender/build_bookshelf.py lines 64–65` | 12.5 |
| B24 | BOOKSHELF | GodotDevWorkbench (trace) | side_bm() — the rounding assertion | `tools/blender/build_bookshelf.py — side_bm() assertion (Command output)` | 13.08 |
| B25 | HANDEDIT | GodotDesignFigure | Captured in my Blender session via the MCP | `evidence/a3-hand-edit-before.png` | 9.79 |
| B26 | HANDEDIT | GodotDesignFigure | My screenshots | `evidence/a3-hand-edit-attempt-duplicate.png · a3-hand-edit-during-own.png · a3-hand-edit-third-shelf-own.png` | 20.89 |
| B27 | HANDEDIT | GodotDesignFigure | Captured in my Blender session via the MCP — same camera | `evidence/a3-hand-edit-after.png` | 21.25 |
| B28 | CHECK | GodotDevWorkbench (trace) | tools/inspect_glb.py — bookshelf.glb | `python3 tools/inspect_glb.py — bookshelf.glb (Command output)` | 13.78 |
| B29 | CHECK | GodotDevWorkbench (code) |  | `godot/tests/check_assets.gd lines 82–95 · verbatim · Reconstruction` | 7.15 |
| B30 | CHECK | GodotDevWorkbench (trace) | Headless — W × H × D, metres | `timeout 120 godot --headless --path godot --script res://tests/check_assets.gd (Command output)` | 10.11 |
| B31 | CHECK | GodotDevWorkbench (trace) | check_assets.gd — negative test | `check_assets.gd against a deliberately wrong height (Command output)` | 17.3 |
| B32 | GODOT | GodotDevWorkbench (code) |  | `godot/scenes/AssetShowcase.tscn lines 44–66 · verbatim · Reconstruction` | 8.81 |
| B33 | GODOT | recorded clip | Godot engine capture — scripted camera, native 4K | `capture/godot-showcase-orbit-4k.mp4` | 8.49 |
| B34 | GODOT | GodotDesignFigure | My screenshots | `evidence/a3-godot-editor-own.png` | 13.03 |
| B35 | GODOT | GodotDesignFigure | My screenshots | `evidence/a3-orbit-*-own.png` | 17.96 |
| B36 | VERDICT | ClaudeVerdictArtifact | Built | `SCRIPT.md` | 14.89 |
| B37 | VERDICT | ClaudeVerdictArtifact | Verified | `SCRIPT.md` | 18.33 |
| B38 | VERDICT | ClaudeVerdictArtifact | Revised | `SCRIPT.md` | 23.72 |
| B39 | VERDICT | ClaudeVerdictArtifact | Roles | `SCRIPT.md` | 16.62 |
| B40 | VERDICT | ClaudeVerdictArtifact | Still uncertain · Next | `SCRIPT.md` | 17.58 |
| B41 | VERDICT | ClaudeVerdictArtifact | Source | `SCRIPT.md` | 8.75 |
| B42 | YOUR_TURN | ClaudeComposerAsk | Reconstruction (Claude composer) | `SCRIPT.md` | 11.95 |
| B43 | OUTRO | ClaudeTitleOutro | locked outro card | `OUTRO-LOCK.md` | 5.65 |
