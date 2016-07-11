from flask import Flask, render_template
app = Flask ( __name__ )

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
	return render_template('about.html')

@app.route ( '/companies' )
def companies ():
	companies = [    
		{
            "id": 1,
            "name": "Yahoo",
            "symbol": "YHOO",
            "stock_exchange": "NASDAQ",
            "location": "USA",
            "currency": "US Dollars"
        },
        {
            "id": 2,
            "name": "XILAM Animation",
            "symbol": "XIL.PA",
            "stock_exchange": "PAR",
            "location": "France",
            "currency": "Euro"
        },
        {
            "id": 3,
            "name": "The Vitec Group",
            "symbol": "VTC.L",
            "stock_exchange": "LSE",
            "location": "Great Britain",
            "currency": "Pound sterling"
        }]
	return render_template('companies.html',
							title='Companies',
							companies=companies)

@app.route ( '/companies/<id>' )
def company (id):
	return render_template('company.html')

@app.route ( '/currencies' )
def currencies ():
	currencies = [
	    {
            "id": 1,
            "name": "US Dollars",
            "currency_code": "USD",
            "exchange": "NASDAQ",
            "location": "USA",
            "number_of_official_users": 9
        },
        {
            "id": 2,
            "name": "Euro",
            "currency_code": "EUR",
            "exchange": "PAR",
            "location": "France",
            "number_of_official_users": 19
        },            
        {
            "id": 3,
            "name": "Pound sterling",
            "currency_code": "GBP",
            "exchange": "LSE",
            "location": "Great Britain",
            "number_of_official_users": 1
        }]
	return render_template('currencies.html',
							title='Currencies',
							currencies=currencies)

@app.route ( '/currencies/<id>' )
def currency (id):
	return render_template('currency.html')

@app.route ( '/locations' )
def locations ():
	locations = [
	    {
            "id": 1,
            "location": "USA",
            "capital": "Washington, D.C.",
            "stock_exchange": "NASDAQ",
            "currency": "US Dollars",
            "GDP_Nominal": "$18.558 trillion" 

        },
        {
            "id": 2,
            "location": "France",
            "capital": "Paris",
            "stock_exchange": "PAR",
            "currency": "Euro",
            "GDP_Nominal": "$2.647 trillion"
        },
        {
            "id": 3,
            "location": "United Kingdom",
            "capital": "London",
            "stock_exchange": "LSE",
            "currency": "Pound sterling",
            "GDP_Nominal": "$2.849 trillion"
        }]
	return render_template('locations.html',
						    title='Locations',
						    locations=locations)

@app.route ( '/locations/<id>' )
def location (id):
	return render_template('location.html')

@app.route ( '/stockmarkets' )
def stockmarkets ():
	markets=[
	        {
                "id": 1,
                "name": "NASDAQ",
                "location": "USA",
                "currency": "US Dollars",
                "points": 4862.57,
                "change": "+.041%"
            },
            {
                "id": 2,
                "name": "PAR",
                "location": "France",
                "currency": "Euro",
                "points": 32.15,
                "change": "-2.46%"
            },
            {
                "id": 3,
                "name": "LSE",
                "location": "Great Britain",
                "currency": "Pound sterling",
                "points": 32.15,
                "change": "-2.46%"
            }]
	return render_template('stockmarkets.html',
							title='Exchanges',
							markets=markets)

@app.route ( '/stockmarkets/<id>' )
def market (id):
	return render_template('stockmarket.html')