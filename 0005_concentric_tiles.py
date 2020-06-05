size(1200, 1200)
background(0)
noStroke()
fill(255)
el_width = width / 25
range_top = width + int(round(el_width * 1.125))

for y in range(0, range_top, el_width):
    for x in range(0, range_top, el_width):
        noStroke()
        fill(255)
        ellipse(x, y, el_width, el_width)
        for z in range(el_width, 0, - el_width / 3):
            noFill()
            stroke(0)
            ellipse(x, y, z, z)
