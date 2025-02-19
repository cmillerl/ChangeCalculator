class Countries:
    def __init__(self):
        
        self.countries = set()

        self.usdCountries = {"USA", "PUERTO RICO", "GUAM", "AMERICAN SAMOA", "NORTHERN MARIANA ISLANDS", 
                             "VIRGIN ISLANDS", "TURKS AND CAICOS", "BRITISH VIRGIN ISLANDS", "ECUADOR", 
                             "EL SALVADOR", "TIMOR-LESTE", "PALAU", "MICRONESIA", "MARSHALL ISLANDS", "BONAIRE",
                             "SINT EUSTATIUS", "SABA"}
        
        self.euroCountries = {"FRANCE", "GERMANY", "ITALY", "PORTUGAL", "SPAIN", 
                          "IRELAND", "AUSTRIA", "BELGIUM", "CYPRUS", "ESTONIA", "FINLAND", 
                          "GREECE", "LATVIA", "LITHUANIA", "LUXEMBOURG", "MALTA", "NETHERLANDS", 
                          "SLOVAKIA", "SLOVENIA", "CROATIA"}
        
        self.yenCountries = {"JAPAN"}

        self.gbpCountries = {"UK", "BRITISH ANTARCTIC TERRITORY", "BRITISH INDIAN OCEAN TERRITORY", "EGYPT",
                            "FALKLAND ISLANDS", "GIBRALTAR", "GUERNSEY", "ISLE OF MAN", "JERSEY", 
                            "LEBANON", "SAINT HELENA", "ASCENSION", "SOUTH GEORGIA", "SOUTH SANDWICH ISLANDS",
                            "SOUTH SUDAN", "SUDAN", "SYRIA", "TRISTAN DA CUNHA"}

        #Adds all countries to the set.
        self.countries.update(self.usdCountries)
        self.countries.update(self.euroCountries)
        self.countries.update(self.yenCountries)
        self.countries.update(self.gbpCountries)