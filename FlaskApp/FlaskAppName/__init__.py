from flask import Flask
app = Flask ( __name__ )
@app . route ( '/' )
def homepage ():
	return "que bonito es un entierro"
	if __name__ == "__main__" :
		app . run ()
