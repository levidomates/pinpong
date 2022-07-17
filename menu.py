import pygame 

FPS = 60

BLACK = (0,0,0)
WHITE = (250,250,250)
WIDTH,HEIGTH = 665,450

window = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()

pygame.display.set_caption('pinpon game')
win_font = pygame.font.SysFont("impact",60)
win_text = win_font.render('WIN',1,WHITE)

play_font = pygame.font.SysFont('impact',50)

menu_font = pygame.font.SysFont('impact',30)
player_font = pygame.font.SysFont('impact',40)
speed_font = pygame.font.SysFont('impact',35)


class Game_over():
    def __init__(self,flag3=-1):
        self.flag3 = flag3 
    def game_menu(self,circle,position):

        if circle.score1 == 10:

            border1 = 5
            border2 = 5
            flag1,flag2 = True,True
            window.blit(win_text,(115,70)) 
            
            if 245 > position[0] > 90 and 250 > position[1] > 200:
                play_text = menu_font.render('Play again',1,BLACK)
                border1 = 0
                flag1 = False
                self.flag3 = 0
            if 245 > position[0] > 90 and 320 > position[1] > 270:
                menu_text = menu_font.render('Main menu',1,BLACK)
                border2 = 0
                flag2 = False
                self.flag3 = 1
                
            if flag1 == True:
                play_text = menu_font.render('Play again',1,WHITE)
                border1 = 5
            if flag2 == True:
                menu_text = menu_font.render('Main menu',1,WHITE)
                border2 = 5

            pygame.draw.rect(window,WHITE,(90,200,155,50),border1)
            pygame.draw.rect(window,WHITE,(90,270,155,50),border2)
            window.blit(menu_text,(100,275))
            window.blit(play_text,(105,205))

        if circle.score2 == 10:
            border1 = 5
            border2 = 5
            flag1,flag2 = True,True
            
            window.blit(win_text,(430,70)) 
            
            if 560 > position[0] > 405 and 250 > position[1] > 200:
                play_text = menu_font.render('Play again',1,BLACK)
                border1 = 0
                flag1 = False
                self.flag3 = 0
            if 560 > position[0] > 405 and 320 > position[1] > 270:
                menu_text = menu_font.render('Main menu',1,BLACK)
                border2 = 0
                flag2 = False
                self.flag3 = 1
    
            if flag1 == True:
                play_text = menu_font.render('Play again',1,WHITE)
                border1 = 5
            if flag2 == True:
                menu_text = menu_font.render('Main menu',1,WHITE)
                border2 = 5

            pygame.draw.rect(window,WHITE,(405,200,155,50),border1)
            pygame.draw.rect(window,WHITE,(405,270,155,50),border2)
            window.blit(menu_text,(415,275))
            window.blit(play_text,(420,205))
