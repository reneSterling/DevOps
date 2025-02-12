#Accept the string value from the user

data = input("Please enter your text\n");

#print(data)

#Write to a file

with open("My First File.txt", "w") as file:
    file.write(data)
    file.close()

print("\nFinished writing to file, please confirm.")
