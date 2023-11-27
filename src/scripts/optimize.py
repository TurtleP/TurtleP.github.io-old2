from pathlib import Path
import subprocess

# TurtleP.github.io/src
root_dir = Path().cwd() / "src"

# TurtleP.github.io/src/.vuepress/public/VRChat
photos_dir = root_dir / ".vuepress/public/VRChat"

# TurtleP.github.io/.VRChat/VRChat
backup_dir = Path().cwd() / ".VRChat/VRChat"

command = "magick {input} -dither FloydSteinberg -colors 255 {output}"

for item in backup_dir.rglob("*.png"):
    destination = photos_dir / item.parent.name # VRChat/{year}/{name}
    Path(destination).mkdir(exist_ok=True)

    subprocess.run(command.format(input=str(item), output=str(destination / item.name)))
