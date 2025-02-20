from Countries import *
from Currencies import *
from Shared import *
from time import sleep


class CurrencyConverter:
    def __init__(self, symbol, bills, coins):
        self.symbol = symbol
        self.bills = bills
        self.coins = coins

    def makeChange(self):
        """
        Prompts the user to enter the amount of change to give in decimal form.

        If the input is invalid or less than or equal to zero, the user is prompted to try again.

        Calls the calculateChange method with the change amount in cents rounded to two decimal places * 100.
        """
        try:
            changeAmount = round(float(input(f"\nEnter the amount of change in decimal form: {self.symbol}")), 2)  # fmt: skip
            if changeAmount <= 0:
                invalidInputHandler()
                return self.makeChange()
            else:
                self.calculateChange(int(changeAmount * 100))
        except ValueError:
            invalidInputHandler()
            return self.makeChange()

    def calculateChange(self, changeAmount):
        """
        Calculates the change to give in bills and coins based on the selected currencies.

        Starts with the highest denomination and works down to the lowest denomination.
        """

        changeAmountString = f"{changeAmount / 100:.2f}"
        print(f"\nThe amount of change to give is: {self.symbol}{changeAmountString}")
        print("\nThe bills and coins to give are")
        print("-------------------------------")

        for name, value in self.bills.items():
            count, changeAmount = divmod(changeAmount, int(value * 100))
            if count > 0:
                print(f"{int(count)} - {name}")

        for name, value in self.coins.items():
            count, changeAmount = divmod(changeAmount, int(value * 100))
            if count > 0:
                print(f"{int(count)} - {name}")
