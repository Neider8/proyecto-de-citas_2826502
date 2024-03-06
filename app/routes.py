from . import app
from . models import Medico, Paciente, Consultorio, Cita
from flask import render_template

#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

#crear ruta pacientes
@app.route("/pacientes")
def get_all_medicos():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)

#crear ruta consultorios
@app.route("/consultorios")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)

#crear ruta consultorios
@app.route("/citas")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)