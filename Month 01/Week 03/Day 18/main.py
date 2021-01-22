import turtle as t
import random

screen = t.Screen()

timmy = t.Turtle()
timmy.shape('turtle')
timmy.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def make_random_walk(step_number):
    timmy.penup()
    screen.bgcolor(random_color())
    for _ in range(step_number):
        timmy.color('olivedrab')
        timmy.dot(random.randint(3, 40), random_color())
        timmy.setheading(90 * random.randint(0, 3))
        timmy.forward(random.randint(1, 50))
        timmy.pensize(random.randint(1, 10))


make_random_walk(500)

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shapes(shape_side_n)


screen.exitonclick()
