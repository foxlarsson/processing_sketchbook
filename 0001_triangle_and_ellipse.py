size(800, 800)

x1 = 0
y = 10
noFill()

while x1 < 300:
    triangle(x1, 50, 220, 180, 110, y)
    x1 += 5
    y += 10

z = 50
while z < 750:
    ellipse(width * 2/3, z, 80, 80)
    z += 5
