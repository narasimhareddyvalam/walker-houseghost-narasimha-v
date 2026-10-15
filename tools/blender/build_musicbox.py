"""Build the MusicBox asset (CHANGE-BRIEF.md, Assignment 3, asset 1, as revised by A3-2).

Every live execute_blender_code call during the build sent HELPERS plus exactly one
step_* function from this file, followed by a call to it. Run headless from an empty
scene with:

    blender -b --factory-startup --python-exit-code 1 -P tools/blender/build_musicbox.py [-- out.blend]

Default output: blender/musicbox.blend (relative to the repository root).

Units are metres. +Z is up, -Y is the front. The root empty MusicBox sits at the world
origin, which is the centre of the underside of the plinth. Meshes are built at their
final size and orientation in bmesh, so no object carries rotation or scale to apply.
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
# Edges sharper than this stay hard: cylinder caps (90). Bevel chamfers (45) and
# 12-segment cylinder sides (30) shade smooth; weighted normals keep big faces flat.
SMOOTH_ANGLE = math.radians(60)
ROOT = "MusicBox"
PLINTH_H = 0.015  # the box stands on the plinth; every part above it is offset by this


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


def cylinder(radius, depth, segments=12):
    """Capped cylinder along Z, centred. Segment count is always explicit."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=segments,
                          radius1=radius, radius2=radius, depth=depth)
    return bm


def weighted_normals(obj):
    """Face-area weighted normals, baked into the mesh: chamfers shade round, big faces flat."""
    mod = obj.modifiers.new("WeightedNormal", "WEIGHTED_NORMAL")
    mod.mode = "FACE_AREA"
    mod.keep_sharp = True
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    baked = bpy.data.meshes.new_from_object(obj.evaluated_get(dg),
                                            preserve_all_data_layers=True, depsgraph=dg)
    old = obj.data
    obj.modifiers.remove(mod)
    obj.data = baked
    bpy.data.meshes.remove(old)
    baked.name = obj.name


def finish(name, bm, mat_names, location):
    """bmesh -> named mesh + named object, parented to the root, normals outside."""
    remove_existing(name)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    me.shade_smooth()
    me.set_sharp_from_angle(angle=SMOOTH_ANGLE)
    for m in mat_names:
        me.materials.append(material(m))
    obj = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(obj)
    obj.parent = bpy.data.objects[ROOT]
    obj.location = location
    weighted_normals(obj)
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
    bpy.context.view_layer.update()
    meshes = [o for o in bpy.data.objects if o.type == "MESH"]
    pts = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
    lo = [round(min(p[i] for p in pts), 4) for i in range(3)]
    hi = [round(max(p[i] for p in pts), 4) for i in range(3)]
    print("asset min", lo, "max", hi, "size", [round(hi[i] - lo[i], 4) for i in range(3)])
    print("tris", sum(tris(o) for o in meshes), "/ 320 | objects", len(meshes), "/ 6")
    for o in meshes:
        bm = bmesh.new()
        bm.from_mesh(o.data)
        non_manifold = sum(1 for e in bm.edges if not e.is_manifold)
        flipped = sum(1 for e in bm.edges if e.is_manifold and not e.is_contiguous)
        bmesh.ops.triangulate(bm, faces=bm.faces)
        volume = sum(f.verts[0].co.dot(f.verts[1].co.cross(f.verts[2].co))
                     for f in bm.faces) / 6
        bm.free()
        print(f"  {o.name}: rot {tuple(o.rotation_euler)} scale {tuple(o.scale)}"
              f" non-manifold {non_manifold} inconsistent-winding {flipped}"
              f" signed-volume {volume:+.2e} ({'outward' if volume > 0 else 'INWARD'})")
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
    step_plinth()
    step_body()
    step_lid()
    step_key_shaft()
    step_key_bow()
    step_clasp()
    step_check_and_save(out)
