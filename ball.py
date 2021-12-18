from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")

    def restart(self):
        self.goto(0, 0)

    def bounce_back(self):
        self.left(180 - 2 * self.heading())
