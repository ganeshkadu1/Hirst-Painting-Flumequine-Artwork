import turtle
from turtle import Turtle
import random

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)