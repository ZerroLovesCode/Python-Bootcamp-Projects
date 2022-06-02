from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.bgcolor('black')
scr.title('Pong')
scr.setup(width=800, height=600)
scr.listen()
scr.tracer(0)

p1 = Paddle()
p1.init_position((350, 0))

p2 = Paddle()
p2.init_position((-350, 0))

ball = Ball()

score = Scoreboard()

scr.onkey(p1.move_paddle_up, "Up")
scr.onkey(p1.move_paddle_down, "Down")
scr.onkey(p2.move_paddle_up, "w")
scr.onkey(p2.move_paddle_down, "s")

running = True
while running:
    # time.sleep(0.01)
    scr.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(p1) < 50 or ball.xcor() < -320 and ball.distance(p2) < 50:
        # ball.inc_speed()
        ball.bounce_x()

    #  When the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.lpoint()

    #  When the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.rpoint()


scr.exitonclick()
