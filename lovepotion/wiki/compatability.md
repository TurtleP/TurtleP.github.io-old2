!> Löve Potion is a work in progress, so things may be missing. Please open an issue on the [GitHub Repository](https://github.com/TurtleP/LovePotion) if there's a feature you'd like to request.

## Trello Board

It would be rather tedious for me to list out everything that *is* compatable, but also ***horrible*** for anything that's just specific for Löve Potion. However, I made a [Trello Board](https://trello.com/b/T1FlF1sY/l%C3%B6ve-potion) from the start of making Löve Potion to show everything currently implemented and also upcoming features. It's not a roadmap. Please keep in mind this Trello Board only reflects the Nintendo Switch version. However, the main difference is a larger lack of some graphics functions on 3DS.

## 3DS functions

?> Custom fonts are loaded in via a *.bcfnt file. Do not use a *.ttf. A tool for converting *.ttf files to this new format will be provided in the future by devkitPro.

- `love.graphics.newFont(path, size)` will take the path to a *.bcfnt file, and `size` for the scale. Alternatively, one can load a system font using the follwing names in place of the path parameter:

|Name|Notes|
|----|-----------|
|standard|JPN, USA, EUR, and AUS regions font|
|chinese|Chinese font|
|korean|Korean font|
|taiwanese|Taiwanese font|

- `love.graphics.set3D(enable)` enable or disable 3D with `true` or `false`
- `love.graphics.setDepth(depth)` set the 3D depth
- `love.graphics.setScreen(screen)` set the screen to render to: `"top"` or `"bottom"`

## System Functions

- `love.system.hasInternet()` returns whether or not the system has an internet connection*
- `love.system.getRegion()` returns the region of the system (USA, Japan, etc.)
- `love.system.getUsername()` returns the name of the user running Löve Potion (or your game)

*not yet implemented

## Gamepad Constants

?> Löve Potion only uses the `love.gamepad*` callbacks for input handling (with the joycon or the 3DS system itself).

### Face Buttons

|Button|Description  |
|------|-------------|
|a     | The A button|
|b     | The B button|
|y     | The Y button|
|x     | The X button|

### Directional Buttons

|Button |Description  |
|-------|-------------|
|dpup   | D-Pad Up    |
|dpdown | D-Pad Down  |
|dpright| D-Pad Right |
|dpleft | D-Pad Left  |

### Shoulder Buttons

|Button|Description    |
|------|---------------|
|l     | The L button  |
|r     | The R button  |
|zl    | The ZL button |
|zr    | The ZR button |

### Special Buttons

#### Nintendo Switch

|Button|Description   |
|------|--------------|
|plus  | The + button |
|minus | The - button |

#### Nintendo 3DS

|Button|Description        |
|------|-------------------|
|start |The 'start' button |
|select|The 'select' button|
