from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

comanda = []

@app.route("/")
def home():
    return render_template("menu.html", comanda=comanda)

@app.route("/adauga/<item>")
def adauga_iteme(item):
    comanda.append(item)
    print(f"Ai comandat -> {item}")
    return redirect(url_for('home'))

@app.route("/afiseaza")
def afiseaza_comanda():
    if comanda:
        print(f"Pana acum ai comandat:  {comanda}")
    else:
        print("Lista goala!")
    return redirect(url_for('home'))

@app.route("/goleste")
def goleste_comanda():
    comanda.clear()
    return redirect(url_for('home'))





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
