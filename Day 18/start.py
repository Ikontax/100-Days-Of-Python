import turtle as t
from turtle import Screen
import random


tim = t.Turtle()
t.colormode(255)
screen = Screen()

tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =  (r, g, b )
    return random_color

def draw_spitograph(size_of_gab):
    for _ in range(int(360/ size_of_gab)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gab)    
    
draw_spitograph(5)
screen.exitonclick()
