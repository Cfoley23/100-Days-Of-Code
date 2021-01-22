import colorgram
import turtle as t
import random
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171),
              (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120),
              (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194),
              (183, 192, 201), (214, 177, 191)]
timmy = t.Turtle()
t.colormode(255)
timmy.speed(0)
timmy.color('darkgreen')
timmy.shape('turtle')
screen = t.Screen()
timmy.hideturtle()

num_of_dots = 100
timmy.penup()
timmy.setx(-200)
timmy.sety(-200)
for dot_count in range(1, num_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen.exitonclick()
