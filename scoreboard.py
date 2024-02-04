FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def update_level(self):
        self.write(f"Level: {self.level}", align='left', font=FONT)
