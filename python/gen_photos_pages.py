from pathlib import Path

directories = list()

root_dir = Path().cwd().parent

(root_dir / "gallery").mkdir(exist_ok=True)
photos_path = (root_dir / "images/VRChat")

page_buffer = None
with open("template_main.txt", "r") as file:
    page_buffer = file.read()

for filepath in photos_path.glob("*"):
    directories.append(filepath.name)


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


def generate_page(index, year) -> str:
    gallery_page = (root_dir / f"gallery/{year}.html")
    total_years = len(directories) - 1

    with gallery_page.open("w") as page:
        page.write(page_buffer.format(year=year).replace(
            "[", "{").replace("]", "}") + "\n")

        buttons = "two" if index == 0 or index == total_years else "three"
        with open(f"template_buttons_{buttons}.txt", "r") as file:
            button_data = generate_buttons(
                index, year, total_years, file.read())
            page.write(button_data)


for index, year in enumerate(directories):
    generate_page(index, year)
