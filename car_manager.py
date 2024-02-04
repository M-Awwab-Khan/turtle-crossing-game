from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

"""
Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. 
"""

class CarManager(Turtle):
    cars = []
    move_speed = STARTING_MOVE_DISTANCE
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.fillcolor(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        CarManager.cars.append(self)

    def move(self, player):
        for car in CarManager.cars:
            car.goto(car.xcor() - CarManager.move_speed, car.ycor())
            if ((car.xcor() - player.xcor() <= 20) or (car.ycor() - player.ycor() <= 10)) and (car.distance(player) < 25):
                return True
