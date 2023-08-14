from pathlib import Path

import yaml

# TurtleP.github.io/src
root_dir = Path().cwd() / "src"

# TurtleP.github.io/src/.vuepress/public/VRChat
photos_dir = root_dir / ".vuepress/public/VRChat"

output_tree = dict()


def gather_paths():
    for item in photos_dir.rglob("*.png"):
        album_year = item.parent.name
        photo_output = Path(f"/VRChat/{item.parent.name}/{item.name}")

        if not album_year in output_tree:
            output_tree[album_year] = list()

        output_tree[album_year].append(photo_output.as_posix())

    build_slides()


with open(Path(__file__).parent / "year.txt", "r") as file:
    year_format = file.read()

with open(Path(__file__).parent / "photo.txt", "r") as file:
    photo_format = file.read()


def build_slides():
    current_index = 0

    output_buffers = dict()
    for album_year in output_tree:
        if not album_year in output_buffers:
            add = "\n\n"
            if album_year != "2019":
                add = "---\n\n"

            output_buffers[
                album_year
            ] = f"{add}{year_format.format(album_year=album_year)}"

            current_index = 0

        for photo_path in output_tree[album_year]:
            output_buffers[album_year] += photo_format.format(photo_path=photo_path)
            current_index += 1

            add = "\n--\n\n"
            if current_index == len(output_tree[album_year]):
                add = "\n"

            output_buffers[album_year] += add

    with open("test.md", "w") as file:
        file.write("@slidestart")
        for album_year in output_buffers:
            file.write(output_buffers[album_year])
        file.write("@slideend")


if __name__ == "__main__":
    gather_paths()
