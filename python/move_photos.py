# This script moves all the photos to their respective folders
# once this is complete, photo_data.py should be ran

import re
import shutil
from pathlib import Path

import yaml

root_dir = Path().cwd().parent
images_path = (root_dir / "images/VRChat")


def get_year(filename: str) -> str:
    match = re.search(r"(\d{4})-\d{2}-\d{2}", filename)

    return match.group(1)


def main():
    for item in images_path.glob("*.png"):
        year = get_year(item.name)
        folder = (images_path / year)

        if not folder.exists():
            folder.mkdir()

        shutil.copy2(str(item), str(folder))
        item.unlink()


if __name__ == "__main__":
    main()
