?> Please read everything carefully. Follow all necessary links and read those thoroughly. They contain important information.

## Getting Started

In order to start contributing, you will need to follow [the instructions on the devkitPro wiki](https://devkitpro.org/wiki/Getting_Started) for setting up a development environment.

### Dependencies

Once the environment is set up, open your terminal and sync the package listing:

<!-- tabs:start -->
#### **Windows (msys2)**
```bash
pacman -Syu
```
#### **Unix-like (Linux, macOS)**
```bash
sudo (dkp-)pacman -Syu
```
<!-- tabs:end -->

Once the packages have syncronized, run the following:

<!-- tabs:start -->
#### **Windows (msys2)**
```bash
pacman -S switch-dev 3ds-dev
```
#### **Unix-like (Linux, macOS)**
```bash
sudo (dkp-)pacman -S switch-dev 3ds-dev devkit-env
```
<!-- tabs:end -->

!> The following information is for development purposes only! Do not build Löve Potion directly if you don't understand programming or are not going to contribute. It only leads to [fragmentation](https://en.wikipedia.org/wiki/Market_fragmentation). If you wish to package your game for distribution, please see [Game Distribution](packaging)

Install the required portlibs:

<!-- tabs:start -->

#### **Windows (msys2)**
```bash
pacman -S switch-sdl2 switch-sdl2_mixer switch-sdl2_ttf switch-sdl2_image switch-sdl2_gfx switch-curl 3ds-sdl 3ds-sdl_mixer 3ds-libpng 3ds-curl
```

#### **Unix-like (Linux, macOS)**
```bash
sudo (dkp-)pacman -S switch-sdl2 switch-sdl2_mixer switch-sdl2_ttf switch-sdl2_image switch-sdl2_gfx switch-curl 3ds-sdl 3ds-sdl_mixer 3ds-libpng 3ds-curl
```
<!-- tabs:end -->

### Compiling

Once everything is set up, simply [fork and clone the repository](https://help.github.com/articles/fork-a-repo/). Afterwards, using the terminal, change your directory to where Löve Potion was cloned:

```bash
cd LovePotion
```

and run `make`

## Pull Requests

### Naming

When you open a new [pull request](https://help.github.com/articles/about-pull-requests/), please give it an easy to recognize name such as `fix-filesystem-reading`. This will help track down [when a defect occurs](https://sqa.stackexchange.com/a/20258) in the event of it being merged (after approval) from a future commit.

### Brace Style

Curly braces ({}) should always be [Allman style](https://pbs.twimg.com/media/CXlB_kpVAAA0pDM.png) for consistency. However, if a statement is only a single-line long, please omit the braces:

```cpp
if (something)
    printf("Woah!");
else if (otherThing)
    printf("Amazing!");
else
    printf("Welp");
```

### Variable & Function Names

- Variable names should be in camelCase
- Class names should be in Titlecase
    - Functions should be as CamelCase
- Lua wrapper functions should be treated like variable names
- Modules are *namespaces*
    - Treat their functions like Class functions

### File Structure

- Header (\*.h) files should be placed inside the *include* folder.
- Source (\*.cpp) files in the *source* folder.
    - Each LÖVE object has a class header/source file and a Lua wrapper.
        - Put it under *objects/{object_type}/*
        - Lua wrapper files must be named as *wrap_{object}*
    - If the file is for a module, put it under *modules*.