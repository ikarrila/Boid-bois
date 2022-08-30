from p5 import Vector, stroke, circle

#creating a class for boid with a position and velocity as vector
class Boid():
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)


    def show(self):
        stroke(255)
        circle((self.position.x, self.position.y), radius=10)