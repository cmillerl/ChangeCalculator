class Countries:
    def __init__(self):

        self.countries = set()

        self.usdCountries = {
            "AMERICAN SAMOA",
            "BONAIRE",
            "BRITISH VIRGIN ISLANDS",
            "ECUADOR",
            "EL SALVADOR",
            "GUAM",
            "MARSHALL ISLANDS",
            "MICRONESIA",
            "NORTHERN MARIANA ISLANDS",
            "PALAU",
            "PUERTO RICO",
            "SABA",
            "SINT EUSTATIUS",
            "TIMOR-LESTE",
            "TURKS AND CAICOS",
            "USA",
            "VIRGIN ISLANDS",
        }

        self.euroCountries = {
            "AUSTRIA",
            "BELGIUM",
            "CROATIA",
            "CYPRUS",
            "ESTONIA",
            "FINLAND",
            "FRANCE",
            "GERMANY",
            "GREECE",
            "IRELAND",
            "ITALY",
            "LATVIA",
            "LITHUANIA",
            "LUXEMBOURG",
            "MALTA",
            "NETHERLANDS",
            "PORTUGAL",
            "SLOVAKIA",
            "SLOVENIA",
            "SPAIN",
        }

        self.yenCountries = {"JAPAN"}

        self.gbpCountries = {
            "ASCENSION",
            "BRITISH ANTARCTIC TERRITORY",
            "BRITISH INDIAN OCEAN TERRITORY",
            "EGYPT",
            "FALKLAND ISLANDS",
            "GIBRALTAR",
            "GUERNSEY",
            "ISLE OF MAN",
            "JERSEY",
            "LEBANON",
            "SAINT HELENA",
            "SOUTH GEORGIA",
            "SOUTH SANDWICH ISLANDS",
            "SOUTH SUDAN",
            "SUDAN",
            "SYRIA",
            "TRISTAN DA CUNHA",
            "UK",
        }

        self.rmbCountries = {"CHINA"}

        self.audCountries = {
            "ASHMORE AND CARTIER ISLANDS",
            "AUSTRALIA",
            "AUSTRALIAN ANTARCTIC TERRITORY",
            "CHRISTMAS ISLAND",
            "COCOS ISLANDS",
            "CORAL SEA ISLANDS",
            "HEARD ISLAND",
            "KIRIBATI",
            "MCDONALD ISLANDS",
            "NAURU",
            "NORFOLK ISLAND",
        }

        self.cadCountries = {"CANADA"}

        # Adds all countries to the set.
        self.countries.update(self.usdCountries)
        self.countries.update(self.euroCountries)
        self.countries.update(self.yenCountries)
        self.countries.update(self.gbpCountries)
        self.countries.update(self.rmbCountries)
        self.countries.update(self.audCountries)
        self.countries.update(self.cadCountries)
