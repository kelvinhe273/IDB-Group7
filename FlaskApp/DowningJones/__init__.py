from flask import Flask, render_template
app = Flask ( __name__ )

@app . route ( '/' )
def homepage ():
	return render_template('index.html')

@app . route ( '/company' )
def company ():
        return render_template('company.html')

#ashdgakhsd
if __name__ == "__main__" :
	app.run()

#
