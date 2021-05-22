#physics.py



class PhysBase:

    def __init__(self, g=10):
        if type(g) != float and type(g) != int:
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



if __name__ == '__MAIN__':
    pass
