import random
from turtle import Turtle


COLORS = ["Khaki", "Green", "Red", "Blue", "Deep Pink", "Grey", "Pink", "light sea green", "Cyan", "medium turquoise"]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(random.choice(COLORS))
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1
        self.color(random.choice(COLORS))

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.8
        self.color(random.choice(COLORS))

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05
        self.color(random.choice(COLORS))
