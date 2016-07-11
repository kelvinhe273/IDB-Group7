import requests
import json
import sqlite3
import csv

from yahoo_oauth import OAuth1
oauth = OAuth1(None, None, from_file='keys.json')

if not oauth.token_is_valid():
	oauth.refresh_access_token()

endpoints = ['Symbol', 'Name', ' Exchange', 'Currency']
base_url = "http://dev.markitondemand.com/Api/v2/"
lookup_url = base_url + "Lookup/"
quote_url = base_url + "Quote/"

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Company')
cur.execute('CREATE TABLE Company (symbol TEXT, name TEXT, exchange TEXT, currency TEXT, location TEXT, open_price TEXT, previous_price TEXT, percent_change TEXT, year_high TEXT, ask_price TEXT, eps TEXT, peg TEXT,days_range TEXT, percent_change_fifty TEXT, percent_change_twohundred TEXT, volume TEXT, avg_volume TEXT, market_cap TEXT)')

cur.execute('DROP TABLE IF EXISTS Exchange')
cur.execute('CREATE TABLE Exchange (exchange TEXT, name TEXT, currency TEXT, location TEXT, market_cap_exchange TEXT)')

cur.execute('DROP TABLE IF EXISTS Location')
cur.execute('CREATE TABLE Location (name TEXT, iso TEXT, capital TEXT, gdp TEXT, currency TEXT, location_exchange TEXT)')

cur.execute('DROP TABLE IF EXISTS Currency')
cur.execute('CREATE TABLE Currency (name TEXT,currency TEXT, locations TEXT, exchanges TEXT, exchange_rate Integer)')


f = open('yahoo.csv')
csv_f = csv.reader(f)
for row in csv_f:
	source = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22' +row[0] +'%22)&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&format=json'

	try:
		resp = requests.get(source)
		# print(resp.text)
		symbol = resp.json()['query']['results']['quote']['symbol']
		if symbol is None:
			continue
		print(symbol)
		name = resp.json()['query']['results']['quote']['Name']
		exchange =  resp.json()['query']['results']['quote']['StockExchange']
		open_price = resp.json()['query']['results']['quote']['Open']
		previous_price = resp.json()['query']['results']['quote']['PreviousClose']
		percent_change = resp.json()['query']['results']['quote']['ChangeinPercent']
		year_high = resp.json()['query']['results']['quote']['YearHigh']
		ask_price = resp.json()['query']['results']['quote']['Ask']
		eps = resp.json()['query']['results']['quote']['EPSEstimateCurrentYear']
		peg = resp.json()['query']['results']['quote']['PEGRatio']
		days_range = resp.json()['query']['results']['quote']['DaysRange']
		percent_change_fifty = resp.json()['query']['results']['quote']['PercentChangeFromFiftydayMovingAverage']
		percent_change_twohundred = resp.json()['query']['results']['quote']['PercentChangeFromTwoHundreddayMovingAverage']
		volume = resp.json()['query']['results']['quote']['Volume']
		avg_volume = resp.json()['query']['results']['quote']['AverageDailyVolume']
		market_cap = resp.json()['query']['results']['quote']['MarketCapitalization']
	except ValueError:
		print("failed to decode")
		continue

	except TypeError:
		print("failed to decode")
		continue
	
	# if exchange == "NMS":
	# 	exchange = "NASDAQ"

	if exchange == "NMS" or exchange == "LSE" or exchange == "PAR" or exchange == "HKG" or exchange == "MEX" or exchange == "TAI" or exchange == "BER" or exchange == "MUN" or exchange == "FRA" or exchange == "TOR" or exchange == "ASE":

		if exchange == "NMS":
			location = 'USA'
			iso = 'US'
			capital = 'Washington DC'
			gdp = '16.77 trillion USD'
			exchangeName = 'National Market System'
			market_cap_exchange = '19,223 billion'

		elif exchange == "LSE":
			location = 'Great Britain'
			iso = 'GB'
			capital = 'London'
			gdp = '2.678 trillion USD'
			exchangeName = 'London Stock Exchange'
			market_cap_exchange = '6,187 billion'

		elif exchange == "PAR":
			location = 'France'
			iso = 'FR'
			capital = 'Paris'
			gdp = '2.806 trillion USD'
			exchangeName = 'Paris Stock Exchange'
			market_cap_exchange = '3,321 billion'

		elif exchange == "HKG":
			location = 'Hong Kong'
			iso = 'HK'
			capital = 'none'
			gdp = '274 billion USD'
			exchangeName = 'Hong Kong Stock Exchange'
			market_cap_exchange = '3,325 billion'

		elif exchange == "MEX":
			location = 'Mexico'
			iso = 'MX'
			capital = 'Mexico City'
			gdp = '1.261 trillion USD'
			exchangeName = 'Mexico Stock Exchange'
			market_cap_exchange = '402.99 billion'

		elif exchange == "TAI":
			location = 'Taiwan'
			iso = 'TW'
			capital = 'Taipei'
			gdp = '474 billion USD'
			exchangeName = 'Taiwan Stock Exchange'
			market_cap_exchange = '861 billion'

		elif exchange == "BER":
			location = 'Berlin, Germany'
			iso = 'DE'
			capital = 'Berlin'
			gdp = '3.355 trillion USD'
			exchangeName = 'Berlin Stock Exchange'
			market_cap_exchange = '1,176 billion'

		elif exchange == "MUN":
			location = 'Munich, Germany'
			iso = 'DE'
			capital = 'Berlin'
			gdp = '3.355 trillion USD'
			exchangeName = 'Munich Stock Exchange'
			market_cap_exchange = '1,762 billion'

		elif exchange == "FRA":
			location = 'Frankfurt, Germany'
			iso = 'DE'
			capital = 'Berlin'
			gdp = '3.355 trillion USD'
			exchangeName = 'Frankfurt Stock Exchange'
			market_cap_exchange = '1,762 billion'

		elif exchange == "TOR":
			location = 'Toronto, Canada'
			iso = 'CA'
			capital = 'Ottawa'
			gdp = '1.827 trillion USD'
			exchangeName = 'Toronto Stock Exchange'
			market_cap_exchange = '1,939 billion'

		elif exchange == "ASE":
			location = 'Athens, Greece'
			iso = 'GR'
			capital = 'Athens'
			gdp = '242.2 billion USD'
			exchangeName = 'Athens Stock Exchange'
			market_cap_exchange = '43.85 billion'

		currency =  resp.json()['query']['results']['quote']['Currency']
		

		if currency == "EUR":
			location_cur = 'Greece,Germany,France'
			exchnages_cur = 'ASE, FRA, MUN, BER, PAR'
			exchange_rate = 1.10
			curName = 'Euro'

		elif currency == "GBp":
			location_cur = 'Great Britain'
			exchnages_cur = 'LSE'
			exchange_rate = 1.30
			curName = 'Sterling Pound'

		elif currency == 'MXN':
			location_cur = 'Mexico'
			exchnages_cur = 'MEX'
			exchange_rate = .054
			curName = 'Peso'

		elif currency == 'TWD':
			location_cur = 'Taiwan'
			exchnages_cur = 'TAI'
			exchange_rate = .031
			curName = 'Taiwan New Dollar'

		elif currency == 'CAD':
			location_cur = 'Canada'
			exchnages_cur = 'TOR'
			exchange_rate = .76
			curName = 'Canadian Dollar'

		elif currency == 'USD':
			location_cur = 'United States'
			exchnages_cur = 'NMS'
			exchange_rate = 1
			curName = 'US Dollars'

		elif currency == 'HKD':
			location_cur = 'Hong Kong'
			exchnages_cur = 'HKG'
			exchange_rate = .13
			curName = 'Hong Kong dollar'

		if location == 'Athens, Greece':
			location_exchange = 'Athens Stock Exchange'
		elif location == 'Toronto, Canada':
			location_exchange = 'Toronto Stock Exchange'
		elif location == 'Frankfurt, Germany':
			location_exchange = 'Frankfurt Stock Exchange'
		elif location == 'Munich, Germany':
			location_exchange = 'Munich Stock Exchange'
		elif location == 'Berlin, Germany':
			location_exchange = 'Berlin Stock Exchange'
		elif location == 'Taiwan':
			location_exchange = 'Taiwan Stock Exchange'
		elif location == 'Mexico':
			location_exchange = 'Mexico Stock Exchange'
		elif location == 'Hong Kong':
			location_exchange = 'Hong Kong Stock Exchange'
		elif location == 'France':
			location_exchange = 'Paris Stock Exchange'
		elif location == 'Great Britain':
			location_exchange = 'London Stock Exchange'
		elif location == 'USA':
			location_exchange = 'National Market System'

		cur.execute('INSERT INTO Company (Symbol, Name, Exchange, Currency, Location , Open_Price, Previous_Price, Percent_Change, Year_High, Ask_Price, Eps, Peg, Days_Range, Percent_Change_Fifty, Percent_Change_Twohundred, Volume, Avg_Volume, Market_Cap) VALUES ( ?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ) ',
			(symbol, name, exchange, currency, location , open_price, previous_price, percent_change, year_high, ask_price, eps, peg, days_range, percent_change_fifty, percent_change_twohundred, volume, avg_volume, market_cap))
		cur.execute('INSERT INTO Exchange (Exchange, Name, Currency, Location , Market_Cap_Exchange) VALUES ( ?, ?, ?, ?, ?) ',
			(exchange,exchangeName, currency, location, market_cap_exchange))
		cur.execute('INSERT INTO Currency (Name,Currency, Locations, Exchanges, Exchange_Rate) VALUES (?, ?, ?, ?, ?) ',
			(curName, currency, location_cur, exchnages_cur, exchange_rate))
		cur.execute('INSERT INTO Location (Name, Iso, Capital, Gdp, Currency, Location_Exchange) VALUES (?, ?, ?, ?, ?, ?) ',
			(location, iso,capital,gdp, currency, location_exchange))

		conn.commit()



print 'Location:'
cur.execute('SELECT * FROM Location')
for row in cur :
	print row
conn.commit()
cur.close()


