"""Export one asset .blend as binary glTF (.glb), +Y Up, for Godot.

Run once per asset, headless, so the live session is never touched:

    blender -b blender/<asset>.blend --python-exit-code 1 -P tools/blender/export_glb.py -- godot/assets/models/<asset>.glb

Rotation and scale are already zero and one on every object (the build scripts never
set them), so export_apply has nothing to bake; it is on so that a hand edit made later
in the viewport is still exported as the viewer sees it.
"""

import os, sys
import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
out = os.path.abspath(argv[0])
os.makedirs(os.path.dirname(out), exist_ok=True)

# export_format's items are filled in at call time, so they cannot be read beforehand
# (doing so returns an empty list). An invalid value raises TypeError listing the valid
# ones, and --python-exit-code 1 turns that into a non-zero exit.
bpy.ops.export_scene.gltf(
    filepath=out,
    export_format="GLB",
    export_yup=True,          # +Y Up: Blender is Z-up, glTF and Godot are Y-up
    export_apply=True,        # apply modifiers and any later hand-made transforms
    export_materials="EXPORT",
    export_normals=True,      # carries the weighted and smooth-by-angle normals
    export_cameras=False,
    export_lights=False,
)
print("exported", out, os.path.getsize(out), "bytes")
