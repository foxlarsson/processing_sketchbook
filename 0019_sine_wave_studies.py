def setup():
    size(1200, 1200)
    background(255)
    stroke(0)
    noLoop()


i = float(0)
def draw():
    global i
    range_max = width
    while i < range_max:
        with pushMatrix():
            translate(0, height * 0.07)
            line(i, y1(i), i, y2(i))
        with pushMatrix():
            translate(0, height * 0.27)
            line(i, b1(i), i, b2(i))
        with pushMatrix():
            translate(0, height * 0.415)
            line(i, d1(i), i, d2(i))
        with pushMatrix():
            translate(0, height * 0.535)
            line(i, f1(i), i, f2(i))
        with pushMatrix():
            translate(0, height * 0.63)
            line(i, h1(i), i, h2(i))
        with pushMatrix():
            translate(0, height * 0.725)
            line(i, j1(i), i, j2(i))
        with pushMatrix():
            translate(0, height * 0.82)
            line(i, l1(i), i, l2(i))
            line(i, n1(i), i, n2(i))
        with pushMatrix():
            translate(0, height * 0.93)
            line(i, p1(i), i, p2(i))
        i += 1
    # save('0019_sine_wave_studies.png')
    
# 1
def y1(t):
    return sin(t / 15) * 50

def y2(t):
    return sin(t / 15) *  50 + 70

# 2
def b1(t):
    return sin(t / 5) * 30

def b2(t):
    return sin(t / 5) *  60

# 3
def d1(t):
    return sin(t / 20) * 50

def d2(t):
    return sin(t / 10) *  20

# 4
def f1(t):
    return sin(t / 40) * 50

def f2(t):
    return sin(t / 10) *  20

# 5
def h1(t):
    return sin(t / 40) * 20

def h2(t):
    return sin(t / 120) *  20

# 6
def j1(t):
    return sin(t / 20) * 20

def j2(t):
    return sin(t / 20) *  20 + cos(t / 20) *  20

# 7
def l1(t):
    return sin(t / 60) * 10

def l2(t):
    return sin(t / 30) *  30

def n1(t):
    return cos(t / 40) * 30

def n2(t):
    return cos(t / 40) * 30 + 2

# 8
def p1(t):
    return sin(t / 60) * 50

def p2(t):
    return sin(t / 10) *  10
