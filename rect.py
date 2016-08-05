import os,sys
import pygame  #lazy but responsible (avoid namespace flooding)

class Character:
    def __init__(self,rect):
        self.rect = pygame.Rect(rect)
        self.click = False
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill((255,0,0))
    def update(self,surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

def main(Screen,Player):
    game_event_loop(Player)
    Screen.fill(0)
    Player.update(Screen)
def game_event_loop(Player):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

if __name__ == "__main__": #만일 이 파일이 인터프리터에 의해서 실행되는 경우라면

    pygame.init()
    Screen = pygame.display.set_mode((1000,600)) #디스플레이 크기 설정
    MyClock = pygame.time.Clock() #타이머
    MyPlayer = Character((5,5,100,100)) #클래스-Character를 실행
    MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen,MyPlayer) #스크린을 업데이트한다.
        pygame.display.update()
        MyClock.tick(60)

