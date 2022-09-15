from p5 import size

#opening a window
def setup():
    size(width, height)

def draw():
    for boid in flock:
        boid.show()

#
def main():
    setup()
    for x in range(fps)
        draw()
     
    
    
 if __name__ == '__main__':
    main()
