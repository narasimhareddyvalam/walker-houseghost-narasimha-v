"""Read .glb files directly (no Blender, no Godot) and print what was actually exported.

    python3 tools/inspect_glb.py godot/assets/models/*.glb

Per file: every node with its transform, the asset's bounds in glTF space (Y up), the
triangle count, and each material's base colour converted back to sRGB hex, so it can be
compared with the hex values in CHANGE-BRIEF.md.
"""

import json, struct, sys


def read_glb(path):
    with open(path, "rb") as f:
        data = f.read()
    magic, version, _ = struct.unpack_from("<4sII", data, 0)
    assert magic == b"glTF" and version == 2, (path, magic, version)
    length, kind = struct.unpack_from("<I4s", data, 12)
    assert kind == b"JSON"
    return json.loads(data[20:20 + length])


def linear_to_srgb_hex(rgb):
    def enc(c):
        c = c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
        return round(max(0.0, min(1.0, c)) * 255)
    return "#" + "".join(f"{enc(c):02X}" for c in rgb[:3])


def main(paths):
    for path in paths:
        g = read_glb(path)
        print(f"== {path}")
        print("  asset:", g["asset"].get("generator"), "| up axis: glTF is always +Y up")
        nodes = g["nodes"]
        lo, hi, tris = [1e9] * 3, [-1e9] * 3, 0
        for n in nodes:
            t = n.get("translation", [0, 0, 0])
            extra = {k: n[k] for k in ("rotation", "scale", "matrix") if k in n}
            print(f"  node {n['name']:<14} translation {[round(v, 4) for v in t]}"
                  f" {extra if extra else '| no rotation, no scale'}")
            if "mesh" in n:
                for prim in g["meshes"][n["mesh"]]["primitives"]:
                    acc = g["accessors"][prim["attributes"]["POSITION"]]
                    for i in range(3):  # children of an unrotated, unscaled root: offset only
                        lo[i] = min(lo[i], acc["min"][i] + t[i])
                        hi[i] = max(hi[i], acc["max"][i] + t[i])
                    tris += g["accessors"][prim["indices"]]["count"] // 3
        size = [round(hi[i] - lo[i], 4) for i in range(3)]
        print(f"  bounds min {[round(v, 4) for v in lo]} max {[round(v, 4) for v in hi]}")
        print(f"  size x {size[0]} | y (up) {size[1]} | z {size[2]} | lowest point y = {round(lo[1], 4)}")
        print(f"  triangles {tris}")
        for m in g.get("materials", []):
            pbr = m.get("pbrMetallicRoughness", {})
            base = pbr.get("baseColorFactor", [1, 1, 1, 1])
            line = (f"  material {m['name']:<16} base {linear_to_srgb_hex(base)}"
                    f" metallic {pbr.get('metallicFactor', 1.0)} roughness {pbr.get('roughnessFactor', 1.0)}"
                    f" double-sided {m.get('doubleSided', False)}")
            if "emissiveFactor" in m:
                strength = m.get("extensions", {}).get("KHR_materials_emissive_strength", {}).get("emissiveStrength", 1.0)
                line += f" emissive {linear_to_srgb_hex(m['emissiveFactor'])} x{strength}"
            print(line)


if __name__ == "__main__":
    main(sys.argv[1:])
