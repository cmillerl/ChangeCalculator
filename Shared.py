from Countries import *
from Currencies import *
from time import sleep
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(levelname)s - %(message)s',
    handlers = [logging.StreamHandler()]
)

def invalidInputHandler():
    """
    Handles:
        Invalid input by prompting the user to try again or exit the program.

    Returns:
        True if the user wants to try again, otherwise exits the program.

    Raises:
        ValueError if input can't be converted to a string.
    """

    logging.warning("Invalid Input. Do you want to try again?")
    sleep(2)
    try:
        response = input("Enter yes, no, or exit: ").lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no", "exit"]:
            print("Exiting program...")
            exit()
        else:
            logging.error("Invalid input. Exiting the program.".upper())
            sleep(2)
            invalidInputHandler()
    except ValueError:
        logging.error("Invalid input. Exiting the program.".upper())
