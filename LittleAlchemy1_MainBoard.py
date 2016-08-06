#1. Let's Import Library!
import pygame,os, sys
from pygame.locals import *
import random
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
monstimer=100 #monster 타이머 : 얘가 0이 되면 리젠
monstimer1=0 #monstimer가 0이 되도록 조절한다.
monspos=[[640,100]]
healthvalue=190

#3. Load images
fire=pygame.image.load("resources/images/fire.jpg")
steam=pygame.image.load("resources/images/steam_gas.jpg")
wood=pygame.image.load("resources/images/Wood.jpg")
monsterimg1=pygame.image.load("resources/images/dude.png") #monsterimage를 추가한다.
monsterimg=monsterimg1
healthbar=pygame.image.load("resources/images/healthbar.png")
health=pygame.image.load("resources/images/health.png")

#4. keep looping through
while 1:
    monstimer-=1
    #5. clear the screen before drawing it again
    screen.fill(0)

    #6. place the elements
    screen.blit(fire, pos_fire)
    screen.blit(steam, pos_steam)
    screen.blit(wood, pos_wood)
    #6-1. Show me the monster (timer가 0이 될때마다 monster가 나오게 한다.)
    if monstimer==0:
        monster.append([640, random.randint(50,430)]) #[640, 50~430 랜덤이라는 좌표를 추가한다.
        monstimer=100-(monstimer1*2)
        if monstimer1>=35:
            monstimer1=35
        else:
            monstimer1+=5
    index=0
    for monster in monspos:
        if monster[0]<=0:
            monspos.pop(index)
        monspos[0][0]-=3
    index+=1
    for monster in monspos:
        screen.blit(monsterimg1, monster) ###### 아직 에러가 있음.. 몬스터가 특정 위치로 가면 사라짐;; 얘도 tuple로 인한 문제로 보임.

    #6-2. Show me the money (monster가 체력이 달아 없어질 때마다 돈이 더해진다.)
        font = pygame.font.Font(None, 24)
        money=0
        # if num_mons-=1:
        #money+=20
        show_text=font.render(str(money)+":"+str('$').zfill(2), True, (255,255,0))
        textRect= show_text.get_rect()
        textRect.topright=[1000,5]
        screen.blit(show_text,textRect)
    #6-3. Draw health bar
    screen.blit(healthbar,(monspos[0][0], monspos[0][1])) #피통은 구현함..
    #for health1 in range(0,150):
       # screen.blit(health, (health1*8.8)) #얘는 에러가 난다. 원래 blit의 두번째 칸에는 좌표나 tuple, 근데 tuple이 뭔지 모름


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


