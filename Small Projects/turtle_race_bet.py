import turtle
from turtle import Turtle, Screen
import random

scr = Screen()
scr.setup(height=600, width=500)
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtle_list = []

h = -200

for t in range(0, 7):
    newTurt = Turtle(shape='turtle')
    newTurt.penup()
    newTurt.color(colors[t])
    newTurt.goto(-230, h)
    turtle_list.append(newTurt)
    h += 50

start_race = False

user_bet = scr.textinput(title="Make your bet!", prompt="Which turtle is going to win the race? (Enter a color)")
if user_bet:
    start_race = True

while start_race:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 250:
            print(f'The winner is {turtle.color()[0]} turtle!')
            if user_bet.lower() == turtle.color():
                print('You have won the bet!')
            else:
                print('You have lost the bet...')
            start_race = False
