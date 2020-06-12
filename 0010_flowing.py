def setup():
    size(1200, 1200)
    rectMode(CENTER)
    noLoop()
    background(255)
    noFill()

def draw_tile(max_width, step):        
    for i in range(5, max_width, step):
        strokeWeight(random(1, 4))
        rect(0, 0, i, i)
        rotate(radians(2))
        
def draw():
    translate(width * 0.5, height * 0.5)
    draw_tile(int(width * 1.5), 10)
    save('0010_flowing_9.png')
    
