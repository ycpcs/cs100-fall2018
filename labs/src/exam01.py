__author__ = 'Donald J. Hake II'

import turtle
from math import *

def drawSquareFromCenter(turtle,x):
    turtle.penup()
    turtle.forward(-x/2)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.pendown( )
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.penup( )
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.right(90)


def main():
    # create turtle
    bob = turtle.Turtle()

    # get user input
    size = int(input("Enter size of square: "))

    # TASK 0: create and initialize all variables
    # TODO 0: create and initialize variables using the variable names supplied
    # TODO 0: replace 0's with actual calculations
    # CALC 1: calculate diagonals of diamonds from size of squares
    diagDiamond1 = 0
    diagDiamond2 = 0
    diagDiamond3 = 0
    diagDiamond4 = 0

    # CALC 2: calculate sizes of diamonds from their diagonals
    sizeDiamond1 = 0
    sizeDiamond2 = 0
    sizeDiamond3 = 0
    sizeDiamond4 = 0

    # CALC 3: calculate diagonal of squares
    diagSquare = 0

    # TASK 1: draw the 4 diamonds first, from smallest to largest
    # TODO 1: position cursor to draw diamonds around origin


    # TODO 2: draw 1st diamond, centered around origin


    # TODO 3: draw 2nd diamond, centered around origin


    # TODO 4: draw 3rd diamond, centered around origin


    # TODO 5: draw 4th diamond, centered around origin


    # TASK 2: draw squares, clockwise, starting with top square, moving directly between square centers
    # TODO 6: position cursor to center of top square


    # TODO 7: draw top square


    # TODO 8: move directly to center of right square (center to center)


    # TODO 9: draw right square


    # TODO 10: move directly to center of bottom square (center to center)


    # TODO 11: draw bottom square


    # TODO 12: move directly to center of left square (center to center)


    # TODO 13: draw left square


    # TASK 3: leave cursor at top of diagram
    # TODO 14: move cursor to top of diagram, facing right


    # wait for user input before exiting
    input("Press any key to exit")

main()