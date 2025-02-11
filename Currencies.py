class Currencies:
    def __init__(self):

        self.usBills = {"One Hundred Dollars": 100,
                        "Fifty Dollars": 50, 
                        "Twenty Dollars": 20, 
                        "Ten Dollars": 10, 
                        "Five Dollars": 5, 
                        "Dollars": 1}
        
        self.usCoins = {"Quarters": 0.25, 
                        "Dimes": 0.10, 
                        "Nickels": 0.05, 
                        "Pennies": 0.01}
        
        self.usSymbol = "$"

        self.euroBills = {"Five Hundred Euros": 500, 
                          "Two Hundred Euros": 200, 
                          "One Hundred Euros": 100, 
                          "Fifty Euros": 50, 
                          "Twenty Euros": 20, 
                          "Ten Euros": 10, 
                          "Five Euros": 5}
        
        self.euroCoins = {"Two Euro Coins": 2, 
                          "One Euro Coins": 1, 
                          "Fifty Euro Cents": 0.50, 
                          "Twenty Euro Cents": 0.20, 
                          "Ten Euro Cents": 0.10, 
                          "Five Euro Cents": 0.05, 
                          "Two Euro Cents": 0.02, 
                          "One Euro Cents": 0.01}
        
        self.euroSymbol = "€"
