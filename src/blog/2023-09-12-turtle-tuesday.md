---
title: Exciting Updates on LÖVE Potion 3.0 Pre-Release 5
date: 2023-09-12
excerpt: Improvements to overall application stability™ and performance.
tags: ["turtle tuesday", "lovepotion"]
---

It's been some time since I last spoke about LÖVE Potion. If you're unfamiliar with it, it's a port and reimplementation of [LÖVE2D](https://love2d.org) for Nintendo consoles via homebrew. Currently the supported consoles include 3DS and Switch (and Wii U, t least on version 3.0). So today we'll be talking about what's new in the latest pre-release!

### New 3DS Graphics Backend
The main portion of the new pre-release has to do with the Nintendo 3DS version. Prior to this, it was using [citro2d](https://github.com/devkitpro/citro2d). This is explicitly a 2D rendering library frontend of [citro3d](https://github.com/devkitpro/citro3d).

Don't get me wrong, While citro2d has its purpose and is very useful, I had grown tired of its limitations for what I needed. I mean, sure, I had code from my friend piepie which helped with rendering n-gon polygons and other various shapes like arcs which utilized some magical math and triangle rendering with depth tricks. While this worked, it really annoyed me because it looked horrible inside the codebase. It was only as efficient as it could be, too. I also wanted it to be inline with the Switch and Wii U primitive rendering code.

I then proposed the idea to DeltaV about potentially swapping out citro2d for citro3d. After all, citro2d really just used citro3d in the grand scheme of things. If memory serves, the response was something like, "it shouldn't be too hard". That gave me the motivation to start making a test project in a stripped down environment. The good news is that everything just *worked*. The bad news.. I had some work on optimizing the rendering operations, but Delta helped me work that one out later on.

The new citro3d backend also let me refactor the Font class and now when users render text, can colorize their text as they could on normal LÖVE (and on Switch/Wii U).

### New LÖVE Objects
Now with this new backend, I was able to safely add SpriteBatch objects and Meshes! Meshes are rather limited, though and I think the make them better I would definitely need to implement Buffers. So for now, I've released what I could do with the Mesh objects and will come back to them later when I've properly assessed how a Buffer is going to be dealt with.

SpriteBatches are super useful since you can pretty much draw any number of sprites with a specified texture at once. This is more optimal than doing several calls of `love.graphics.draw` for a given texture. I don't have the other numbers on me, but on hardware, I rendered the first **_90_** tiles of Super Mario Bros.'s 1-1 at 60fps. That doesn't sound like much, but for a Nintendo 3DS it is.

Likewise, Meshes allow users to create custom vertex buffers. You can set up the coordinates, texture uvs, and colors easily and draw them to the screen. They're mainly useful, I think, for 3D rendering but I could be wrong. I haven't used Meshes outside of the testing I did.

## Conclusion
I'm stupidly proud of how far LÖVE Potion has come. I remember the early homebrew days where I used Ocarina of Time to launch what is now called "rednand" (redirected NAND). It used to be called "emunand" (emulated NAND) - which I think makes more sense, but that's not important. Then I found out that Videah was making LÖVE Potion and oh boy was I excited about that. I was always willing to test things for them and things rendering at like 15 FPS were quite exciting. Of course, at the time LÖVE Potion was written in C and didn't even follow what official LÖVE did (well, it did (mostly) but I mean code-wise to ensure compatability).

The next pre-release is likely going to add the physics module and compressed texture loading for Switch and Wii U. After that, the video module and then we'll be considered on-par with 2.x. Only thing after that is having people make games, find bugs, and fixing them.
