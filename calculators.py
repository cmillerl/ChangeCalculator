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

    def countrySelection(self, country):
        """
        If the country is in the set of countries, the currency symbol, bills, and coins are assigned based on the country.

        Promps the user to select which bills and coins to include in the change calculation with the promptBillsCoins method.

        If the country is not in the set of countries, the user is prompted to try again or exit the program.
        """

        country = country.upper()

        usdCountries = self.countryClass.usdCountries
        euroCountries = self.countryClass.euroCountries
        yenCountries = self.countryClass.yenCountries
        gbpCountries = self.countryClass.gbpCountries

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
