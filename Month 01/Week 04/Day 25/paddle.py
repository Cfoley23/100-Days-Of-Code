from turtle import Turtle
MOVEMENT_AMOUNT = 30
PADDLE_WIDTH = 4
PADDLE_HEIGHT = 1

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVEMENT_AMOUNT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVEMENT_AMOUNT
        self.goto(self.xcor(), new_y)
