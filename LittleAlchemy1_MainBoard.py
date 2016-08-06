#1. Let's Import Library!
import pygame,os, sys
from pygame.locals import *
#1-1. Make it easier


#2. Initialize game!
pygame.init()
width, height=1280,960
screen=pygame.display.set_mode((width, height))
pos_fire=[50,700]
pos_steam=[250,700]
pos_wood=[400,700]
pos_lib=[pos_fire,pos_steam,pos_wood]
keys=[False,False,False,False]

#3. Load images
fire=pygame.image.load("resources/images/fire.jpg")
steam=pygame.image.load("resources/images/steam_gas.jpg")
wood=pygame.image.load("resources/images/Wood.jpg")

#4. keep looping through
while 1:
    #5. clear the screen before drawing it again
    screen.fill(0)

    #6. place the elements
    screen.blit(fire, pos_fire)
    screen.blit(steam, pos_steam)
    screen.blit(wood, pos_wood)
    #6-1. Method for moving elements


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


    #9 - Move player
    #9.1- Select Material
    if event.type==pygame.KEYDOWN:
        if event.key==K_f:
            material=pos_lib[0]
        if event.key==K_s:
            material=pos_lib[1]
        if event.key==K_w:
            material=pos_lib[2]


    if event.type==pygame.KEYDOWN:
        if event.key==K_UP:
           material[1]-=5
        elif event.key==K_DOWN:
            material[1]+=5
        if event.key==K_RIGHT:
          material[0]+=5
        elif event.key==K_LEFT:
            material[0]-=5


