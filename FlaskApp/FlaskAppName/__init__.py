from flask import Flask
app = Flask ( __name__ )
@app . route ( '/' )
def homepage ():
	return "Hi there, how are you doing? It’s a beautiful day, let’s go play outside "
	if __name__ == "__main__" :
		app . run ()
