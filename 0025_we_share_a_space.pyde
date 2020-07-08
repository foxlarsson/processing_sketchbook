def setup():
    size(1200, 1200)
    rectMode(CENTER)
    noLoop()
    background(255)
    strokeWeight(2)


def draw():
    cells_per_row = 12
    gutter = 0
    cell_size = width / cells_per_row
    cell_offset = cell_size / 2
    background(0)
    translate(cell_offset, cell_offset)
    for x in range(cells_per_row):
        for y in range(cells_per_row):
            rect(cell_size * x - 1, cell_size * y, cell_size - gutter, cell_size - gutter)
            for i in range(cell_size * x, cell_size * x + cell_size, 3):
                line(i, random(cell_size * y, cell_size * y + cell_size),
                     i, random(cell_size * x, cell_size * x + cell_size))
    # save('0025_we_share_a_space_10.png')
