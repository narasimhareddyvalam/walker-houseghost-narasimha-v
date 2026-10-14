"""Build the MusicBox asset (CHANGE-BRIEF.md, Assignment 3, asset 1).

Every live execute_blender_code call during the build sent HELPERS plus exactly one
step_* function from this file, followed by a call to it. Run headless from an empty
scene with:

    blender -b --factory-startup --python-exit-code 1 -P tools/blender/build_musicbox.py [-- out.blend]

Default output: blender/musicbox.blend (relative to the repository root).

Units are metres. +Z is up, -Y is the front. The root empty MusicBox sits at the world
origin, which is the centre of the underside. Meshes are built at their final size and
orientation in bmesh, so no object carries rotation or scale to apply.
"""

# ==== HELPERS ===================================================================
import bpy, bmesh, math
from mathutils import Matrix, Vector

# Shared library: hex is sRGB as written in CHANGE-BRIEF.md; (hex, metallic, roughness).
LIBRARY = {
    "M_Wood_Warm":     ("#6B4428", 0.0, 0.6),
    "M_Wood_Dark":     ("#4A2E19", 0.0, 0.6),
    "M_Brass":         ("#9A7B3F", 1.0, 0.4),
    "M_Ceramic_Amber": ("#A15A26", 0.0, 0.35),
    "M_Shade_Cream":   ("#F0DCA8", 0.0, 0.8),
}
# 12 segments put 30 degrees between neighbouring faces; 40 keeps them smooth while
# 1-segment bevels (45) and caps (90) stay sharp.
SMOOTH_ANGLE = math.radians(40)
ROOT = "MusicBox"


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def hex_to_linear(h):
    h = h.lstrip("#")
    return tuple(srgb_to_linear(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))


def material(name):
    mat = bpy.data.materials.get(name)
    if mat:
        return mat
    hexv, metallic, roughness = LIBRARY[name]
    mat = bpy.data.materials.new(name)
    if mat.node_tree is None:
        mat.use_nodes = True
    bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    sock = {s.identifier: s for s in bsdf.inputs}
    lin = hex_to_linear(hexv)
    sock["Base Color"].default_value = (*lin, 1.0)
    sock["Metallic"].default_value = metallic
    sock["Roughness"].default_value = roughness
    mat.diffuse_color = (*lin, 1.0)  # viewport solid mode only
    return mat


def remove_existing(name):
    obj = bpy.data.objects.get(name)
    if obj:
        data = obj.data
        bpy.data.objects.remove(obj)
        if data and data.users == 0:
            bpy.data.meshes.remove(data)


def box(size, bevel=0.0, segments=0):
    """Cube scaled to size (metres) in mesh data, centred, optionally bevelled."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    if segments:
        bmesh.ops.bevel(bm, geom=list(bm.verts) + list(bm.edges), offset=bevel,
                        offset_type="OFFSET", segments=segments, profile=0.5,
                        affect="EDGES", clamp_overlap=True)
    return bm


def finish(name, bm, mat_name, location):
    """bmesh -> named mesh + named object, parented to the root, normals outside."""
    remove_existing(name)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    me.shade_smooth()
    me.set_sharp_from_angle(angle=SMOOTH_ANGLE)
    me.materials.append(material(mat_name))
    obj = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(obj)
    obj.parent = bpy.data.objects[ROOT]
    obj.location = location
    return obj


def tris(obj):
    return sum(len(p.vertices) - 2 for p in obj.data.polygons)


def report(obj):
    bpy.context.view_layer.update()
    mw = obj.matrix_world
    pts = [mw @ Vector(c) for c in obj.bound_box]
    lo = [min(p[i] for p in pts) for i in range(3)]
    hi = [max(p[i] for p in pts) for i in range(3)]
    r = lambda v: tuple(round(x, 4) for x in v)
    print(f"{obj.name} | mesh {obj.data.name} | mat {[m.name for m in obj.data.materials]}")
    print(f"  loc {r(obj.location)} | rot_deg {r(math.degrees(a) for a in obj.rotation_euler)}"
          f" | scale {r(obj.scale)} | dims {r(obj.dimensions)}")
    print(f"  world min {r(lo)} max {r(hi)} | tris {tris(obj)}")
    total = sum(tris(o) for o in bpy.data.objects if o.type == "MESH")
    print(f"  running total {total} / 320 tris")


# ==== STEP 0: empty the scene, create the root ===================================
def step_clear():
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj)
    for coll in list(bpy.data.collections):
        bpy.data.collections.remove(coll)
    for block in (bpy.data.meshes, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        for item in list(block):
            block.remove(item)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0
    root = bpy.data.objects.new(ROOT, None)
    root.empty_display_type = "PLAIN_AXES"
    root.empty_display_size = 0.05
    scene.collection.objects.link(root)
    print("objects:", [o.name for o in bpy.data.objects],
          "| meshes:", len(bpy.data.meshes), "| materials:", len(bpy.data.materials))


# ==== STEP 1: body — 0.24 W x 0.17 D x 0.12 H, 2-segment bevel ====================
def step_body():
    bm = box((0.24, 0.17, 0.12), bevel=0.006, segments=2)
    bmesh.ops.translate(bm, vec=(0, 0, 0.06), verts=bm.verts)  # underside on z = 0
    report(finish("MB_Body", bm, "M_Wood_Warm", (0, 0, 0)))


# ==== STEP 2: lid — 0.008 thick, hinged on the body's back top edge, open 18 deg ===
# 0.12 + 0.17*sin(18) + 0.008*cos(18) = 0.180 m overall, as the brief specifies.
def step_lid():
    bm = box((0.24, 0.17, 0.008), bevel=0.002, segments=1)
    # Back-bottom edge of the lid onto the origin, so the origin is the hinge line.
    bmesh.ops.translate(bm, vec=(0, -0.085, 0.004), verts=bm.verts)
    # Negative about X lifts the front (-Y) edge.
    bmesh.ops.rotate(bm, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(-18), 3, "X"),
                     verts=bm.verts)
    report(finish("MB_Lid", bm, "M_Wood_Dark", (0, 0.085, 0.12)))


# ==== STEP 3: key shaft — 12-vertex cylinder along +X out of the right face =======
# Origin on the right face at z = 0.05, on the shaft's axis: the point a key turns on.
# Revised 2026-10-14 from r 0.005 x 0.025: see CHANGE-BRIEF.md, revision A3-1.
def step_key_shaft():
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=12,
                          radius1=0.006, radius2=0.006, depth=0.030)
    bmesh.ops.rotate(bm, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(90), 3, "Y"),
                     verts=bm.verts)
    # Runs x = -0.002 .. 0.028 from the face: 2 mm sunk into the body, no visible seam.
    bmesh.ops.translate(bm, vec=(0.013, 0, 0), verts=bm.verts)
    report(finish("MB_KeyShaft", bm, "M_Brass", (0.12, 0, 0.05)))


# ==== STEP 4: key handle — flat bow, 0.008 x 0.050 x 0.040, 1-segment bevel ========
# Revised 2026-10-14 from 0.006 x 0.035 x 0.025: see CHANGE-BRIEF.md, revision A3-1.
def step_key_handle():
    bm = box((0.008, 0.050, 0.040), bevel=0.0015, segments=1)
    # Centred on the shaft axis, overlapping the shaft end by 1 mm.
    report(finish("MB_KeyHandle", bm, "M_Brass", (0.151, 0, 0.05)))


# ==== STEP 5: clasp — 0.024 x 0.004 x 0.022, front face, top centre, no bevel ======
def step_clasp():
    bm = box((0.024, 0.004, 0.022))
    # Sunk 0.5 mm into the front face (y = -0.085).
    report(finish("MB_Clasp", bm, "M_Brass", (0, -0.0865, 0.107)))


# ==== STEP 6: whole-asset check and save =========================================
def step_check_and_save(path):
    bpy.context.view_layer.update()
    meshes = [o for o in bpy.data.objects if o.type == "MESH"]
    pts = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
    lo = [round(min(p[i] for p in pts), 4) for i in range(3)]
    hi = [round(max(p[i] for p in pts), 4) for i in range(3)]
    print("asset min", lo, "max", hi, "size", [round(hi[i] - lo[i], 4) for i in range(3)])
    print("tris", sum(tris(o) for o in meshes), "/ 320 | objects", len(meshes), "/ 5")
    for o in meshes:
        bm = bmesh.new()
        bm.from_mesh(o.data)
        non_manifold = sum(1 for e in bm.edges if not e.is_manifold)
        centre = sum((f.calc_center_median() for f in bm.faces), Vector()) / len(bm.faces)
        inward = sum(1 for f in bm.faces
                     if f.normal.dot(f.calc_center_median() - centre) < 0)
        bm.free()
        print(f"  {o.name}: rot {tuple(o.rotation_euler)} scale {tuple(o.scale)}"
              f" non-manifold {non_manifold} inward-facing {inward}")
    print("data names:", sorted(o.name for o in bpy.data.objects),
          sorted(m.name for m in bpy.data.meshes), sorted(m.name for m in bpy.data.materials))
    bpy.ops.wm.save_as_mainfile(filepath=path)
    print("saved", path)


if __name__ == "__main__":
    import os, sys
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.abspath(argv[0]) if argv else os.path.join(repo, "blender", "musicbox.blend")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    step_clear()
    step_body()
    step_lid()
    step_key_shaft()
    step_key_handle()
    step_clasp()
    step_check_and_save(out)
