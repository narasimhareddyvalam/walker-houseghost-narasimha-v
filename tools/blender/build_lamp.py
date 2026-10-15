"""Build the BedsideLamp asset (CHANGE-BRIEF.md, Assignment 3, asset 2, as revised by A3-4).

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
BUDGET = 420  # revision A3-4; the original brief budget was 340
MAX_SHAPES = 6


def finish(name, bm, mat_names, location, weighted=False):
    # weighted=True only for parts with large flat caps next to rounded edges.
    return lib.finish(name, bm, mat_names, location, ROOT, weighted=weighted)


def report(obj):
    lib.report(obj, BUDGET)


# ==== STEP 0: empty the scene, create the root, point the session at lamp.blend ===
# Saving at once means a later save can never land on another asset's .blend.
def step_clear(path):
    lib.clear_scene(ROOT)
    bpy.ops.wm.save_as_mainfile(filepath=path)
    print("session file:", bpy.data.filepath)


# ==== STEP 1: foot — 16-sided walnut disc, r 0.078 x 0.018, on the floor ========
def step_foot():
    bm = lib.cylinder(0.078, 0.018, segments=16)
    bmesh.ops.translate(bm, vec=(0, 0, 0.009), verts=bm.verts)  # underside on z = 0
    report(finish("LP_Foot", bm, ["M_Wood_Dark"], (0, 0, 0), weighted=True))


# ==== STEP 2: base — 12-sided glossy ceramic drum, r 0.07 x 0.14, rounded rims ===
# Both rim edge loops get a 2-segment, 25 mm bevel: the pill shape in the reference.
# Sunk 2 mm into the foot: z = 0.016 .. 0.156.
def step_base():
    bm = lib.cylinder(0.07, 0.14, segments=12)
    rims = [e for e in bm.edges
            if all(abs(abs(v.co.z) - 0.07) < 1e-6 for v in e.verts) and len(e.link_faces) == 2
            and any(abs(f.normal.z) > 0.99 for f in e.link_faces)]
    bmesh.ops.bevel(bm, geom=rims, offset=0.025, offset_type="OFFSET", segments=2,
                    profile=0.5, affect="EDGES", clamp_overlap=True)
    print("rim edges bevelled:", len(rims), "(expect 24)")
    bmesh.ops.translate(bm, vec=(0, 0, 0.07), verts=bm.verts)  # origin at its underside
    report(finish("LP_Base", bm, ["M_Ceramic_Amber"], (0, 0, 0.016), weighted=True))


# ==== STEP 3: collar — 12-sided brass disc, r 0.032 x 0.008, on top of the base ===
def step_collar():
    bm = lib.cylinder(0.032, 0.008, segments=12)
    bmesh.ops.translate(bm, vec=(0, 0, 0.004), verts=bm.verts)
    report(finish("LP_Collar", bm, ["M_Brass"], (0, 0, 0.156), weighted=True))


# ==== STEP 4: neck — 12-sided brass rod, r 0.009, from the collar through the shade ==
# Runs z = 0.160 .. 0.420 and passes 15 mm through the shade's top: its tip is the
# finial, so the finial costs no seventh shape.
def step_neck():
    bm = lib.cylinder(0.009, 0.26, segments=12)
    bmesh.ops.translate(bm, vec=(0, 0, 0.13), verts=bm.verts)  # origin at its foot
    report(finish("LP_Neck", bm, ["M_Brass"], (0, 0, 0.160)))


# ==== STEP 5: bulb — UV sphere 8 x 4, r 0.032, on the neck inside the shade =======
def step_bulb():
    bm = lib.uv_sphere(0.032, segments=8, rings=4)
    report(finish("LP_Bulb", bm, ["M_Shade_Cream"], (0, 0, 0.290)))


# ==== STEP 6: shade — 24-sided drum, open bottom, closed top =====================
# r 0.14 at the bottom to r 0.13 at the top, z = 0.245 .. 0.405. A single surface;
# the material is double-sided.
def step_shade():
    bm = lib.cylinder(0.14, 0.16, segments=24, radius_top=0.13)
    bottom = min(bm.faces, key=lambda f: f.calc_center_median().z)
    bmesh.ops.delete(bm, geom=[bottom], context="FACES_ONLY")
    bmesh.ops.translate(bm, vec=(0, 0, 0.08), verts=bm.verts)  # origin at the rim
    obj = finish("LP_Shade", bm, ["M_Shade_Cream"], (0, 0, 0.245))
    report(obj)
    cap = max(obj.data.polygons, key=lambda p: p.center.z)
    sides = [p for p in obj.data.polygons if p.index != cap.index]
    sides_out = sum(1 for p in sides if Vector((p.center.x, p.center.y, 0)).dot(p.normal) > 0)
    print(f"  faces {len(obj.data.polygons)} | sides facing outward {sides_out} / {len(sides)}"
          f" | cap ({len(cap.vertices)}-gon) normal z {cap.normal.z:+.2f}"
          f" | double-sided {not obj.data.materials[0].use_backface_culling}")


# ==== STEP 7: whole-asset check and save =========================================
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
    step_collar()
    step_neck()
    step_bulb()
    step_shade()
    step_check_and_save(out)


# ==== LIVE CALL LOG ==============================================================
# Every execute_blender_code body run for this asset, verbatim, in order. Kept as data
# so that git shows exactly what ran in the live session.
LIVE_CALLS = r"""
--- Build 1 (revision A3-3, superseded by A3-4), 2026-10-14; the file as committed at d8caf4b ---
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

--- Build 2 (revision A3-4), 2026-10-14 ---
[read-only check before clearing: had the open lamp been hand-edited?]
import bpy
print("unsaved changes:", bpy.data.is_dirty)
for o in bpy.data.objects:
    print(o.name, "loc", tuple(round(v, 4) for v in o.location),
          "rot", tuple(round(v, 4) for v in o.rotation_euler),
          "scale", tuple(round(v, 4) for v in o.scale),
          "dims", tuple(round(v, 4) for v in o.dimensions))
for m in bpy.data.materials:
    print(m.name, tuple(round(c, 4) for c in m.diffuse_color))

[step 0, steps 1-6 and step 7: the same three-line exec bodies as build 1, with NAME in
 step_foot, step_base, step_collar, step_neck, step_bulb, step_shade]

--- View-only calls after build 1 (changed no geometry) ---
[deselect, Material Preview, three-quarter view]
import bpy, math
from mathutils import Euler
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type == "VIEW_3D":
            region = next(r for r in area.regions if r.type == "WINDOW")
            with bpy.context.temp_override(window=window, area=area, region=region):
                bpy.ops.object.select_all(action="DESELECT")
            space = area.spaces.active
            space.shading.type = "MATERIAL"
            space.overlay.show_relationship_lines = False
            r3d = space.region_3d
            r3d.view_perspective = "PERSP"
            r3d.view_rotation = Euler((math.radians(75), 0, math.radians(30)), "XYZ").to_quaternion()
            r3d.view_location = (0.0, 0.0, 0.21)
            r3d.view_distance = 0.9
            area.tag_redraw()
"""

