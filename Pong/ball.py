from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.xmov = 0.03
        self.ymov = 0.03

    def move(self):
        nx = self.xcor() + self.xmov
        ny = self.ycor() + self.ymov
        self.goto(nx, ny)

    def bounce_y(self):
        self.ymov *= -1

    def bounce_x(self):
        self.xmov *= 1.4
        self.ymov *= 1.4
        self.xmov *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.xmov = 0.03
        self.ymov = 0.03
        self.bounce_x()

