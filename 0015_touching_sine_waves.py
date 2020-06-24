t = float(0)

def setup():
    size(800, 800)
    background(0)
    stroke(255)
    strokeWeight(2)
    noLoop()

def x(t):
    return t

def y(t):
    return sin(t / 15) * 50

def draw():
    for i in range(20):
        translate(0, height / random(2, 20))
        for t in range(0, width, 1):
            strokeWeight(random(1, 8))
            t = float(t)
            point(x(t), y(t))
    # save('0015_sine_wave_pattern_3.png')
