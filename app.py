from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("index.html")
	#return "<h1>Hola mundo</h1>"

@app.route("/ejercicios")
def url_coffee():
 	tipos = [
 		"Inferior",
 		"Superior"
 	]
 	return render_template("gymonline.html", tipos=tipos, nombre="Gimnasio Online")

if __name__ == "__main__":
	app.run(debug=True)