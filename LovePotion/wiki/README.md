## Welcome ♥

As you probably know by now, LÖVE is a framework for making 2D games in the Lua programming language. It can be used in anything from friendly open-source projects, to evil, closed-source proprietary ones. 

This wiki will refer to what is implemented (so far) in Löve Potion which will follow the official LÖVE API. Please note that not *all* functions of LÖVE will be able to be implemented at this time until it moves from SDL2 to pure OpenGL on Nintendo Switch. The 3DS version also has a very limited selection of the graphics API.

![](lovepotion.png)

## Hello World
This is the full source for 'hello world' in Löve Potion.

```lua
function love.draw()
    love.graphics.print('Hello World!', 400, 300)
end
```