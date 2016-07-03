from flask import Flask, render_template
app = Flask ( __name__ )

@app . route ( '/' )
def homepage ():
	return render_template('index.html')

@app . route ( '/euro' )
def euro1 ():
        return render_template('euro.html')

@app . route ( '/euro.html' )
def euro2 ():
        return render_template('euro.html')

if __name__ == "__main__" :
	app.run()

#
