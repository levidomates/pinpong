import pygame 
pygame.init()
import time
FPS = 60

BLACK = (0,0,0)
WHITE = (250,250,250)
WIDTH,HEIGTH = 665,450

window = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Ping pong Game!")
score_one_font = pygame.font.SysFont("impact",40)
score_two_font = pygame.font.SysFont("impact",40)

flag = 5
degree_one = 1
degree_two = 2
speed_one = 5
speed_two = 5
flag_burn = True

def move(player_one,player_two,keys_pressed):

    if keys_pressed[pygame.K_w] and player_one.y > 0:
        player_one.y -= 10
    if keys_pressed[pygame.K_s] and player_one.y < 350:
        player_one.y += 10

    if keys_pressed[pygame.K_UP] and player_two.y > 0:
        player_two.y -= 10
    if keys_pressed[pygame.K_DOWN] and player_two.y < 350:
        player_two.y += 10

def ball_move(ball,speed,player_one,player_two,list_x,list_last_x,ball_list):

    global flag
    global degree_one
    global degree_two
    global speed_one
    global speed_two
    global flag_burn

    if ball.x in list_x and player_one.y < ball.y < player_one.y + 100:
        flag = 1
        degree_one = ball.y - player_one.y
        flag_burn = False
    if ball.x in list_last_x and player_two.y < ball.y < player_two.y + 100:
        degree_two = ball.y - player_two.y 
        flag = 2
        flag_burn = False
    if ball.y < 10:
        flag = 3
    if ball.y > 450:
        flag = 4

    if flag == 1:
        if degree_one > 50:
            speed_one = (degree_one-50) / 5
            ball.x += speed 
            ball.y += speed_one
        if degree_one < 50: 
            speed_one = degree_one / 5
            ball.x += speed
            ball.y -= speed_one
    if flag == 2:
        if degree_two > 50:
            speed_two = (degree_two-50) / 5 
            ball.x -= speed
            ball.y += speed_two
        if degree_two < 50:
            speed_two = degree_two / 5
            ball.x -= speed
            ball.y -= speed_two
    if flag == 3:
        if ball_list[0] < ball_list[1]:
            ball.x -= speed
            ball.y += speed_two
        if ball_list[0] > ball_list[1]:
            ball.x += speed 
            ball.y += speed_one
    if flag == 4:
        if ball_list[0] < ball_list[1]:
            ball.x -= speed
            ball.y -= speed_two
        if ball_list[0] > ball_list[1]:
            ball.x += speed
            ball.y -= speed_one
    if flag == 5 :
        ball.x += speed
    if flag == 6:
        ball.x -= speed

def ball_burn(ball):

    global flag_burn
    global flag
    if ball.x < 0:
        flag = 5
        flag_burn = True
        ball.x = 350
        ball.y = 200
    if ball.x > 665:
        flag = 6
        flag_burn = True
        ball.x = 350
        ball.y = 200

def border():
    a = 0
    while a < 450:
        pygame.draw.rect(window,WHITE,(325,15+a,15,20))
        a += 50

def draw_window(player_one,player_two,ball,score_one,score_two):

    window.fill(BLACK)

    border()

    score_one_text = score_one_font.render("{}".format(score_one),1,WHITE)
    score_two_text = score_two_font.render("{}".format(score_two),1,WHITE)

    window.blit(score_one_text,(175,0))
    window.blit(score_two_text,(475,0))
    pygame.draw.rect(window,WHITE,player_one)
    pygame.draw.rect(window,WHITE,player_two)
    pygame.draw.circle(window,WHITE,(ball.x,ball.y),6)
    pygame.display.update()

def list_maker(list_x,list_last_x):
    for i in range(20,46):
        list_x.append(i)
    for i in range(630,646):
        list_last_x.append(i)

def main():
    list_x = []
    list_last_x = []
    ball_list = [1,2,3]
    score_one = 0
    score_two = 0
    list_maker(list_x,list_last_x)
    speed = 10
    clock = pygame.time.Clock()
    player_one = pygame.Rect(20,100,15,100)
    player_two = pygame.Rect(630,200,15,100)
    ball = pygame.Rect(350,200,15,15)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ball_list.insert(0,ball.x)
        if len(ball_list) > 2:
            ball_list.remove(ball_list[len(ball_list)-1])
        if flag_burn == True:
            speed = 4
        if flag_burn == False:
            speed = 10
        if ball.x < 10:
            if speed == 10:
                score_two += 1
            else: 
                score_two += 0.5
                score_two = int(score_two)
        if ball.x > 655:
            if speed == 10:
                score_one += 1
            else:
                score_one += 0.5
                score_one = int(score_one)
        keys_pressed = pygame.key.get_pressed()
        
        move(player_one,player_two,keys_pressed)
        ball_move(ball,speed,player_one,player_two,list_x,list_last_x,ball_list)
        ball_burn(ball)

        draw_window(player_one,player_two,ball,score_one,score_two)

    pygame.quit()

if __name__ == "__main__":
    main()