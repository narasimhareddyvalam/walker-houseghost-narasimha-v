"""Write gamedev-evidence.json for the Assignment 3 film (schema 1, code-then-result-v1).

Inventories every authored file under godot/ (not .godot/, .git/ or .uid), ties the files
this assignment added to the narrated beats that explain them, and excludes the Assignment 2
2D-slice files with a reason. Run after the result clips are rendered, since their hashes
are recorded:

    python3 youtube/claude-liam-houseghost-a3-gamedev/build_evidence.py
"""

import hashlib, json
from pathlib import Path

REEL = Path(__file__).resolve().parent
GAME = REEL.parent.parent / "godot"
sheet = json.loads((REEL / "beat_sheet.json").read_text())
beats = {b["beat_id"]: b for b in sheet["beats"]}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


files = sorted(p.relative_to(GAME).as_posix() for p in GAME.rglob("*")
               if p.is_file() and not any(x in (".godot", ".git") for x in p.relative_to(GAME).parts)
               and p.suffix != ".uid")

components = [
    {"id": "props", "beat_ids": ["B28", "B30"],
     "explanation": "The three exported props: binary glTF files built in Blender, and the import settings Godot generated for them.",
     "match": lambda f: f.startswith("assets/models/")},
    {"id": "showcase", "beat_ids": ["B32", "B33"],
     "explanation": "The showcase scene the assignment specifies: a floor, one light, a camera and the three props side by side at game scale.",
     "match": lambda f: f == "scenes/AssetShowcase.tscn"},
    {"id": "headless-check", "beat_ids": ["B29", "B30", "B31"],
     "explanation": "The headless check: loads each prop, composes its transforms, and compares bounding box, node scale, up axis and lowest point with the brief.",
     "match": lambda f: f == "tests/check_assets.gd"},
    {"id": "captures", "beat_ids": ["B02", "B33"],
     "explanation": "The scripts that render the showcase still and the native 4K orbit used in the film.",
     "match": lambda f: f in ("tests/capture_showcase.gd", "tests/capture_orbit.gd")},
]

records, exclusions = [], []
for f in files:
    ids = [c["id"] for c in components if c["match"](f)]
    if ids:
        role = {"props": "exported 3D prop" if f.endswith(".glb") else "import settings",
                "showcase": "3D scene", "headless-check": "headless check script",
                "captures": "film capture script"}[ids[0]]
        records.append({"path": f, "sha256": sha(GAME / f), "role": role, "component_ids": ids})
    else:
        exclusions.append({"path": f, "reason": "Assignment 2 2D slice (scripts, scenes, art, audio, project settings), "
                           "unchanged by this assignment; this film explains the three 3D props, their scene and their checks."})

comp_out = []
for c in components:
    comp_out.append({"id": c["id"], "explanation": c["explanation"], "beat_ids": c["beat_ids"],
                     "files": [r["path"] for r in records if c["id"] in r["component_ids"]]})

excerpts = []
for bid in ("B29", "B32"):
    props = beats[bid]["shot"]["remotion"]["props"]
    path = props["path"].split("godot/", 1)[1].split(":")[0]
    start = props["startLine"]
    text = props["code"]
    excerpts.append({"beat_id": bid, "path": path, "start_line": start,
                     "end_line": start + len(text.split("\n")) - 1, "text": text})

pairs = [
    {"code_beat": "B29", "result_beat": "B30",
     "observation": "All three props arrive within 2 mm of the brief, height along Y, every node scale 1, lowest point at zero.",
     "media": {"path": "media/B30.mp4", "sha256": sha(REEL / "media/B30.mp4")}},
    {"code_beat": "B32", "result_beat": "B33",
     "observation": "The scene those lines define, rendered by Godot as the camera orbits the three props.",
     "media": {"path": "media/B33.mp4", "sha256": sha(REEL / "media/B33.mp4")}},
]

build_id = hashlib.sha256("".join(r["sha256"] for r in records).encode()).hexdigest()
data = {"schema_version": 1, "teaching_contract": "code-then-result-v1",
        "game": {"name": "houseghost-a3", "build_id": build_id},
        "components": comp_out, "files": records, "exclusions": exclusions,
        "excerpts": excerpts, "code_result_pairs": pairs}
(REEL / "gamedev-evidence.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
print(f"{len(records)} files in components · {len(exclusions)} excluded · {len(excerpts)} excerpts · {len(pairs)} pairs")
