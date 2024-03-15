from . import app, db
from . models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request, flash , redirect

#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

#crear ruta pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes )

#crear ruta consultorios
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

#crear ruta citas
@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)
##-----------------------------------------------------------------------------------------------------------------------------------------
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
                            paciente = paciente )
#-------------------------------------------------------------------------------------------------------------------------------------------
#crear ruta cita id
@app.route("/citas/<int:id>")
def get_cita_by_id(id):
    cita = Cita.query.get(id)
    return render_template("cita.html", 
                            cita = cita )

#crear ruta consultorio id
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html", 
                            consultorio = consultorio )
#-------------------------------------------------------------------------------------------------------------------------------------------
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
        flash("Medico registrado correctamente")
        return redirect("/medicos")
#---------------------------------------------------------------------------------------------------------------------------------------------
###formularios
@app.route("/pacientes/create" , methods = [ "GET" , "POST"])
def create_paciente():
   
    if( request.method == "GET" ):
        ##EL USUARIO INGRESO CON NAVEGADOR CON http://localhost:5000/medicos/create
        tipo_sangre = [
            "O+",
            "O-",
            "A+"
        ]
        return render_template("paciente_form.html",
                            tipo_sangre = tipo_sangre )
    
    elif(request.method == "POST"):
        #cuando se presiona "guardar"
        #crear un objeto de tipo paciente
        new_paciente = Paciente(nombres = request.form["nombre"],
                                apellidos = request.form["apellidos"],
                                tipo_identificacion = request.form["ti"],
                                numero_identificacion = request.form["ni"],
                                altura = request.form["al"],
                                tipo_sangre = request.form["ts"]
                                )

        db.session.add(new_paciente)
        db.session.commit()
        return "paciente registrado"

##formulario citas
@app.route("/citas/create" , methods = [ "GET" , "POST"])
def create_cita():
   
    if( request.method == "GET" ):
        ##EL USUARIO INGRESO CON NAVEGADOR CON http://localhost:5000/medicos/create
        fecha = [
            "1/10/2024",
            "2/12/2024",
            "5/11/2024"
        ]
        return render_template("cita_form.html",
                            fechas = fecha )
    
    elif(request.method == "POST"):

        new_cita = Cita(
                                paciente_id = request.form["paciente_id"],
                                medico_id = request.form["medico_id"],
                                consultorio_id = request.form["consultorio_id"],
                                valor = request.form["valor"]
                                )

        db.session.add(new_cita)
        db.session.commit()
        return "cita registrado"

##formulario consultorios
@app.route("/consultorios/create" , methods = [ "GET" , "POST"])
def create_consultorio():
   
    if( request.method == "GET" ):
        ##EL USUARIO INGRESO CON NAVEGADOR CON http://localhost:5000/medicos/create
        numero = [
            "101",
            "102",
            "103",
            "104",
            "105",
            "200",
            "201",
            "202"
        ]
        return render_template("consultorio_form.html",
                            numeros = numero )
    
    elif(request.method == "POST"):

        new_consultorio = Consultorio(numero = request.form["nu"])

        db.session.add(new_consultorio)
        db.session.commit()
        return "consultorio registrado"
#--------------------------------------------------------------------------------------------------------------------------------------
###Medico update
@app.route("/medicos/update/<int:id>", methods=["POST" , "GET"])
def update_medico(id):
    especialidades = [
            "Urologo",
            "Cardiologo",
            "Ginecologo"
         ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html",
                           medico_update = medico_update,
                           especialidades = especialidades)
    elif(request.method == "POST"):
       
        #actualizar el paciente, con los datos del form
        medico_update.nombres = request.form["nombres"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return redirect("/medicos")
    
@app.route("/medicos/delete/<int:id>")
def delete_medicos(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")

###Paciente update
@app.route("/pacientes/update/<int:id>", methods=["POST" , "GET"])
def update_paciente(id):
    tipo_sangre = [
            "O+",
            "O-",
            "A+"
         ]
    paciente_update = Paciente.query.get(id)
    if(request.method == "GET"):
        return render_template("paciente_update.html",
                           paciente_update = paciente_update,
                           tipo_sangre = tipo_sangre)
    elif(request.method == "POST"):
       
        #actualizar el paciente, con los datos del form
        paciente_update.nombres = request.form["nombres"]
        paciente_update.apellidos = request.form["apellidos"]
        paciente_update.tipo_identificacion = request.form["ti"]
        paciente_update.numero_identificacion = request.form["ni"]
        paciente_update.altura = request.form["al"]
        paciente_update.tipo_sangre = request.form["ts"]
        db.session.commit()
        return redirect("/pacientes")
    
@app.route("/pacientes/delete/<int:id>")
def delete_pacientes(id):
    paciente_delete = Paciente.query.get(id)
    db.session.delete(paciente_delete)
    db.session.commit()
    return redirect("/pacientes")

###Consultorio update
@app.route("/consultorios/update/<int:id>", methods=["POST" , "GET"])
def update_consultorio(id):
    numero = [
            "101",
            "102",
            "103",
            "104",
            "105",
            "106",
            "107",
            "201",
            "202",
            "203"
         ]

    consultorio_update = Consultorio.query.get(id)
    if(request.method == "GET"):

        return render_template("consultorio_update.html",
                           consultorio_update = consultorio_update,
                           numero = numero)
    elif(request.method == "POST"):

        consultorio_update.numero = request.form["nu"]
        db.session.commit()
        return redirect("/consultorios")

@app.route("/consultorios/delete/<int:id>")
def delete_consultorios(id):
    paciente_delete = Consultorio.query.get(id)
    db.session.delete(consultorio_delete)
    db.session.commit()
    return redirect("/consultorios")
        
        