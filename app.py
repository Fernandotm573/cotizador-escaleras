from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/cotizar', methods=['POST'])
def cotizar():
    tipo = request.form['tipo']
    altura = float(request.form['altura'])
    material = request.form['material']
    acabado = request.form['acabado']

    tipos = {"recta": 1.0, "caracol": 1.5, "L": 1.3}
    materiales = {"acero carbono": 1.0, "inoxidable": 1.8}
    acabados = {"pintura": 1.0, "galvanizado": 1.2}

    base_precio = 100

    precio = base_precio * altura
    precio *= tipos[tipo]
    precio *= materiales[material]
    precio *= acabados[acabado]

    return render_template('resultado.html', precio=round(precio, 2))

if __name__ == '__main__':
    app.run(debug=True)
