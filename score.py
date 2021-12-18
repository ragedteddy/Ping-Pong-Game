from turtle import Turtle

class Score(Turtle):

    def __init__(self, x, y):
        super(Score, self).__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x, y)
        self.write("0", font=("Verdana",
                                            50, "normal"))
        self.score = 0

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", font=("Verdana",
                                        50, "normal"))