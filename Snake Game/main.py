from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)

s = Snake()
f = Food()
sc = Scoreboard()


scr.listen()
scr.onkey(s.up, "Up")
scr.onkey(s.down, "Down")
scr.onkey(s.left, "Left")
scr.onkey(s.right, "Right")

run = True
while run:
    scr.update()
    time.sleep(0.1)
    s.move()

    #  detect collision with food
    if s.snake_body[0].distance(f) < 15:
        f.refresh()
        sc.inc_score()
        s.extend()

    if s.snake_body[0].xcor() > 280 or s.snake_body[0].xcor() < -280 or s.snake_body[0].ycor() > 280 or s.snake_body[0].ycor() < -280:
        sc.game_over()
        run = False

    for seg in s.snake_body:
        if seg != s.snake_body[0] and s.snake_body[0].distance(seg) <= 10:
            run = False
            sc.game_over()

scr.exitonclick()
