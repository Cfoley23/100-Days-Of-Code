from turtle import Turtle, Screen
import random

is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
screen.setup(width=500, height=400)
screen.bgpic('turtle.png')
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle Will Win The Race? Pick A Color:  ")
y_position = [-80, -50, -10, 30, 60, 90]
all_turtles = []



for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'Congratulations! The {winning_color} is the winner!')
            else:
                print(f"Better luck next time. The {winning_color} turtle won.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
