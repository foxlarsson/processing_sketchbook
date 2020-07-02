t = 0


def setup():
    size(1200, 1200)
    background(0)
    noLoop()
    colorMode(HSB)


def draw():
    global t
    translate(width / 2, height / 2)
    while t < 360:
        for dist_from_center in range(60, width, 40):
            fill(dist_from_center * 0.28, 230, 230, 100)
            for row in range(13):
                with pushMatrix():
                    translate(dist_from_center, 0)
                    rotate(radians(t))
                    equi_tri(50)
                    t += 0.02
                rotate(radians(360 / 13))
    save('0022_outward.png')


def equi_tri(length):
    triangle(0, - length, length * sqrt(3) / 2, length / 2, - length * sqrt(3) / 2, length / 2)
