# This is used to generate the photos.yml file under data
# Saves me time from having to write it all out.

import re
import shutil
from pathlib import Path

import yaml

root_dir = Path().cwd().parent
images_path = (root_dir / "images/VRChat")

output_tree = {"images": []}
out_dir = (root_dir / "_data/photos.yml")


def get_year(date: str) -> str:
    match = re.search(r"(\d{4})-\d{2}-\d{2}", date)

    return match.group(1)


def fix_resolution(filepath: str) -> Path:
    match = re.search(r"(\d{4}x\d{4})", filepath)

    if match.group(1) != "1920x1080":
        return Path(filepath.replace(match.group(1), "1920x1080"))

    return Path(filepath)


renamed = list()
for item in images_path.glob("*"):
    if item.is_file():
        year = get_year(item.name)
        folder = (images_path / year)

        if not folder.exists():
            folder.mkdir()

        moved_path = shutil.copy2(str(item), str(folder))

        output_path = f"images/VRChat/{year}/{item.name}"
        output_tree["images"].append({"path": output_path})

        item.unlink()

with out_dir.open("w") as file:
    file.write(yaml.dump(output_tree))
