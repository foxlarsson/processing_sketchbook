size(1200, 1200)
ellipseMode(CENTER)
background(0)



# tangle of growing lines
for x in range(0, width, 10):
    line_top_x = random(0, width)
    line_top_y = random(0, height)
    strokeWeight(2)
    stroke(255)
    line(x, height, line_top_x, line_top_y)
    strokeWeight(1)
    stroke(0)
    line(x, height, line_top_x, line_top_y)


# massive circle
noStroke()
ellipse(0, height / 2, height, height)

# save('0011_different_16.png')
