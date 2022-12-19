from pathlib import Path

import yaml

root_dir = Path().cwd()
photos_dir = (root_dir / "images/VRChat")
out_dir = (root_dir / "_data/photos.yml")

parent = Path(f"/images/VRChat")
output_tree = dict()


def main():
    for item in photos_dir.rglob("*.png"):
        album_year = item.parent.name
        photo_output = (parent / item.parent.name / item.name)

        if not album_year in output_tree:
            output_tree[album_year] = list()

        output_tree[album_year].append(photo_output.as_posix())

    with out_dir.open("w") as file:
        file.write(yaml.dump(output_tree))


if __name__ == "__main__":
    main()
