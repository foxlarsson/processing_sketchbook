def setup():
    size(1200, 1200)
        

def polygon(x, y, radius, npoints):
    angle = TWO_PI / npoints
    with beginClosedShape():
        a = 0
        while a < TWO_PI:
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            vertex(sx, sy)
            a += angle
            

def draw_polygons(max_size, min_size, sides, step, stroke_weight):
    strokeWeight(stroke_weight)
    for i in range(int(max_size), int(min_size), -step):
            polygon(0, 0, i, sides)

def draw():
    # background
    fill(0)
    rect(0, 0, width / 2, height)
    fill(255)
    rect(width / 2, 0, width, height)
    
    # polygons
    strokeWeight(1.5)
    with pushMatrix():
        translate(width * 0.5, height * 0.5)
        rotate(frameCount / -100.0)
        draw_polygons(260, 70, 7, 11, 1.2)
        
    with pushMatrix():
        translate(width * 0.5, height * 0.5)
        rotate(frameCount / 100.0)
        draw_polygons(155, 0, 7, 15, 2.7)

    # saveFrame('frames/####.png')
