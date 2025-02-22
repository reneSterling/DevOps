#Accept the string value from the user
# A calculator accepting 2 numbers and an arithmetic operation and writing to file

num1 = int(input("Please enter your first number:\n"));
operator = input("Please enter an arithmetic operator:\n");
num2 = int(input("Please enter your second number:\n"));
ans = 0

#Match Case in Python

match operator:
    case '*':
        ans = num1 * num2
    case '/':
         ans = num1 / num2
    case '%':
         ans = num1 % num2
    case '+':
        ans = num1 + num2 
    case '-':
        ans = num1 + num2


#Write to a file
with open("Calculation.txt", "a") as file:
   file.write(str(num1) +" "+operator+" "+str(num2)+" = "+str(ans) + '\n')
   file.close()

#Multiple concatenation
print("Finished writing to file\n")



