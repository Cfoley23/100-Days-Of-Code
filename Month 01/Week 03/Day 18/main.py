from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('olivedrab')


# square movement
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(50):
#     timmy.pendown()
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon in random colors
num_sides = 10
colors = []

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3,11):
    draw_shapes(shape_side_n)




screen = Screen()
screen.exitonclick()