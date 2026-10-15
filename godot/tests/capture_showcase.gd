extends SceneTree
## Renders the Assignment 3 showcase scene once and saves it, then quits.
## Needs a window (a headless run renders nothing):
##
##   timeout 60 godot --path godot --resolution 1920x1080 --script res://tests/capture_showcase.gd -- <out.png>
##
## This is a still from the fixed camera. It is evidence of the composition and lighting,
## not a substitute for orbiting each asset by hand.

var _frames := 0
var _out := "res://../evidence/a3-showcase.png"


func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() > 0:
		_out = args[0]
	change_scene_to_file("res://scenes/AssetShowcase.tscn")


func _process(_delta: float) -> bool:
	_frames += 1
	if _frames < 30:  # let shadows, sky radiance and auto-exposure settle
		return false
	var img := get_root().get_texture().get_image()
	var err := img.save_png(_out)
	print("saved %s (%dx%d) err=%d" % [_out, img.get_width(), img.get_height(), err])
	return true  # quit
