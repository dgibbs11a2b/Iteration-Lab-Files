#----------------------------------------
#David Gibbs
#February 13, 2020
#
#This program prompts the user for the number of sides,
#the length of the side, the color of the line,
#and finally, the fill color of the polygon and then
#draws the polygon to the screen and fills it.
#----------------------------------------

import turtle
#imports the turtle library
wn = turtle.Screen()    
#prepares the graphics window
john = turtle.Turtle()
#assigns the name John to our turtle
sides = int(input("How many sides do you want ?: "))
#prompts the user for the number of sides for the figure
angle = 360 / sides
#divides 360 by the number of sides in the polygon
length = int(input("What is the length of sides: "))
#sets the length in units that john should move forward
line_color = input("Input the color of the lines: ")
#receives input for colors such as purple or green 
john.color(line_color)
#assigns the color above to john's pen on his tail
fill_color = input("Input the fill color for the polygon:" )    
john.fillcolor(fill_color)
#sets the fill color for the figure
john.begin_fill()    

for i in range(sides):    
        john.forward(length)  
        john.left(angle)    
john.end_fill()
wn.exitonclick() 
