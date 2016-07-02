from flask import Flask, render_template
app = Flask ( __name__ )

@app . route ( '/' )
def homepage ():
	return "que bonito es un entierro"
#ashdgakhsd
if __name__ == "__main__" :
	app . run ()
