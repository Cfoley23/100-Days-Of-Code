import turtle

bob = turtle.Turtle()
joe = turtle.Turtle()
joe.ht()
bob.ht()
bob.color('olivedrab')
joe.color('yellow')
bob.pensize(1.5)
joe.pensize(1.5)
bob.shape('turtle')
bob.pencolor('red')
bob.shapesize(stretch_wid=2, stretch_len=2)
bob.speed(0)
joe.speed(0)
bob.screen.bgcolor('black')


def draw_circles(name, circle_size, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        name.circle(circle_size)
        name.setheading(name.heading() + size_of_gap)

def draw_squares(turtle_name, color, square_size, size_of_gap):
    turtle_name.color(color)
    for _ in range(int(360 / size_of_gap)):
        for _ in range(4):
            turtle_name.forward(square_size)
            turtle_name.left(90)
        turtle_name.setheading(turtle_name.heading() + size_of_gap)


draw_circles(bob, 100, 20)
draw_circles(joe, 325, 15)
draw_squares(bob, 'purple', 180, 10)
draw_squares(joe, 'green', 400, 5)


bob.screen.exitonclick()