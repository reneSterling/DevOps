#Accept the string value from the user
# A calculator accepting 2 numbers and an arithmetic operation and writing to file

data1 = int(input("Please enter your first number:\n"));
data2 = int(input("Please enter your first number:\n"));
operator = int(input("Please enter an arithmetic operator:\n"));
ans = data1 + data2

print(ans)

#Write to a file

with open("My First File.txt", "w") as file:
    file.write(ans)
    file.close()

print("\nThe calculation of youe two numbers is " + ans)
