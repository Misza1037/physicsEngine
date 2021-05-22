class Vector:
    def __init__(self, x, y):
        if type(x) != int and type(x) != float:
            raise TypeError('')
        if type(y) != int and type(y) != float:
            raise TypeError('')
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y +other.y)
    def __neg__(self):
        return Vector(-self.x, -self.y)
    def __sub__(self, other):
        return self + (-other)
    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'
    def __repr__(self):
        return f'v[{self.x},{self.y}]'
    def __mul__(self, other):
        return Vector(self.x*other.x, self.y*other.y)
