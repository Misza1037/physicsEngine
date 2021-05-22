#physics.py
from vectors import Vector
import pygame


class PhysBase:

    def __init__(self, screen, screenSize, dtv, g = Vector(0, 1), bCoeff = 0.8):
        if type(g) != Vector:
            raise TypeError('PhysBase.__init__(): g | invalid type')
        self.g = g
        self.objects = {}
        self.nextUsedID = 0
        self.screen = screen
        self.dtv = dtv
        self.screenSize = screenSize
        self.bCoeff = bCoeff
    def addObject(self, ID, object):
        if ID in self.objects:
            raise ValueError('PhysBase.addObject.(): ID | invalid value | ID already occupied')
        self.objects[ID] = object


    def removeObject(self, givenID):
        self.objects.pop(givenID)



class PhysObject:

    def __init__(self, base, mass = 1, x=0, y=0, color=(0,0,0), r=10):
        if type(base) != PhysBase:
            raise TypeError('PhysObject.__init__(): base | invalid type')
        if type(mass) != float and type(mass) != int:
            raise TypeError('PhysObject.__init__(): mass | invalid type')
        self.mass = mass
        self.base = base
        self.externalForces = {}
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        self.v0 = Vector(6, 0)
        self.temporaryForce = []

    def applyForce(self, forceVector, ID):
        if ID in self.externalForces:
            raise ValueError('PhysObject.applyForce(): ID | invalid value | ID already occupied')#!
        else:
            self.externalForces[ID] = forceVector

    def removeForce(self, ID):
        if ID in self.externalForces:
            self.externalForces.pop(ID)

    def acceleration(self):
        externalForcesSum = Vector(0,0)
        for i in self.externalForces:
            if self.externalForces[i] != None:
                externalForcesSum += self.externalForces[i]
        for i in self.temporaryForce:
            externalForcesSum += i
        #print(externalForcesSum + self.base.g)
        #print(Vector(1/self.mass, 1/self.mass))
        #print(self.mass)
        return (externalForcesSum + self.base.g) * Vector(1/self.mass, 1/self.mass)
    def velocity(self):
        if self.y == self.base.screenSize[1]-self.r:
            if abs(self.v0.x) < 0.3: self.v0.x = 0
            if abs(self.v0.y) < 0.3: self.v0.y = 0
        rv = self.v0 + self.acceleration() * self.base.dtv
        self.v0 = rv*Vector(0.9995, 0.99995)
        if abs(self.v0.x) < 0.3 and abs(self.v0.y) < 0.3:
            self.rv = Vector(0,0)
            self.v0 = Vector(0,0)
        return rv
    def cycle(self):
         vel = self.velocity() * self.base.dtv
         self.x += vel.x
         if self.y != self.base.screenSize[1]-self.r:
             self.y += vel.y
         self.temporaryForce = []
    def implementTemporaryForce(self, forceVector):
        self.temporaryForce.append(forceVector)
    #def applyGravitationalForce(self, other):
    #    ox = other.x
    #    oy = other.y
    #    other.implementTemporaryForce(gForce)


    def isCollidingWithScreenBorder(self):
        xmax = self.base.screenSize[0]
        ymax = self.base.screenSize[1]
        if self.x-self.r <= 0:
            self.v0 = Vector(-self.v0.x*self.base.bCoeff, self.v0.y)
            self.x = 1 + self.r
        elif self.x+self.r >= xmax:
            self.v0 = Vector(-self.v0.x*self.base.bCoeff, self.v0.y)
            self.x = xmax - 1 - self.r
        elif self.y-self.r <= 0:
            self.v0 = Vector(self.v0.x, -self.v0.y*self.base.bCoeff)
            self.y = 1 + self.r
        elif self.y+self.r > ymax:
            self.v0 = Vector(self.v0.x, -self.v0.y*self.base.bCoeff)
            self.y = ymax - 1 - self.r
        elif self.y+self.r > ymax - 2 and self.v0.y < 1:
            self.v0 = Vector(self.v0.x, 0)
            self.y=ymax-self.r




    def draw(self):
        pygame.draw.circle(self.base.screen, self.color, (int(self.x), int(self.y)), self.r)
if __name__ == '__MAIN__':
    pass
