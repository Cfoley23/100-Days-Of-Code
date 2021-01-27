from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def draw_border(self):
        self.color('white')
        self.ht()
        # drawing the middle and self
        self.penup()
        self.goto(410, 310)
        self.setheading(180)
        self.pd()
        for lines in range(2):
            self.fd(810)
            self.lt(90)
            self.fd(610)
            self.lt(90)
        self.pu()
        self.goto(0, -300)
        self.setheading(90)
        for line in range(16):
            self.pd()
            self.fd(19.5)
            self.pu()
            self.fd(19.5)