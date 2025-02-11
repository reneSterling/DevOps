#This python code is used to take a number from a user and check if it
#is positive, negative, zero or not a number
# This will be my first pull and push into a repo

num = 0

num = int(input ("Please enter a number:\n"))

if num > 0:
    print ("Your number is positive")

elif num < 0:
    print ("Your number is negative")

elif num == 0:
    print ("Your number is zero")
else:
    print ("What you entered is not a number")