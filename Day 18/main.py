from turtle import Turtle, Screen

# import colorgram


# colors = colorgram.extract('image.jpg', 20)

# color_list = []

# position = 0

# for _ in colors:
#     first_color = colors[position]
#     position += 1
#     rgb = first_color.rgb
#     color_tuple = (rgb[0],rgb[1], rgb[2] )
#     color_list.append(color_tuple)

# print(color_list)

screen = Screen()
tim = Turtle()
color_list = [(235, 234, 231), (235, 229, 232), (236, 34, 108), (221, 232, 237), (146, 27, 66), (230, 238, 233), (239, 75, 35), (7, 147, 92), (222, 170, 43), (183, 158, 47), 
              (44, 191, 232), (27, 126, 193), (253, 223, 0), (125, 193, 77), (84, 26, 88), (178, 39, 100), (244, 219, 48), (29, 169, 119), (203, 60, 32), (208, 131, 165)]
tim.speed("slowest")
tim.pensize(20)
tim.penup()
tim.position(-250, -100)

for _ in range(0, 10):
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    tim.pendown()



screen.exitonclick()