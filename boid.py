
#creating a class for boid with a position and velocity as vector
class Boid():
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)