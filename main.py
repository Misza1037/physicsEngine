import physics
from vectors import Vector
PB = physics.PhysBase()
PB.addObject('obj1', physics.PhysObject(PB, 0))
PB.objects['obj1'].mass += 1
PB.objects['obj1'].applyForce(Vector(0, 1), 'push1')
print(PB.objects['obj1'])
print(PB.objects['obj1'].externalForces)
print(PB.objects['obj1'].mass)
print(PB.objects['obj1'].acceleration())
PB.removeObject('obj1')
