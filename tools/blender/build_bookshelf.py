"""Build the Bookshelf asset (CHANGE-BRIEF.md, Assignment 3, asset 3, as revised by A3-7).

Every execute_blender_code body run for this asset is logged verbatim in LIVE_CALLS
at the end of this file. Run headless from an empty scene with:

    blender -b --factory-startup --python-exit-code 1 -P tools/blender/build_bookshelf.py [-- out.blend]

Default output: blender/bookshelf.blend (relative to the repository root).

Units are metres. +Z is up, -Y is the front. The root empty Bookshelf sits at the world
origin, which is the centre of the underside. Meshes are built at their final size and
orientation in bmesh, so no object carries rotation or scale to apply.
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

ROOT = "Bookshelf"
BUDGET = 360
MAX_SHAPES = 6
SIDE_T = 0.03        # side panel thickness; the sides rise 2.5 cm above the top board
INNER_W = 0.58       # between the side panels
TOP_Z = 0.975        # top surface of the top board
SHELF_T = 0.02


def board(size, bevel=0.0, segments=0):
    return lib.box(size, bevel=bevel, segments=segments)


def finish(name, bm, mat, centre):
    return lib.finish(name, bm, [mat], centre, ROOT)


def report(obj):
    lib.report(obj, BUDGET)


def side_bm():
    """0.03 x 0.30 x 1.00 panel, centred, top front and back corners rounded (r 0.03).

    The corners are rounded FIRST: bevelling the front edges first made Blender's overlap
    clamp shrink the 3 cm rounding to about 3 mm, and the corners came out square. Then the
    two long front edges get a 1-segment 3 mm bevel so they catch a highlight.
    """
    bm = board((SIDE_T, 0.30, 1.0))
    # Both ends at the top and on the same face (front or back): the two edges running
    # across the panel's thickness. Edges running front-to-back also have |y| = 0.15 at
    # both ends, so the ends must share the same y.
    top_corners = [e for e in bm.edges
                   if all(abs(v.co.z - 0.5) < 1e-6 and abs(abs(v.co.y) - 0.15) < 1e-6 for v in e.verts)
                   and abs(e.verts[0].co.y - e.verts[1].co.y) < 1e-6]
    assert len(top_corners) == 2, len(top_corners)
    bmesh.ops.bevel(bm, geom=top_corners, offset=0.03, offset_type="OFFSET", segments=4,
                    profile=0.5, affect="EDGES", clamp_overlap=False)
    # The long front edges: both ends on the front face, running most of the height.
    front = [e for e in bm.edges
             if all(abs(v.co.y + 0.15) < 1e-6 for v in e.verts)
             and abs(e.verts[0].co.z - e.verts[1].co.z) > 0.5]
    assert len(front) == 2, len(front)
    bmesh.ops.bevel(bm, geom=front, offset=0.003, offset_type="OFFSET", segments=1,
                    profile=0.5, affect="EDGES", clamp_overlap=True)
    # Proof the rounding happened: the front face must stop 3 cm below the top.
    # (The mesh is centred, so world height is local z + 0.5; the top is at 1.00.)
    front_top = max(v.co.z for v in bm.verts if abs(v.co.y + 0.15) < 1e-6) + 0.5
    print(f"rounded corners: 2 | front edges: 2 | front face top z = {front_top:.4f} (expect 0.9700)")
    assert abs(front_top - 0.97) < 1e-4, front_top
    return bm


# ==== STEP 0: empty the scene, create the root, point the session at bookshelf.blend
def step_clear(path):
    lib.clear_scene(ROOT)
    bpy.ops.wm.save_as_mainfile(filepath=path)
    print("session file:", bpy.data.filepath)


# ==== STEPS 1-2: sides — 0.03 x 0.30 x 1.00, full height, rounded top corners =====
# Their lower ends are the legs; nothing spans the floor between them.
def step_side_l():
    report(finish("BS_Side_L", side_bm(), "M_Wood_Warm", (-(INNER_W / 2 + SIDE_T / 2), 0, 0.5)))


def step_side_r():
    report(finish("BS_Side_R", side_bm(), "M_Wood_Warm", (INNER_W / 2 + SIDE_T / 2, 0, 0.5)))


# ==== STEP 3: top — 0.58 x 0.29 x 0.025, set BETWEEN the sides, 2.5 cm below them ===
# Flush with the front; its back meets the back panel.
def step_top():
    bm = board((INNER_W, 0.29, 0.025), bevel=0.002, segments=1)
    report(finish("BS_Top", bm, "M_Wood_Warm", (0, -0.005, TOP_Z - 0.0125)))


# ==== STEPS 4-5: shelves — 0.58 x 0.277 x 0.02 at a third and two-thirds ==========
# Front edge 1 cm back from the sides' front (y = -0.14), back edge on the back panel.
SHELF_D = 0.277
SHELF_Y = -0.14 + SHELF_D / 2


def step_shelf_low():
    bm = board((INNER_W, SHELF_D, SHELF_T), bevel=0.002, segments=1)
    report(finish("BS_Shelf_Low", bm, "M_Wood_Warm", (0, SHELF_Y, 0.36)))


def step_shelf_mid():
    bm = board((INNER_W, SHELF_D, SHELF_T), bevel=0.002, segments=1)
    report(finish("BS_Shelf_Mid", bm, "M_Wood_Warm", (0, SHELF_Y, 0.65)))


# ==== STEP 6: back — 0.58 x 0.008 x 0.875, inset 5 mm from the back edge =========
# Runs z = 0.10 .. 0.975, so the bottom bay is open beneath it, as in the reference.
def step_back():
    bm = board((INNER_W, 0.008, TOP_Z - 0.10))
    report(finish("BS_Back", bm, "M_Wood_Dark", (0, 0.15 - 0.005 - 0.004, 0.10 + (TOP_Z - 0.10) / 2)))


# ==== STEP 7: whole-asset check and save =========================================
def step_check_and_save(path):
    lib.check_and_save(path, BUDGET, MAX_SHAPES)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.abspath(argv[0]) if argv else os.path.join(repo, "blender", "bookshelf.blend")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    step_clear(out)
    step_side_l()
    step_side_r()
    step_top()
    step_shelf_low()
    step_shelf_mid()
    step_back()
    step_check_and_save(out)


# ==== LIVE CALL LOG ==============================================================
# Every execute_blender_code body run for this asset, verbatim, in order. Kept as data
# so that git shows exactly what ran in the live session.
LIVE_CALLS = r"""
--- Build 1 (revision A3-5, superseded by A3-7), 2026-10-14; the file as committed at d93009e ---
[read-only check before clearing: had the open lamp been hand-edited?]
import bpy
print("file:", bpy.data.filepath, "| unsaved changes:", bpy.data.is_dirty)
for o in bpy.data.objects:
    print(o.name, "loc", tuple(round(v, 4) for v in o.location),
          "rot", tuple(round(v, 4) for v in o.rotation_euler),
          "scale", tuple(round(v, 4) for v in o.scale),
          "dims", tuple(round(v, 4) for v in o.dimensions))
for m in bpy.data.materials:
    print(m.name, tuple(round(c, 4) for c in m.diffuse_color))

[step 0]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_bookshelf.py"
ns = {"__name__": "build_bookshelf", "__file__": path}
exec(compile(open(path).read(), path, "exec"), ns)
ns["step_clear"]("/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/blender/bookshelf.blend")

[steps 1-6, one call each, NAME in step_top, step_side_l, step_side_r, step_shelf_low,
 step_shelf_mid, step_back]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_bookshelf.py"
ns = {"__name__": "build_bookshelf", "__file__": path}
exec(compile(open(path).read(), path, "exec"), ns)
ns["NAME"]()

[step 7]
path = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/tools/blender/build_bookshelf.py"
ns = {"__name__": "build_bookshelf", "__file__": path}
exec(compile(open(path).read(), path, "exec"), ns)
ns["step_check_and_save"]("/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/blender/bookshelf.blend")

[read-only: coplanar faces between parts, the z-fighting check]
import bpy
from mathutils import Vector
objs = [o for o in bpy.data.objects if o.type == "MESH"]
faces = []
for o in objs:
    mw = o.matrix_world
    for p in o.data.polygons:
        n = (mw.to_3x3() @ p.normal).normalized()
        pts = [mw @ o.data.vertices[i].co for i in p.vertices]
        faces.append((o.name, n, pts))
def axis(n):
    for i in range(3):
        if abs(abs(n[i]) - 1) < 1e-4: return i
    return None
hits = set()
for i, (a, na, pa) in enumerate(faces):
    ax = axis(na)
    if ax is None: continue
    for b, nb, pb in faces[i+1:]:
        if a == b or axis(nb) != ax: continue
        if abs(pa[0][ax] - pb[0][ax]) > 1e-6: continue
        o1, o2 = [k for k in range(3) if k != ax]
        lo = lambda P, k: min(p[k] for p in P); hi = lambda P, k: max(p[k] for p in P)
        if (min(hi(pa,o1),hi(pb,o1)) - max(lo(pa,o1),lo(pb,o1)) > 1e-4 and
            min(hi(pa,o2),hi(pb,o2)) - max(lo(pa,o2),lo(pb,o2)) > 1e-4):
            same = na.dot(nb) > 0
            hits.add((a, b, "xyz"[ax], round(pa[0][ax], 4), "SAME-facing (visible fight)" if same else "facing each other (hidden contact)"))
for h in sorted(hits): print(h)
print("total", len(hits))

--- Build 2 (revision A3-7), 2026-10-14 ---
[read-only check before clearing: had the open bookshelf been hand-edited? Same body as in
 build 1's first call.]

[step 0, steps 1-6 and step 7: the same three-line exec bodies as build 1, with NAME in
 step_side_l, step_side_r, step_top, step_shelf_low, step_shelf_mid, step_back]

[steps 1-2 again, after the views showed square corners: step_side_l, step_side_r, the
 same three-line exec bodies, against the file with the bevel order corrected; then
 step 7 again]

--- View-only calls before build 2 (changed no geometry) ---
[select BS_Shelf_Mid, open the N sidebar, Material Preview, frame the bookshelf]
import bpy, math
from mathutils import Euler
obj = bpy.data.objects["BS_Shelf_Mid"]
for o in bpy.data.objects:
    o.select_set(False)
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type == "VIEW_3D":
            space = area.spaces.active
            space.shading.type = "MATERIAL"
            space.show_region_ui = True
            space.overlay.show_relationship_lines = False
            for region in area.regions:
                if region.type == "UI":
                    try:
                        region.active_panel_category = "Item"
                    except Exception as e:
                        print("tab:", e)
            r3d = space.region_3d
            r3d.view_perspective = "PERSP"
            r3d.view_rotation = Euler((math.radians(72), 0, math.radians(28)), "XYZ").to_quaternion()
            r3d.view_location = (0.0, 0.0, 0.5)
            r3d.view_distance = 2.6
            area.tag_redraw()
(then the same sidebar loop alone, once more, after the redraw)

[Window > Save Screenshot, from inside Blender]
import bpy, os
out = "/Users/narasimhareddyvalam/Desktop/walker-houseghost-narasimha-v/evidence/a3-blender-window.png"
window = bpy.context.window_manager.windows[0]
area = next(a for a in window.screen.areas if a.type == "VIEW_3D")
region = next(r for r in area.regions if r.type == "WINDOW")
with bpy.context.temp_override(window=window, area=area, region=region):
    result = bpy.ops.screen.screenshot(filepath=out)
print(result, os.path.exists(out), os.path.getsize(out) if os.path.exists(out) else 0)
"""

