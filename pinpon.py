import pygame
pygame.init()
from menu import Game_over


FPS = 60

BLACK = (0,0,0)
WHITE = (250,250,250)
WIDTH,HEIGTH = 665,450

window = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Ping pong Game!")
clock = pygame.time.Clock()

score_one_font = pygame.font.SysFont("impact",40)
score_two_font = pygame.font.SysFont("impact",40)

player1 = pygame.Rect(20,100,15,100)
player2 = pygame.Rect(630,200,15,100)
ball_img = pygame.Rect(345,225,15,15)

score_one_font = pygame.font.SysFont("impact",40)
score_two_font = pygame.font.SysFont("impact",40)

win_font = pygame.font.SysFont("impact",60)
win_text = win_font.render('WIN',1,WHITE)

play_font = pygame.font.SysFont('impact',30)
menu_font = pygame.font.SysFont('impact',30)

class Ball():

    def __init__(self,ball,player1,player2,speed=5,score1=0,score2=0,speed1=5,speed2=3,flag=5,degree1=10,degree2=10,player_left=[],player_right=[],ball_list=[[0,0],[0,0]]):

        self.flag = flag
        self.speed = speed
        self.ball = ball

        self.player1 = player1
        self.player2 = player2 

        self.score1 = score1 
        self.score2 = score2

        self.speed1 = speed1 
        self.speed2 = speed2

        self.degree1 = degree1
        self.degree2 = degree2 

        self.player_left = player_left
        self.player_right = player_right
        self.ball_list = ball_list

       

    def ball_list_maker(self,):
        self.ball_list.insert(0,self.ball.x)
        if len(self.ball_list) > 2:
            self.ball_list.remove(self.ball_list[len(self.ball_list)-1])

    def list_maker(self,):
        for i in range(20,46):
            self.player_left.append(i)
        for i in range(630,646):
            self.player_right.append(i)

    def bounce(self,):
        if self.ball.y > 450:    
            self.flag = 3
        if self.ball.y < 0:
            self.flag = 2

    def burn(self,):
        if self.ball.x < 0:
            self.ball.x,self.ball.y= 345,225
            self.flag = 5
            self.score2 += 1
        if self.ball.x > 665:
            self.ball.x,self.ball.y = 345,225
            self.flag = 6
            self.score1 += 1

    def ball_start(self,):
        if self.flag == 5:
            self.speed = 4
            self.ball.x  += self.speed

        if self.flag == 6:
            self.speed = 4
            self.ball.x -= self.speed

    def move(self,):

        self.ball_list_maker()
        self.burn()
        self.ball_start()
        self.bounce()

        #player1,player2
        if self.ball.x in self.player_left and self.player1.y < self.ball.y < player1.y + 100: 
            self.flag = 0
            self.degree1 = self.ball.y - self.player1.y
            self.speed = 10
        if self.ball.x in self.player_right and self.player2.y < self.ball.y < player2.y + 100: 
            self.flag = 1
            self.degree2 = self.ball.y - self.player2.y
            self.speed = 10

        #move
        if self.flag == 0:
            if self.degree1 > 50:
                self.speed1 = (self.degree1-50) / 5
                self.ball.x += self.speed 
                self.ball.y += self.speed1
            if self.degree1 < 50: 
                self.speed1 = self.degree1 / 5
                self.ball.x += self.speed
                self.ball.y -= self.speed1
        if self.flag == 1:
            if self.degree2 > 50:
                self.speed2 = (self.degree2-50) / 5 
                self.ball.x -= self.speed
                self.ball.y += self.speed2
            if self.degree2 < 50:
                self.speed2 = self.degree2 / 5
                self.ball.x -= self.speed
                self.ball.y -= self.speed2
        if self.flag == 2:
            if self.ball_list[0] < self.ball_list[1]:
                self.ball.x -= self.speed
                self.ball.y += self.speed2
            if self.ball_list[0] > self.ball_list[1]:
                self.ball.x += self.speed 
                self.ball.y += self.speed1
        if self.flag == 3:
            if self.ball_list[0] < self.ball_list[1]:
                self.ball.x -= self.speed
                self.ball.y -= self.speed2
            if self.ball_list[0] > self.ball_list[1]:
                self.ball.x += self.speed
                self.ball.y -= self.speed1

class Player():

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2

    def plate_move(self,keys_pressed):

        if keys_pressed[pygame.K_w] and self.player1.y > 0:
            self.player1.y -= 10
        if keys_pressed[pygame.K_s] and self.player1.y < 350:
            self.player1.y += 10

        if keys_pressed[pygame.K_UP] and self.player2.y > 0:
            self.player2.y -= 10
        if keys_pressed[pygame.K_DOWN] and self.player2.y < 350:
            self.player2.y += 10

def border():
    a = 0
    while a < 450:
        pygame.draw.rect(window,WHITE,(325,15+a,15,20))
        a += 50

def score(circle):
    score_one_text = score_one_font.render("{}".format(circle.score1),1,WHITE)
    score_two_text = score_two_font.render("{}".format(circle.score2),1,WHITE)
    window.blit(score_one_text,(145,0))
    window.blit(score_two_text,(470,0))

def draw_window(circle,player,game_over,position):
    window.fill(BLACK)
    score(circle)
    game_over.game_menu(circle,position) 
    pygame.draw.rect(window,WHITE,player.player1)
    pygame.draw.rect(window,WHITE,player.player2)
    pygame.draw.circle(window,WHITE,(circle.ball.x,circle.ball.y),6)
    border()
    pygame.display.update()

def main():
    run = True
    circle = Ball(ball_img,player1,player2)
    player = Player(player1,player2)
    game_over = Game_over()
    circle.list_maker()
 
    while run:
      
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        position = [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if game_over.flag3 == 0:
                    circle.score1 = 0
                    circle.score2 = 0
                
        if circle.score1 != 10 and circle.score2 != 10:
            circle.move()
            player.plate_move(keys_pressed)
        
        draw_window(circle,player,game_over,position)
        
     
          
    pygame.quit()



    
    