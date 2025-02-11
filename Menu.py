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
            print("Invalid country entered. Try again or type 'exit' to quit.")
            sleep(3)
            self.welcomeMessage()

    def countrySelection(self, country):
        country = country.upper()

        symbol = None
        bills = {}
        coins = {}

        usdCountries = self.countryClass.usdCountries
        euroCountries = self.countryClass.euroCountries
    
        if country in self.countryClass.countries:
            if country in usdCountries:
                symbol = self.currencyClass.usSymbol
                bills = self.currencyClass.usBills
                coins = self.currencyClass.usCoins
            elif country in euroCountries:
                symbol = self.currencyClass.euroSymbol
                bills = self.currencyClass.euroBills
                coins = self.currencyClass.euroCoins
        
            selectedBills, selectedCoins = self.promptBillsCoins(bills, coins)
            converter = CurrencyConverter(symbol, selectedBills, selectedCoins)
            converter.makeChange()

        elif country.lower() == "exit":
            print("Exiting program.")
            exit()
        else:
            print("Invalid country entered. Try again or type 'exit' to quit.")
            sleep(3)
            self.welcomeMessage()

    def promptBillsCoins(self, bills, coins):
        print("\nYou can choose which bills and coins to include in the change calculation.")
        print("Type 'all' to include everything, or type specific bill/coin names separated by commas.")
        sleep(3)

        print("\nAvailable Bills:")
        for bill in bills.keys():
            print(f"- {bill}")

        print("\nAvailable Coins:")
        for coin in coins.keys():
            print(f"- {coin}")

        userInput = input("\nEnter your selection separated by commas or 'all' to include everything: ").strip().lower()

        if userInput == "all":
            return bills, coins

        selectedBills = {}
        selectedCoins = {}

        selectedItems = [item.strip().title() for item in userInput.split(",")]

        for bill in bills:
            if bill.title() in selectedItems:
                selectedBills[bill] = bills[bill]

        for coin in coins:
            if coin.title() in selectedItems:
                selectedCoins[coin] = coins[coin]

        if not selectedBills and not selectedCoins:
            print("No valid selections made. All bills and coins will be included.")
            return bills, coins

        return selectedBills, selectedCoins
