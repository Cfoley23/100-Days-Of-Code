from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280

# turtle that controls the player and moves the piece across the screen < ^ >
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle.gif')
        self.pu()
        self.go_to_start()
        self.color('olivedrab')
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
