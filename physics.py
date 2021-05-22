#physics.py
class physBase:
    def __init__(self, g=10):
        if type(g) != float or type(g) != int:
            raise TypeError('physBase.__init__(): >g< variable invalid type')
        self.g = g
class physObject:
    def __init__(self, mass):
        self.mass = mass
