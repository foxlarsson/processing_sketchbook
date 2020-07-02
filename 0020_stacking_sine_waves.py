def setup():
    size(1200, 1200)
    background(255)
    stroke(0)
    noLoop()
    
    
def draw():
    for y in range(-20, height + 80, 40):
        draw_wave(y)
    save('0020_stacking_sine_waves.png')


def draw_wave(y):
    i = float(0)
    while i < width + 91:
            with pushMatrix():
                translate(-91, y)
                line(i, d1(i), i, d2(i))
            i += 1


def d1(t):
    return sin(t / 20) * 50

def d2(t):
    return sin(t / 10) *  20
