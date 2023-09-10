from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()


colors = ["yellow", "dark orange", "medium slate blue", "spring green", "deep pink", "dodger blue"]
tim.speed("fast")
tim.width(10)

is_in_screen = True

while is_in_screen:
    tim.pencolor(random.choice(colors))
    direction = random.randrange(0, 2)
    if direction == 0:
        tim.right(90)
    else:
        tim.left(90)
    tim.forward(random.randint(0, 100))
        

    

    
    





x
screen.exitonclick()
