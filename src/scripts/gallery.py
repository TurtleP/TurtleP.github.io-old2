from pathlib import Path

import calendar
import re

# set up paths
SOURCE_DIR = "src"  # src
SCRIPTS_DIR = "scripts"  # scripts
VRCHAT_DIR = ".vuepress/public/VRChat"  # .vuepress/public/VRChat
OUTPUT_DIR = "gallery"  # gallery

ROOT_DIR = Path().cwd() / SOURCE_DIR
PHOTOS_DIR = ROOT_DIR / VRCHAT_DIR
DATE_REGEX = re.compile(r"(\d{4}-\d{2}-\d{2})")
TEMPLATES_DIR = (ROOT_DIR / SCRIPTS_DIR) / "templates"
GALLERY_DIR = ROOT_DIR / OUTPUT_DIR

# set up data
CONTENT_TEMPLATE = None
content = dict()

PAGE_TEMPLATE = None
STYLE_TEMPLATE = None


def read_templates() -> None:
    global CONTENT_TEMPLATE
    global PAGE_TEMPLATE
    global STYLE_TEMPLATE

    with open(TEMPLATES_DIR / "content.md", "r") as file:
        CONTENT_TEMPLATE = file.read()

    with open(TEMPLATES_DIR / "page.md", "r") as file:
        PAGE_TEMPLATE = file.read()

    with open(TEMPLATES_DIR / "style.md", "r") as file:
        STYLE_TEMPLATE = file.read()


def setup_content_buffers(path) -> tuple[str, str]:
    date_match = DATE_REGEX.search(path.name)
    split = date_match.group(1).split("-")
    month_int = int(split[1])

    year = split[0]
    month = calendar.month_name[month_int]

    global content

    if not year in content:
        content[year] = dict()

    if not month in content[year]:
        content[year][month] = list()

    content[year][month].append(f"  <img src='{path}' />\n")

    return year, month


def build_page(year: str, content: str) -> str:
    buffer = PAGE_TEMPLATE.format(year=year, content=content)
    buffer += STYLE_TEMPLATE

    return buffer


def main() -> None:
    read_templates()

    for item in PHOTOS_DIR.rglob("*.png"):
        setup_content_buffers(item)

    for year in content:
        year_buffer = ""

        for month in content[year]:
            content_data = "".join(content[year][month])
            buffer = CONTENT_TEMPLATE.format(month=month, content=content_data)
            year_buffer += f"{buffer}\n"

        with open(f"{GALLERY_DIR / year}.md", "w") as file:
            file.write(build_page(year, year_buffer))


if __name__ == "__main__":
    main()
