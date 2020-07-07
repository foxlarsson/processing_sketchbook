t = 0


def setup():
    size(1200, 1200)
    background(0)
    colorMode(HSB)


def draw():
    global t
    translate(width / 2, height / 2)
    rotate(radians(t))
    for i in range(90):
        rotate(radians(360/90))
        with pushMatrix():
            translate(0, 330)
            rotate(radians(t))
            equi_tri(240)
    t += 2
    # saveFrame('/frames/0024_circle_game_####.png')


def equi_tri(length):
    triangle(0, - length, length * sqrt(3) / 2, length / 2, - length * sqrt(3) / 2, length / 2)
