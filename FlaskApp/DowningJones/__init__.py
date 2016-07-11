from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import subprocess

app = Flask ( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy(app)

from models import *

@app.route ( '/' )
def homepage ():
	return render_template('index.html',
							title='Downing Jones')

@app.route ( '/index' )
def index ():
	return render_template('index.html',
						    title='Downing Jones')

@app.route ( '/about' )
def about ():
	return render_template('about.html',
                            title='About')

@app.route ( '/companies' )
def companies ():
    companies = Company.query.distinct(Company.symbol)
    return render_template('companies.html',
                            title='Companies',
                            companies=companies)

@app.route ( '/companies/<id>' )
def company (id):
    company = Company.query.get(id)
    return render_template('company.html',
                            title=company.name,
                            company=company)

@app.route ( '/currencies' )
def currencies ():
	currencies = Currency.query.distinct(Currency.currency)
	return render_template('currencies.html',
							title='Currencies',
							currencies=currencies)

@app.route ( '/currencies/<id>' )
def currency (id):
    currency = Currency.query.get(id)
    return render_template('currency.html',
                            title=currency.name,
                            currency=currency)

@app.route ( '/locations' )
def locations ():
	locations = Location.query.distinct(Location.name)
	return render_template('locations.html',
						    title='Locations',
						    locations=locations)

@app.route ( '/locations/<id>' )
def location (id):
    location = Location.query.get(id)
    return render_template('location.html',
                            title=location.name,
                            location=location)

@app.route ( '/stockmarkets' )
def stockmarkets ():
	markets = Exchange.query.distinct(Exchange.name)
	return render_template('stockmarkets.html',
							title='Exchanges',
							markets=markets)

@app.route ( '/stockmarkets/<id>' )
def market (id):
    market = Exchange.query.get(id)
    return render_template('stockmarket.html',
                            title=market.name,
                            market=market)

@app.route ( '/api/run_tests')
def tests ():
    try:
        process = subprocess.Popen(['python3', '/var/www/FlaskApp/DowningJones/tests.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate()
        return str({'out': str(out), 'err': str(err)})
    except Exception as exc:
        return str(exc)
