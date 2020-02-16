#----------------------------------------
#David Gibbs
#February 12, 2020
#
#This program will print the numbers 12,10,32,3,66,17,42,99, and 20
#each on a new line. It will then print these numbers squared and display them 
#on a new line
#----------------------------------------
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#Assigns "numbers'" as the variable
for i in numbers:
    print(i)
#Creates the for loop for each interval of numbers and then
#displays it to the screen 

for i in numbers:
    print("The square of", i, "is", i**2)
#Creates the for loop for each interval of numbers and calculates the square
#for each number and then displays it to the screen
