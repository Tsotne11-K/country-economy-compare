class CountryEconomy:
    def __init__(self):
        self.data = {
            "Georgia": 15000,
            "France": 2600000,
            "Italy": 2000000,
            "Spain": 1400000
        }

    def compare(self, country1, country2):
        gdp1 = self.data.get(country1, 0)
        gdp2 = self.data.get(country2, 0)
        if gdp1 > gdp2:
            return f"{country1} ეკონომიკურად ძლიერია ვიდრე {country2}.\n({gdp1} მლნ USD vs {gdp2} მლნ USD)"
        elif gdp2 > gdp1:
            return f"{country2} ეკონომიკურად ძლიერია ვიდრე {country1}.\n({gdp2} მლნ USD vs {gdp1} მლნ USD)"
        else:
            return f"{country1} და {country2} ეკონომიკურად თანაბარი არიან.\n({gdp1} მლნ USD)"

