# This automate git commands

import os

com = input("Please type your commit message")

os.system("git add .")

os.system(f'git commit -m ' "{com} ")

os.system("git push origin main")

