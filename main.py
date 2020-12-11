from turtle import Turtle, Screen
import random

hirst = Turtle()

colors = ["Red", "Blue", "Green", "Yellow", "Cyan", "Pink", "Magenta", "Gray", "Purple", "Black"]

def drawShapes(sides):
    hirst.color(random.choice(colors))
    angle = 360 / sides
    for _ in range(sides):
        hirst.left(angle)
        hirst.forward(100)
        

def main():
    for sides in range(3, 11):
        drawShapes(sides)


main()
screen = Screen()
screen.exitonclick()