from flask import Flask
from __init__ import db

class Exchange(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String(80))
    name = db.Column(db.String(80))
    market_cap_exchange = db.Column(db.String(80))
    currency = db.Column(db.String(80))
    location = db.Column(db.String(80))
    # location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    # location = db.relationship('Location', uselist=False)
    # currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))

    def __init__(self, name, name_code, currency, location, market_cap):
        """
        self.name the name of the Exchange
        self.name_code the three letter symbol for the exchange
        self.market_cap the market cap of the exchange
        self.location the location of the Exchange
        self.currency the currency the Exchange uses
        """
        self.name = name
        self.name_code = name_code
        self.market_cap = market_cap
        self.location = location
        self.currency = currency

    def __repr__(self):
        """
        returns the Exchange's self.name attribute
        """
        return '<Exchange %r>' % self.name

class Currency(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)    #pk can be the iso code
    name = db.Column(db.String(80))
    currency = db.Column(db.String(80))
    locations = db.Column(db.String(80))
    exchanges = db.Column(db.String(80))
    exchange_rate = db.Column(db.Integer)
    # exchanges = db.relationship('Exchange', backref='currency', lazy='dynamic')
    # locations = db.relationship('Location', backref='currency', lazy='dynamic')

    def __init__(self, name, code, locations, exchanges, exchange_rate):
        """
        self.locations the location of all relevant countries
        self.name the name of the currency type
        self.code the currency code
        self.exchanges the relevant exchanges that use this currency
        self.exchange_rate is the exchange rate compared to the USD
        """
        self.locations = locations
        self.name = name
        self.code = code
        self.exchanges = exchanges
        self.exchange_rate = exchange_rate

    def __repr__(self):
        """
        returns the Currency's self.name attribute
        """
        return '<Currency %r>' % self.name

class Company(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(80))
    name = db.Column(db.String(80))
    exchange = db.Column(db.String(80))
    currency = db.Column(db.String(80))
    location = db.Column(db.String(80))
    open_price = db.Column(db.String(80))
    previous_price = db.Column(db.String(80))
    percent_change = db.Column(db.String(80))
    year_high = db.Column(db.String(80))
    ask_price = db.Column(db.String(80))
    eps = db.Column(db.String(80))
    peg = db.Column(db.String(80))
    days_range = db.Column(db.String(80))
    percent_change_fifty = db.Column(db.String(80))
    percent_change_twohundred = db.Column(db.String(80))
    volume = db.Column(db.String(80))
    avg_volume = db.Column(db.String(80))
    market_cap = db.Column(db.String(80))
    foreign_id = db.Column(db.Integer)
    # location_id = db.Column(db.Integer, db.ForeignKey('foreign_id'))
    # location = db.relationship('Location', uselist=False)
    # location_name = location.Location.name
    # exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'))
    # exchange = db.relationship('Exchange', uselist=False)
    # currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    # currency = db.relationship('Currency', uselist=False)

    def __init__(self, symbol, name, exchange, currency, location, open_price, 
        prev_price, percent_change, year_high, ask_price, eps, peg, days_range, 
        percent_change_fifty, percent_change_twohundred, volume, avg_volume, market_cap):
        """
        self.name the name of the Company
        self.symbol the symbol of the Company
        self.location the location of the Company
        self.currency the currecny the Company uses
        self.open_price the open price for that stock that day
        self.prev_price th eclosing price of that stock the previous day
        self.percent_change the percent it has changed today
        self.year_high the highest p[rice of the year for that stock
        self.ask_price the asking price for that stock
        self.eps the eps for that stock
        self.peg the peg for that stock
        self.days_range the range of days for info about that stock
        self.percent_change_fifty the percent change in fifty days for that stock
        self.percent_change_twohundred the percent change in 200 days for that stock
        self.volume  the volume for that stock
        self.avg_volume the average volume for that stock
        self.market_cap the market capitalization for that stock

        """
        self.name = name
        self.symbol = symbol
        self.location = location
        self.exchange = exchange
        self.currency = currency
        self.open_price = open_price
        self.prev_price = prev_price
        self.percent_change = percent_change
        self.year_high = year_high
        self.ask_price = ask_price
        self.eps = eps
        self.peg = peg
        self.days_range = days_range
        self.percent_change_fifty = percent_change_fifty
        self.percent_change_twohundred = percent_change_twohundred
        self.volume = volume
        self.avg_volume = avg_volume
        self.market_cap = market_cap

    def __repr__(self):
        """
        returns the Company's self.name attribute
        """
        return '<Company %r>' % self.name

class Location(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)        #pk can be the iso code
    name = db.Column(db.String(80))
    iso = db.Column(db.String(2))
    capital = db.Column(db.String(80))
    gdp = db.Column(db.String(80))
    currency = db.Column(db.String(80))
    location_exchange = db.Column(db.String(80))

    def __init__(self, name, iso, capital, gdp, currency, location_exchange):
        """
        self.iso the two letter id for the country of the location
        self.name the name (country) of the location
        self.capital the capital of the location
        self.gdp the GDP(Nominal) of the location
        self.currency the currency of the location
        """
        self.iso = iso
        self.name = name
        self.capital = capital
        self.gdp = gdp
        self.currency = currency
        self.location_exchange = location_exchange

    def __repr__(self):
        """
        returns the location's self.name attribute
        """
        return '<Location %r>' % self.name
