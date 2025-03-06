# This script automates the creation of a folder.


import os

fold = "Automations"

# this variable stores the location of where you want the folder to be saved. 
loc = os.path.join (os.getcwd(), fold )


#loc = os.path.join ("C:/Users/Window 10/Desktop/DevOps Practice", fold)


#create a User-defined function
def auto(): 
    if not(os.path.exists(loc)):
        os.makedirs(loc)

        #string formatting, advanced concatenation
        print (f"Your folder '{fold}' has been created successfully!" )

      #print ("Your folder" + fold + "has been created successfully")


    else:
        print ("Folder already exists!") 

# built in variable that runs scripts directly
if __name__ == "__main__":
    auto()

