"""Build the MusicBox asset (CHANGE-BRIEF.md, Assignment 3, asset 1, as revised by A3-2).

Every execute_blender_code body run for this asset is logged verbatim in LIVE_CALLS
at the end of this file. Run headless from an empty
scene with:

    blender -b --factory-startup --python-exit-code 1 -P tools/blender/build_musicbox.py [-- out.blend]

Default output: blender/musicbox.blend (relative to the repository root).

Units are metres. +Z is up, -Y is the front. The root empty MusicBox sits at the world
origin, which is the centre of the underside of the plinth. Meshes are built at their
final size and orientation in bmesh, so no object carries rotation or scale to apply.
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

ROOT = "MusicBox"
BUDGET = 320
PLINTH_H = 0.015  # the box stands on the plinth; every part above it is offset by this
box, cylinder = lib.box, lib.cylinder


def finish(name, bm, mat_names, location):
    return lib.finish(name, bm, mat_names, location, ROOT)


def report(obj):
    lib.report(obj, BUDGET)


# ==== STEP 0: empty the scene, create the root ===================================
def step_clear():
    lib.clear_scene(ROOT)


# ==== STEP 1: plinth — 0.26 x 0.19 x 0.015, 1 cm overhang, 1-segment chamfer =====
def step_plinth():
    bm = box((0.26, 0.19, PLINTH_H), bevel=0.004, segments=1)
    bmesh.ops.translate(bm, vec=(0, 0, PLINTH_H / 2), verts=bm.verts)  # underside on z = 0
    report(finish("MB_Plinth", bm, ["M_Wood_Dark"], (0, 0, 0)))


# ==== STEP 2: body — 0.24 x 0.17 x 0.12, 2-segment bevel, hollowed ===============
# The flat top is inset to leave 12 mm walls and pushed 0.10 m down, leaving a 20 mm
# floor. The cavity's faces take material slot 1 (dark wood), so the inside reads deep.
def step_body():
    bm = box((0.24, 0.17, 0.12), bevel=0.006, segments=2)
    bmesh.ops.translate(bm, vec=(0, 0, 0.06), verts=bm.verts)  # underside on z = 0
    top = max(bm.faces, key=lambda f: (f.normal.z > 0.99, f.calc_area()))
    inset = bmesh.ops.inset_individual(bm, faces=[top], thickness=0.006, depth=0.0)
    ext = bmesh.ops.extrude_face_region(bm, geom=[top])
    floor_verts = [e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, vec=(0, 0, -0.10), verts=floor_verts)
    bmesh.ops.delete(bm, geom=[top], context="FACES_ONLY")  # extrude leaves the old face
    # A cavity face has every vertex inside the opening (|x| <= 0.108, |y| <= 0.073);
    # every outside face reaches the 0.114 / 0.079 flat-top edge or beyond.
    cavity = [f for f in bm.faces
              if all(abs(v.co.x) < 0.110 and abs(v.co.y) < 0.075 for v in f.verts)]
    for f in cavity:
        f.material_index = 1
    print("inset faces", len(inset["faces"]), "| cavity faces", len(cavity), "(expect 5)")
    report(finish("MB_Body", bm, ["M_Wood_Warm", "M_Wood_Dark"], (0, 0, PLINTH_H)))


# ==== STEP 3: lid — 0.24 x 0.17 x 0.012, hinged at the back, open 70 deg ==========
# The hinge sits at y = 0.079, where the body's flat top begins inside its 6 mm bevel,
# and the lid is dropped until its lowest point touches the rim: no gap at the hinge.
def step_lid():
    bm = box((0.24, 0.17, 0.012), bevel=0.003, segments=1)
    bmesh.ops.translate(bm, vec=(0, -0.085, 0.006), verts=bm.verts)  # back-bottom edge at 0
    bmesh.ops.rotate(bm, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(-70), 3, "X"),
                     verts=bm.verts)  # negative about X lifts the front (-Y) edge
    low = min(v.co.z for v in bm.verts)
    bmesh.ops.translate(bm, vec=(0, 0, -low), verts=bm.verts)
    report(finish("MB_Lid", bm, ["M_Wood_Dark"], (0, 0.079, PLINTH_H + 0.12)))


# ==== STEP 4: key shaft — 12-vertex cylinder along +X out of the right face =======
# Origin on the right face, on the shaft's axis: the point a key turns on.
def step_key_shaft():
    bm = cylinder(0.006, 0.030)
    bmesh.ops.rotate(bm, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(90), 3, "Y"),
                     verts=bm.verts)
    # Runs x = -0.002 .. 0.028 from the face: 2 mm sunk into the body, no visible seam.
    bmesh.ops.translate(bm, vec=(0.013, 0, 0), verts=bm.verts)
    report(finish("MB_KeyShaft", bm, ["M_Brass"], (0.12, 0, PLINTH_H + 0.05)))


# ==== STEP 5: key bow — upright oval, 0.040 x 0.056, 5 mm thick, in line with shaft ==
# A butterfly key's bow lies in the plane of its shaft, so it faces the front (-Y).
def step_key_bow():
    bm = cylinder(0.020, 0.005)
    bmesh.ops.rotate(bm, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(90), 3, "X"),
                     verts=bm.verts)  # disc axis along Y
    bmesh.ops.scale(bm, vec=(1.0, 1.0, 1.4), verts=bm.verts)  # oval, taller than wide
    # Centre 0.166: overlaps the shaft end (0.148) by 2 mm.
    report(finish("MB_KeyBow", bm, ["M_Brass"], (0.166, 0, PLINTH_H + 0.05)))


# ==== STEP 6: clasp — 0.024 x 0.004 x 0.022, front face, hanging from the rim =====
def step_clasp():
    bm = box((0.024, 0.004, 0.022))
    # Sunk 0.5 mm into the front face (y = -0.085); top 2 mm below the rim.
    report(finish("MB_Clasp", bm, ["M_Brass"], (0, -0.0865, PLINTH_H + 0.107)))


# ==== STEP 7: whole-asset check and save =========================================
def step_check_and_save(path):
    lib.check_and_save(path, BUDGET, 6)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.abspath(argv[0]) if argv else os.path.join(repo, "blender", "musicbox.blend")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    step_clear()
    step_plinth()
    step_body()
    step_lid()
    step_key_shaft()
    step_key_bow()
    step_clasp()
    step_check_and_save(out)


# ==== LIVE CALL LOG ==============================================================
# Every execute_blender_code body run for this asset, verbatim, in order. Kept as data
# so that git shows exactly what ran in the live session.
LIVE_CALLS = r"""
--- Build 1 (5 shapes, superseded by revision A3-2) and revision A3-1 (larger key) ---
Each call sent this file's then HELPERS block plus one step function and a call to it;
the exact text is this file as committed at dd9fdbf (build 1) and f3f4052 (A3-1). The
save calls used a literal path, /Users/narasimhareddyvalam/Desktop/walker-houseghost-
narasimha-v/blender/musicbox.blend, in place of the __main__ argument.

--- Build 2 (revision A3-2), 2026-10-14; the file as committed at 1265b93 ---
[step 0]
<the then step_clear() function and ROOT = "MusicBox", pasted inline, followed by:>
step_clear()

[steps 1-6, one call each, NAME in step_plinth, step_body, step_lid, step_key_shaft,
 step_key_bow, step_clasp]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_musicbox.py"
ns = {"__name__": "build_musicbox"}
exec(compile(open(path).read(), path, "exec"), ns)
ns["NAME"]()

[step 7]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_musicbox.py"
ns = {"__name__": "build_musicbox"}
exec(compile(open(path).read(), path, "exec"), ns)
ns["step_check_and_save"]("/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/blender/musicbox.blend")

--- View-only and read-only calls (changed no geometry, saved nothing) ---
[frame the asset]
import bpy
for o in bpy.data.objects:
    o.select_set(o.name.startswith("MB_") or o.name == "MusicBox")
bpy.context.view_layer.objects.active = bpy.data.objects["MusicBox"]
framed = 0
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type == "VIEW_3D":
            region = next(r for r in area.regions if r.type == "WINDOW")
            area.spaces.active.shading.type = "MATERIAL"
            with bpy.context.temp_override(window=window, area=area, region=region):
                bpy.ops.view3d.view_selected()
            framed += 1
print("framed viewports:", framed)

[set a three-quarter view; run three times with these values]
import bpy, math
from mathutils import Euler
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type == "VIEW_3D":
            r3d = area.spaces.active.region_3d
            r3d.view_perspective = "PERSP"
            r3d.view_rotation = Euler((math.radians(62), 0, math.radians(32)), "XYZ").to_quaternion()
            r3d.view_location = (0.03, 0.0, 0.14)
            r3d.view_distance = 0.55
            area.tag_redraw()
(first run used rotation (65, 0, 35) with view_selected instead of a location; the second
also deselected every object and set distance 0.75)

[deselect, hide parent lines]
import bpy
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type == "VIEW_3D":
            region = next(r for r in area.regions if r.type == "WINDOW")
            with bpy.context.temp_override(window=window, area=area, region=region):
                bpy.ops.object.select_all(action="DESELECT")
            space = area.spaces.active
            space.overlay.show_relationship_lines = False
            space.region_3d.view_distance = 0.5
            area.tag_redraw()
print("selected:", [o.name for o in bpy.context.selected_objects])

[inspect the cavity's shading]
import bpy
me = bpy.data.objects["MB_Body"].data
cav = [p for p in me.polygons if p.material_index == 1]
for p in cav:
    print(p.index, "verts", len(p.vertices), "normal", tuple(round(c, 3) for c in p.normal), "smooth", p.use_smooth)
sharp = me.attributes.get("sharp_edge")
print("sharp edges total:", sum(1 for d in sharp.data if d.value) if sharp else "no attribute")
print("has custom normals:", me.has_custom_normals)
"""
