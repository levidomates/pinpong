import pygame
import random 
pygame.init()
FPS= 60
BLACK = (0,0,0)
WHITE = (250,250,250)
WIDTH,HEIGHT = 620,400

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping pong Game!")

score1_font = pygame.font.SysFont('impact',40)
score2_font = pygame.font.SysFont('impact',40)
winner_font = pygame.font.SysFont('impact',60)
click_font = pygame.font.SysFont('impact',40)

flag1 = True
flag2 = False
flag3 = False
flag4 = False

def draw_window(player1,player2,border,ball,score1,score2,flag_screen,winner):

    window.fill(BLACK)
    if flag_screen == False:
        score1_text = score1_font.render("{}".format(score1),1,WHITE)
        score2_text = score2_font.render("{}".format(score2),1,WHITE)
        window.blit(score1_text,(150,0))
        window.blit(score2_text,(450,0))
        pygame.draw.rect(window,WHITE,border)
        pygame.draw.rect(window,WHITE,player1)
        pygame.draw.rect(window,WHITE,player2)
        pygame.draw.circle(window,WHITE,(ball.x,ball.y),6)
    if flag_screen == True:
        winner_text = winner_font.render("WINNER {}".format(winner),1,WHITE)
        window.blit(winner_text,(100,150))
        click_text = click_font.render("play again >>> space",1,WHITE)
        window.blit(click_text,(250,250))
    pygame.display.update()

def controll(player1,player2,key_pressed):

    if key_pressed[pygame.K_w] and player1.y > 0:
        player1.y -= 10
    if key_pressed[pygame.K_s] and player1.y < 340:
        player1.y += 10
    if key_pressed[pygame.K_UP] and player2.y > 0:
        player2.y -= 10
    if key_pressed[pygame.K_DOWN] and player2.y < 340:
        player2.y += 10

def move(speed,ball,ball_list,player1_list,player2_list):

    global flag1 
    global flag2 
    global flag3
    global flag4
    flag5 = False
    flag6 = False

    for i in player1_list:
        for a in i:
            if a == ball.y:
                flag5 = True
    for i in player2_list:
        for a in i:
            if a == ball.y:
                flag6 = True

    if ball.x == 20 and flag5 == True:
        flag1 = True
        flag2 = False
        flag3 = False
        flag4 = False

    if ball.y == 0:
        flag1 = False
        flag2 = True
        flag3 = False
        flag4 = False

    if ball.x == 600 and flag6 == True:
        flag1 = False
        flag2 = False
        flag3 = True
        flag4 = False

    if ball.y == 400:
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = True

    if flag1 == True:
        if ball_list[0][1] > ball_list[1][1]:
            ball.x += speed
            ball.y += speed
        else: 
            ball.x += speed
            ball.y -= speed
    if flag2 == True:
        if ball_list[0][0] < ball_list[1][0]:
            ball.x -= speed
            ball.y += speed
        else:
            ball.x += speed 
            ball.y += speed
    if flag3 == True:
        if ball_list[0][1] < ball_list[1][1]:
            ball.x -= speed
            ball.y -= speed
        else:
            ball.x -= speed
            ball.y += speed
    if flag4 == True:
        if ball_list[0][0] > ball_list[1][0]:
            ball.x += speed
            ball.y -= speed
        else:
            ball.x -= speed
            ball.y -= speed

def ball_cordinate(ball,ball_list):
    free_list = []
    free_list.append(ball.x)
    free_list.append(ball.y)
    ball_list.insert(0,free_list)
def player1_list_maker(player1,player1_list):
    free_list = []
    for i in range(0,61):
        free_list.append(player1.y+i)
    player1_list.insert(0,free_list)
def player2_list_maker(player2,player2_list):
    free_list = []
    for i in range(0,61):
        free_list.append(player2.y+i)
    
    player2_list.insert(0,free_list)
def list_maker(list):
    a = 160
    b = 100
    while True:
        free_list = []
        free_list.append(a)
        free_list.append(b)
        list.append(free_list)
        b += 20
        if b == 260:
            a += 20
            b = 100
        if a == 260:
            break

def main():
    flag_screen = False
    ball_list = [[0,0],[0,0]]
    player1_list = []
    player2_list = []
    list = []
    score1 = 0
    score2 = 0
    speed = 5
    clock = pygame.time.Clock()
    winner = ""
    run = True
    player1 = pygame.Rect(0,100,20,60)
    player2 = pygame.Rect(600,100,20,60)
    border = pygame.Rect(300,0,20,400)
    ball = pygame.Rect(250,250,20,20)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if len(ball_list) > 2:
            ball_list.remove(ball_list[len(ball_list)-1])
        if len(player1_list) > 3:
            player1_list.remove(player1_list[len(player1_list)-1])
        if len(player2_list) > 3:
            player2_list.remove(player2_list[len(player2_list)-1])
        if ball.x < 0:
            score2 += 1
            tomato = random.choice(list)
            pygame.time.wait(1000)
            ball.x = tomato[0]
            ball.y = tomato[1]
        if ball.x > 620:
            tomato = random.choice(list)
            pygame.time.wait(1000)
            ball.x = tomato[0]
            ball.y = tomato[1]
            score1 += 1
        if score1 == 10:
            winner = "player-1"
        if score2 == 10:
            winner = "player-2"
        if score1 == 10 or score2 == 10 and flag_screen == False:
            flag_screen = True
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            score1 = 0
            score2 = 0
            flag_screen = False

        if flag_screen == False:
            player2_list_maker(player2,player2_list)
            player1_list_maker(player1,player1_list)
            list_maker(list)
            ball_cordinate(ball,ball_list)
            controll(player1,player2,key_pressed)
            move(speed,ball,ball_list,player1_list,player2_list)
        draw_window(player1,player2,border,ball,score1,score2,flag_screen,winner)

    pygame.quit()


if __name__ == "__main__":
    main()