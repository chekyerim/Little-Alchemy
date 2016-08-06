#1. Let's Import Library!
import pygame,os, sys
from pygame.locals import *
#1-1. Make it easier

#2. Initialize game!
pygame.init()
width, height=1280,960
fire_pos=[50,700]
screen=pygame.display.set_mode((width, height))

#3. Load images
fire=pygame.image.load("resources/images/fire.jpg")

#4. keep looping through
while 1:
    #5. clear the screen before drawing it again
    screen.fill(0)

    #6. place the elements
    screen.blit(fire, fire_pos)
    #6-1. Method for moving elements
    position=pygame.mouse.get_pos()
    pos_fire=fire.get_rect()


    #7. update the screen
    pygame.display.flip()

    #8. loop through the events
    for event in pygame.event.get():
        #check if the event is X button
        if event.type==pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        #Move elements
        if event.type==pygame.MOUSEBUTTONDOWN:
            if fire.Rect.collidepoint(event.pos) :
               pygame.Rect(fire).move(fire, position)
               fire_pos = (position[0], position[1])
    screen.blit(fire, pos_fire)
