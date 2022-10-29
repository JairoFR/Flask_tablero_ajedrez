
from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def index():
    return render_template("index.html",  c=8, f=8, color1 = "red", color2 = "black")	

@app.route('/4')
def columnas():
    return render_template("index.html", c=4, f=8, color1 = "red", color2 = "black")	

@app.route('/<int:x>/<int:y>')
def tabla_nueva(x,y):
    return render_template("index.html", c=x, f=y, color1 = "red", color2 = "black")	

@app.route('/<int:x>/<int:y>/<string:colors>/<string:colore>')
def tabla_nueva2(x,y,colors,colore):
    return render_template("index.html", c=x, f=y, color1 = colors, color2 = colore)	




    

if __name__=="__main__":    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
