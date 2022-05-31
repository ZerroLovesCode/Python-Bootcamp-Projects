from turtle import Screen
from snake import Snake
from food import Food
import time


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)

s = Snake()
f = Food()

scr.listen()
scr.onkey(s.up, "Up")
scr.onkey(s.down, "Down")
scr.onkey(s.left, "Left")
scr.onkey(s.right, "Right")

run = True
while run:
    scr.update()
    time.sleep(0.07)
    s.move()

    #  detect collisions
    if s.snake_body[0].distance(f) < 15:
        f.refresh()

scr.exitonclick()
