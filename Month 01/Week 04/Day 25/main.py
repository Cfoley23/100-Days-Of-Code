from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title('THIS IS PYPONG')
screen.setup(width=800, height=600)
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    scoreboard.draw_border()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect a collision with the upper or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -370:
        ball.bounce_x()
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
