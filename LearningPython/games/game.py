from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)/255
    g = random.randint(0, 255)/255
    b = random.randint(0, 255)/255
    return r, g, b


screen = Screen()
screen.setup(width=1500, height=1500)
screen.bgcolor("black")
turtle = Turtle()
turtle.pensize(40)
turtle.speed(100)


def up():
    turtle.setheading(90)
    turtle.forward(40)


def down():
    turtle.setheading(270)
    turtle.forward(40)


def left():
    turtle.setheading(180)
    turtle.forward(40)


def right():
    turtle.setheading(0)
    turtle.forward(40)


screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")

while True:
    turtle.color(random_color())
