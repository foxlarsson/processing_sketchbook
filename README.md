# processing_sketchbook
Small digital sketches created while learning [Processing](https://py.processing.org/) (its Python mode).

Sharing the code to document my process and in case you're curious how this one or that one is made. I will add links to the corresponding images/videos later (I post them on [my twitter](https://twitter.com/foxlarssonart)).

### 0026_how_will_this_go.pyde | 13.07.2020

**Context**: This one, to me, is an image of exploration and wonder.

Yesterday I completed the [Math Adventures with Python](https://nostarch.com/mathadventures) Harmonograph project. It's a program that models two pendulums swinging and slowly decaying, plotting the trails they leave, and after that played with all sorts of amplitudes, frequency, phase shift and decay factor values, until I stumbled upon this mix of geometry and intense glowing ring.

Again, even though I originally thought I'd be working only in black and white, the pic seemed to call for color. It has two layers of semi-transparent randomly sized (within a range) and placed circles going on. It took a while to find the right combination of intensty and texture. And I can't wait to get to the fractal part of the book, so I can have shapes deform in organic-like ways.

I tried using randomSeed() with several numbers (pretty much right out of my head) instead of just going on straight to random(). It's something I learned from an interview with [Manolo Gamboa](https://twitter.com/manoloidee) - he does that so that while there's the randomness, he can also recreate the image at a later time if he chooses to.

While working on this pic, I had this anxiety creep up, over and over: if I don't fully understand this formula (the equation that models the pendulum's oscillations), if I know I could never have come up with it myself (my understanding of math and physics is really basic, to put it generously), can I really use it in my art?

Oddly, it's a fear/anxiety that seems to come up with whatever medium I use. A more radical form of this used to be: if I can't do this when dropped into the wild alone in the middle of nowhere with just a knife and a box of matches, does this really count? If I can't do this from scratch, does this really count?

It's and odd kind of worry to have. People play cello without being able to make their own cello from scratch. People write code without being able to build their own computer from scratch (including physically creating each of the individual components and mining the materials).

It's and odd worry, but it's there.

It's interesting that those Processing sketches lately end up very representative of what I'm going through at the moment. THis pic is a perfect representation of now. I'm about to go on vacation and, for the frst time that I can remember, consciously give myself a break. And explore what happens if I rest and give myself time to recover. I'm about to go live in my grandfather's country house without piling on loads of work. Just living, feeding myself and going for walks with my doggo. Drawing and studying if I want to. And I'm all tingly, and somewhat anxious too, about the experiment. And full of wonder and exploration. And t's almost magic to look up at the pic when it's done and see just that.


**Image/video links:** []()




### 0025_we_share_a_space.pyde | 08.07.2020

**Context**: I'd been thinking about grids since doing the [Math Adventures with Python](https://nostarch.com/mathadventures) Rainbow Grid project. Somewhat before that too, but the project gave me the toolset for implementing grids. So I rewrote the code I was using there to build the grid in a way that allows me to just specify the number of cells per row and the size of the gutter between them, and then the details are calculated automatically.  Although I think I'll rewrite it again later using lists.

We share a space was almost an accident. I was messing around with things, and I was thinking of just having those random sets of lines growing in each cell, but somehow ended up with this crazy thing with the left bottom side being filled with those flowing, almost full length thick black bars. I am still figuring out why and how this works, the strangest thing is that they seem to have some opacity, especially at the bottom, even though they're all technically supposed to be just plain solid black. But even though I don't quite understand how this image works and why my code does exactly what it does, it captivates me. On one hand there's something statistical or mathematical to it, and it seems like it should be visualizing some sort of data, on the other hand I love the abstracted rhythm, and the contrast between the two sides. It makes me want to look longer.

I called it "We share a space".

**Image/video links:** []()




### 0024_circle_game.pyde | 06.07.2020

**Context**: Today is my 100th day of #100DaysOfCode. I finished chapter 5 (Transforming Shapes with Geometry) and started chapter 6 (Creating Oscillations with Trigonometry) of [Math Adventures with Python](https://nostarch.com/mathadventures). I might have to go a bit slower on this one to really understand what I'm doing. Or maybe just practice a lot. There are some really beautiful things there.

I discovered a version of this image while working through the part about Roger Antonsen's 90 rotating equilateral triangles, stored it away in a separate sketch file and came back to it after completing the pattern in the book (the black and white and the rainbow version). I was captivated by the criss-cross patterns revealed in the middle and on the outer edge of the circle as the triangles rotate, and by the line going through the whole circle, as if turning it inside out, as the triangles rotate.

I tried a version where the top triangle is hidden and blends in with the rest of the pattern, but I liked this triangle being there and even ended up adding extra rotation to the circle as a whole, to make the triangle roll around it.

I froze watching the animation several times. Reminded me of the Entertainment. Although there's definitely no wobbly lense physics experiments here.  But the way the pattern moves in and out of itself is oddly captivating. I thought I'd be doing less animation, but sometimes it's irresistible.

Mom liked this one. She sent me a message saying so. That's not too usual.

I've been loving the book so far, and I'm looking forward to the sine wave section.

Since my client work has been called of I've been drawing and painting more and doing my weird painted objects. I'm happy making them. I'll also be working on a pair of wire crowns for K. It's good. I am happier that way.

I am thinking about my next round of #100DaysOfCode and what I'll be focusing on, and I think it's my Processing sketches and, slowly, the Django course. The most precious thing that's come out of this round has been discovering Processing and finally finding a way to introduce my art and my code to each other. It feels special, it feels like a space to grow in.

I'm proud to have finished this round. And so grateful for all the support on twitter and all the people I've met. I never expected anything even close. I feel like I'm starting to find my way.

**Image/video links:** []()




### 0023_breathing.py | 02.07.2020

**Context**: This one came from the realization that I could also programmatically change the fill color's opacity. It actually came from a mistake, I was thinking of slowly lowering the opacity, and instead made it drop very rapidly, so there's almost an abrupt break. And I held my breath when I saw it. The splash of color, the intricate tangling lines at the edges, the soft layering of the slightly see-through triangles, and the absolute blackness around. It's somehow focused and calm and vibrant and breathing all at the same time.

The pic reuses the code from 0022_outward almost verbatim, but the rate of the color change is different (it's the most magical when the edge just starts turning a light greenish blue, but never quite gets there), and there's the opacity drop.

I like today's work. And there's so much more to explore.

Also, I think it's remarkable seeing how much calmer the 3rd piece is compared to the first.

**Image/video links:** []()




### 0022_outward.py | 02.07.2020

**Context**: Another thing I learned from chapter 5 (of [Math Adventures with Python](https://nostarch.com/mathadventures)) was using colorMode() and using HSB color mode to change colors based on position. It's easier than with RGB since only one of the numbers defines the actual hue of the color. The book had a cool project with creating a grid of squares with the fill color changing based on the mouse position.

0022_outward mostly reuses the code from 0021_orchestrated with a few small tweaks, and the color changes based on the distance from the point of origin (which has been translated to be in the middle of the canvas). I wanted this one to be static (technically, visually there's a lot of movement), so it' made with noLoop().

I spent quite a while looking for the right rate of the color change.

I like the dense spiral and the strong outward movement, and I like the way the opacity brings in air to the layered triangles.

When I started this series/sketchbook I thought I'd be working in black and white, but it seems that just like on paper, I sometimes crave a big color splash. And I can never resist a rainbow.

**Image/video links:** []()




### 0021_orchestrated.py | 02.07.2020

**Context**: I spent three hours working through chapter 5 of [Math Adventures with Python](https://nostarch.com/mathadventures) - Transforming Shapes with Geometry. While a lot of the things were things I had already done in one form or another, they were coupled with some geometry, and all of this together really helped solidify them in my head. Moving things around and transoforming them with code is a very different way of thinking from what I'm used to with pen and paper.

I reviewed rotate(), translate() and push/popMatrix(), and also the way things change depending on where you place them in your nested loops.

The chapter (I got through about half, then dove into my own art) was very much in line with what I'd been thinking yesterday when I'd started missing my simple squares.

Rotating shapes and the tracks they leave are beautiful.

I started 0021_orchestrated after doing excercise 5.1 in the book (which asks to create a circle with rotating equilateral triangles placed at equal intervals). The rotating triangles were way too irresistable.

I added more rows, and the churning effect was both disturbing and gripping. When playing with the pattern I discovered that when spacing out the shapes in each circle with angles divisible by 3 and 2, I'd get star-like regular shapes, but with numbers like 11 or 13 I'd get spirals. (I might be getting the generaliztion in this explanation wrong, but some sort of trend like that).

I slowed the piece down a bit when exporting and turning into a gif, it's too solid a depiction of an anxiety attack, as if somebody had taken a picture of what's going on in my head when I'm overwhelmed and panicked and stressed to the verge of sanity. You can see the effect if you run the code.

When slowed down there's more dialog there, not just panic. There's the beauty of the synchronous movement, the disturbing churning of the element in the center, the seemingly slower (though technically identical) rotation of the outer triangles.

I'm still in distress over the large conflict I'm going through. But reading the book and going through some of the excercises helped me get myself back. It's good to be able to make art again. Follow-along art and code projects seem to have that effect on me: you know what to do, exactly in what order, and you get something beautiful as a result. And that lets me start breathing again and I start making my own stuff and feeling alive.

**Image/video links:** []()




### 0020_stacking_sine_waves.py | 01.07.2020

**Context**: I wanted to make something with one of the sine wave patterns I came up with in sine_wave_studies, so I tried building a pattern with the fourth wave. I like the movement in the pattern, but I think I'm starting to miss the simplicity of my squares.

I took part in [Noite de Processing](https://garoa.net.br/wiki/Noite_de_Processing#30.2F06.2F20:_.5BONLINE.5D_.23.E3.81.A4.E3.81.B6.E3.82.84.E3.81.8DProcessing.2Ctweets_da_comunidade_japonesa_de_programa.C3.A7.C3.A3o_criativa_-_Alexandre_Villares) yesterday, it was about the #つぶやきProcessing hashtag. Catching yourself listening to something about bitwise operators in Portuguese at 3 a.m. is amusing. =) In truth though, I had a great time.

Although technically I have more free time right now, I am very stressed out by the conflict with my client, so I can barely focus. So it's just a simple sketch for today. Hopefully, I'll be back on my feet in a couple of days and able to focus on longer periods of time. For now it's just one step at a time. Get out of bed - check, workout - check, feed self proper food - check, open sketchbook - check, walk the beast - check, open processing sketchbook - check.

**Image/video links:** []()




### 0019_sine_wave_studies.py | 29.06.2020

**Context**: I was somewhat fuzzy on how sine functions work (apart from the fact that they produce a regular wave), so I did some experiments with the kinds of patterns you can build with sine functions. Each of the waves here is made with lines connecting the dots in two separate sine functions, the x point is the same for both, but the y's are different. I think I'll finally be able to remember that what you divede t by determines how close the wave peaks are to each other (the smaller the number, the closer), and what you multiply the sine function by determines how tall the waves are. Some of the patterns could be fun to play with, but I'd probably want to think of ways of making them a little less regular, otherwise things are too perfect.

**Image/video links:** []()




### 0018_connected.py | 29.06.2020

**Context**: This one is actually the main building block of 0017_the_pull.py - the pull is made of nine of those elements repeated and partly overlapping. I was starting a new sketch, and I wanted to reuse so of the code from the pull, so I copied it in, left only the central element, and it turned out that it was beautiful on its own. So I cleaned it up a bit: the lines now are drawn the exact number of times needed to go the full circle, but without going on for a second circle and starting to overlap with the older lines. And before you ask, nope, there was no math behind that, just experiment, trying smaller and bigger numbers.

Today was a terrible day, so seeing something beautiful really made it better.

**Image/video links:** []()





### 0017_the_pull.py | 27.06.2020

**Context**: Still inspired by Alexander Miller's [tutorial](https://youtu.be/LaarVR1AOvs) and parametric equations, plus I wanted to create something with actual lines this time, not just dots (the sine waves in the previous sketches are actually made up of individual dots).

I mostly prefer static images to animation, I think it's fun to create movement while nothing is actually moving. And there's so much to play with in the static plane, that adding the extra level of animation feels almost wasteful, so for now I am using noLoop() with a set number of repetitions.Although movement and animation could be fun in a work that interacted with something like sounds or the viewer's actions. But for now static pictures give so much to explore, that I feel I'll be doing mostly static for quite a while.

I forgot yet again that the parameter in the equations needs to be a float, so I kept getting weird results for a pretty long time.

I like this one. There's a lot to look at and a lot of movement going on.

I still have a very vague theoretical understanding of how the sine and cosine functions move the dots (although I do know how the waves themselves look), but I play around a lot changing individual elements, and  sometimes it feels like it's making a little more sense. But even though I'm not an algebra/geometry master I love playing around with the values and seeing how things change. And looking for compelling images.

P.S.: I still haven't figured out how to set up a grid for repeat elements, so this code violates DRY reeeeeeeeeeeeee-ally badly, I'll try to get to that some time soon =))

**Image/video links:** []()




### 0016_maybe_summer.py | 26.06.2020

**Context**: This one's a variation of 0015, code-wise. When I saw the fluctuating, almost hand-drawn looking sine waves there, I wanted to experiment with color and layering them immediately.

The color value for the wave is chosen every time a new wave is drawn, and the colors are stored in a dictionary.

I guesss I could have just stored them in a list, but a dictionary allowed me to also store the color names. Mostly for my own convenience, no other big reasons.

I imported the random module, so I could use .choice() for picking a color, and because of that I could no longer use Processing's built-in random() for picking random integers for stroke weight and had to replace those with random.randint().

I was so happy the first time I saw those waves of colors all layered and playing with each other, I just ran the code over and over like a happy kid. =))

In other news I have payed off my last credit card today, and that feels amazing. And it's my personal TGIF today, for the first time in eternit, and I won't be working at all until Monday, so I can make art, sleep, go for walks, or even sleep or do nothing!

**Image/video links:** []()




### 0015_touching_sine_waves.py | 25.06.2020

**Context**: I finally had the time to get back to a bit of Processing. It felt good.

I went simple with this one. A couple of days ago I followed [Alexander Miller](https://spacefiller.space/)'s tutorial called [Recreating Vintage Computer work with Processing](https://youtu.be/LaarVR1AOvs) showing how to creata flowing trailing shapes made of lines. It's inspired by John Whitney's art, and Alexander explains how parametric equations work and how to use them for making thhose flowing moving shapes.

It was a lot of fun, and the tutorial was just really relaxing to follow, and it turns out that parametric equations are basically just a set of equations that each do their own thing with the same parameter.

I was thinking of building something more complex (and static) out of lines, but ended up falling in love after I saw the first sine wave drawn in wight dots across black, and that had to become a pattern.

Because the sine waves are drawn with dots, it was fun making them look more blobby and imperfect. I like that on one hand they're perfect sine waves, but on the other hand the line has this flowing chunkiness.

It was nice to get back to processing. I was scared that I wouldn't know how to approach it any more.

Made some art with my hands later on too. Working on transforming a Darth Vader mask figurine that I have with pinks and blues and neons. And had some nice sketchbook time.

I've been thinking that drawing out things in dots gives a lot of opportunity to play with line texture - as opposed to using line() where the thickness will just be the strokeWeight() you set. So I think I'll be playing with that more. It's fun. And diving in some more into using parametric equations, they're also a lot of fun. Even with my really non-scientific methods of using them where I just play around with sometimes random values until I see something that looks just right.

**Image/video links:** []()




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
