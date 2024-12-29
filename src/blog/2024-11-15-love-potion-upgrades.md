---
title: Fixes, Features, and a Little LÖVE
excerpt: Announcing the latest iteration of LÖVE Potion, version 3.1.0, with exciting new changes and numerous fixes. A complete overhaul for better stability™ and enhancements.
date: 2024-11-15
tags: ["lovepotion"]
---

Hello everyone, hope you're doing well! It's been a minute since I posted anything noteworthy to my blog, but here we go. Let's talk about something I've been cooking for a little over half a year now: the newest iteration of LÖVE Potion, 3.1.0. While it's still not fully done, I did want to express the excitement of the new changes and mountain of fixes to the codebase that should make *you* excited as well. Seriously.

## A Clean Slate

Now, the first thing to mention is probably some context. Internally, all of LÖVE Potion's code has been overhauled *again*. Yes, again. The same reason that 3.0 exists as it currently does because *that* was its own rewrite. One could argue this should be considered 4.0, not 3.1.0, but the internal changes are really just stability™ and a few enhancements, nothing major.

Anyway, it all started when I had to do some bugfixes for 3.0 - and I think it was [#226](https://github.com/lovebrew/lovepotion/issues/226) and me trying to go through the codebase and find the correct `Source` object file. Even the user who posted the issue and made a PR had a tough time (including compilation and other things). See, in 3.0 I was advised with the brilliant idea of *templating* classes. Each class that required console-specific code would be templated and implemented from an enum which was decided at compile time. At first, this seemed like a genuine great idea, keeping the code separated and do platform-specific stuff as needed. Until it wasn't, because there was *so much code duplication* at some point. Hell, even writing out the templated stuff began to wear on me and become a massive chore.

I asked around the homebrew scene as to what I could do better. Someone (I believe TuxSH) had suggested using [Curiously Recurring Template Pattern](https://en.cppreference.com/w/cpp/language/crtp) and it seemed to be a good solution. I got to work in a private repository to flesh things out and, for the most part, not a lot of things actually needed this pattern. Then the realization of not even needing it came and I just have regular Object-Oriented Programming and (pure) virtual methods.

Fast forward to today, almost everything from 3.0 is reimplemented and the codebase is *much* cleaner than before. This makes maintaining stuff so much easier.

## Testing Grounds

One of the major things that I found out was that 3.0 had a lot of issues. Not like GitHub Issues, but actual code problems that I needed to fix. It was definitely more performant than 2.4, but we're talking things like expected versus actual results of function calls.

Luckily, user [ellraiser](https://github.com/ellraiser) had started making a LÖVE focused [test suite](https://github.com/ellraiser/love-test) that ran all function calls to do exactly what I needed. It was an invaluable resource to validate the code I'd written so far and be absolutely sure things were exactly like the official version of LÖVE. One notable example was that `File:read()` had been incorrect and only pushed one of the return values to the Lua stack. It turned out that another function pushed multiple values, but I only pushed a single one.

The last time I ran the suite was on April 4, 2024. Most if not all tests that could run passed which was awesome. The tests did not run any graphics, audio, physics, or keyboard cases (simply because none of those modules were implemented yet). Prior to this day, there were some filesystem-related failures, which took me some time to debug, but ultimitely the baseline had been set once everything was running smoothly (except Wii U hashing stuff - blame it being big endian for that).

For those curious, here are the overall rankings of the top 3 functions that ran on each console (in the fastest console to slowest to finish)

1. Nintendo Switch - **1.122s**
  - love.thread.Channel: 0.204s
  - love.timer.getTime: 0.101s
  - love.timer.sleep: 0.101s
2. Nintendo Wii U - **2.470s**
  - love.sound.SoundData: 0.269s (*nice*)
  - love.filesystem.File: 0.225s
  - love.filesystem.getDirectoryItems: 0.226s
3. Nintendo 3DS - **5.105s**
  - love.sound.SoundData: 0.814s
  - love.filesystem.getDirectoryItems: 0.687s
  - love.filesystem.File: 0.499s

## New Features

### Remote Debugging

This was a feature that was also backported to 3.0 (and inspired by similar homebrew tools and LÖVE for Android's use of adb) that allows a TCP socket to connect to your console and redirect all `print` calls from Lua back to your PC. It's super useful and has saved a lot of debugging time on my own end before getting the graphics API into the consoles, considering a Lua error ends up being `print`ed as well as displayed graphically based on the LÖVE code. It's as simple as enabling the `console` flag in `conf.lua` and using something like [`telnet`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/telnet) or [`netcat`](https://nmap.org/ncat/guide/index.html) to connect to the device IP on port 8000. When the flag is enabled, the console will wait for a connection up to 10 seconds before automatically resuming.

### Graphics API Changes & Enhancements

#### Screen Dimensions

While everything should be a near perfect replica of official LÖVE, users are aware that `love.graphics.getWidth`, `love.graphics.getHeight`, and `love.graphics.getDimensions` all take a string parameter that will then return the dimension(s) of that screen. This is now much more optional, as it will automatically fetch the screen information of what is currently being rendered and return it as appropriate. You can still request it manually (or it's planned at the very least if I haven't added it yet) for when you want a specific screen.

#### The `love.draw` Callback

Not too much of a noteworthy thing, but now `love.draw` will pass the current 3D slider value on Nintendo 3DS as a secondary parameter. This makes it a *lot* easier to draw stereoscopic 3D items on the screen.

#### Better Batched Rendering

LÖVE Potion 3.0 already had batched draw calls, but honestly it was awful. While it *sort of* batched draw calls (as in, more or less did), it used purely vertices and that took up a lot of memory, which especially on 3DS, we do not have a lot of. When I started working on the graphics API, I stared at the beast that LÖVE utilized for batched draw calls. I was terrified since it made no sense at all, but over time as I learned about how to use citro3d on 3DS I was able to figure it out. LÖVE uses a combination of a vertex buffer and index buffer which leads to reduced memory usage overall when drawing.

This gives the 3DS a massive performance boost when rendering (and a boost for the other consoles, but unsure how significant). How massive are we talking? Rendering a ton of text no longer lags the whole damn console. You can also render like 200 "points" (which are just circles and their radii calculated by point size) and still have 60FPS. I even did a test with *500* points and that dropped it to 40fps which is still insane *and that was technically 1,000 because it rendered to both screens*.

#### Pure citro3d Backend

A massive undertaking, to some degree. LÖVE Potion 3.0 for Nintendo 3DS currently uses *citro2d* which focuses only on the two-dimensional aspect of drawing. If I was going to make 3.1.0 worth the rewrite I absolutely had to use citro3d instead to give myself more flexibility and control. citro2d can only render certain primitives and fonts, but we had to match what LÖVE could do. Learning the API wasn't terrible, but I certainly did struggle getting the `StreamBuffer` class set up.

## Conclusion

LÖVE Potion 3.1.0 is shaping up to be a massive leap forward in performance, usability, and features. While it’s not fully done yet, I’m thrilled about how far it has come and grateful for the support of the homebrew community. If you’re interested in testing, contributing, or just trying out the new features, stay tuned for the release or check out the GitHub repository! Let me know your thoughts — every bit of feedback helps make LÖVE Potion even better.

Thank you again to the following people who have supported and helped me: TuxSH, ellraiser, piepie62, mtheall, fincs, DeltaV, Nawias, the community for LÖVE, and the original inspiration to keep the project going all these years - Videah.
