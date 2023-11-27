from pathlib import Path

import calendar
import re

import json

from PIL import Image, ExifTags

# TurtleP.github.io/src
root_dir = Path().cwd() / "src"

# TurtleP.github.io/src/.vuepress/public/VRChat
photos_dir = root_dir / ".vuepress/public/VRChat"

gallery_data = dict()
date_regex = re.compile(r"(\d{4}-\d{2}-\d{2})")


def get_date(path):
    date_match = date_regex.search(path.name)
    split = date_match.group(1).split("-")

    year = split[0]
    month = calendar.month_name[int(split[1])]

    return year, month


for item in photos_dir.rglob("*.png"):
    year, month = get_date(item)

    if not year in gallery_data:
        gallery_data[year] = dict()

    if not month in gallery_data[year]:
        gallery_data[year][month] = list()

    gallery_data[year][month].append(f"/VRChat/{year}/{item.name}")

MONTH_HTML = "<h2>{title}</h2>"
PHOTOS_DIV = """
<div class="image-preview">
{content}</div>

"""
PHOTO_SRC = """  <img src="{url}"/>\n"""

photo_buffer = ""
buffer = ""

for year in gallery_data:
    with open(photos_dir / f"gallery_{year}.txt", "w") as file:
        for month in gallery_data[year]:
            buffer += MONTH_HTML.format(title=month)
            for photo_path in gallery_data[year][month]:
                photo_buffer += PHOTO_SRC.format(url=photo_path)

            buffer += PHOTOS_DIV.format(content=photo_buffer)
            photo_buffer = ""

        file.write(buffer)
        buffer = ""
