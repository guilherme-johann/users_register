from exercises.exercise115a.library.files import *
from time import sleep
from os import remove

# Try to found the file
file = "data.txt"
if not fileexistence(file):
    createfile(file)

# Main menu
while True:
    answer = menu(["List registered users", "Register a new user","Delete registered users", "Leave the system"])
    if answer == 1:
        # Option of list the users
        readfile(file)
    elif answer == 2:
        # Option of register a new user
        header("New Register")
        name = str(input("Name:"))
        age = readinteger("Age:")
        register(file, name, age)
    elif answer == 3:
        remove('data.txt')
        print("All the users were deleted.")
        createfile(file)
    elif answer == 4:
        # Option to leave the program
        header("\033[0;33mThe system was closed, see you soon!\033[m")
        break
    else:
        header("\033[0;31mERROR! Choose a valid option.\033[m")
    sleep(1.5)
