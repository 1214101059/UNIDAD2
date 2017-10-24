from DVRS_evaluacion import potencialgravitatorio
from DVRS_evaluacion import FarenheitCelsius
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Bienvenido, es un gusto tenerte aqui')


@app.route('/calculate', methods=['POST'])
def execute() -> 'html':
    G = float(request.form['G'])
    M = float(request.form['M'])
    r = float(request.form['r'])
    C = float(request.form['C'])
    result = potencialgravitatorio(G, M, r)
    result2 = FarenheitCelsius(C)
    title = "Formulario para calcular el potencial gravitacional y convertir grados Celsius a Farenheit"
    return render_template('results.html', the_G=G, the_M=M, the_r=r,
                           the_C=C,
                           the_result=result,
                           the_result2=result2,
                           the_title=title)


app.run(debug=True)
