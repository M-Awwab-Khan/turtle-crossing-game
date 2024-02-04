FONT = ("Courier", 24, "normal")
from turtle import Turtle

"""
Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
"""

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)
