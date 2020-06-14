def setup():
    size(1200, 1200)
    noLoop()
    background(0)


def draw():
    margin = width / 12
    num_squares = (width - margin * 2) / 12
    max_width = width - margin - num_squares
    max_height = height - margin - num_squares
    noFill()
    stroke(255)
    for x in range(margin, width - margin - num_squares, num_squares):
        for y in range(margin, height - margin - num_squares, num_squares):        
            with pushMatrix():
                translate(x + 10, y + 10)
                if x > max_width / 2 and y > max_height / 2:
                    rotate(radians(random(0, 360)))
                square(0, 0, num_squares - 30)
    # save('0012_and_then_3.png')
