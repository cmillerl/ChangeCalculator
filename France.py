from Shared import *
from time import sleep

countries.append("France")

class France:
    def __init__(self):
        self.bills = []
        self.coins = []
    
    def includedBillsMethod(self):
        try:
            print("Which bills would you like to include for giving change?")
            print("1. All")
            print("2. €200, €100, €50, €20, 10€, €5")
            print("3. €100, €50, €20, €10, €5")
            print("4. €50, €20, €10, €5")
            print("5. €20, €10, €5")
            print("6. €10, €5")
            print("7. €5")
            print("8. None")
            includedBills = int(input("Enter a valid number 1-8: "))
        except ValueError:
            invalidNumberHandler()
            return self.includedBillsMethod()

        if includedBills == 1:
            self.bills = [(500, "Five Hundred Euros"), (200, "Two Hundred Euros"), (100, "One Hundred Euros"), (50, "Fifty Euros"), (20, "Twenty Euros"), (10, "Ten Euros"), (5, "Five Euros")]
        elif includedBills == 2:
            self.bills = [(200, "Two Hundred Euros"), (100, "One Hundred Euros"), (50, "Fifty Euros"), (20, "Twenty Euros"), (10, "Ten Euros"), (5, "Five Euros")]
        elif includedBills == 3:
            self.bills = [(100, "One Hundred Euros"), (50, "Fifty Euros"), (20, "Twenty Euros"), (10, "Ten Euros"), (5, "Five Euros")]
        elif includedBills == 4:
            self.bills = [(50, "Fifty Euros"), (20, "Twenty Euros"), (10, "Ten Euros"), (5, "Five Euros")]
        elif includedBills == 5:
            self.bills = [(20, "Twenty Euros"), (10, "Ten Euros"), (5, "Five Euros")]
        elif includedBills == 6:
            self.bills = [(10, "Ten Euros"), (5, "Five Euros")]
        elif includedBills == 7:
            self.bills = [(5, "Five Euros")]
        elif includedBills == 8:
            self.bills = []
        else:
            invalidNumberHandler()
            return self.includedBillsMethod()

    def includedCoinsMethod(self):
        try:
            print("Which coins would you like to include for giving change?")
            print("1. All")
            print("2. €1, Cinquante Centimes, Vingt Centimes, Dix Centimes, Cinq Centimes, Deux Centimes, Un Centime")
            print("3. Cinquante Centimes, Vingt Centimes, Dix Centimes, Cinq Centimes, Deux Centimes, Un Centime")
            print("4. Vingt Centimes, Dix Centimes, Cinq Centimes, Deux Centimes, Un Centime")
            print("5. Dix Centimes, Cinq Centimes, Deux Centimes, Un Centime")
            print("6. Cinq Centimes, Deux Centimes, Un Centime")
            print("7. Deux Centimes, Un Centime")
            print("8. Un Centime")
            includedCoins = int(input("Enter a valid number 1-8: "))
        except ValueError:
            invalidNumberHandler()
            return self.includedCoinsMethod()

        if includedCoins == 1:
            self.coins = [(2, "Two Euros"), (1, "One Euros"), (0.50, "Cinquante Centimes"), (0.20, "Vingt Centimes"), (0.10, "Dix Centimes"), (0.05, "Cinq Centimes"), (0.02, "Deux Centimes"), (0.01, "Un Centimes")]
        elif includedCoins == 2:
            self.coins = [(1, "One Euros"), (0.50, "Cinquante Centimes"), (0.20, "Vingt Centimes"), (0.10, "Dix Centimes"), (0.05, "Cinq Centimes"), (0.02, "Deux Centimes"), (0.01, "Un Centimes")]
        elif includedCoins == 3:
            self.coins = [(0.50, "Cinquante Centimes"), (0.20, "Vingt Centimes"), (0.10, "Dix Centimes"), (0.05, "Cinq Centimes"), (0.02, "Deux Centimes"), (0.01, "Un Centimes")]
        elif includedCoins == 4:
            self.coins = [(0.20, "Vingt Centimes"), (0.10, "Dix Centimes"), (0.05, "Cinq Centimes"), (0.02, "Deux Centimes"), (0.01, "Un Centimes")]
        elif includedCoins == 5:
            self.coins = [(0.10, "Dix Centimes"), (0.05, "Cinq Centimes"), (0.02, "Deux Centimes"), (0.01, "Un Centimes")]
        elif includedCoins == 6:
            self.coins = [(0.05, "Cinq Centimes"), (0.02, "Deux Centimes"), (0.01, "Un Centimes")]
        elif includedCoins == 7:
            self.coins = [(0.02, "Deux Centimes"), (0.01, "Un Centimes")]
        elif includedCoins == 8:
            self.coins = [(0.01, "Un Centimes")]
        else:
            invalidNumberHandler()
            return self.includedCoinsMethod()

    def makeChange(self):
        try:
            changeAmount = round(float(input("Enter the amount of change in decimal form (example 17.54): €")), 2)
            if changeAmount <= 0:
                invalidNumberHandler()
                return self.makeChange()
            else:
                self.calculateChange(int(changeAmount * 100))
        except ValueError:
            invalidNumberHandler()
            return self.makeChange()

    def calculateChange(self, changeAmount):
        changeAmountString = (changeAmount / 100)
        print(f"\nThe amount of change to give is: €{changeAmountString}")
        print("\nThe bills and coins to give are")
        print("-------------------------------")
        for value, name in self.bills + self.coins:
            value = int(value * 100)
            count, changeAmount = divmod(changeAmount, value)
            if count > 0:
                print(int(count), name)