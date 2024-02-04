from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    cars = []
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
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())
            if ((car.xcor() - player.xcor() <= 20) or (car.ycor() - player.ycor() <= 10)) and (car.distance(player) < 25):
                print('collided')
