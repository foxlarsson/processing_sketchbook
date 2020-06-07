def setup():
    size(1200, 1200)
    # white background for lines
    noStroke()
    fill(255)
    quad(0, 0, 400 - 10, 0, (400 - 10) * 2.5, height, 0, height)
    
    # white underlay for twisted shape =)
    noFill()
    strokeWeight(7)
    stroke(255)
    quad(0, 0, 0, width / 5, height, 0, height, width * 0.75)
    
    strokeWeight(1)
    stroke(0)
    for i in range(-10, width / 3, 5):
        line(i, 0, i * 5, height)
        
    # black quad over lines
    noStroke()
    fill(0)
    quad(400 - 10, 0, width, 0, width, height, (400 - 10) * 2.5, height)
    
    
    # white twisted   
    
    fill(255)
    quad(0, 0, 0, width / 5, height, 0, height, width * 0.74)

        
def polygon(x, y, radius, npoints):
    angle = TWO_PI / npoints
    with beginClosedShape():
        a = 0
        while a < TWO_PI:
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            vertex(sx, sy)
            a += angle

def draw():    
    # black circle
    stroke(255)
    strokeWeight(3)
    fill(0)
    ellipseMode(CENTER)
    ellipse(width * 0.7, height * 0.145, 300, 300)
    
    strokeWeight(2.5)    
    with pushMatrix():
            translate(width * 0.7, height * 0.145)
            rotate(frameCount / 400.0)
            polygon(0, 0, 80, 3)
    # saveFrame('/frames/####.png')
