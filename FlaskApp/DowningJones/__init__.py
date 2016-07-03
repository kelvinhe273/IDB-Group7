from flask import Flask, render_template
app = Flask ( __name__ )

@app.route ( '/' )
def homepage ():
	return render_template('index.html')

@app.route ( '/index.html' )
def index ():
	return render_template('index.html')

@app.route ( '/about.html' )
def about ():
	return render_template('about.html')

@app.route ( '/base.html' )
def base ():
	return render_template('base.html')

@app.route ( '/company.html' )
def company ():
	return render_template('company.html')

@app.route ( '/company1.html' )
def company1 ():
	return render_template('company1.html')

@app.route ( '/company2.html' )
def company2 ():
	return render_template('company2.html')

@app.route ( '/company3.html' )
def company3 ():
	return render_template('company3.html')

@app.route ( '/currency.html' )
def currency ():
	return render_template('currency.html')

@app.route ( '/dollars.html' )
def dollars ():
	return render_template('dollars.html')

@app.route ( '/euros.html' )
def euros ():
	return render_template('euros.html')

@app.route ( '/fra.html' )
def fra ():
	return render_template('fra.html')

@app.route ( '/france.html' )
def france ():
	return render_template('france.html')

@app.route ( '/greatbritain.html' )
def greatbritain ():
	return render_template('greatbritain.html')

@app.route ( '/location.html' )
def location ():
	return render_template('location.html')

@app.route ( '/lse.html' )
def lse ():
	return render_template('lse.html')

@app.route ( '/nasdaq.html' )
def nasdaq ():
	return render_template('nasdaq.html')

@app.route ( '/pounds.html' )
def pounds ():
	return render_template('pounds.html')

@app.route ( '/stockmarket.html' )
def stockmarket ():
	return render_template('stockmarket.html')

@app.route ( '/us.html' )
def us ():
	return render_template('us.html')

if __name__ == "__main__" :
	app.run()
