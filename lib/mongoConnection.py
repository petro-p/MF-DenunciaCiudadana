from pymongo import MongoClient

MONGO_URL_ATLAS = 'mongodb+srv://admin:admin123@denuncias-dkzqn.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

db = client['denuncias']

usuarios = db['usuarios']
denuncias = db['denuncias']


def comprobarLogin(email):
    user = {}
    resultados = registrados.find(
        {'email': email}, {'_id': 0, 'nombre': 1, 'password': 1, 'email': 1, 'user_group': 1})
    resultados = list(resultados)

    for resultado in resultados:
        user.update(
            {'email': resultado['email'], 'nombre': resultado['nombre'], 'password': resultado['password'], 'user_group': resultado['user_group']})
    return user
