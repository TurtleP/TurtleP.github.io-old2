from pathlib import Path

import yaml

root_dir = Path().cwd().parent
photos_dir = (root_dir / "images/VRChat")
out_dir = (root_dir / "_data/photos.yml")

output_tree = {"images": []}

for item in photos_dir.rglob("*.png"):
    output_path = f"/images/VRChat/{item.parent.name}/{item.name}"
    output_tree["images"].append({"path": output_path})

with out_dir.open("w") as file:
    file.write(yaml.dump(output_tree))
