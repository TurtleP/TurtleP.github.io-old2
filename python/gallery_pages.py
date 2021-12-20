# This is used when a new yearly album is available
# the script will generate /gallery/{year}.html with proper navigation buttons
# along with the data that it should hold

from pathlib import Path

directories = list()

root_dir = Path().cwd().parent

(root_dir / "gallery").mkdir(exist_ok=True)
photos_path = (root_dir / "images/VRChat")
templates_dir = "page_templates"


def generate_buttons(index: int, year: str, years: int, buffer: str) -> str:
    current_year = int(year)

    previous_year = current_year - 1
    previous_text = f"{previous_year} Photos"

    next_year = current_year + 1
    next_text = f"{next_year} Photos"

    if index == 0:
        previous_year = "index"
        previous_text = "Gallery Home"
    elif index == years:
        next_year = "index"
        next_text = "Gallery Home"

    return buffer.format(previous=f"/gallery/{previous_year}", previous_text=previous_text,
                         next=f"/gallery/{next_year}", next_text=next_text)


def generate_page(index: int, year: str) -> str:
    page_buffer = None
    with open(f"{templates_dir}/template_main.txt", "r") as file:
        page_buffer = file.read()

    gallery_page = (root_dir / f"gallery/{year}.html")
    total_years = len(directories) - 1

    with gallery_page.open("w") as page:
        page.write(page_buffer.format(year=year).replace(
            "[", "{").replace("]", "}") + "\n")

        buttons = "two" if index == 0 or index == total_years else "three"
        with open(f"{templates_dir}/template_buttons_{buttons}.txt", "r") as file:
            button_data = generate_buttons(
                index, year, total_years, file.read())
            page.write(button_data)


def main():
    for filepath in photos_path.glob("*"):
        directories.append(filepath.name)

    for index, year in enumerate(directories):
        generate_page(index, year)


if __name__ == "__main__":
    main()
