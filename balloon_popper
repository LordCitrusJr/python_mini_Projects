from turtle import *

# Creates variables
diameter = 40
pop_diameter = 100

# This function begins the program and draws a baloon
def draw_balloon() :
  color("red")
  dot(diameter)

# This function will inflate the baloon and check if it will pop.
def inflate_balloon() :
# Since we're adding to a variable outside of the function, we need to add 'global' to it 
  global diameter
  diameter += 10
  draw_balloon()
# Since we're only reading the pop_diameter variable, we don't need to use the 'global' command
  if diameter >=pop_diameter:
    clear()
    write("POP!")
    diameter = 40

# This command draws the balloon
draw_balloon()

# This runs the inflate_balloon function on Up Arrow key press.
onkey(inflate_balloon, "Up")

# The onkey won't work until you use the listen command to check for key presses.
listen()
done()
