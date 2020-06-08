size(1200, 1200)
background(0)
stroke(255) 
 
 
def draw_section_pattern(center_x, center_y):
    for _ in range(240):
        x = random(0, width)
        y = random(0, height)
        line(x, y, center_x, center_y)
 
draw_section_pattern(width * 0.25, height * 0.25)
draw_section_pattern(width * 0.75, height * 0.25)
draw_section_pattern(width * 0.25, height * 0.75)
draw_section_pattern(width * 0.75, height * 0.75)

ellipseMode(CENTER)
noFill()
stroke(0)
strokeWeight(7)
for _ in range(12):
    x = random(60, width - 60)
    y = random(60, height - 60)
    ellipse(x, y, 110, 110)
        
# save('0009_looking_for_light.png')
