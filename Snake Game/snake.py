from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.snake_body = []
        x = 0
        for i in range(3):
            t1 = Turtle(shape='square')
            t1.penup()
            t1.color('white')
            t1.goto(x, 0)
            self.snake_body.append(t1)
            x -= 20

    def move(self):
        for x in range(len(self.snake_body) -1, 0, -1):
            nx = self.snake_body[x-1].xcor()
            ny = self.snake_body[x-1].ycor()
            self.snake_body[x].goto(nx, ny)

        self.snake_body[0].forward(20)
        # self.snake_body[0].left(90)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90 )