"""Shared helpers and the one material library for every Assignment 3 asset.

Imported by each tools/blender/build_<asset>.py. Rule 4 of CHANGE-BRIEF.md (one shared
five-material library) is enforced here: a build script can only ask for a material by a
name in LIBRARY.

Units are metres, +Z up, -Y front. Meshes are built at their final size and orientation
in bmesh, so no object ever carries rotation or scale to apply.
"""

import bpy, bmesh, math
from mathutils import Matrix, Vector

# Hex is sRGB as written in CHANGE-BRIEF.md; converted to linear before use.
LIBRARY = {
    "M_Wood_Warm":     {"hex": "#6B4428", "metallic": 0.0, "roughness": 0.6},
    "M_Wood_Dark":     {"hex": "#4A2E19", "metallic": 0.0, "roughness": 0.6},
    "M_Brass":         {"hex": "#9A7B3F", "metallic": 1.0, "roughness": 0.4},
    "M_Ceramic_Amber": {"hex": "#A15A26", "metallic": 0.0, "roughness": 0.35},
    # Revision A3-3: the shade and bulb glow, so the lamp reads as lit without a
    # second light in the Godot scene.
    "M_Shade_Cream":   {"hex": "#F0DCA8", "metallic": 0.0, "roughness": 0.8,
                        "emission": 1.0},
}
# Edges sharper than this stay hard: cylinder caps (90). Bevel chamfers (45) and
# cylinder and sphere sides (30 or less) shade smooth.
SMOOTH_ANGLE = math.radians(60)


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def hex_to_linear(h):
    h = h.lstrip("#")
    return tuple(srgb_to_linear(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))


def material(name):
    mat = bpy.data.materials.get(name)
    if mat:
        return mat
    spec = LIBRARY[name]
    mat = bpy.data.materials.new(name)
    if mat.node_tree is None:
        mat.use_nodes = True
    bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    sock = {s.identifier: s for s in bsdf.inputs}
    lin = hex_to_linear(spec["hex"])
    sock["Base Color"].default_value = (*lin, 1.0)
    sock["Metallic"].default_value = spec["metallic"]
    sock["Roughness"].default_value = spec["roughness"]
    if spec.get("emission"):
        sock["Emission Color"].default_value = (*lin, 1.0)
        sock["Emission Strength"].default_value = spec["emission"]
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


def cylinder(radius, depth, segments=12, radius_top=None, caps=True):
    """Cylinder (or truncated cone) along Z, centred. Segment count is always explicit."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=caps, cap_tris=False, segments=segments,
                          radius1=radius, radius2=radius if radius_top is None else radius_top,
                          depth=depth)
    return bm


def uv_sphere(radius, segments, rings):
    """UV sphere, centred. Segment and ring counts are always explicit."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segments, v_segments=rings, radius=radius)
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


def finish(name, bm, mat_names, location, root, weighted=True):
    """bmesh -> named mesh + named object, parented to root, normals outside.

    weighted=True for flat-faced parts with bevels; curved parts keep plain smooth
    normals, which weighting would only distort.
    """
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
    obj.parent = bpy.data.objects[root]
    obj.location = location
    if weighted:
        weighted_normals(obj)
    return obj


def tris(obj):
    return sum(len(p.vertices) - 2 for p in obj.data.polygons)


def report(obj, budget):
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
    print(f"  running total {total} / {budget} tris")


def clear_scene(root):
    """Empty the file of objects, collections and data; create the root empty."""
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
    empty = bpy.data.objects.new(root, None)
    empty.empty_display_type = "PLAIN_AXES"
    empty.empty_display_size = 0.05
    scene.collection.objects.link(empty)
    print("objects:", [o.name for o in bpy.data.objects],
          "| meshes:", len(bpy.data.meshes), "| materials:", len(bpy.data.materials))


def check_and_save(path, budget, max_shapes, open_meshes=()):
    """Whole-asset check, then save. open_meshes are intentionally open surfaces:
    their boundary edges are expected and signed volume does not apply."""
    bpy.context.view_layer.update()
    meshes = [o for o in bpy.data.objects if o.type == "MESH"]
    pts = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
    lo = [round(min(p[i] for p in pts), 4) for i in range(3)]
    hi = [round(max(p[i] for p in pts), 4) for i in range(3)]
    print("asset min", lo, "max", hi, "size", [round(hi[i] - lo[i], 4) for i in range(3)])
    print("tris", sum(tris(o) for o in meshes), f"/ {budget} | objects", len(meshes),
          f"/ {max_shapes}")
    for o in meshes:
        bm = bmesh.new()
        bm.from_mesh(o.data)
        boundary = sum(1 for e in bm.edges if e.is_boundary)
        non_manifold = sum(1 for e in bm.edges if not e.is_manifold and not e.is_boundary)
        flipped = sum(1 for e in bm.edges if e.is_manifold and not e.is_contiguous)
        if o.name in open_meshes:
            facing = "open surface, volume n/a"
        else:
            bmesh.ops.triangulate(bm, faces=bm.faces)
            volume = sum(f.verts[0].co.dot(f.verts[1].co.cross(f.verts[2].co))
                         for f in bm.faces) / 6
            facing = f"signed-volume {volume:+.2e} ({'outward' if volume > 0 else 'INWARD'})"
        bm.free()
        print(f"  {o.name}: rot {tuple(o.rotation_euler)} scale {tuple(o.scale)}"
              f" open-edges {boundary} non-manifold {non_manifold}"
              f" inconsistent-winding {flipped} {facing}")
    print("data names:", sorted(o.name for o in bpy.data.objects),
          sorted(m.name for m in bpy.data.meshes), sorted(m.name for m in bpy.data.materials))
    bpy.ops.wm.save_as_mainfile(filepath=path)
    print("saved", path)
