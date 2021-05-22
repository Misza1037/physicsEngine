#physics.py
from vectors import Vector
import pygame


class PhysBase:

    def __init__(self, screen, dtv, g = Vector(0, 1)):
        if type(g) != Vector:
            raise TypeError('PhysBase.__init__(): g | invalid type')
        self.g = g
        self.objects = {}
        self.nextUsedID = 0
        self.screen = screen
        self.dtv = dtv

    def addObject(self, ID, object):
        if ID in self.objects:
            raise ValueError('PhysBase.addObject.(): ID | invalid value | ID already occupied')
        self.objects[ID] = object


    def removeObject(self, givenID):
        self.objects.pop(givenID)



class PhysObject:

    def __init__(self, _physBase, mass = 1, x=0, y=0, color=(0,0,0), r=10):
        if type(_physBase) != PhysBase:
            raise TypeError('PhysObject.__init__(): _physBase | invalid type')
        if type(mass) != float and type(mass) != int:
            raise TypeError('PhysObject.__init__(): mass | invalid type')
        self.mass = mass
        self._physBase = _physBase
        self.externalForces = {}
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        self.v0 = Vector(0,0)
        self.temporaryForce = []

    def applyForce(self, forceVector, ID):
        if ID in self.externalForces:
            if self.externalForces[ID] == None:
                self.externalForces[ID] = forceVector
            else:
                raise ValueError('occupied')#!
        else:
            self.externalForces[ID] = forceVector

    def removeForce(self, ID):
        if ID in self.externalForces:
            self.externalForces[ID] = None

    def acceleration(self):
        externalForcesSum = Vector(0,0)
        for i in self.externalForces:
            if self.externalForces[i] != None:
                externalForcesSum += self.externalForces[i]
        #print(externalForcesSum + self._physBase.g)
        #print(Vector(1/self.mass, 1/self.mass))
        #print(self.mass)
        return (externalForcesSum + self._physBase.g) * Vector(1/self.mass, 1/self.mass)
    def velocity(self):
        rv = self.v0 + self.acceleration() * self._physBase.dtv
        self.v0 = rv
        return rv
    def cycle(self):
         self.temporaryForce = []
         vel = self.velocity() * self._physBase.dtv
         print(vel)
         self.x += vel.x
         self.y += vel.y
    def implementTemporaryForce(self, forceVector):
        self.temporaryForce.append(forceVector)
    def applyGravitationalForce(self, other):
        ox = other.x
        oy = other.y
        other.implementTemporaryForce(gForce)
    def draw(self):
        pygame.draw.circle(self._physBase.screen, self.color, (int(self.x), int(self.y)), self.r)
if __name__ == '__MAIN__':
    pass
