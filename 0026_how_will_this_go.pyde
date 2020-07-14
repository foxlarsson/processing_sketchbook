def setup():
    size(1200, 1200)
    noLoop()
    colorMode(HSB)


def draw():
    t = 0
    points = []
    randomSeed(28318321)
    
    noStroke()
    for n in range(6000):
        fill(random(75, 255), 255, 52, 80)
        el_size = random(3, 230)
        ellipse(random(- 80, width + 80), random(- 80, height + 80), el_size, el_size)
    
    for n in range(700):
        fill(random(75, 255), 255, 255, 90)
        el_size = random(3, 13)
        ellipse(random(- 80, width + 80), random(- 80, height + 80), el_size, el_size)
    
    while t < 700:
        points.append(double_harmonograph(t))
        t += 0.01
    
    translate(width / 2, height / 2)    
    stroke(255)
    strokeWeight(1)
    for index, p in enumerate(points):
        if index < len(points) - 1:
            line(p[0], p[1], points[index + 1][0], points[index + 1][1])
    
    # save('0026_how_will_this_go.png')


def double_harmonograph(t):
    a1, a2, a3, a4 = 600, 600, 600, 600  # amplitudes
    f1, f2, f3, f4 = 0.6, 1.2, 1.4, 1.4  # frequencies
    p1, p2, p3, p4 = PI / 2, 0, -PI / 6, 0  # phase shifts
    d1, d2, d3, d4 = 0.5, 0.0062, 0, 0  # decay constants
    
    x = a1 * cos(f1 * t + p1) * exp(-d1 * t) + a3 * cos(f3 * t + p3) * exp(-d3 * t)
    y = a2 * sin(f2 * t + p2) * exp(-d2 * t) + a4 * sin(f4 * t + p4) * exp(-d4 * t)
    return[x, y]
    
