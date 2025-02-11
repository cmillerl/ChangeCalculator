from Countries import *
from Currencies import *
from time import sleep

def invalidHandler():
    print("Invalid Entry. Do you want to try again?")
    sleep(1)
    try:
        response = input("Enter 'y' for yes or 'n' to exit: ").lower()
        if response == "y":
            return True
        elif response == "n" or "exit":
            print("Exiting program...")
            exit()
        else:
            invalidHandler()
    except ValueError:
        print("Error in Shared.py: invalidHandler()")
        print("Exiting program...")
        exit()
