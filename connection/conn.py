from pymongo import MongoClient


class Conexion:
    def __init__(self, uri, database):
        self.client = MongoClient(uri)
        self.db = self.client[database]

    def obtener_registros(self, collect, condition={}):
        collection = self.db[collect]
        data = collection.find(condition)
        return list(data)

    def obtener_registro(self, collect, condition={}):
        collection = self.db[collect]
        data = collection.find_one(condition)
        return data

    def insertar_registros(self, collect, data):
        collection = self.db[collect]
        result = collection.insert_many(data)
        print(f'Inserts rows -> {result.inserted_ids}')

    def insertar_registro(self, collect, data):
        collection = self.db[collect]
        result = collection.insert_one(data)
        print(f'Insert row -> {result.inserted_id}')

    def actualizar_registro(self, collect, condition, change, multi=False):
        collection = self.db[collect]
        collection.updated_one(condition, {
            "$set": change
        }, multi)
        print(f'Se actualizo el registro')

    def eliminar_registro(self, collect, condition):
        collection = self.db[collect]
        collection.delete_one(condition)
        print(f'Se elimino un registro')
