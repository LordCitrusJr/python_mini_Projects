from turtle import *

# Setting some startup commands
speed(0)
bgcolor("#D2691E")

# Creating move variable
move_distance = 50

# Setting height and width variables
height = window_height()
width = window_width()

# Moving the turtle to ocean drawing starting point
penup()
goto(300, height)
pendown()

# Drawing ocean
color("blue")
begin_fill()
goto(0, height)
goto(round(width / 2), height)
goto(round(width / 2), -height)
goto(300, -height)
goto(300, height)
end_fill()

# Changing cursor to turtle and moving it to start point
penup()
goto(round(-width / 2) + 200, 0)
shape("turtle")
color("green")


# Movement functions
def move_up():
    setheading(90)
    forward(move_distance)


def move_down():
    setheading(270)
    forward(move_distance)


def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()


def move_left():
    setheading(180)
    forward(move_distance)


# Win condition check
def check_goal():
    if xcor() > 300:
        hideturtle()
        color("White")
        write("YOU WIN!")
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Right")
        onkey(None, "Left")


# Checking for movement keys
onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_right, "Right")
onkey(move_left, "Left")
listen()

# To keep window open
done()
