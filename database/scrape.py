import requests
import json
import sqlite3
import csv

endpoints = ['Symbol', 'Name', ' Exchange', 'Currency']
base_url = "http://dev.markitondemand.com/Api/v2/"
lookup_url = base_url + "Lookup/"
quote_url = base_url + "Quote/"

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Company')
cur.execute('CREATE TABLE Company (symbol TEXT, name TEXT, exchange TEXT, currency TEXT)')

cur.execute('DROP TABLE IF EXISTS Exchange')
cur.execute('CREATE TABLE Exchange (exchange TEXT, currency TEXT)')

cur.execute('DROP TABLE IF EXISTS Location')
cur.execute('CREATE TABLE Location (currency TEXT)')

cur.execute('DROP TABLE IF EXISTS Currency')
cur.execute('CREATE TABLE Currency (currency TEXT)')


f = open('yahoo.csv')
csv_f = csv.reader(f)
for row in csv_f:
	source = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22' +row[0] +'%22)&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&format=json'


	resp = requests.get(source)
	# print(resp.text)
	symbol = resp.json()['query']['results']['quote']['symbol']
	#print(symbol)
	name = resp.json()['query']['results']['quote']['Name']
	exchange =  resp.json()['query']['results']['quote']['StockExchange']
	if exchange == "NMS":
		exchange = "NYSE"
	currency =  resp.json()['query']['results']['quote']['Currency']

	if currency == 'USD' or currency == 'GBp' or currency == 'EUR':

		if exchange == "NYSE" or exchange == "PAR" or exchange == "LSE":

			cur.execute('INSERT INTO Company (Symbol, Name, Exchange, Currency) VALUES ( ?, ?, ?, ?) ',
				(symbol, name, exchange,currency))
			cur.execute('INSERT INTO Exchange (Exchange, Currency) VALUES ( ?, ?) ',
				(exchange, currency))
			cur.execute('INSERT INTO Location (Currency) VALUES (?) ',
				(currency,))
			cur.execute('INSERT INTO Currency (Currency) VALUES (?) ',
				(currency,))

			conn.commit()



print 'Company:'
cur.execute('SELECT * FROM Company')
for row in cur :
	print row
conn.commit()
cur.close()

