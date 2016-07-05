from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)

class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    points = db.Column(db.Float)
    change = db.Column(db.Float)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('Location', backref='exchange', uselist=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship('Currency', backref='exchange', uselist=False)

    def __init__(self, name, points, change, location, currency):
        self.name = name
        self.points = points
        self.change = change
        self.location = location
        self.currency = currency

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    code = db.Column(db.String(80))
    num_users = db.Column(db.Integer)
    #exchange defined as a backref on currency
    #location defined as a backref on location

    def __init__(self, name, code, num_users):
        self.name = name
        self.code = code
        self.num_users = num_users

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    symbol = db.Column(db.String(80))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('Location', uselist=False)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'))
    exchange = db.relationship('Exchange', uselist=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship('Currency', uselist=False)

    def __init__(self, name, symbol, location, exchange, currency):
        self.name = name
        self.symbol = symbol
        self.location = location
        self.exchange = exchange
        self.currency = currency

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    capital = db.Column(db.String(80))
    gdp = db.Column(db.Float)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship('Currency', backref='location', uselist=False)
    #exchange defined as a backref on exchange

    def __init__(self, name, capital, gdp, currency):
        self.name = name
        self.capital = capital
        self.gdp = gdp
        self.currency = currency
