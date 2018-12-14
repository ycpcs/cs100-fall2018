# Import turtle graphics library
import turtle
from random import randint

# Import math functions
from math import *

# draw a wall at location x extending from yTop to yBottom
# with the specified pen color and pen width
# wall passes in a wall 3-tuple consisting of (x, yTop, yBottom)
def drawWallAtPosition(turtle, wall, color, width):

    # save current position and orientation
    (xold,yold) = turtle.position()
    heading = turtle.heading()
    oldWidth = turtle.width()

    # get x and y extents of wall
    (x, yTop, yBottom) = wall

    # position turtle to upper-left corner
    turtle.penup()
    turtle.setposition(x, yTop)
    turtle.setheading(270)
    turtle.pensize(width)
    turtle.color(color)

    # draw wall
    turtle.pendown()
    turtle.forward(yTop-yBottom)

    # return turtle to original position and orientation
    turtle.penup()
    turtle.setposition(xold, yold)
    turtle.setheading(heading)
    turtle.pensize(oldWidth)
    turtle.color("black")

# returns the new heading for the turtle
#    "bounces" turtle off either wall
def getNewHeading(turtle):
    return 540 - turtle.heading()

# checks for collision of turtle with right wall
#    (x,y) is a 2-tuple of the position of the turtle
#    (wallX, wallY1, wallY2) is a 3-tuple of the x-position of the wall,
#             and the y-positions of the top and bottom of the wall
# if x is to left of the right wall, or outside the top or bottom boundaries
#     of the wall, return False, otherwise return True
def checkRightWallCollision(turtle,wall):

    (x,y) = turtle.position()
    (wallX,wallY1,wallY2) = wall

    # TODO 1: insert the logic to detect the turtle's collision with the right wall
    # TODO 1: return True or False, based on the above comments
    # TODO 1: include the following prompt in the logic

    print("Collision with right wall")





# checks for collision of turtle with left wall
#    (x,y) is a 2-tuple of the position of the turtle
#    (wallX, wallY1, wallY2) is a 3-tuple of the x-position of the wall,
#             and the y-positions of the top and bottom of the wall
# if x is to right of the left wall, or outside the top or bottom boundaries
#     of the wall, return False, otherwise return True
def checkLeftWallCollision(turtle, wall):
    (x, y) = turtle.position()
    (wallX, wallY1, wallY2) = wall

    # TODO 2: insert the code to detect the turtle's collision with the left wall
    # TODO 2: return True or False, based on the above comments
    # TODO 2: include the following prompt in the logic

    print("Collision with left wall")






# TODO 3: define a function getNumCollisions() that accepts no arguments,
# TODO 3:    prompts the user for a value between 1 and 20 inclusive,
# TODO 3:    and returns that value.
# TODO 3: Use the prompt that has been provided below (uncomment the line to use
# TODO 3:    it in the function)
# TODO 3: prompt user for a guess for the # of collisions that will occur given
# TODO 3:    the random heading of the turtle, as it bounces between the walls
# TODO 3: validate the user input so that the function only returns a guess after
# TODO 3:     the user has entered a value between 1 and 20 inclusive


#  guess = int(input("Guess the number of collisions between 1 and 20 "))





# Creates a game board with two random vertical walls with the turtle beginning at the top
#    with a random downward heading fro 10-50 degrees.
# The user enters a guess for the number of collisions before the turtle reaches the bottom
#    by reflecting (bouncing) off the walls.
# The program then outputs how the user's guess compared to the actual number of collisions
def main():
    # create turtle
    bob = turtle.Turtle()

    # set speed to FAST
    bob.delay = 0.01

    # get random wall x-positions in the range of +/- 10-50
    leftX = -randint(10,50)
    rightX = randint(10,50)

    # get random lengths for the walls in the range of +/- 100-150
    maxY = 100 + randint(0,50)
    minY = -maxY

    # create wall objects
    leftWall = (leftX,maxY,minY)
    rightWall = (rightX,maxY,minY)

    # draw walls
    drawWallAtPosition(bob,leftWall,"red",3)
    drawWallAtPosition(bob,rightWall,"red",3)

    # position turtle at top of left wall with random heading
    #    in range 10-50 degrees facing downward
    heading = 360 - randint(10,50)
    bob.setposition(leftX+1,maxY-1)
    bob.setheading(heading)
    (x,y) = bob.position()

    # initialize variables
    collisionCount = 0
    guess = 0

    # TODO 4: call getNumCollisions() storing the returned value in guess




    # continue moving the turtle until it reaches the bottom
    while y > minY:
        # move turtle forward 1
        bob.pendown()
        bob.forward(1)
        bob.penup()


        # TODO 5: If a collision occurs with either wall
        # TODO 5:    assign the value returned by calling getNewHeading() to heading
        # TODO 5:    and count the collision
        # TODO 5:    include the following prompt in the logic

        print("Collision", collisionCount, "/", guess)






        # set turtles' heading to the newly acquired heading and get current position
        bob.setheading(heading)
        (x,y) = bob.position()

    # TODO 6: provide logic to compare guess to actual number of collisions so that
    # TODO 6: each prompt below is only output for its respective logical result

    print("There were less collisions than you guessed")

    print("There were more collisions than you guessed")

    print("CONGRATULATIONS! You guessed correctly!")

    print("Error")

    # exit program
    input("Press any key to exit")

main()

