import physics
PB = physics.PhysBase()
PB.addObject('obj1', physics.PhysObject(PB, 10))
PB.objects['obj1'].mass += 10
PB.removeObject('obj1')
