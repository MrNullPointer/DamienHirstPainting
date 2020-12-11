from turtle import Turtle, Screen
import random

hirst = Turtle()

colors = ["#2F4F4F", "#fafcc2", "#9ab3f5", "#ffa5a5", "#794c74", "#AFEEEE", "#FF6347", "#00FF00", "#48D1CC", "#ff9b93", "#4e8d7c", "#d35d6e", "#db6400", "#bce6eb", "#f05454", "#cad315", "#7e7474", "#2d6187", "#555555"]
directions = [0, 90, 180, 270]


def drawShapes(sides):
    hirst.color(random.choice(colors))
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
        hirst.color(random.choice(colors))


def main():
    #     for sides in range(3, 11):
    #         drawShapes(sides)
    randomWalk()


main()
screen = Screen()
screen.exitonclick()