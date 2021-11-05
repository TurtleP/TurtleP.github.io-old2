# This is used to generate the photos.yml file under data
# Saves me time from having to write it all out.

import re
import shutil
from pathlib import Path

import yaml

__images = Path("images/VRChat")

__output_tree = {"images": []}
__outdir = "_data/photos.yml"


def get_year(date: str) -> str:
    match = re.search("(\d{4})-\d{2}-\d{2}", date)

    return match.group(1)


for item in __images.glob("*"):
    if item.is_file():
        __year = get_year(item.name)

        __folder = (__images / __year)

        if not __folder.exists():
            __folder.mkdir()

        __path = shutil.move(str(item), str(__folder))
        __output_tree["images"].append({"path": f"/{__path}"})

with open(__outdir, "w") as file:
    file.write(yaml.dump(__output_tree))
