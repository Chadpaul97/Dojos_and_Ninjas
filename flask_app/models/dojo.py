from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def save_dojo(data):
        query="INSERT into dojos (name) VALUES(%(name)s)"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos"
        query_results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        dojos = []

        for d in query_results:
            dojo = cls(d)
            dojos.append(dojo)

        return dojos



    @classmethod
    def get_all_ninjas(cls,data):
        query= "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        query_results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        dojo = cls(query_results[0])
        for ninja in query_results:
            ninjas_data = {
                'id': ninja['id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'dojos_id':ninja['dojos_id'],
                'created_at': ninja['created_at'],
                'updated_at': ninja['updated_at']
            }
            dojo.ninjas.append( Ninja(ninjas_data) )
        return dojo