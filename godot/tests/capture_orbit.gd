extends SceneTree
## Records the Assignment 3 showcase with the scene's own camera orbiting the assets,
## for the film, as native 3840x2160 frames rendered by Godot:
##
##   godot --path godot --fixed-fps 30 --script res://tests/capture_orbit.gd -- <out_dir>
##
## Movie Maker records at the window's size, and the OS will not open a window larger than
## the screen, so the scene is rendered into a 3840x2160 SubViewport and each frame Godot
## draws there is saved as a PNG; ffmpeg joins them. The orbit is scripted, so this is
## engine footage of the scene, not gameplay. It moves only the camera; the assets and the
## light stay exactly as saved.

const SECONDS := 16.0
const FPS := 30.0
const WARMUP := 3                          # frames for shadows and sky radiance to settle
const SIZE := Vector2i(3840, 2160)
const TARGET := Vector3(-0.1, 0.4, 0.0)    # the middle of the three assets
const RADIUS := 2.1
const HEIGHT := 0.95

var _frame := 0
var _out := "user://orbit"
var _viewport: SubViewport
var _camera: Camera3D


func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() > 0:
		_out = args[0]
	DirAccess.make_dir_recursive_absolute(_out)
	_viewport = SubViewport.new()
	_viewport.size = SIZE
	_viewport.msaa_3d = Viewport.MSAA_4X
	_viewport.render_target_update_mode = SubViewport.UPDATE_ALWAYS
	get_root().add_child(_viewport)
	var scene: Node = (load("res://scenes/AssetShowcase.tscn") as PackedScene).instantiate()
	_viewport.add_child(scene)
	_camera = scene.get_node("Camera")
	_place_camera(0)


func _process(_delta: float) -> bool:
	# The texture read here is the frame drawn for the previous camera position.
	var shot := _frame - WARMUP
	if shot >= 0:
		_viewport.get_texture().get_image().save_png("%s/f%04d.png" % [_out, shot])
	_frame += 1
	_place_camera(maxi(_frame - WARMUP, 0))
	return shot >= int(SECONDS * FPS) - 1


## Starts in front (+Z, where the scene's camera sits) and turns 300 degrees, ending short
## of the start so a loop or cut does not repeat the opening frame.
func _place_camera(i: int) -> void:
	var angle := deg_to_rad(300.0) * i / (SECONDS * FPS)
	var eye := TARGET + Vector3(sin(angle) * RADIUS, HEIGHT - TARGET.y, cos(angle) * RADIUS)
	# look_at_from_position also works before the scene has entered the tree (first frame).
	_camera.look_at_from_position(eye, TARGET, Vector3.UP)
