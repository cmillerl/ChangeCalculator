from USA import *
from France import *
from Shared import *
from time import sleep

class Menu:
    def __init__(self):
        self.welcomeMessage()

    def welcomeMessage(self):
        print("""\nWelcome to the Currency Exchange Calculator.
                 
This tool helps you calculate precise denomination breakdowns for any monetary amount.
Select your country and customize which denominations to include in the calculation.
Multiple international currencies are supported, with regular updates.

Please type the name of a country from the options below to begin.\n""")

        for i, country in enumerate(sorted(countries)):
            if i < len(countries) - 1:
                print(country + " | ", end = "")
            else:
                print(country, end = "")    

        try:
            print("\n")
            country = input("Enter a country: ").lower()
            if country == "usa":
                us = USA()
                us.includedBillsMethod()
                us.includedCoinsMethod()
                us.makeChange()
            elif country == "france":
                fr = France()
                fr.includedBillsMethod()
                fr.includedCoinsMethod()
                fr.makeChange()
            elif country == "exit":
                print("Exiting program.")
                exit()
            else:
                print("Invalid country entered. Try again or type 'exit' to quit.")
                sleep(3)
                return self.welcomeMessage()
        except ValueError:
                print("Invalid country entered. Try again or type 'exit' to quit.")
                sleep(3)
                return self.welcomeMessage()
