from countries import *
from currencies import *
from time import sleep
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
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
    try:
        i = 0
        maxUserAttemps = 4
        while i < maxUserAttemps:
            if i == maxUserAttemps - 1:
                print("Too many invalid inputs. Exiting program...")
                exit()
            i += 1
            response = input("Enter yes, no, or exit: ").lower().strip()
            if response in ["y", "yes"]:
                return True
            elif response in ["n", "no", "exit"]:
                print("Exiting program...")
                exit()
    except ValueError:
        logging.critical("Invalid input. Exiting the program.".upper())
