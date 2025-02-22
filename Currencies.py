class Currencies:
    def __init__(self):

        self.currencies = {"USD", "EURO", "YEN", "GBP"}

        self.usdBills = {
            "One Hundred Dollars": 100,
            "Fifty Dollars": 50,
            "Twenty Dollars": 20,
            "Ten Dollars": 10,
            "Five Dollars": 5,
            "Dollars": 1,
        }

        self.usdCoins = {
            "Quarters": 0.25,
            "Dimes": 0.10,
            "Nickels": 0.05,
            "Pennies": 0.01,
        }

        self.usdSymbol = "$"

        self.euroBills = {
            "Five Hundred Euros": 500,
            "Two Hundred Euros": 200,
            "One Hundred Euros": 100,
            "Fifty Euros": 50,
            "Twenty Euros": 20,
            "Ten Euros": 10,
            "Five Euros": 5,
        }

        self.euroCoins = {
            "Two Euro Coins": 2,
            "One Euro Coins": 1,
            "Fifty Euro Cents": 0.50,
            "Twenty Euro Cents": 0.20,
            "Ten Euro Cents": 0.10,
            "Five Euro Cents": 0.05,
            "Two Euro Cents": 0.02,
            "One Euro Cents": 0.01,
        }

        self.euroSymbol = "€"

        self.yenBills = {
            "Ten Thousand Yen Notes": 10000,
            "Five Thousand Yen Notes": 5000,
            "Two Thousand Yen Notes": 2000,
            "One Thousand Yen Notes": 1000,
        }

        self.yenCoins = {
            "Five Hundred Yen Bicolor Clad Coins": 500,
            "Hundred Yen Cupro-Nickel Coins": 100,
            "Fifty Yen Cupro-Nickel Coins": 50,
            "Ten Yen Bronze Coins": 10,
            "Five Yen Brass Coins": 5,
            "One Yen Aluminum Coins": 1,
        }

        self.yenSymbol = "¥"

        self.gbpBills = {
            "One Hundred Pounds": 100,
            "Fifty Pounds": 50,
            "Twenty Pounds": 20,
            "Ten Pounds": 10,
            "Five Pounds": 5,
            "One Pounds": 1,
        }

        self.gbpCoins = {
            "Two Pounds": 2,
            "Fifty Pences": 0.50,
            "Twenty Pences": 0.20,
            "Ten Pences": 0.10,
            "Five Pences": 0.05,
            "Two Pences": 0.02,
            "One Pences": 0.01,
        }

        self.gbpSymbol = "£"
