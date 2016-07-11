from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
db = SQLAlchemy(app)

class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    points = db.Column(db.Float)
    change = db.Column(db.Float)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    # location = db.relationship('Location', uselist=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))

    def __init__(self, name, name_code, change, location, currency):
        """
        self.name the name of the Exchange
        self.points the point change of the Exchange
        self.change the change in percentage of the Exchange
        self.location the location of the Exchange
        self.currency the currency the Exchange uses
        """
        self.name = name
        self.name_code = name_code
        self.change = change
        self.location = location
        self.currency = currency

    def __repr__(self):
        """
        returns the Exchange's self.name attribute
        """
        return '<Exchange %r>' % self.name

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)    #pk can be the iso code
    iso = db.Column(db.String(3))
    name = db.Column(db.String(80))
    code = db.Column(db.String(80))
    num_users = db.Column(db.Integer)
    exchanges = db.relationship('Exchange', backref='currency', lazy='dynamic')
    locations = db.relationship('Location', backref='currency', lazy='dynamic')

    def __init__(self, name, code, num_users):
        """
        self.iso the three letter id for the currency
        self.name the name of the currency type
        self.code the currency code
        self.num_users the number of countries that use this currency
        """
        self.iso = iso
        self.name = name
        self.code = code
        self.num_users = num_users

    def __repr__(self):
        """
        returns the Currency's self.name attribute
        """
        return '<Currency %r>' % self.name

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    symbol = db.Column(db.String(80))
    open_price = db.Column(db.String(80))
    prev_price = db.Column(db.String(80))
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
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('Location', uselist=False)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'))
    exchange = db.relationship('Exchange', uselist=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship('Currency', uselist=False)

    def __init__(self, name, symbol, location, exchange, currency, open_price, prev_price, percent_change, year_high, ask_price, eps, peg, days_range, percent_change_fifty, percent_change_twohundred, volume, avg_volume, market_cap):
        """
        self.name the name of the Company
        self.symbol the symbol of the Company
        self.location the location of the Company
        self.currency the currecny the Company uses
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
    id = db.Column(db.Integer, primary_key=True)        #pk can be the iso code
    iso = db.Column(db.String(2))
    name = db.Column(db.String(80))
    capital = db.Column(db.String(80))
    gdp = db.Column(db.Float)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    exchanges = db.relationship('Exchange', backref='location', lazy='dynamic')

    def __init__(self, name, capital, gdp, currency):
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

    def __repr__(self):
        """
        returns the location's self.name attribute
        """
        return '<Location %r>' % self.name
