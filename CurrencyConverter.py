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
        try:
            changeAmount = round(float(input(f"\nEnter the amount of change in decimal form: {self.symbol}")), 2)
            if changeAmount <= 0:
                invalidHandler()
                return self.makeChange()
            else:
                self.calculateChange(int(changeAmount * 100))
        except ValueError:
            invalidHandler()
            return self.makeChange()
        
    def calculateChange(self, changeAmount):
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