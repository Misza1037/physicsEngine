#main.py
import physics
import pygame
from vectors import Vector
from time import sleep
screenSize = [700, 700]
pygame.init()
dtv = 0.2
screen = pygame.display.set_mode(screenSize)
PB = physics.PhysBase(screen, screenSize, Vector(dtv, dtv))
PB.addObject('obj1', physics.PhysObject(base=PB, mass=1, x=350, y=350, color=(0,0,124), r=35))
#PB.objects['obj1'].applyForce(Vector(0, 1), 'push1')
#PB.removeObject('obj1')
activeBackgroundColor = (255, 255, 255)
mainLoopRunning = True
while mainLoopRunning:
    #pyGame event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoopRunning = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print(Vector((PB.objects['obj1'].x - event.pos[0])*0.1, (PB.objects['obj1'].y - event.pos[0])*0.1))
            #PB.objects['obj1'].implementTemporaryForce(Vector((PB.objects['obj1'].x - event.pos[0])*-0.1, (PB.objects['obj1'].y - event.pos[1])*-0.1))
    #print(pygame.mouse.get_pressed())
    if pygame.mouse.get_pressed()[0] == 1:
        pos = pygame.mouse.get_pos()
        PB.objects['obj1'].implementTemporaryForce(Vector((PB.objects['obj1'].x - pos[0])*-.015, (PB.objects['obj1'].y - pos[1])*-.015))
    screen.fill(activeBackgroundColor)
    for object in PB.objects:
        PB.objects[object].isCollidingWithScreenBorder()
        PB.objects[object].cycle()
        PB.objects[object].draw()
        #if PB.objects[object].v0 != Vector(0,0): print(PB.objects[object].v0)
    pygame.display.flip()
    sleep(.005)
pygame.quit()
