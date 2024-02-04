from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.fillcolor(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))

    def move(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())
