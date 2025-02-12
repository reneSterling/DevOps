#This accepts a name and age from the user and displays name is "Eligible" 
# if age is greater than 18

u_name = " "
u_age = 0

u_name = str(input ("Please enter your name:\n"))
u_age = int(input("Please enter your age:\n"))

if u_age >= 18:
    print (u_name + ": Eligible to vote")
else:
    print ("Sorry you are not eligible to vote.")





