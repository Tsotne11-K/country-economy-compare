class CountryEconomy:
    def __init__(self):
        self.data = {
            "Georgia": 15000,  
            "France": 2600000,
            "Italy": 2000000,
            "Spain": 1400000
        }

        self.currency_rates = {
            "Georgia": 2.7,    
            "France": 0.85,   
            "Italy": 0.85,    
            "Spain": 0.85     
        self.currency_names = {
            "Georgia": "GEL",
            "France": "EUR",
            "Italy": "EUR",
            "Spain": "EUR"
        }

    def convert_amount(self, amount, from_country, to_country):
    
        rate_from = self.currency_rates.get(from_country, 1)
        rate_to = self.currency_rates.get(to_country, 1)

        amount_in_usd = amount / rate_from
        amount_in_to_currency = amount_in_usd * rate_to
        return round(amount_in_to_currency, 2), self.currency_names[to_country]

    def compare(self, country1, country2):
        gdp1 = self.data.get(country1, 0)
        gdp2 = self.data.get(country2, 0)
        if gdp1 > gdp2:
            return f"{country1} ეკონომიკურად ძლიერია ვიდრე {country2}.\n({gdp1} მლნ USD vs {gdp2} მლნ USD)"
        elif gdp2 > gdp1:
            return f"{country2} ეკონომიკურად ძლიერია ვიდრე {country1}.\n({gdp2} მლნ USD vs {gdp1} მლნ USD)"
        else:
            return f"{country1} და {country2} ეკონომიკურად თანაბარი არიან.\n({gdp1} მლნ USD)"
