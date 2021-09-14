from flask import Flask, json, jsonify, request
import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin',
    database='db-encuesta'
)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.post('/usuarios')
def CrearUsuario():
    #request = lo que envia el cliente
    #response = lo que voy a responder

    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO usuario(nombre,email,contrasena) 
        VALUES(%s,%s,%s)''',(
        datos['nombres'],
        datos['email'],
        datos['contrasena']
        ))

    db.commit()

    return jsonify({
        "mensaje": "usuario creado exitosamente"
    })

@app.get('/usuarios')
def ListarUsuarios():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    return jsonify(usuarios)


@app.put('/usuarios/<id>')
def actualizarUsuario(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE usuario set nombre=%s, 
        email=%s, contrasena=%s where id=%s''',(
            datos['nombre'],
            datos['email'],
            datos['contrasena'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "Usuario actualizado correctamente"
    })

@app.delete('/usuarios/<id>')
def eliminarUsuario(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM usuario WHERE id=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "Usuario eliminado correctamente"                      
    })

@app.post('/encuesta')
def CrearEncuesta():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO encuesta(nombre,descrip,imagen) 
        VALUES(%s,%s,%s)''',(
        datos['nombre'],
        datos['descrip'],
        datos['imagen']
        ))

    db.commit()

    return jsonify({
        "mensaje": "Encuesta creada exitosamente"
    })

@app.get('/encuesta')
def listarEncuestas():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from encuesta')
    encuesta = cursor.fetchall()
    return jsonify(encuesta)

@app.put('/encuesta/<id>')
def actualizarEncuesta(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE encuesta set nombre=%s, 
        descrip=%s, imagen=%s where idenc=%s''',(
            datos['nombre'],
            datos['descrip'],
            datos['imagen'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "Encuesta actualizada correctamente"
    })

@app.delete('/encuesta/<id>')
def eliminarEncuesta(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM encuesta WHERE idenc=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "Encuesta eliminada correctamente"                      
    })

@app.post('/preguntas')
def CrearPreguntas():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO preguntas(tipopreg,pregunta) 
        VALUES(%s,%s)''',(
        datos['tipopreg'],
        datos['pregunta'],        
        ))

    db.commit()

    return jsonify({
        "mensaje": "Pregunta creada exitosamente"
    })

@app.get('/preguntas')
def listarPreguntas():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from preguntas')
    preguntas = cursor.fetchall()
    return jsonify(preguntas)

@app.post('/respuestas')
def CrearRespuesta():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO respuestas(idusu,idpreg,idenc,resp) 
        VALUES(%s,%s,%s,%s)''',(
        datos['idusu'],
        datos['idpreg'],
        datos['idenc'],
        datos['resp'],        
        ))

    db.commit()

    return jsonify({
        "mensaje": "Respuesta creada exitosamente"
    })

@app.get('/respuestas')
def listarRespuestas():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from respuestas')
    respuestas = cursor.fetchall()
    return jsonify(respuestas)

app.run(debug=True)