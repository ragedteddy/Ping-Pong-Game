from turtle import Turtle


class Ping(Turtle):

    def __init__(self, x, y):
        super(Ping, self).__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.goto(x, y)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 30)
