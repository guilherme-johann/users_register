from exercises.exercise115a.library.interface import *


def fileexistence(name):
    try:
        f = open(name, "rt")
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createfile(name):
    try:
        f = open(name, "wt+")
        f.close()
    except:
        print("\033[0;31mThere was an error creating the file...\033[m")
    else:
        print(f"\033[0;32mFile {name} created with success!\033[m")


def readfile(name):
    try:
        f = open(name, "rt")
    except:
        print("\033[0;31mThere was an error reading the file...\033[m")
    else:
        header("Registered Users")
        for line in f:
            data = line.split(";")
            data[1] = data[1].replace("\n", "")
            print(f"{data[0]:<30}{data[1]:>3} years")
    finally:
        f.close()


def register(file, name="unknown", age=0):
    try:
        f = open(file, "at")
    except:
        print("\033[0;31mThere was an error while opening the file.\033[m")
    else:
        try:
            f.write(f"{name};{age}\n")
        except:
            print("\033[0;31mThere was an error while registering the data.\033[m")
        else:
            print(f"\033[0;32m{name} is now registered!\033[m")
            f.close()
