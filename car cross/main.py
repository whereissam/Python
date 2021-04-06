import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_car:
        # print(car)
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 300:
        player.win()
        score.get_score()
        car_manager.get_speed()

screen.exitonclick()
