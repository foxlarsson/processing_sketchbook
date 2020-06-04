def setup():
    size(1200, 1200)
    background(22, 10, 46)


def draw_ellipse_sectors(x, y, el_width, el_height, sec_width, color_1, color_2):
    fill(color_1)
    stroke(color_2)
    step = sec_width * 2
    for i in range(0 + sec_width, 360 + sec_width, step):
        arc(x, y, el_width, el_height, radians(i), radians(i + sec_width))
    fill(color_2)
    stroke(color_1)
    for i in range(0, 360, step):
        arc(x, y, el_width, el_height, radians(i), radians(i + sec_width))
        

def draw():
    x = int(random(0, width))
    y = int(random(0, width))
    min_width = 70 
    el_width = min_width * 2
    color_1, color_2 = 0, 255
    colors = [color_1, color_2]
    # draw sectors, reverse, draw sectors
    draw_ellipse_sectors(x, y, el_width * 2, el_width * 2, 6, colors[0], colors[1])
    colors.reverse()
    draw_ellipse_sectors(x, y, el_width, el_width, 6, colors[0], colors[1])
    # saveFrame('frames/####.png')
    

        
