from turtle import Screen, Turtle
from ball import Ball
from ping import Ping
from score import Score
import turtle, time

screen = Screen()
screen.bgcolor("black")
screen.setup(1200, 600)
screen.title("My Ping Pong")
screen.listen()

pong = Ball()
ping1 = Ping(573, 0)
ping2 = Ping(-580, 0)
score1 = Score(-100, 200)
score2 = Score(50, 200)

turtle.onkey(ping1.up, "Up")
turtle.onkey(ping1.down, "Down")
turtle.onkey(ping2.up, "w")
turtle.onkey(ping2.down, "s")

game = Turtle()
game.penup()
game.hideturtle()
game.color("blue")
game.goto(-75, -100)

def reload():
    game.write("Press 'r' to begin.", font=("Verdana",
                                            15, "normal"))

def play():
    game.clear()
    pong.left(20)
    while True:
        if ping1.distance(pong) < 15 or ping2.distance(pong) < 15:
            pong.bounce_back()
        time.sleep(0.001)
        if pong.xcor() > 600:
            score1.update()
            pong.restart()
            reload()
            break
        elif pong.xcor() < -600:
            score2.update()
            pong.restart()
            reload()
            break
        if pong.ycor() > 300 or pong.ycor() < -300:
            pong.left(360 - 2 * pong.heading())
        pong.forward(10)

reload()
turtle.onkey(play, "r")

screen.exitonclick()
