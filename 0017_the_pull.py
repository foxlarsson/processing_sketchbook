def setup():
    size(1200, 1200)
    background(255)
    stroke(0)
    strokeWeight(1)
    noLoop()


i = float(0)
def draw():
    global i
    range_max = 500
    # 0
    while i < range_max:
        with pushMatrix():
            translate(0, 0)
            line(x1(i), y1(i), x2(i), y2(i))
        with pushMatrix():
            translate(width / 2, 0)
            line(x1(i), y1(i), x2(i), y2(i))
        with pushMatrix():
            translate(width, 0)
            line(x1(i), y1(i), x2(i), y2(i))
        # height / 2
        with pushMatrix():
            translate(0, height / 2)
            line(x1(i), y1(i), x2(i), y2(i))
        with pushMatrix():
            translate(width / 2, height / 2)
            line(x1(i), y1(i), x2(i), y2(i))
        with pushMatrix():
            translate(width, height / 2)
            line(x1(i), y1(i), x2(i), y2(i))
        # height
        with pushMatrix():
            translate(0, height)
            line(x1(i), y1(i), x2(i), y2(i))
        with pushMatrix():
            translate(width / 2, height)
            line(x1(i), y1(i), x2(i), y2(i))
        with pushMatrix():
            translate(width, height)
            line(x1(i), y1(i), x2(i), y2(i))
        i += 1
    # save('0017_the_pull.png')

def x1(t):
    return sin(t / 10) * 400

def y1(t):
    return cos(t / 10) * 500

def x2(t):
    return sin(t / 30) * 300

def y2(t):
    return cos(t / 30) * cos(t / 30) * 100
