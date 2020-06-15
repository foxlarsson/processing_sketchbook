def setup():
    size(1200, 1200)
    noLoop()
    background(0)


def draw():
    margin = 0
    num_squares = (width - margin * 2) / 16
    max_width = width - margin - num_squares
    max_height = height - margin - num_squares
    noFill()
    stroke(255)
    for i in range(20):
        for x in range(margin, width + num_squares, num_squares):
            for y in range(margin, height + num_squares, num_squares):        
                with pushMatrix():
                    translate(x + 10, y + 10)
                    rotate(radians(random(0, 360)))
                    square(0, 0, num_squares - 30)
    # save('0014_cottongrass_5.png')
