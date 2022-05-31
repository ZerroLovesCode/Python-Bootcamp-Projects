from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('yellow')
        self.score = 0
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 20, 'bold'))

    def inc_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=('Arial', 20, 'bold'))
