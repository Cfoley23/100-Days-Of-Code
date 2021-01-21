import turtle as t
import random

timmy = t.Turtle()
timmy.shape('turtle')
timmy.speed(0)
t.colormode(255)
timmy.color('olivedrab')
screen = t.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

screen.bgcolor(random_color())

# my solution
def spirograph_circle(num_circles):
    for _ in range(num_circles):
        timmy.pencolor(random_color())
        timmy.circle(random.randint(50, 200), 360)
        timmy.right(5)


# angela's solution
def draw_circles(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_circles(5)


#spirograph_circle(100)

screen.exitonclick()