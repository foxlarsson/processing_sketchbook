size(1200, 1200)
background(0)
ellipseMode(CENTER)


def draw_line(smallest_el, y):
    x = 0
    while x < width + smallest_el:
        ellipse(x, y, smallest_el, smallest_el)
        for z in range(int(smallest_el), 0, int(- smallest_el / 3)):
            noFill()
            stroke(255)
            ellipse(x, y, z, z)
        smallest_el *= 1.4
        x += smallest_el * 0.85
        

smallest_size = 20
y = height + smallest_size
while y > -100:
    draw_line(smallest_size, y)
    y -= 80

save('0006_growing.png')
