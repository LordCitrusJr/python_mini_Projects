# Imports python turtle and random libraries
from turtle import *
from random import *

# Sets speed, bg to black, and hides turtle icon
speed(0)
bgcolor("black")
hideturtle()

# Creates variables to keep the dots in the window
width = window_width()
height = window_height()


# This function draws the dot with a random size
def draw_star(xpos, ypos):
    size = randrange(4, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")


# the loop that chooses a random pos and draws a dot
for x in range(100):
    xpos = randrange(round(-width / 2), round(width / 2))
    ypos = randrange(round(-height / 2), round(height / 2))
    draw_star(xpos, ypos)
done()
