from pygame import *
from main_classes import GameSprite, Player

'''Varables'''
background_color = (200,255,255)
window = display.set_mode((600,500))
clock = time.Clock()
ball = GameSprite(picture_image='tennis_ball.png',picture_x=50,picture_y=50,picture_width=60,picture_height=60,picture_speed=1)
racket1 = Player(picture_image='racket.png',picture_x=5,picture_y=240,picture_width=30,picture_height=150,picture_speed=2)
racket2 = Player(picture_image='racket.png',picture_x=560,picture_y=240,picture_width=30,picture_height=150,picture_speed=2)
speed_x = 2
speed_y = 2
font.init()
font1 = font.Font(None,35)
player1_lose = font1.render('Player one loses!',True, (180,0,0))
player2_lose = font1.render('Player two loses!',True, (180,0,0))
game = True
lose_win = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if lose_win:
        window.fill(background_color)
        ball.reset(window)

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y >= 440 or ball.rect.y <= 0 :
            speed_y *= -1

        if sprite.collide_rect(racket2,ball) or sprite.collide_rect(racket1,ball): 
            speed_x *= -1

        if ball.rect.x <= 0: 
            window.blit(player1_lose, (200, 200))
            finsh = False

        if ball.rect.x >= 600: 
            window.blit(player2_lose, (200, 200))
            finsh = False


        racket1.reset(window)
        racket1.update_rocket1()

        racket2.reset(window)
        racket2.update_rocket2()


    display.update()
    clock.tick(60)    
