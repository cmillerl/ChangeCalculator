class Countries:
    def __init__(self):
        
        self.countries = {"USA"}
        
        self.euroCountries = {"FRANCE", "GERMANY", "ITALY", "PORTUGAL", "SPAIN", 
                          "IRELAND", "AUSTRIA", "BELGIUM", "CYPRUS", "ESTONIA", "FINLAND", 
                          "GREECE", "LATVIA", "LITHUANIA", "LUXEMBOURG", "MALTA", "NETHERLANDS", 
                          "SLOVAKIA", "SLOVENIA", "CROATIA"}
        
        self.countries.update(self.euroCountries)