from . import app, db
from . models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request

#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

#crear ruta pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)

#crear ruta consultorios
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

#crear ruta consultorios
@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)

#crear ruta traer el medico por id(get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    #return "id del medico:" + str(id)
    #traer el medico por id utilizando la entidad Medico
    medico = Medico.query.get(id)
    #y meterlo a una vista
    return render_template("medico.html", 
                            med = medico )

#crear ruta traer el paciente por id(get)
@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    #return "id del paciente:" + str(id)
    #traer el paciente por id utilizando la entidad Paciente
    paciente = Paciente.query.get(id)
    #y meterlo a una vista
    return render_template("paciente.html", 
                            p = paciente )

#crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ "GET" , "POST"])
def create_medico():
    ##
    ####mostrar el formulario: metodo GET
    ##
    if( request.method == "GET" ):
        ##EL USUARIO INGRESO CON NAVEGADOR CON http://localhost:5000/medicos/create
        especialidades = [
            "Cardiologia",
            "Pediatria",
            "Oncologia"
        ]
        return render_template("medico_form.html",
                            especialidades = especialidades )
    

### Cuando el usuario presiona el boton guardar
### los datos del formulario viajan al servidor
## utilizando el metodo POST

    elif(request.method == "POST"):
        #cuando se presiona "guardar"
        #crear un objeto de tipo medico
        new_medico = Medico(nombres = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
#añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        return "medico registrado"
