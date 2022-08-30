from p5 import size

#opening a window
def setup():
    size(width, height)

def draw():
    for boid in flock:
        boid.show()