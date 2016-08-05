#1. Let's Import Library!
import pygame,os, sys
from pygame.locals import *
#1-1. Make it easier
class Character:
    def __init__(self, rect):
        self.rect=pygame.Rect(rect)
        self.click.False
        self.image=pygame.Surface(self, rect.size).convert()
        self.image.fill((255,0,0))
    def update(self,surface):
        if self.click:
                self.rect.center=pygame.mouse.get_pos()
        surface.blit(self.image, self.rect)
def main(Screen, Player)
   # game_event

#2. Initialize game!
pygame.init()
width, height=1280,960
screen=pygame.display.set_mode((width, height))

#3. Load images
fire=pygame.image.load("resources/images/fire.jpg")
steam=pygame.image.load("resources/images/steam_gas.jpg")
wood=pygame.image.load("resources/images/Wood.jpg")

#4. keep looping through
while 1:
    #5. clear the screen before drawing it again
    screen.fill(0)

    #6. place the elements
    screen.blit(fire, (50, 700))
    screen.blit(steam, (250, 700))
    screen.blit(wood, (450, 700))
    #6-1. Method for moving elements
    position=pygame.mouse.get_pos()
    pos_fire=fire.get_rect()
    pos_steam=steam.get_rect()
    pos_wood=wood.get_rect()

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
            if fire.rect.collidepoint(event.pos) :
                pos_fire = position
            elif fire.rect.collidepoint(event.pos) :
                pos_steam == position
            elif wood.rect.collidepoint(event.pos) :
                pos_wood == position
    screen.blit(fire, pos_fire)
    screen.blit(steam,pos_steam)
    screen.blit(wood, pos_wood)

