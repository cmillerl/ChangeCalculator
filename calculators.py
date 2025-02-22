from countries import *
from currencies import *
from utils import *
from time import sleep


class Calculators:
    def __init__(self):
        self.countryClass = Countries()
        self.currencyClass = Currencies()
        self.symbol = None
        self.bills = {}
        self.coins = {}

    def countrySelection(self):
        """
        If the country is in the set of countries, the currency symbol, bills, and coins are assigned based on the country.

        Promps the user to select which bills and coins to include in the change calculation with the promptBillsCoins method.

        If the country is not in the set of countries, the user is prompted to try again or exit the program.
        """

        countries = sorted(self.countryClass.countries)
        print()
        # Sorts the countries alphabetically before iterating through the set.
        for i, country in enumerate(countries):
            formattedCountries = (country.upper() if country in {"USA", "UK"} else country.title())  # fmt: skip
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
        except ValueError:
            invalidInputHandler()
            self.countrySelection()

        usdCountries = self.countryClass.usdCountries
        euroCountries = self.countryClass.euroCountries
        yenCountries = self.countryClass.yenCountries
        gbpCountries = self.countryClass.gbpCountries
        rmbCountries = self.countryClass.rmbCountries
        audCountries = self.countryClass.audCountries
        cadCounrties = self.countryClass.cadCountries

        if country.lower() == "exit":
            print("Exiting program...")
            exit()

        if country not in self.countryClass.countries:
            invalidInputHandler()
            self.ui.welcomeMessage()

        if country in usdCountries:
            self.symbol = self.currencyClass.usdSymbol
            self.bills = self.currencyClass.usdBills
            self.coins = self.currencyClass.usdCoins
        elif country in euroCountries:
            self.symbol = self.currencyClass.euroSymbol
            self.bills = self.currencyClass.euroBills
            self.coins = self.currencyClass.euroCoins
        elif country in yenCountries:
            self.symbol = self.currencyClass.yenSymbol
            self.bills = self.currencyClass.yenBills
            self.coins = self.currencyClass.yenCoins
        elif country in gbpCountries:
            self.symbol = self.currencyClass.gbpSymbol
            self.bills = self.currencyClass.gbpBills
            self.coins = self.currencyClass.gbpCoins
        elif country in rmbCountries:
            self.symbol = self.currencyClass.rmbSymbol
            self.bills = self.currencyClass.rmbBills
            self.coins = self.currencyClass.rmbCoins
        elif country in audCountries:
            self.symbol = self.currencyClass.audSymbol
            self.bills = self.currencyClass.audBills
            self.coins = self.currencyClass.audCoins
        elif country in cadCounrties:
            self.symbol = self.currencyClass.cadSymbol
            self.bills = self.currencyClass.cadBills
            self.coins = self.currencyClass.cadCoins

        selectedBills, selectedCoins = self.ui.promptBillsCoins(self.bills, self.coins)  # fmt: skip
        self.bills = selectedBills
        self.coins = selectedCoins
        self.ui.promptChangeAmount()

    def currencySelection(self):
        """
        Prompts the user to select a currency from the available options.

        If the user enters an invalid selection, the user is prompted to try again or exit the program.
        """

        print()
        print("You can choose from the following currencies")
        print("--------------------------------------------")
        currencies = list(sorted(self.currencyClass.currencies))
        for i, currency in enumerate(currencies):
            if i == len(currencies) - 1:
                print(currency.upper())
            else:
                print(currency.upper(), end=" | ")

        try:
            print()
            selectedCurrency = input(str("Enter a currency: ")).upper().strip()
        except ValueError:
            invalidInputHandler()
            self.currencySelection()

        if selectedCurrency not in self.currencyClass.currencies:
            invalidInputHandler()
            self.currencySelection()

        if selectedCurrency == "USD":
            self.symbol = self.currencyClass.usdSymbol
            self.bills = self.currencyClass.usdBills
            self.coins = self.currencyClass.usdCoins
        elif selectedCurrency == "EURO":
            self.symbol = self.currencyClass.euroSymbol
            self.bills = self.currencyClass.euroBills
            self.coins = self.currencyClass.euroCoins
        elif selectedCurrency == "YEN":
            self.symbol = self.currencyClass.yenSymbol
            self.bills = self.currencyClass.yenBills
            self.coins = self.currencyClass.yenCoins
        elif selectedCurrency == "GBP":
            self.symbol = self.currencyClass.gbpSymbol
            self.bills = self.currencyClass.gbpBills
            self.coins = self.currencyClass.gbpCoins
        elif selectedCurrency == "RMB":
            self.symbol = self.currencyClass.rmbSymbol
            self.bills = self.currencyClass.rmbBills
            self.coins = self.currencyClass.rmbCoins
        elif selectedCurrency == "AUD":
            self.symbol = self.currencyClass.audSymbol
            self.bills = self.currencyClass.audBills
            self.coins = self.currencyClass.audCoins
        elif selectedCurrency == "CAD":
            self.symbol = self.currencyClass.cadSymbol
            self.bills = self.currencyClass.cadBills
            self.coins = self.currencyClass.cadCoins
            

        selectedBills, selectedCoins = self.ui.promptBillsCoins(self.bills, self.coins)  # fmt: skip
        self.bills = selectedBills
        self.coins = selectedCoins
        self.ui.promptChangeAmount()

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

    def userSelection(self):
        """
        Prompts the user to select a country or currency.

        If the user enters an invalid selection, the user is prompted to try again or exit the program.
        """

        print("You can choose from the following options")
        print("-----------------------------------------")
        print("1. Select a country")
        print("2. Select a currency")

        try:
            print()
            selection = input("Enter 1 or 2: ").strip()
            if selection == "1":
                self.countrySelection()
            elif selection == "2":
                self.currencySelection()
            else:
                invalidInputHandler()
                self.userSelection()
        except ValueError:
            invalidInputHandler()
            self.userSelection()
