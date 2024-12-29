---
title: Good News, Everyone!
excerpt: Updating the blog after almost seven months. Sharing progress on streaming, gaming, and maintaining a positive outlook despite challenges.
date: 2022-12-18
tags: ["lovepotion", "novel"]
---

## Intro

Long time no posting.. It's been uh, almost seven months since the last blog post. I think it's been long enough that it warrants an update from me. It's pretty hard to remember that I have a blog sometimes, and even when I do, find something to write about. Especially trying to not make a lot of the updates about negative things So, let's get started with what's what.

## Streaming

I used to go by the name "TurtleP95" on Twitch, although I switched that around once I got a bit more serious into this hobby. Well, that plus other factors which I won't exactly cover in this post (still not quite ready to talk about that). Regardless, things have been going decently well. I have a few frequent visitors who stick around in chat and talk to me. I'm not too fussed with whether I have a ton of people watching, as it's really a bad mental state to have.

I've been going through my Steam library one game at a time (well, kinda) to finish whatever I have. It's very rewarding, finally beating something and sharing that with others who enjoy your content. Hell, even if I didn't stream, it would be super nice to complete these games. That's the issue, though, is I rarely find time aside from streaming to even play games that have a campaign and finish them. Which, I mean, I do have the time, but it's the feeling of not having that and just not doing it.

I also have my own little Discord community that has a decent amount of people. We hang out occasionally in the voice chats, playing something like Guilty Gear, Melty Blood, Monster Hunter, etc. It's a great time as we joke around with each other.

## Programming

So, if you recall, I work on [software known as LÖVE Potion](https://github.com/lovebrew/lovepotion). If you don't, well, I don't blame you, since I haven't spoken much about it recently. I was talking with my friend piepie after I had been thinking about doing a whole new rewrite. I initially did a whole entire rewrite for version 2.0, but it was kind of bad in all honesty. I had the idea of common header files and splitting the source files up, but it was not great, especially for maintaining code down the line.

The new 3.0 rewrite fixes a lot of this by introducing templated classes for common data. Not every class gets this, but there are some core classes which required this. Some include the Source, Font, and Joystick objects (although some modules were also templated, such as Font and Image). There are also numerous quality of life fixes to the code's health, like using modern C++ types, like `std::span` and `std::unique_ptr`. These were mainly suggested by DeltaV, who noted a few ridiculous issues that were cropping up in the original 2.x codebase. This isn't all, though, as I've got support for Wii U coming (and it's working at the moment).

At the moment, I'm slowly working on implementing the graphics module. The 3DS can render textures and fonts right now, but I need to get that working on Switch. It's close, but there's a lot of functions left to implement, at least for Fonts. They are so obnoxiously complicated - not to say *overcomplicated*, just really annoying to implement. The Wii U version can only, at least graphically, clear the screen to your designated background color. However, all platforms can do a lot of the basic non-graphical functionalities. There is still no mouse module (obviously) and physics along with video aren't implemented. Physics has some warnings to fix, since it has some recursive call warnings I ran into and didn't know about until recently. Part of that is because the LÖVE codebase does not use  `this->` when handling class members, making it harder for me (or anyone) to really follow something like "is it the class member or parameter?".

## Writing

Ah yeah, the novel I'm working on. The thing that I keep saying I'll work on and then I don't because I forget to. There really haven't been any updates regarding this, which sucks. Writing is a lot of fun since I get to unleash a ton of creativity onto some digital paper in Microsoft Word and just let it flow, see where it takes me. Every time I remind myself of this project, I sigh deeply and wish I had more motivation. I might just have been getting burnt out when writing too much as well, but either way, it's definitely something I truly want to keep working on. Maybe in 2023 I'll get motivation.

## Twitter

My main Twitter account has been inactive for a *long* time. I don't really use it anymore, ever since I started streaming. I made a vtuber Twitter account, started following people, people followed me occassionally. All was good. Although it came to a point of two issues happening where I decided to stop using Twitter altogether.

Originally I thought nothing of the acquisition by Elon Musk, thinking it won't be that bad. I mean, I've obviously heard the stories™ of him buying stuff and then stuff going wrong. I merely didn't expect it to get as bad as it was, though. There's a lot that I could mention, but it's pretty obvious that if you tried looking up what's going wrong with Twitter currently and in the past month, it.. well, it's bad.

The other reasoning has to do with vtuber Twitter. I've mentioned this bit on my Mastodon account before and I'll say it again. I don't care if it's going to sound like a "hot take" either, because it's just unfortunately such a factual observation: there is so much negativity and drama going on it's not even funny. The amount of times that I've seen someone I follow *or* some random "Topics for you" pop up about vtubers where they do nothing but *complain* is absurd. Majority of the time they complain that their viewer counts are dropping, other times that their Twitter follower count is dipping. One person in particular started questioning themselves as to whether they were "good enough".

Now, to be fair, it's not just vtuber Twitter. There's probably a ton of accounts that do nothing but complain or be negative about stuff. However, I saw none of that on my original account. On top of that, sure I don't know what's going on in their lives that they might feel really down. Maybe they're depressed, maybe they're stressed from something, *_I don't know_*. What I *do* know is that online media like Twitter is not the place you should *really* be venting that kind of stuff, at the very least *often*. Repeatedly seeing this stuff even affected me and my streaming. I started to worry about viewer counts and how nobody followed me on Twitter and all. I escaped that mindset a few times, and I can keep doing it, but I would strongly prefer not needing to by separating myself from all of this.

I don't think I really need to mention the content that popped up where people were basically horny-posting pictures of their vtuber models. I'm not on vtuber Twitter - nor Twitter in general - to see that kind of content. Sure, sexual content sells and drives people to do stuff, but it's just sad to see if you have to pull that kind of stuff to gain an audience. I'm not sure if this or people constantly complaining is worse in terms of being an attention seeker, in all honestly. Regardless, if they want to  make that kind of content, by all means, do it, but I myself don't really approve of it.

I've moved over to Mastodon under a single account now. Programming updates for LÖVE Potion, streaming, personal stuff, etc are all posted on there.

## Conclusion

That's about everything that's happened. Lots of good things this time around, less negative things. It's a step forward, but that's life sometimes. Not everything will always be a positive situation, but on the flip side, not everything can be negative. Hoping to do another update whenever and that it's something good.
