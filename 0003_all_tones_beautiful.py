from itertools import cycle, chain

def setup():
    size(1600, 1600)
    # grad_start = 0
    

def y_cycle(x, y, circle_size, step):
    for fill_tone in cycle(chain(range(0, 255, 51), range(255, 0, -51))):
        fill(fill_tone)
        ellipse(x, y, circle_size, circle_size)
        y += step
        if y > 1650:
            break
        

# Define colors
b1 = color(255)
b2 = color(0)


def setGradient(x, y, w, h, c1, c2):
    noFill()
# Left to right gradient
    for i in range(x, x + w + 1):
        inter = map(i, x, x + w, 0, 1)
        c = lerpColor(c1, c2, inter)
        stroke(c)
        line(i, y, i, y + h)

def draw():
    setGradient(0, 0, width / 2, height, b1, b2)
    setGradient(width / 2, 0, width / 2, height, b2, b2)
    y = 5
    fill_tone = 0
    stroke(0)
    circle_size = 30
    step = int(circle_size * 1.1)
    for x in range(10, 1650, step):
        y_cycle(x, y, circle_size, step)
    
    save('all_tones_beautiful.png')
