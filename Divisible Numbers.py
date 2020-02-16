#----------------------------------------
#David Gibbs
#February 13, 2020
#
#This program repeats integers between 1 and 50. For each number
#that is divisible by three, it will print "divisible by three"
#instead of the number, and for each number that is divisible by
#five, it will print "Divisible by five" instead of the number.
#For numbers that are divisible by both three and five, the program will print,
#"Divisible by both". Otherwise, it will just print the number

for number in range (1, 50):
#sets the range of iteration between 1 and 49
    if (number % 5 == 0) and (number % 3 == 0):
        print("Divisible by both")
#checks to see if number in range is divisible by 5 with a remainder of 0,
#and 3 with a remainder of 0 (no decimals), if so, then it prints
#"Divisible by both" instead of the number.        
    elif (number % 3 == 0):
        print("Divisible by three")
#checks to see if number in range is divisible by 3 with a remainder of 0,
#(no decimals) if so,then it prints "Divisible by three" instead of number. 
    elif (number % 5 == 0):
        print("Divisible by five")
#checks to see if number in range is divisible by 3 with a remainder of 0,
#(no decimals) if so,then it prints "Divisible by five" instead of number. 
    else:
        print(number)
#if none of the above applies, then it prints only the number.
