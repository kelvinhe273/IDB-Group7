import os
import requests
from flask import Flask, render_template, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import subprocess

app = Flask ( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
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
        
        return str(out) + str(err)
    except Exception as exc:
        return str(exc)

@app.route ('/api/exchange/<int:id>', methods=['GET'])
def get_exchange(id):
    market = Exchange.query.get(id)
    return jsonify(id = id,
                   name = market.name, 
                   name_code = market.exchange,
                   market_cap = market.market_cap_exchange,
                   location = market.location,
                   currency = market.currency)

@app.route ('/api/location/<int:id>', methods=['GET'])
def get_location(id):
    location = Location.query.get(id)
    return jsonify(id = id,
                   name = location.name, 
                   iso = location.iso,
                   capital = location.capital,
                   GDP = location.gdp,
                   location = location.location_exchange,
                   currency = location.currency)

@app.route ('/api/currency/<int:id>', methods=['GET'])
def get_currency(id):
    currency = Currency.query.get(id)
    return jsonify(id = id,
                   name = currency.name, 
                   exchange_rate = currency.exchange_rate,
                   exchanges = currency.exchanges,
                   locations = currency.locations,
                   currency = currency.currency)

@app.route ('/api/company/<int:id>', methods=['GET'])
def get_company(id):
    company = Company.query.get(id)
    return jsonify(id = id,
                   name = company.name, 
                   symbol = company.symbol,
                   exchange = company.exchange,
                   location = company.location,
                   open_price = company.open_price,
                   previous_price = company.previous_price,
                   percent_change = company.percent_change,
                   year_high = company.year_high,
                   ask_price = company.ask_price,
                   eps = company.eps,
                   peg = company.peg,
                   days_range = company.days_range,
                   percent_change_fifty = company.percent_change_fifty,
                   percent_change_twohundred = company.percent_change_twohundred,
                   volume = company.volume,
                   avg_volume = company.avg_volume,
                   market_cap = company.market_cap)


"""
Minor routing changes for POST request
"""

@app.route ('/search', methods=['GET', 'POST'])
def search ():
    queries = {}
    hackString = ""
    url = request.form['url']
    thisString = url.split('=')
    # index = 0
    # for x in thisString:
    #   hackString += thisString[index]
    #   index = index + 1
    # hackString = hackString.split(" ")
    queries = thisString
    # index2 = 0
    for i in queries:
      search_query1 = Location.query.filter(or_(Location.name.contains(queries[0]),Location.iso.contains(queries[0]), Location.capital.contains(queries[0]),Location.gdp.contains(queries[0]),Location.currency.contains(queries[0]), Location.location_exchange.contains(queries[0])))
      search_query2 = Exchange.query.filter(or_(Exchange.exchange.contains(queries[0]),Exchange.name.contains(queries[0]),Exchange.market_cap_exchange.contains(queries[0]),Exchange.currency.contains(queries[0]),Exchange.location.contains(queries[0])))
      search_query3 = Currency.query.filter(or_(Currency.name.contains(queries[0]),Currency.currency.contains(queries[0]),Currency.locations.contains(queries[0]),Currency.exchanges.contains(queries[0]), Currency.exchange_rate.contains(queries[0])))
      search_query4 = Company.query.filter(or_(Company.symbol.contains(queries[0]),Company.name.contains(queries[0]),Company.exchange.contains(queries[0]),Company.currency.contains(queries[0]),Company.location.contains(queries[0]),Company.open_price.contains(queries[0]),Company.previous_price.contains(queries[0]),Company.percent_change.contains(queries[0]),Company.year_high.contains(queries[0]),Company.ask_price.contains(queries[0]),Company.eps.contains(queries[0]),Company.peg.contains(queries[0]),Company.percent_change_fifty.contains(queries[0]),Company.volume.contains(queries[0]),Company.avg_volume.contains(queries[0]),Company.market_cap.contains(queries[0])))
    return render_template('search.html',  queries = queries, queries1 = search_query1, queries2= search_query2, queries3 =search_query3, queries4 = search_query4 ,title="Search")