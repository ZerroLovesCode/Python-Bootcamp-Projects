from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def init_position(self, coords):
        self.goto(coords)

    def move_paddle_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


