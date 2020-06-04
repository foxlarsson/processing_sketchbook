# processing_sketchbook
Small digital sketches created while learning [Processing](https://py.processing.org/) (its Python mode).

Sharing the code to document my process and in case you're curious how this one or that one is made. I will add links to the corresponding images/videos images later (I post them on [my twitter](https://twitter.com/foxlarssonart)).

### 0004_dashed_and_radial.py | 04.06.2020

**Context**: I got the idea of doing dashed sectors when doing the basic arcs section in the [Getting Started with Processing.py](https://www.oreilly.com/library/view/getting-started-with/9781457186820/) book, but could not get it to work yesterday while trying it with radians (I might try again later, but honestly, I find degrees a lot less confusing). After being stuck on that for half an hour, I, of course, noticed, that the very next page suggests using radian() to convert from degrees to radians - so you can just use degrees.

I was planning a static pattern with sectors split into black and white blocks checker board style, but I didn't like how wide they get as the circle grow, and the two rows ended up looking like the most fun.

Happy about the idea of putting the color values in a list and reversing the list when I want to reverse the colors (instead of reassigning the values every time)

Haven't actually tried making anything with transformations or otherwise animated, but played around with random placement for the discs. I actually forgot that draw() executes as long as the code is running, so I thought I'd just randomly place one disc, and got a shower of them endlessly appearing on the screen.

My friend M. said it was horribly anxiety-inducing, but I somehow find it relaxing. Ended up staring for at least fifteen minutes, and I don't keep still for long very often. So I decided to leave the eternally spawning circles.

Also my first try at saving the output as a video. I think I took out the saveFrame('frames/####.png') line from the code when I posted it here, but it basically saves an image every frame, and then you can put them together into a video using Processing's Movie Maker.

Twitter does pretty horrible things to the video quality if I share it as video there, so if I keep doing these, I guess I'll need to think of a less quality killing way of sharing the output. Otherwise instead of the crispy patternness there's muddy muddiness, and it's way less fun.

Thinking of playing around with rotate() tomorrow (read the names of the available functions in bed, because, again, I couldn't sleep). It's almost breathtaking to see code take physical form like this. I've been looking for ways to bring my art and my code together for a long time, and this is starting to feel close to home. And it's very relaxing, somehow. I'm usually an anxiety nightmare, so I really value the things that seem even a little relaxing.

**Image/video links:** []()



### 0003_all_tones_beautiful.py | 03.06.2020

**Context**: I couldn't sleep all night. I was awake thinking about the BLM protests and about how racism sucks. And how killing people sucks. This is my very straightforward rendition of how ridiculous the idea that one tone is somehow better or more important than another is.

This one took a good three or four hours to figure out. I had the image in my mind, but getting the loops and iterations right took a whole lot of trial and error. Especially goint from 0 to 255 to 0 repeteadly while also drawing shapes. Discovered that itertools has awesome cycle() and chain() functions that, put together, let me do just that. (Before I googled and stack overflow-ed it, I spent over an hour trying to iterate in that way by hand). =)

The backgroudn gradient proved both harder and easier than I thought. I also first tried to write it myself by drawing lines from left to right and changing the tone, but I kept getting weird divides. I think I have an idea why now, but I'd need to experiment to see. Ended up realising that this must be a pretty commont thing, googling it and, of course, finding it in the reference.

I like the way it turned out. Spent a lot of time balancing the density and the gradient and shade change speeds. =)

**Image/video links:** []()



### 0002_circle_pattern_in_magenta_and_purple.py | 02.06.2020

**Context**: I liked the stacking/concentric elements in the previous sketch, and the patternish and 3d-ish look they give. Working with triangles seems scarier, so tried reusing the stacked circles (stroke and no fill) to create a pattern. Tried using fill and stroke.

**Image/video links:** []()



### 0001_triangle_and_ellipse.py | 02.06.2020

**Context**: First sketch. Took a look at the first four introductory tutorials, felt lost by the fourth, then found Getting Started with Processing.py by Casey Reas, Ben Fry, and Allison Parrish, and the first three chapters really helped me get off the ground and stop being confused.

After figuring out how lines and basic shapes work, tried using loops.

I'm loving the whole new way of thinking with this way of producing images. And I love it that this translates rhymes well with my love for patterns and repeating elements. 

**Image/video links:** []()
