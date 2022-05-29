from turtle import Turtle, Screen


t = Turtle()


def move_forward():
    t.forward(10)

def turn_right():
    t.right(5)

def turn_left():
    t.left(5)

def move_back():
    t.back(10)

def clear_screen():
    t.penup()
    t.clear()
    t.home()
    t.pendown()


scr = Screen()

scr.onkey(key="w", fun=move_forward)
scr.onkey(key="d", fun=turn_right)
scr.onkey(key="a", fun=turn_left)
scr.onkey(key="s", fun=move_back)
scr.onkey(key='c', fun=clear_screen)

scr.listen()
scr.exitonclick()



scr.exitonclick()