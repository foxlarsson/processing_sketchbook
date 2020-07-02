t = 0


def setup():
    size(1200, 1200)
    background(0)


def draw():
    global t
    translate(width / 2, height / 2)
    for dist_from_center in range(70, width, 40):
        for i in range(13):
            with pushMatrix():
                translate(dist_from_center, 0)
                rotate(radians(t))
                equi_tri(50)
                t += 0.02
            rotate(radians(360 / 13))
    # saveFrame('/frames/0021_in_my_head_####.png')


def equi_tri(length):
    triangle(0, - length, length * sqrt(3) / 2, length / 2, - length * sqrt(3) / 2, length / 2)
