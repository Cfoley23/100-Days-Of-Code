import turtle
import random

# turtle object
#img_turtle = turtle.Turtle()

# registering the image
# as a new shape
#turtle.register_shape('example.gif')

# setting the image as cursor
#img_turtle.shape('example.gif')


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2.5
CAR_COLOR = ["car_blue.gif", "car_green.gif", "car_pink.gif", "car_orange.gif", "car_purple.gif", "car_yellow.gif"]


# generate random cars and move them across the screen
class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.ht()
        #self.shape(random.choice(CAR_COLOR))

        turtle.register_shape("car_green.gif")

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = turtle.Turtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            # for rand_gif in CAR_COLOR:
            #     turtle.register_shape(rand_gif)
            new_car.shape(random.choice(CAR_COLOR))
            random_y = random.randint(-225, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
