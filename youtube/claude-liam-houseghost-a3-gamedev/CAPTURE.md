# CAPTURE — footage for the Assignment 3 film

All footage is real output of my own Blender session or of Godot, recorded 2026-10-15.
The MP4 files are kept out of git (course rule: no MP4 on GitHub); this file records what
they are, how they were made and their hashes, so each can be matched to the film.

| File | What it shows | Format | SHA-256 |
|---|---|---|---|
| `capture/blender-bookshelf-turntable.mp4` | Bookshelf, final (A3-8), BS_Shelf_Bottom selected | 2940×1846, 24 fps, 240 frames, 10.0 s | `bb5dc6b7714f6e47624440004e818d6197796d13126ff463e098949dead44aba` |
| `capture/blender-musicbox-turntable.mp4` | Music box, final (A3-2), MB_Body selected | 2940×1846, 24 fps, 240 frames, 10.0 s | `43df3a1efcb6c694bad6edc4e0c8c0612f640731c1f2b6ade3ea8f3026aaaad8` |
| `capture/blender-lamp-turntable.mp4` | Lamp, final (A3-4, A3-6), LP_Shade selected | 2940×1846, 24 fps, 240 frames, 10.0 s | `2280e1f04e49629fc8ab8d90e2e95a41eab3c99b0c10a1cf2cd5d379b01b8491` |
| `capture/godot-showcase-orbit-4k.mp4` | AssetShowcase.tscn, the three assets, scripted camera orbit (300°) | 3840×2160, 30 fps, 480 frames, 16.0 s | `f6ac7b673316f4cdb9df4cc8d61589c95ce6f0cb178e373d542db01867c238da` |

## How each was made

**Blender turntables — "Capture of my Blender session, camera driven via the MCP".**
My live Blender 5.2.2 window, with the committed `.blend` file open and nothing modified or
saved (each run ends with `unsaved: False`). Through `execute_blender_code`, the viewport view
was turned 1.5° per frame for 240 frames (360°), and after each step Blender's own
*Window › Save Screenshot* operator (`bpy.ops.screen.screenshot`) captured the whole window —
viewport, Outliner, Properties, the N sidebar's Item tab and the statistics overlay. ffmpeg
joined the frames at 24 fps (`libx264`, CRF 16). The window was captured from inside Blender
because macOS would not bring Blender in front of a full-screen VS Code for a desktop
recording; the frames are Blender's own rendering of its window, not a reconstruction.

**Godot orbit — "Godot engine capture, scripted camera, native 4K".** Godot 4.7.2 running
`godot/tests/capture_orbit.gd` on `AssetShowcase.tscn`: the scene is rendered into a 3840×2160
SubViewport (MSAA 4×) and each frame the engine draws is saved, then joined by ffmpeg at 30 fps.
Only the camera moves (300° around the three assets); the assets and the one light are as
saved. Godot's Movie Maker was tried first and recorded only 1920×1080, because it records at
the window's size and macOS will not open a window larger than the screen.

**Not recorded:** my hand edit. It had already happened; re-performing it for a recording would
be a re-enactment, so the film uses my own screenshots of the real edit.
