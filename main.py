import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "w")

game_on = True 
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.crate_car()
    car_manager.move_cars()

    # collison with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # reaching the top
    if player.at_finish_line():
        player.go_back()
        car_manager.speed_up()
        scoreboard.update_scoreboard()



screen.exitonclick()