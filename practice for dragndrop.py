import os, sys
import pygame

class Character:
    def __init__(self, rect):
        self.rect=pygame.Rect(rect)
        self.click=False
        self.image=pygame.Surface(self, rect.size).convert()
        self.image.fill((255,0,0)) # 색상을 지정합니다.
    def update(self, surface): #객체가 클릭되면 그림을 움직이게 한다?
        if self.click:
            self.rect.center=pygame.mouse.get_pos()
        surface.blit(self.image, self.rect)

def main(Screen,Player):
     game_event_loop(Player)
     Screen.fill(0) #배경화면 셋팅
     Player.update(Screen)
def game_event_loop(Player): #게임의 이벤트 루프를 만듭니다.
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
           if Player.rect.collidepoint(event.pos):
               Player.click=True
        elif event.type == pygame.MOUSEBUTTONUP:
            Player.click=False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

if __name__=="__main__":

    pygame.init()
    Screen = pygame.display.set_mode((1000,600)) #디스플레이 크기 설정
    MyClock=pygame.time.Clock() #타이머
    MyPlayer=Character((0,0,150,150)) #클래스-Character를 실행
    MyPlayer.rect.center=Screen.get_rect().center
    while 1:
        main(Screen, MyPlayer)
        pygame.digplay.update()
        MyClock.tick(60)
