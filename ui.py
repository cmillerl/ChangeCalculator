from countries import *
from currencies import *
from calculators import *
from time import sleep


class UserInterface:
    def __init__(self):
        self.calc = Calculators()
        self.calc.ui = self
        self.welcomeMessage()

    def welcomeMessage(self):
        print(
            """\nWelcome to the Currency Exchange Calculator.
                 
This tool helps you calculate precise denomination breakdowns for any monetary amount.
Select your country and customize which denominations to include in the calculation.
Multiple international currencies are supported, with regular updates.

Please type the name of a country from the options below to begin. If you want to exit, type 'exit'.\n"""
        )

        countries = sorted(self.calc.countryClass.countries)
        # Sorts the countries alphabetically before iterating through the set.
        for i, country in enumerate(countries):
            formattedCountries = (country.upper() if country == "USA" else country.title())  # fmt: skip
            if i % 10 == 0 and i != 0:
                print("\n")
                print(formattedCountries, end="")
            elif i == 0:
                print(formattedCountries, end="")
            else:
                print(f" | {formattedCountries}", end="")

        try:
            print("\n")
            country = input("Enter a country: ").upper().strip()
            self.calc.countrySelection(country)
        except ValueError:
            invalidInputHandler()
            self.welcomeMessage()

    def promptBillsCoins(self, bills, coins):
        """
        Prompts the user to select which bills and coins to include in the change calculation.

        If the user enters all or makes an invalid selection, all bills and coins are included.

        Parses the user input and adds the selected bills and coins to a dictionary.

        """

        print("\nYou can choose which bills and coins to include in the change calculation.\n")  # fmt: skip
        print("Enter your selection separated by commas or all to include everything.")
        sleep(5)

        print("\nAvailable Bills")
        print("---------------")
        sortedBills = sorted(bills.items(), key=lambda x: float(x[1]), reverse=True)
        for name, value in sortedBills:
            print(f"- {value}")

        print("\nAvailable Coins")
        print("---------------")
        sortedCoins = sorted(coins.items(), key=lambda x: float(x[1]), reverse=True)
        for name, value in sortedCoins:
            print(f" - {value}")

        userInput = (
            input("\nEnter your selection separated by commas or all to include everything: ").strip().lower())  # fmt: skip

        if userInput == "all":
            return bills, coins

        selectedBills = {}
        selectedCoins = {}

        try:
            selectedItems = [
                float(item.strip().replace("$", "")) for item in userInput.split(",")
            ]

            for name, value in bills.items():
                if value in selectedItems:
                    selectedBills[name] = value

            for name, value in coins.items():
                if value in selectedItems:
                    selectedCoins[name] = value

            if not selectedBills and not selectedCoins:
                print("No valid selections made. All bills and coins will be included.")
                return bills, coins

            return selectedBills, selectedCoins
        except ValueError:
            invalidInputHandler()
            return self.promptBillsCoins(bills, coins)

    def promptChangeAmount(self):
        """
        Prompts the user to enter the amount of change to give in decimal form.

        If the input is invalid or less than or equal to zero, the user is prompted to try again.

        Calls the calculateChange method with the change amount in cents rounded to two decimal places * 100.
        """
        try:
            changeAmount = round(float(input(f"\nEnter the amount of change in decimal form: {self.calc.symbol}")), 2)  # fmt: skip
            if changeAmount <= 0:
                invalidInputHandler()
                return self.promptChangeAmount()
            else:
                self.calc.calculateChange(int(changeAmount * 100))
        except ValueError:
            invalidInputHandler()
            return self.promptChangeAmount()
