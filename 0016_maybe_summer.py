import random
t = float(0)

def setup():
    size(1200, 1200)
    background(255)
    stroke(40, 175, 176, 50)
    strokeWeight(2)
    noLoop()

def x(t):
    return t

def y(t):
    return sin(t / 15) * 50

def draw():
    colors = {'dark_blue_gray': (114, 109, 168),
              'amaranth': (219, 50, 77),
              'verdigris': (40, 175, 176),
              'carrot_orange': (241, 143, 1),
              'android_green': (153, 194, 77),
              }
    for i in range(-50, height + 50, 10):
        color = random.choice(list(colors.values()))
        stroke(color[0], color[1], color[2], 50)
        with pushMatrix():
            translate(0, i)
            for t in range(0, width, 1):
                strokeWeight(random.randint(1, 30))
                t = float(t)
                point(x(t), y(t))
    # save('0016_maybe_summer_6.png')
