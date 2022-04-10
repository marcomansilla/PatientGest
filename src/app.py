from flask import Flask, request, jsonify, Response 
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash  
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

app = Flask (__name__)
app.config['MONGO_URI']='mongodb://localhost/Consume_Api'
mongo = PyMongo(app)

#Se crean nuevos usuarios en la BD (Collección Usuarios)
@app.route('/Usuarios', methods=['POST'])
def create_user():
    #Recibo datos
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    

    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.Usuarios.insert_one(
            {'username': username, 'email': email, 'password': hashed_password}
        )
        response = {
            'id':str(id),
            'username': username,
            'password': hashed_password,
            'email': email
                  
        }
        return response 
    else:
        return not_found()

    return {'message':'received'}

#Se trae una lista de los usuarios de la BD
@app.route('/Usuarios', methods=['GET'])
def  get_users():
    users =  mongo.db.Usuarios.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

#Traemos un usuario por ID
@app.route('/Usuarios/<id>', methods=['GET'])
def get_oneuser(id):
    user = mongo.db.Usuarios.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    return Response (response, mimetype='application/json') 

#Eliminamos un usuario por ID
@app.route('/Usuarios/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.Usuarios.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'El usuario ' + id + ' fue eliminado correctamente!'})
    return response

@app.route ('/Usuarios/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and email and password:
        hashed_password = generate_password_hash(password)
        mongo.db.Uusarios.update_one({'_id': ObjectId(id)}, {'$set': {
            'username': username,
            'password': hashed_password,
            'email': email
        }})
        response = jsonify({'message': 'El Usuario ' + id + ' fue actualizado correctamente!'})
        return response

#Control de errores
@app.errorhandler(404)
def not_found(error=None):
    
    response = jsonify({
        'message' : 'No encontramos el recurso: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

#--------------------------------------------------------

#Se crean nuevos pacientes en la BD (Tabla de Pacientes)
@app.route('/Pacientes', methods=['POST'])
def create_patient():
    #Recibo datos
    print(request.json)
    name = request.json['name']
    dni = request.json['dni']
    email = request.json['email']
    codigoPostal = request.json['codigoPostal']
    genero = request.json['genero']
    telefono = request.json['telefono']
    fechaNacimiento = request.json['fechaNacimiento']
    #token = request.json['token']


    if name and dni and email:
        #hashed_password = generate_password_hash(password)
        id = mongo.db.Pacientes.insert_one(
            {'name': name, 
            'dni': dni,
            'email': email,
            'codigoPostal': codigoPostal,
            'genero': genero,
            'telefono': telefono,
            'fechaNacimiento': fechaNacimiento}
        )
        response = {
            'id':str(id),
            'name': name, 
            'dni': dni,
            'email': email,
            'codigoPostal': codigoPostal,
            'genero': genero,
            'telefono': telefono,
            'fechaNacimiento': fechaNacimiento  
        }
        return response 
    else:
        return not_found()

if __name__ == "__main__":
    app.run(debug=True)