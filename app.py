from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# dicționar pentru comanda
lista = {}

@app.route("/")
def home():
    return render_template("menu.html", lista=lista)

@app.route("/adauga/<produs>")
def adauga(produs):
    lista[produs] = lista.get(produs, 0) + 1
    return redirect(url_for("home"))

@app.route("/anulare")
def anulare():
    lista.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
