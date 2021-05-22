#physics.py
from vectors import Vector



class PhysBase:

    def __init__(self, g = Vector(-1, 0)):
        if type(g) != Vector:
            raise TypeError('PhysBase.__init__(): g | invalid type')
        self.g = g
        self.objects = {}
        self.nextUsedID = 0


    def addObject(self, ID, object):
        if ID in self.objects:
            raise ValueError('')#! fill error message
        self.objects[ID] = object


    def removeObject(self, givenID):
        self.objects.pop(givenID)



class PhysObject:

    def __init__(self, _physBase, mass = 1):
        if type(_physBase) != PhysBase:
            raise TypeError('PhysObject.__init__(): _physBase | invalid type')
        if type(mass) != float and type(mass) != int:
            raise TypeError('PhysObject.__init__(): mass | invalid type')
        self.mass = mass
        self._physBase = _physBase
        self.externalForces = {}


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
        print(externalForcesSum + self._physBase.g)
        print(Vector(1/self.mass, 1/self.mass))
        print(self.mass)
        return (externalForcesSum + self._physBase.g) * Vector(1/self.mass, 1/self.mass)
if __name__ == '__MAIN__':
    pass
