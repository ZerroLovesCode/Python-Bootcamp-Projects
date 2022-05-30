from turtle import Turtle, Screen
import time


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor('black')
scr.title('Snake Game')
scr.listen()
scr.tracer(0)

x = 0
snake_body = []

#  initial snake body of size 3
for i in range(3):
    t1 = Turtle(shape='square')
    t1.penup()
    t1.color('white')
    t1.goto(x, 0)
    snake_body.append(t1)
    x -= 20
# scr.update()
run = True
while run:
    scr.update()
    time.sleep(0.1)

    for x in range(len(snake_body)-1, 0, -1):
        newX = snake_body[x-1].xcor()
        newY = snake_body[x-1].ycor()
        snake_body[x].goto(newX, newY)
    snake_body[0].forward(20)
    snake_body[0].left(90)

scr.exitonclick()