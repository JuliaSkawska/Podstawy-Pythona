import math
class Roller:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def getRadius(self):
        return self.radius

    def getHeight(self):
        return self.height

    def baseSA(self):
        return self.radius*self.radius*3.14

    def sideSA(self):
        return self.radius*self.height*2*3.14

    def volume(self):
        return self.baseSA()*self.height

    def longest(self):
        h=self.height**2
        r=(2*self.radius)**2
        return math.sqrt(h+r)
