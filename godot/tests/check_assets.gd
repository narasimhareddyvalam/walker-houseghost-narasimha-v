extends SceneTree
## Headless check for the three Assignment 3 assets.
##
##   timeout 120 godot --headless --path godot --script res://tests/check_assets.gd --fixed-fps 60
##
## For each .glb: loads it, instances it at the origin, and prints the bounding-box size
## of its meshes, the scale of every node, the axis its height lies along, and where its
## lowest point is. Each number is compared with CHANGE-BRIEF.md (as revised).
##
## What this check does NOT prove, stated so it is not over-read:
## - Nothing about how an asset LOOKS: colour on screen, lighting, shading, whether it
##   reads as what it is. A headless run renders nothing. That is the human orbit check.
## - "Lowest point at y = 0" is measured on the mesh bounds in isolation. It proves the
##   origin is at the base; it does not test contact with the scene's floor (there is no
##   collider here, and none of these assets has one), unlike Module 3's floor check.
## - Bounding boxes are axis-aligned boxes around the geometry: they confirm overall size
##   and orientation, not the shape inside the box.
## - It reads the imported scenes, so it inherits any import setting; it does not
##   re-verify the .glb files (tools/inspect_glb.py does that independently).

const ASSETS := [
	# name, path, expected size (x, y up, z) in metres, from CHANGE-BRIEF.md revisions
	["MusicBox", "res://assets/models/musicbox.glb", Vector3(0.316, 0.2968, 0.19)],
	["BedsideLamp", "res://assets/models/lamp.glb", Vector3(0.28, 0.42, 0.28)],
	["Bookshelf", "res://assets/models/bookshelf.glb", Vector3(0.64, 1.0, 0.30)],
]
const TOL := 0.002  # 2 mm

var failures := 0


func _initialize() -> void:
	for spec in ASSETS:
		_check(spec[0], spec[1], spec[2])
	print("RESULT: %s (%d failure%s)" % ["PASS" if failures == 0 else "FAIL",
		failures, "" if failures == 1 else "s"])
	quit(1 if failures else 0)


func _check(asset_name: String, path: String, expected: Vector3) -> void:
	var packed: PackedScene = load(path)
	if packed == null:
		_fail("%s: could not load %s" % [asset_name, path])
		return
	var root: Node3D = packed.instantiate()

	# Transforms are composed by hand from the root down. The instance is never added to
	# the tree: during _initialize a node is not yet inside it, and global_transform then
	# silently returns identity (a first version of this check failed every asset that way).
	var boxes: Array[AABB] = []
	var scales_ok := _walk(root, Transform3D.IDENTITY, boxes)
	var box: AABB = boxes[0]
	for b in boxes.slice(1):
		box = box.merge(b)

	var size := box.size
	# The standing axis is the one the brief's height lies along: find which axis matches it.
	var height_axis := ""
	for i in 3:
		if abs(size[i] - expected.y) <= TOL:
			height_axis += "XYZ"[i]
	print("%s" % asset_name)
	print("  root scale %s | every node scale 1,1,1: %s" % [root.scale, scales_ok])
	print("  bbox size %s (expected %s)" % [_v(size), _v(expected)])
	print("  height %.4f m lies along: %s | lowest point y = %.4f"
		% [expected.y, height_axis if height_axis != "" else "none", box.position.y])

	if not scales_ok:
		_fail("%s: a node has non-unit scale" % asset_name)
	var diff := (size - expected).abs()
	if max(diff.x, max(diff.y, diff.z)) > TOL:
		_fail("%s: size differs from the brief by more than %.0f mm" % [asset_name, TOL * 1000])
	if not height_axis.contains("Y"):
		_fail("%s: height does not lie along Y (lying on its side?)" % asset_name)
	if abs(box.position.y) > TOL:
		_fail("%s: lowest point is %.4f m, not 0 (origin not at the base)" % [asset_name, box.position.y])
	root.free()


## Collects each mesh's bounds in the asset's own space; returns false if any node's
## scale is not 1, 1, 1.
func _walk(n: Node, parent: Transform3D, boxes: Array[AABB]) -> bool:
	var ok := true
	var xform := parent
	if n is Node3D:
		var n3 := n as Node3D
		xform = parent * n3.transform
		if not n3.scale.is_equal_approx(Vector3.ONE):
			ok = false
			print("  %s scale %s" % [n.name, n3.scale])
	if n is MeshInstance3D:
		boxes.append(xform * (n as MeshInstance3D).get_aabb())
	for c in n.get_children():
		ok = _walk(c, xform, boxes) and ok
	return ok


func _v(v: Vector3) -> String:
	return "(%.4f, %.4f, %.4f)" % [v.x, v.y, v.z]


func _fail(msg: String) -> void:
	failures += 1
	print("  FAIL: " + msg)
