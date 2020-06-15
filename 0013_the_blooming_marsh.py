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
    for i in range(24):
        for x in range(margin, width - margin - num_squares, num_squares):
            for y in range(margin, height - margin - num_squares, num_squares):        
                with pushMatrix():
                    translate(x + 10, y + 10)
                    if width * 0.27 < x < width * 0.73 and height * 0.27 < y < height * 0.73:
                        rotate(radians(random(0, 360)))
                    square(0, 0, num_squares - 30)
    # save('0013_mom_sent_me_pictures_of_cottongrass_2.png')
