from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/name/<name>', methods=['GET'])
def ejemplo(name):
    return f"Hola, {name}"

@app.route('/palindromo/<palabra>', methods=['GET'])
def ejercicio1(palabra):
    if ( palabra == palabra[::-1] ):
        return "si es un palindromo"
    else:
        return "no, no es un palindromo"
    

@app.route('/operaciones/<num1>/<num2>', methods=['GET'])
def ejercicio2(num1, num2):
    
    suma = int(num1) + int(num2)
    resta = int(num1) - int(num2)
    mult = int(num1) * int(num2)
    divs = int(num1) / int(num2)

    return f"Suma: {suma} resta: {resta} multiplicacion: {mult} division: {divs}"

@app.route('/ordenar', methods=['GET'])
def ejercicio3():
    # Su código va aquí
    return


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
