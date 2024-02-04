import time
from turtle import Turtle, Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard, FONT

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.move, 'Up')
scoreboard = Scoreboard()

game_is_on = True
i = 12
while game_is_on:
    time.sleep(MOVE_INCREMENT)
    screen.update()
    if i % 12 == 0:
        car = CarManager()
    is_collided = car.move(player)
    if is_collided:
        t = Turtle()
        t.write('Game Over', align='center', font=FONT)
        break
    if player.ycor() > FINISH_LINE_Y:
        player.reset_pos()
        scoreboard.level += 1
        scoreboard.update_level()
        MOVE_INCREMENT *= 0.5

    i += 1

screen.exitonclick()