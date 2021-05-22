import physics
import pygame
from vectors import Vector
from time import sleep
screenSize = [700, 700]
pygame.init()
screen = pygame.display.set_mode(screenSize)
PB = physics.PhysBase(screen, Vector(0.2, 0.2))
PB.addObject('obj1', physics.PhysObject(_physBase=PB, mass=1, x=350, y=350, color=(0,0,124), r=35))
#PB.objects['obj1'].applyForce(Vector(0, 1), 'push1')
#PB.removeObject('obj1')
activeBackgroundColor = (255, 255, 255)
mainLoopRunning = True
while mainLoopRunning:
    #pyGame event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoopRunning = False
    screen.fill(activeBackgroundColor)
    for object in PB.objects:
        PB.objects[object].cycle()
        PB.objects[object].draw()
    pygame.display.flip()
    sleep(.01)
pygame.quit()
