import requests
import json
import sqlite3
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from SQLAlchemy import Table

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

print ('Scraping Data')

endpoints = ['Symbol', 'Name', ' Exchange']
base_url = "http://dev.markitondemand.com/Api/v2/"
lookup_url = base_url + "Lookup/"
quote_url = base_url + "Quote/"


print (lookup_url)
resp = requests.get(lookup_url + "json?input=NFLX")
# print (resp.headers)
# print (resp.encoding)
# print (resp.text)
# print (resp.json())
symbol = resp.json()[0]["Symbol"]
name = resp.json()[0]["Name"]
exchange = resp.json()[0]["Exchange"]



print('')
print('')
print('')
print('')

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Company')
cur.execute('CREATE TABLE Company (symbol TEXT, name TEXT, exchange TEXT)')

cur.execute('INSERT INTO Company (Symbol, Name, Exchange) VALUES ( ?, ?, ?) ',
	(symbol, name, exchange))

conn.commit()

print 'Company:'
cur.execute('SELECT * FROM Company')
for row in cur :
	print row
conn.commit()
cur.close()


print ('Scraping Data')

endpoints = ['Symbol', 'Name', ' Exchange']
base_url = "http://dev.markitondemand.com/Api/v2/"
lookup_url = base_url + "Lookup/"
quote_url = base_url + "Quote/"


print (lookup_url)
resp = requests.get(lookup_url + "json?input=NFLX")
# print (resp.headers)
# print (resp.encoding)
# print (resp.text)
# print (resp.json())

resp_json = resp.json()





resp = requests.get(quote_url + "json?symbol=NFLX")
print (resp.headers)
# print (resp.encoding)
print (resp.text)
