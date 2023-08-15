from pathlib import Path
import subprocess

# TurtleP.github.io/src
root_dir = Path().cwd() / "src"

# TurtleP.github.io/src/.vuepress/public/VRChat
photos_dir = root_dir / ".vuepress/public/VRChat"

command = "magick {input} -dither FloydSteinberg -colors 255 {output}"

for item in photos_dir.rglob("*.png"):
    subprocess.run(command.format(input=str(item), output=str(item)))
