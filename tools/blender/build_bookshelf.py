"""Build the Bookshelf asset (CHANGE-BRIEF.md, Assignment 3, asset 3, as revised by A3-5).

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
TOP_Z = 0.975        # underside of the top slab; the sides run up to it
SHELF_T = 0.02       # shelf and side thickness
INNER_W = 0.56       # between the side panels


def panel(name, size, mat, centre, bevel=0.0, segments=0):
    """A bevelled board, centred on `centre`, origin at its own centre."""
    bm = lib.box(size, bevel=bevel, segments=segments)
    return lib.finish(name, bm, [mat], centre, ROOT)


def report(obj):
    lib.report(obj, BUDGET)


# ==== STEP 0: empty the scene, create the root, point the session at bookshelf.blend
def step_clear(path):
    lib.clear_scene(ROOT)
    bpy.ops.wm.save_as_mainfile(filepath=path)
    print("session file:", bpy.data.filepath)


# ==== STEP 1: top — 0.64 x 0.30 x 0.025, 2-segment bevel, the most-seen edge ======
# Overhangs the carcass by 2 cm each side and 1 cm front and back: the detail that
# makes it furniture rather than a box.
def step_top():
    report(panel("BS_Top", (0.64, 0.30, 0.025), "M_Wood_Warm",
                 (0, 0, TOP_Z + 0.0125), bevel=0.004, segments=2))


# ==== STEPS 2-3: sides — 0.02 x 0.28 x 0.975, standing on the floor ===============
# Their bottoms are the legs: the low shelf sits 6 cm up, as in prop_shelf.png.
def step_side_l():
    report(panel("BS_Side_L", (SHELF_T, 0.28, TOP_Z), "M_Wood_Warm",
                 (-(INNER_W / 2 + SHELF_T / 2), 0, TOP_Z / 2), bevel=0.002, segments=1))


def step_side_r():
    report(panel("BS_Side_R", (SHELF_T, 0.28, TOP_Z), "M_Wood_Warm",
                 (INNER_W / 2 + SHELF_T / 2, 0, TOP_Z / 2), bevel=0.002, segments=1))


# ==== STEPS 4-5: shelves — 0.56 x 0.264 x 0.02, set back 1 cm from the front ======
# Front edge at y = -0.13, back edge against the back panel at y = 0.134.
SHELF_D = 0.264
SHELF_Y = -0.13 + SHELF_D / 2


def step_shelf_low():
    report(panel("BS_Shelf_Low", (INNER_W, SHELF_D, SHELF_T), "M_Wood_Dark",
                 (0, SHELF_Y, 0.06 + SHELF_T / 2), bevel=0.002, segments=1))


def step_shelf_mid():
    report(panel("BS_Shelf_Mid", (INNER_W, SHELF_D, SHELF_T), "M_Wood_Dark",
                 (0, SHELF_Y, 0.50 + SHELF_T / 2), bevel=0.002, segments=1))


# ==== STEP 6: back — 0.56 x 0.006 x 0.915, between the sides, unbevelled ==========
# Revision A3-5: the dark interior in the art is a back panel in shadow.
def step_back():
    report(panel("BS_Back", (INNER_W, 0.006, TOP_Z - 0.06), "M_Wood_Dark",
                 (0, 0.137, 0.06 + (TOP_Z - 0.06) / 2)))


# ==== STEP 7: whole-asset check and save =========================================
def step_check_and_save(path):
    lib.check_and_save(path, BUDGET, MAX_SHAPES)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.abspath(argv[0]) if argv else os.path.join(repo, "blender", "bookshelf.blend")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    step_clear(out)
    step_top()
    step_side_l()
    step_side_r()
    step_shelf_low()
    step_shelf_mid()
    step_back()
    step_check_and_save(out)


# ==== LIVE CALL LOG ==============================================================
# Every execute_blender_code body run for this asset, verbatim, in order. Kept as data
# so that git shows exactly what ran in the live session.
LIVE_CALLS = r"""
--- Build 1 (revision A3-5), 2026-10-14 ---
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
"""

