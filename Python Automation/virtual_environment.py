#This script automates the creation of a virtual environment

import os

print ("We will be setting up a virtual environment")

os.system("python -m venv venv")

os.system("venv\\Scripts\\activate")

os.system("pip install -r one.txt")

print ("Installation complete. You can now use requests and flasks in your projects")