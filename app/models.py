from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

class Market(db.Model):
    id = db.Column(db.Integer, primary_ky=True)
    name = db.Column(db.String(80))
    #location
    #currency

    def __init__(self, name, location, currency):
        self.name = name
        self.location = location
        self.currency = currency

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80)
    #exchange
    #location

    def __init__(self, type, exchange, location):
        self.type = type
        self.exchange = exchange
        self.location = location

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #location
    #exchange
    #currency

    def __init__(self, location, exchange, currency):
        self.location = location
        self.exchange = exchange
        self.currency = currency

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    #exchange
    #currency

    def __init__(self, name, exchange, currency):
        self.name = name
        self.exchange = exchange
        self.currency = currency
