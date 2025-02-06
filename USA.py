from time import sleep
from Shared import *

countries.append("USA")

class USA:
    def __init__(self):
        self.bills = []
        self.coins = []

    def includedBillsMethod(self):
        try:
            print("Which bills would you like to include for giving change?")
            print("1. All")
            print("2. $1, $5, $10, $20, $50")
            print("3. $1, $5, $10, $20")
            print("4. $1, $5, $10")
            print("5. $1, $5")
            print("6. $1")
            includedBills = int(input("Enter a valid number 1-6: "))
        except ValueError:
            print("Invalid input entered. Exiting program.")
            exit()
            
        if includedBills == 1:
            self.bills = [(100, "Hundred Dollar Bills"), (50, "Fifty Dollar Bills"), (20, "Twenty Dollar Bills"), (10, "Ten Dollar Bills"), (5, "Five Dollar Bills"), (1, "Dollar Bills")]
        elif includedBills == 2:
            self.bills = [(50, "Fifty Dollar Bills"), (20, "Twenty Dollar Bills"), (10, "Ten Dollar Bills"), (5, "Five Dollar Bills"), (1, "Dollar Bills")]
        elif includedBills == 3:
            self.bills = [(20, "Twenty Dollar Bills"), (10, "Ten Dollar Bills"), (5, "Five Dollar Bills"), (1, "Dollar Bills")]
        elif includedBills == 4:
            self.bills = [(10, "Ten Dollar Bills"), (5, "Five Dolla Bills"), (1, "Dollar Bills")]
        elif includedBills == 5:
            self.bills = [(5, "Five Dollar Bills"), (1, "Dollar Bills")]
        elif includedBills == 6:
            self.bills = [(1, "Dollar Bills")]
        else:
            print("Invalid number entered. Exiting program.")
            exit()

    def includedCoinsMethod(self):
        try:
            print("Which coins would you like to include for giving change?")
            print("1. All")
            print("2. Penny, Nickel, Dime")
            print("3. Penny, Nickel")
            print("4. Penny")
            includedCoins = int(input("Enter a valid number 1-4: "))

        except ValueError:
            print("Invalid input entered. Exiting program.")
            exit()

        if includedCoins == 1:
            self.coins = [(0.25, "Quarters"), (0.10, "Dimes"), (0.05, "Nickels"), (0.01, "Pennies")]
        elif includedCoins == 2:
            self.coins = [(0.10, "Dimes"), (0.05, "Nickels"), (0.01, "Pennies")]
        elif includedCoins == 3:
            self.coins = [(0.05, "Nickels"), (0.01, "Pennies")]
        elif includedCoins == 4:
            self.coins = [(0.01, "Pennies")]
        else:
            print("Invalid number entered. Exiting program.")
            exit()

    def makeChange(self):
        try:
            changeAmount = round(float(input("Enter the amount of change in decimal form (example 17.54): ")), 2)
            if changeAmount <= 0:
                print("Invalid input. Would you like to try again or exit?")
                sleep(1)
                userOption = input("Enter 'try' or 'exit': ").lower()
                if userOption == "try":
                    self.makeChange()
                elif userOption == "exit":
                    exit()
                else:
                    print("Invalid input. Exiting program.")
                    exit()
            else:
                self.calculateChange(int(changeAmount * 100))
        except ValueError:
            print("Invalid input. Exiting program.")
            exit()

    def calculateChange(self, changeAmount):
        print("The amount of change to give is: $", changeAmount / 100)
        print("The bills and coins to give are")
        print("_______________________________")
        for value, name in self.bills + self.coins:
            value = int(value * 100)
            count, changeAmount = divmod(changeAmount, value)
            if count > 0:
                print(int(count), name)