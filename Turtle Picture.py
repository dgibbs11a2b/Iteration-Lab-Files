#----------------------------------------
#David Gibbs
#February 14, 2020
#
#This program imports the turtle module, and then
#insructs Bradley to move a pre-defined amount of units
#to create a multipoint star
#----------------------------------------

import turtle

wn = turtle.Screen()
#sets up a screen (canvas) to draw a picture
wn.bgcolor("blue")
#creates a blue background for the canvas
wn.title("Draw a star for me Bradley!")
#sets a title
bradley = turtle.Turtle()
#sets the turtle name to Bradley
bradley.pencolor("white")
#sets the pen color to white,
bradley.pensize(2)
#defines the pen size to 2

for i in range(30):
#sets a range of 30 intervals
    bradley.forward(i * 15)
#instructrs bradley the turtle to move forward
    bradley.right(144)
#instructs Bradley the turtle to turn right
turtle.exitonclick()
#gives the ability for the user to click on the window
#and close it after program execution
