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


f = open('companylist.csv')
csv_f = csv.reader(f)
for row in csv_f:
	source = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22' +row[0] +'%22)&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&format=json'


	resp = requests.get(source)
	# print(resp.text)
	symbol = resp.json()['query']['results']['quote']['symbol']
	#print(symbol)
	name = resp.json()['query']['results']['quote']['Name']
	exchange =  resp.json()['query']['results']['quote']['StockExchange']
	currency =  resp.json()['query']['results']['quote']['Currency']

	cur.execute('INSERT INTO Company (Symbol, Name, Exchange, Currency) VALUES ( ?, ?, ?, ?) ',
		(symbol, name, exchange,currency))

	conn.commit()



print('')
print('')
print('')
print('')



print 'Company:'
cur.execute('SELECT * FROM Company')
for row in cur :
	print row
conn.commit()
cur.close()


