# processing_sketchbook
Small digital sketches created while learning [Processing](https://py.processing.org/) (its Python mode).

Sharing the code to document my process and in case you're curious how this one or that one is made. I will add links to the corresponding images/videos later (I post them on [my twitter](https://twitter.com/foxlarssonart)).


### 0014_cottongrass.py | 15.06.2020

**Context**: So I liked the pattern from 0013_the_blooming_marsh so much that I just  had to have a whole field of that goodness. =) 

And now I want a dress with fabric like that. I find looking at it incredibly relaxing because of the balance of regular and irregular elements, and I just want to keep looking. And it still looks like the pic of the marsh with cottongrass blooming that my mom sent me.

When I fall in love with a pattern, it's pretty obsessive, I just want to fill more and more spaces with it and sit there, looking at it and just soaking it in.

**Image/video links:** []()




### 0013_the_blooming_marsh.py | 15.06.2020

**Context**: I thought of this one while finishing 0012_wait.py уesterday, but it was so late I was falling asleep, so I had to try it out today first thing in the morning. I commented out the noLoop() and just watched the rotating squares form their pattern magic for a while. But the noLoop() had to come back, because if the suares rotate and draw new versions of themselves infinitely, in the end it's a solid white shape, and all the fun is in the fine lines and detail and patternness. I though at first that it reminded me of dandelions, but the my friend T. said it was just like that picture of cottongrass blooming on the marsh that my mom had sent me the day before, and it was.

I played around a while with getting only the part of the square in the middle of the size that I wanted to transform into lace fluff, leaving the other squares there around for contrast, and I just really love the magic of this pattern, especially that it's not quite regular, although wtending towards regularity, because the squares are rotating random amounts. But there's still regularity because of a lot of repetition, so you can let your eye wander. And I like the edges too, because some places you can see the squares fanning out.

**Image/video links:** []()




### 0012_wait.py | 14.06.2020

**Context**: I'm on chapter 4 of [Math Adventures with Python](https://nostarch.com/mathadventures), so I've started working through the graphing excercises, built a grid and plotted a parabola. So I was thinking about grids in the evening.

I like fine lines and detail on solid color. And I like the combination of structure and randomness.

I think, pushMatrix(), translate() and rotate() are starting to make sense to me. I actually started this one by playing around with a simple line grid, but then I though some space and some standalone squares would be much more fun. I first thought I would only be adding a tiny bit of rotation and randomness, but I like the squares flying totally out of control. Also, I think this is the first time I'm using an if statement in one of my pics.

This pic is drawn with noLoop(), so that the contents of draw() are only drawn once, without looping. But looping while randomly rotating the squares actually also gives a really cool and interesting effect, with contrast not only in how organized the squares are, but also in texture and density, and I want to experiment more with that tomorrow.

In other news, I completed my second workout today, and I'm really proud of myself. We went for a long evening walk with the doggo, and there was sun, and summer evening air, and the smell of trees, and it was good.

**Image/video links:** []()




### 0011_its_here.py | 13.06.2020

**Context**: I'm still very tired, so doing just little things. This one is a tangle of grass-like rods in the back, and a massive white circle up front. I called it "It's here".

I spent a lot of time experimenting with the circle. I knew the rods were just what I wanted as soon as I saw them. And I though the circle would have heavy stroke and concentric elements. And after a whole bunch of experiments it turned out that I like it best with this huge empty circle. I like the blandness of it, how it's sort of in your face. And you might be there trying to look at the tangle of dainty lines, figuring out how they relate to each other and what they are all about, but there it is, big and bland and very much there.

**Image/video links:** []()




### 0010_flowing.py | 11.06.2020

**Context**: I've been not in a very good space emotionally and intellectually since Monday, so it's just little stuff lately, and even those little thins are pretty heroic, because I can barely think and focus. But I got through the first two chapters of [Math Adventures with Python](https://nostarch.com/mathadventures), tried moving turtles around and then drawing square and star spirals with turtles, and after that I thought I would try to experiment with something similar in Processing, so I put together this script that takes a tiny square and grows it while also rotating it a bit with every iteration. It results in a nice mesmerizing spiral sort of thing, especially if you get the right proportion between how much you turn each square and how far apart the squares are and how fast they grow. Added a bit of randomness in the stroke weights, that makes the pic more interesting and dynamic.

It's not big art, but I'm glad I did something. And I used rotate and transform.

**Image/video links:** []()




### 0009_looking_for_the_light.py | 08.06.2020

**Context**: I played around more with lines that start all over the place, then meet at the same point. Here's another thing that's very different about digital art: the ease with which you can draw white lines on a black background, and have both colors vibrant, clear and non-muddy. The way you can have this glow of absolute white on absolute black.

Since yesterday I've been thinking how I want to turn some of those sketches into actual painting, acrylic on large wooden panels. Some of them with moving parts. I'm not sure how to do that now though at the moment. My home is filled to the brim with older artworks, sculptures and paintings, so there's soon not going to be space to walk. And starting a series of large pieces would be borderline madness now.

I called this one Looking for the Light. Partly because today was a terrible day I guess. I got my period, and it felt like a full scale mental and physical attack on my body and being. Mother nature has blessed me with bouts of acute depression to come with my periods, as if physical pain and the whole thing of dealing with the bleeding was not enough.

I used more random elements in this piece. The points where the lines converge are predefined, but the places the lines start are random. The twelve black circles are randomly placed too. But after writing that up, I spent a while choosing an image where this randomness came together in just the right way.

I like how the points of light seems so very obvious, yet there are all those circles missing them altogether. Technically, of course, the circles are not in any way programmed to interact with the "light", they're just scattered randomly.

I keep forgetting that Processing has its own random() function, import Python's random module, and then see things crash because there's a conflict between the two.

My [Math Adventures with Python](https://nostarch.com/mathadventures) book came today, and I'm looking forward to learning about all this stuff. The book smells like new book and paper and print, and all the math art in there is beautiful.

**Image/video links:** []()




### 0008_keep_still.py | 07.06.2020

**Context**: This is a completely different way of thinking and drawing from the art processes that I'm used to. At least with my current skill level, I can't just go ahead and fill a shape with a pattern for balance, and this forces to think of other ways to find balance. I am also using way more solid tones than I'm used to.

This is a slow piece, the movement of the triangle right between relaxing and excruciating. I like the way it's the only small part that's technically moving, yet in a way it's more static than the lines and angles in the bakground.

I finished reading 1984 on Friday. And took a day off on Saturday.

The tools used in this piece are a combination of those used in previous ones, although technically used quad() is new. I alsoused layering to show/hide parts of the line pattern. Thinking of doing more with converging lines.

**Image/video links:** []()




### 0007_choosing_sides.py | 06.06.2020

**Context**: I was digging around the examples folder (processing has a library of examples built in) and stumbled on the polygons one. So don't think I came up with the formula for drawing a polygon with N sides all by myself. And the polygons file also had an example of using rotate() which I'd been meaning to play with, so I spent a while figuring out how things work there, and then combined that with the concentric outlines idea from the previous sketches.

The use of an abolute point for the shapes' centers (0, 0) + translate() to keep them in the same places while the pushMatrix() works its animation magic is still somewhere between clear and confusing, I experimented a lot there changing values, and it seems that when I use anything other than (0, 0), the shapes start floating around instead of rotating in place, so it has to be (0, 0) with translate() for the actual positioning. That almost makes sense because of the way  you're actually moving the matrix, and not the shape, to animate, but I'll have to spend a few days with the thought to really feel comfortable.

I like the way the shapes fall in and out of alignment as they rotate.

Spent a while playing around with the proportions and the stroke weights, and the step size between the concentric rows in both of the polygons. The fluid movement and vibration had to be balanced out with the heavy solid background.

Thinking of doing something with groups of converging lines tomorrow.

**Image/video links:** []()




### 0006_growing.py | 05.06.2020

**Context**: I was initially experimenting with rows that zoom in and out in circle width (I have a very particular flowing pattern idea for this), but so far I keep getting lost in my loops when I try to do this, so I decided to go for something simpler: rows that just grow from left to right.

I read about ellipseMode() and rectangleMode() that allow you to change what point the first two arguments in ellipse() and rectangle() determine - where it will "grow" from: the corner (invisible if it's a circle), or the center. It can be cool when aligning things, for example.

I spent over two hours playing around with different versions of this script after I figured out the logic of it, playing with distances and proportions, and the way the concentric elements in the larger circles overlap and build the pattern, and where the elements start, and the spacing. So if you see some weird looking numbers that seem oddly specific, that's not some magical mathematical context, it's me playing around with the pic and getting it to look just the way I want it.

I like the combination of coming up with the logic for the picture, but then also using this same logic to make very different images, and thinking what you actually want to see. This is actually something I used to miss when drawing my patterns by hand: the fifty thousand "what ifs". I'll still be drawing by hand though, those two actually feed into each other well, it's almost like the drawing is reinforcing the coding, while the coding is reinforcing the drawing, it's good. And I still, after several days, find the process relaxing, which is unusual. =)

**Image/video links:** []()



### 0005_concentric_tiles.py | 05.06.2020

**Context**: This one was inspired by the nested for loops excercise in the [Getting Started with Processing.py](https://www.oreilly.com/library/view/getting-started-with/9781457186820/) book. I liked the diamonds created by the negative space around the circles, and I wanted to play with that. It somehow also never occured to me to draw rows and columns in a single nested for loop statement instead of a loop for rows and a loop for columns.

I like grids. I hate writing in square grid notebooks, but I love lined and dotted paper. And although this might feel too repetitive as a standalone pattern, I still find it relaxing to look at, and I like the way it starts to blur and move before you eyes when you look for longer. It made me want to experiment with rows that grow and decrease in width in cycles, but I haven't been able to get the exact kind of loop that I want to work so far, I'll keep trying.

Side note: ellipse(x, y, z, z) is pretty terrible variable naming =)

**Image/video links:** []()



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
