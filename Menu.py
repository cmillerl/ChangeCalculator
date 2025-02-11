from Countries import *
from Currencies import *
from CurrencyConverter import *
from time import sleep

class Menu:
    def __init__(self):
        self.countryClass = Countries()
        self.currencyClass = Currencies()
        self.welcomeMessage()

    def welcomeMessage(self):
        print("""\nWelcome to the Currency Exchange Calculator.
                 
This tool helps you calculate precise denomination breakdowns for any monetary amount.
Select your country and customize which denominations to include in the calculation.
Multiple international currencies are supported, with regular updates.

Please type the name of a country from the options below to begin. If you want to exit, type 'exit'.\n""")
        
        countries = sorted(self.countryClass.countries)
        print("\n".join(country.upper() if country == "USA" else country.title() for country in countries), end="")

        try:
            print("\n")
            country = input("Enter a country: ").upper()
            self.countrySelection(country)
        except ValueError:
            invalidHandler()
            self.welcomeMessage()

    def countrySelection(self, country):
        country = country.upper()

        symbol = None
        bills = {}
        coins = {}

        usdCountries = self.countryClass.usdCountries
        euroCountries = self.countryClass.euroCountries
        yenCountries = self.countryClass.yenCountries
    
        if country.lower() == "exit":
            print("Exiting program...")
            exit()
        elif country in self.countryClass.countries:
            if country in usdCountries:
                symbol = self.currencyClass.usdSymbol
                bills = self.currencyClass.usdBills
                coins = self.currencyClass.usdCoins
            elif country in euroCountries:
                symbol = self.currencyClass.euroSymbol
                bills = self.currencyClass.euroBills
                coins = self.currencyClass.euroCoins
            elif country in yenCountries:
                symbol = self.currencyClass.yenSymbol
                bills = self.currencyClass.yenBills
                coins = self.currencyClass.yenCoins
        
            selectedBills, selectedCoins = self.promptBillsCoins(bills, coins)
            converter = CurrencyConverter(symbol, selectedBills, selectedCoins)
            converter.makeChange()
        else:
            invalidHandler()
            self.welcomeMessage()

    def promptBillsCoins(self, bills, coins):
        print("\nYou can choose which bills and coins to include in the change calculation.\n")
        print("Enter your selection separated by commas or all to include everything.")
        sleep(5)

        print("\nAvailable Bills")
        print("---------------")
        sortedBills = sorted(bills.items(), key = lambda x: float(x[1]), reverse = True)
        for name, value in sortedBills:
            print(f"- {value}")

        print("\nAvailable Coins")
        print("---------------")
        sortedCoins = sorted(coins.items(), key = lambda x: float(x[1]), reverse = True)
        for name, value in sortedCoins:
            print(f" - {value}")

        userInput = input("\nEnter your selection separated by commas or all to include everything: ").strip().lower()

        if userInput == "all":
            return bills, coins

        selectedBills = {}
        selectedCoins = {}

        try:
            selectedItems = [float(item.strip().replace("$", "")) for item in userInput.split(",")]

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
            invalidHandler()
            return self.promptBillsCoins(bills, coins)