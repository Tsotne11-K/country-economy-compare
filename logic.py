class CountryEconomy:
    def __init__(self):
        # ეკონომიკური მონაცემები და ვალუტები (USD-ში ეკონომიკა და ვალუტის კურსები)
        self.data = {
            "Georgia": 15000,  # GDP in millions USD
            "France": 2600000,
            "Italy": 2000000,
            "Spain": 1400000
        }
        # ვალუტის კურსი USD-სთან მიმართებით (1 USD = x VAL)
        self.currency_rates = {
            "Georgia": 2.7,    # GEL to USD: 1 GEL = 0.37 USD -> USD to GEL = 2.7
            "France": 0.85,   # EUR, 1 USD = 0.85 EUR
            "Italy": 0.85,    # same EUR zone
            "Spain": 0.85     # same EUR zone
        }
        # ვალუტის სახელები
        self.currency_names = {
            "Georgia": "GEL",
            "France": "EUR",
            "Italy": "EUR",
            "Spain": "EUR"
        }

    def convert_amount(self, amount, from_country, to_country):
        # გადაქცევა USD-ში
        rate_from = self.currency_rates.get(from_country, 1)
        rate_to = self.currency_rates.get(to_country, 1)
        # amount კონვერტაცია USD-ში, მერე to_country ვალუტაში
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
