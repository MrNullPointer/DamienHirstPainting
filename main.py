from turtle import Turtle, colormode, Screen, tiltangle
import random

hirst = Turtle()

colormode(255)
hirst.speed(0)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

directions = [0, 90, 180, 270]


def drawShapes(sides):
    hirst.color(randomColor())
    angle = 360 / sides
    for _ in range(sides):
        hirst.left(angle)
        hirst.forward(100)


def randomWalk():
    for _ in range(500):
        hirst.pensize(5)
        hirst.forward(30)
        hirst.setheading(random.choice(directions))
        hirst.color(randomColor())


def drawSpiralograph(tiltAngle):
    times = 360 // tiltAngle
    for _ in range(times):
        hirst.color(randomColor())
        hirst.circle(100)
        hirst.setheading(hirst.heading() + tiltAngle)

def main():
    #     for sides in range(3, 11):
    #         drawShapes(sides)
    drawSpiralograph(2)

main()
screen = Screen()
screen.exitonclick()