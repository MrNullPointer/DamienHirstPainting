from turtle import Turtle, colormode, Screen
import random

hirst = Turtle()

colormode(255)


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
    hirst.pensize(5)
    hirst.speed(6)
    for _ in range(500):
        hirst.forward(30)
        hirst.setheading(random.choice(directions))
        hirst.color(randomColor())


def main():
    #     for sides in range(3, 11):
    #         drawShapes(sides)
    randomWalk()


main()
screen = Screen()
screen.exitonclick()