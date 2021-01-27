from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.bgcolor('grey')
def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.back(10)


def turn_left():
    timmy.left(5)


def turn_right():
    timmy.right(5)


def shake_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_backwards, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(shake_screen, 'c')

screen.exitonclick()
