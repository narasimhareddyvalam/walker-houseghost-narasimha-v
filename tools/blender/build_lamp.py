"""Build the BedsideLamp asset (CHANGE-BRIEF.md, Assignment 3, asset 2, as revised by A3-3).

Every execute_blender_code body run for this asset is logged verbatim in LIVE_CALLS
at the end of this file. Run headless from an empty scene with:

    blender -b --factory-startup --python-exit-code 1 -P tools/blender/build_lamp.py [-- out.blend]

Default output: blender/lamp.blend (relative to the repository root).

Units are metres. +Z is up, -Y is the front. The root empty BedsideLamp sits at the
world origin, which is the centre of the underside of the foot. Meshes are built at
their final size and orientation in bmesh, so no object carries rotation or scale.
"""

# ==== SETUP =====================================================================
# Shared helpers and the one material library live in asset_lib.py, next to this file.
import os, sys, importlib, math
import bpy, bmesh
from mathutils import Matrix, Vector

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)
import asset_lib as lib
importlib.reload(lib)  # a live Blender session keeps old module versions otherwise

ROOT = "BedsideLamp"
BUDGET = 340
MAX_SHAPES = 6


def finish(name, bm, mat_names, location, weighted=False):
    # Every lamp part is curved; weighted normals would only distort a curved surface.
    return lib.finish(name, bm, mat_names, location, ROOT, weighted=weighted)


def report(obj):
    lib.report(obj, BUDGET)


# ==== STEP 0: empty the scene, create the root, point the session at lamp.blend ===
# Saving at once means a later save can never land on another asset's .blend.
def step_clear(path):
    lib.clear_scene(ROOT)
    bpy.ops.wm.save_as_mainfile(filepath=path)
    print("session file:", bpy.data.filepath)


# ==== STEP 1: foot — 12-sided disc, r 0.055 x 0.012, on the floor ================
def step_foot():
    bm = lib.cylinder(0.055, 0.012, segments=12)
    bmesh.ops.translate(bm, vec=(0, 0, 0.006), verts=bm.verts)  # underside on z = 0
    report(finish("LP_Foot", bm, ["M_Wood_Dark"], (0, 0, 0)))


# ==== STEP 2: base — UV sphere 12 x 6, r 0.07, squashed to 0.8 on Z ===============
# 0.14 wide x 0.112 tall. Its lowest point sits 8 mm into the foot, so it is seated on
# a ring of contact rather than balanced on its pole.
def step_base():
    bm = lib.uv_sphere(0.07, segments=12, rings=6)
    bmesh.ops.scale(bm, vec=(1.0, 1.0, 0.8), verts=bm.verts)
    report(finish("LP_Base", bm, ["M_Ceramic_Amber"], (0, 0, 0.060)))


# ==== STEP 3: neck — 12-sided brass rod, r 0.008, base to the shade's top =========
# Runs z = 0.110 .. 0.419: 6 mm into the base, ending 1 mm under the shade's cap,
# so from below the shade is visibly held by it.
def step_neck():
    bm = lib.cylinder(0.008, 0.309, segments=12)
    bmesh.ops.translate(bm, vec=(0, 0, 0.1545), verts=bm.verts)  # origin at its foot
    report(finish("LP_Neck", bm, ["M_Brass"], (0, 0, 0.110)))


# ==== STEP 4: bulb — UV sphere 8 x 4, r 0.028, on the neck inside the shade =======
def step_bulb():
    bm = lib.uv_sphere(0.028, segments=8, rings=4)
    report(finish("LP_Bulb", bm, ["M_Shade_Cream"], (0, 0, 0.290)))


# ==== STEP 5: shade — 24-sided truncated cone, open bottom, closed top ============
# r 0.10 at the bottom to r 0.065 at the top, z = 0.25 .. 0.42: wider at the bottom,
# as the painting shows. A single surface; the material is double-sided.
def step_shade():
    bm = lib.cylinder(0.10, 0.17, segments=24, radius_top=0.065)
    bottom = min(bm.faces, key=lambda f: f.calc_center_median().z)
    bmesh.ops.delete(bm, geom=[bottom], context="FACES_ONLY")
    bmesh.ops.translate(bm, vec=(0, 0, 0.085), verts=bm.verts)  # origin at the rim
    obj = finish("LP_Shade", bm, ["M_Shade_Cream"], (0, 0, 0.25))
    report(obj)
    cap = max(obj.data.polygons, key=lambda p: p.center.z)
    sides = [p for p in obj.data.polygons if p.index != cap.index]
    sides_out = sum(1 for p in sides if Vector((p.center.x, p.center.y, 0)).dot(p.normal) > 0)
    print(f"  faces {len(obj.data.polygons)} | sides facing outward {sides_out} / {len(sides)}"
          f" | cap ({len(cap.vertices)}-gon) normal z {cap.normal.z:+.2f}"
          f" | double-sided {not obj.data.materials[0].use_backface_culling}")


# ==== STEP 6: whole-asset check and save =========================================
def step_check_and_save(path):
    lib.check_and_save(path, BUDGET, MAX_SHAPES, open_meshes=("LP_Shade",))


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.abspath(argv[0]) if argv else os.path.join(repo, "blender", "lamp.blend")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    step_clear(out)
    step_foot()
    step_base()
    step_neck()
    step_bulb()
    step_shade()
    step_check_and_save(out)


# ==== LIVE CALL LOG ==============================================================
# Every execute_blender_code body run for this asset, verbatim, in order. Kept as data
# so that git shows exactly what ran in the live session.
LIVE_CALLS = r"""
--- Build 1 (revision A3-3), 2026-10-14 ---
[step 0]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_lamp.py"
ns = {"__name__": "build_lamp", "__file__": path}
exec(compile(open(path).read(), path, "exec"), ns)
ns["step_clear"]("/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/blender/lamp.blend")

[steps 1-5, one call each, NAME in step_foot, step_base, step_neck, step_bulb, step_shade]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_lamp.py"
ns = {"__name__": "build_lamp", "__file__": path}
exec(compile(open(path).read(), path, "exec"), ns)
ns["NAME"]()

[step 6]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_lamp.py"
ns = {"__name__": "build_lamp", "__file__": path}
exec(compile(open(path).read(), path, "exec"), ns)
ns["step_check_and_save"]("/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/blender/lamp.blend")
"""

