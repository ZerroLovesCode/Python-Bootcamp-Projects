from turtle import Turtle, Screen
import random

tim = Turtle()

#  Drawing a square:
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

#  Drawing a dashed line:
# for _ in range(0, 10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

#  Drawing shapes on top of each other:
myScr = Screen()
myScr.colormode(255)
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# tim.forward(100)

# for i in range(3, 11):
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(360/i)
#     tim.pencolor(tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]))

#  Random walk:
# tim.pensize(10)
# t = 0
# while t < 200:
#     tim.pencolor(tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]))
#     tim.setheading(random.choice([0, 90, 180, 270]))
#     tim.forward(30)
#     t += 1
#

#  Spirograph:
tim.speed(0)
# num = 0
for i in range(361):
    tim.color(tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]))
    tim.circle(100)
    tim.right(1)
    # num += 1

myScr.exitonclick()