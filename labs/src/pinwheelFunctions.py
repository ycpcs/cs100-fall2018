# Import turtle graphics library
import turtle

# Import math functions
from math import *

# Function to draw a square about the current position
def drawSquareFromCenter(turtle,x):
    turtle.penup()
    turtle.forward(-x / 2)
    turtle.right(90)
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.penup()
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.forward(x / 2)
    turtle.right(90)

# TODO: Right turn movement function
def moveToCenterRightTurn():

# TODO: Diagonal movement function
def moveToCenterDiagonal():

# TODO: Complete program to call functions
#       to draw pinwheel
def main():
    # Create turtle
    bob = turtle.Turtle()

    # Get user input
    size1 = int(input('Enter size for first square: '))

    # Draw first square
    drawSquareFromCenter(bob,size1)

    # Press any key to exit
    input()

main()