import pgzrun
from random import *

HEIGHT= 800
WIDTH = 1000



player1 = Actor('pong_paddle')
player2 = Actor('pong_paddle')
ball = Actor('pong_ball')

player1.x = 20
player1.y = HEIGHT /2

player2.x = 980
player2.y = HEIGHT / 2

ball.x = WIDTH / 2
ball.y = HEIGHT / 2

if randint(1,2) == 1:
    move = "left"
else:
    move = "right"

score1 = 0
score2 = 0
angle = randint(3,6)
speed = 8
start = False
win = False

def update():
    global angle
    global move
    global speed
    global score1
    global score2
    global win
    global start
    if start:
        if win == False:
            if player2.y > 50:
                if keyboard.up:
                    player2.y -= 20
            if player2.y < 750:
                if keyboard.down:
                    player2.y += 20
            if player1.y > 50:
                if keyboard.w:
                    player1.y -= 20
            if player1.y < 750:
                if keyboard.s:
                    player1.y += 20
            if player2.colliderect(ball):
                move = "left"
            elif player1.colliderect(ball):
                move = "right"
            if move == "left":
                ball.x -= speed
            else:
                ball.x += speed
            if ball.y >= 775 or ball.y <= 25:
                angle = -(angle)
            if ball.x > WIDTH or ball.x < 0:
                if ball.x > WIDTH:
                    score1 += 1
                else:
                    score2 += 1
                speed += 0.5
                ball.x = WIDTH / 2
                ball.y = HEIGHT / 2
                angle = randint(3,6)
                if randint(1,2) == 1:
                    move = "left"
                else:
                    move = "right"
            ball.y += angle

def on_key_down(key):
    global start
    start = True

def draw():
    global win
    screen.clear()
    player1.draw()
    player2.draw()
    screen.draw.text(str(score1),(75,50), color="white",fontsize = 45)
    screen.draw.text(str(score2),(925,50), color="white",fontsize = 45)
    if score1 == 20:
        screen.draw.text("player1 wins",(WIDTH/2-230,HEIGHT/2), color="white",fontsize = 100)
        win = True
    elif score2 == 20:
        screen.draw.text("player2 wins",(WIDTH/2-230,HEIGHT/2), color="white",fontsize = 100)
        win = True
    else:
        ball.draw()

pgzrun.go()