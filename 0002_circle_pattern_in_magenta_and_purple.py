size(800, 800)
stroke(166, 3, 160)
fill(83, 72, 181, 30)
background(251, 242, 255)

y = 0

z = 50
while y < 900:
    while z < 750:
        ellipse(y, z, 80, 80)
        z += 5
    y += 80
    z = 50
