class Countries:
    def __init__(self):
        
        self.countries = {"EXIT"}

        self.usdCountries = {"USA", "PUERTO RICO", "GUAM", "AMERICAN SAMOA", "NORTHERN MARIANA ISLANDS", 
                             "VIRGIN ISLANDS", "TURKS AND CAICOS", "BRITISH VIRGIN ISLANDS", "ECUADOR", 
                             "EL SALVADOR", "TIMOR-LESTE", "PALAU", "MICRONESIA", "MARSHALL ISLANDS", "BONAIRE",
                             "SINT EUSTATIUS", "SABA"}
        
        self.euroCountries = {"FRANCE", "GERMANY", "ITALY", "PORTUGAL", "SPAIN", 
                          "IRELAND", "AUSTRIA", "BELGIUM", "CYPRUS", "ESTONIA", "FINLAND", 
                          "GREECE", "LATVIA", "LITHUANIA", "LUXEMBOURG", "MALTA", "NETHERLANDS", 
                          "SLOVAKIA", "SLOVENIA", "CROATIA"}
        
        self.countries.update(self.usdCountries)
        self.countries.update(self.euroCountries)