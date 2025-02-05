from USA import *
from Shared import *
from time import sleep

class Menu:
    def __init__(self):
        self.welcomeMessage()

    def welcomeMessage(self):
        print("\nWelcome to the Change Making Program!")
        print("This program will allow you to make change for any amount of money.")
        print("You can choose which bills and coins you would like to include.")
        print("You can also select a variety of countries (to be added in the future).")
        print("Enter a country to get started as displayed below.\n")

        for i, country in enumerate(countries):
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
            else:
                print("Invalid country entered. Goodbye.")
                exit()
        except ValueError:
            print("Invalid country entered. Goodbye.")
            exit()
