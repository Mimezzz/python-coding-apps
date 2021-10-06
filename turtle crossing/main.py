import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car=CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
game_is_on = True
screen.listen()
screen.onkey(player.go_up,'Up')
scoreboard=Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

# detect when collision with the wall
    if player.ycor()>280:
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()
        scoreboard.update()

# detect when collision with the car
    for i in car.all_cars:
        if i.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()