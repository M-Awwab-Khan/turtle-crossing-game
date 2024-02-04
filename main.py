import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.move, 'Up')

game_is_on = True
i = 12
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i % 12 == 0:
        car = CarManager()
    is_collided = car.move(player)
    if is_collided:
        break
    i += 1

screen.exitonclick()