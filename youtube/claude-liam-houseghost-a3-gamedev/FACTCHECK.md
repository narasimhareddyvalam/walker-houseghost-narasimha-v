# FACTCHECK — every number Liam says, and where it comes from

Checked 2026-10-15 against the repository at game-source commit `d331a4a`.

| Claim (beat) | Value | Source |
|---|---|---|
| Scale (B07) | 250 px = 1 m; capsule 250 px = 1.00 m | `CHANGE-BRIEF.md` scale table; `godot/scenes/Player.tscn` CapsuleShape2D height 250 |
| Boy's standing height (B08) | 341 px figure = 1.36 m; brief said 1.28 m | measured alpha bounds of `godot/assets/art/char_remembered.png` (rows 89–430); correction in `CHANGE-BRIEF.md` |
| Brief committed before building (B09) | commit `722658f`, 2026-10-14 17:48 | `git log` — earlier than every build commit |
| Seven predictions (B09) | 7 | `CHANGE-BRIEF.md` predicted-failure table |
| First scene read (B11) | default scene: cube, light, camera | `get_scene_info` output in `FRICTIONAL.md` |
| Socket (B12) | 127.0.0.1:9876, localhost only | `lsof` output in `FRICTIONAL.md`; `evidence/a3-mcp-panel-own.png` |
| Bookshelf plan (B13) | six boards, 296 / 360 triangles | `evidence/a3-prompt-to-claude-own.png` |
| First music box (B16) | five shapes, 252 triangles, lid 18° | `FRICTIONAL.md` build entry; `CHANGE-BRIEF.md` |
| Music box walls and cavity (B18) | 12 mm walls, 10 cm cavity | `tools/blender/build_musicbox.py` lines 61–64 (inset 0.006 + 6 mm bevel = 12 mm; translate −0.10) |
| Music box triangles (B18) | 312 / 320 | `evidence/a3-stats-musicbox.png`; `tools/inspect_glb.py` |
| Lamp budget (B19) | 340 → 420, before building | `CHANGE-BRIEF.md` revision A3-4 |
| Lamp emission (B21) | 1.0 → 0.4 | `tools/blender/asset_lib.py` lines 23–24; revision A3-6 |
| Bookshelf rounding (B23) | 3 cm intended; clamp reduced it to about 3 mm | `tools/blender/build_bookshelf.py` `side_bm()`; `FRICTIONAL.md` A3-7 entry. **The 3 mm is inferred, not measured**: the overlap clamp limits a bevel to its neighbour's size, and the neighbouring front-edge bevel was 3 mm; the square corners were observed in the views |
| Rounding assertion (B24) | front face top 0.9700 m | `side_bm()` output |
| Hand edit (B27) | six boards, 280 triangles | `evidence/a3-hand-edit-after.png`; `CHANGE-BRIEF.md` A3-8 |
| Export (B28) | binary glTF, +Y up; exact hex colours | `tools/blender/export_glb.py`; `evidence/a3-inspect-glb.txt` |
| Headless table (B30) | 0.3160 × 0.2968 × 0.1900 · 0.2800 × 0.4200 × 0.2800 · 0.6400 × 1.0000 × 0.3000; within 2 mm | `evidence/a3-check-assets.txt` (`check_assets.gd`, TOL 0.002) |
| Negative test (B31) | FAIL, exit 1 | `FRICTIONAL.md` export entry |
| One light (B32) | one `DirectionalLight3D` | `godot/scenes/AssetShowcase.tscn` lines 44–48 |
| Triangle counts (B36) | 312 · 406 · 280, within budgets 320 · 420 · 360 and the course limit of 500 | `evidence/a3-stats-*.png`, `a3-hand-edit-after.png`, `inspect_glb.py` |
| Source revision (B41) | `d331a4a` | `git log -1 -- godot blender tools`; `git diff d331a4a HEAD -- godot blender tools` empty at render time |

Not claimed anywhere in the film: integration into the 2D gameplay; behaviour under every
lighting condition; a review by another person.
