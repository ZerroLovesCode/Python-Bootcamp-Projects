from turtle import Turtle, Screen
import random
#  The colorgram code is just used to extract the color from the painting.
# import colorgram
# colors = colorgram.extract("hirstPainting.jpg", 15)
#
# ctuples = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     ctuples.append((r, b, b))

ctuples = [(198, 119, 119), (125, 23, 23), (187, 50, 50), (170, 56, 56), (5, 83, 83), (201, 205, 205), (109, 85, 85),
           (39, 34, 34), (84, 61, 61), (20, 175, 175), (111, 176, 176), (75, 48, 48)]

tim = Turtle()
myScr = Screen()
myScr.colormode(255)
myScr.bgcolor((100, 150, 150))

total_dots = 100
tim.hideturtle()
tim.penup()
tim.setx(-250)
tim.sety(-200)
tim.speed(0)
for countDots in range(1, total_dots+1):
    # tim.penup()
    tim.dot(20, random.choice(ctuples))
    tim.forward(50)
    if countDots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.right(180)

myScr.exitonclick()

