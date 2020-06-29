def setup():
    size(1200, 1200)
    background(255)
    stroke(0)
    strokeWeight(1)
    noLoop()


i = float(0)
def draw():
    global i
    range_max = 377
    while i < range_max:
        with pushMatrix():
            translate(width / 2, height / 2)
            line(x1(i), y1(i), x2(i), y2(i))
            i += 1
    # save('0018_connected.png')
    

def x1(t):
    return sin(t / 10) * 400

def y1(t):
    return cos(t / 10) * 500

def x2(t):
    return sin(t / 30) * 300

def y2(t):
    return cos(t / 30) * cos(t / 30) * 100
