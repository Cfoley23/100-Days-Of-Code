import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.bgpic('cross_road_bg.gif')
screen.tracer(0)
screen.register_shape('turtle.gif')
screen.register_shape('car_green.gif')
screen.register_shape('car_blue.gif')
screen.register_shape('car_pink.gif')
screen.register_shape('car_purple.gif')
screen.register_shape('car_orange.gif')
screen.register_shape('car_yellow.gif')
car_manager = CarManager()
scoreboard = Scoreboard()

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collisions with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
