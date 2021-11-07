from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojos_id = data["dojos_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_dojos(cls):
        query= "SELECT dojos.name FROM dojos"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos=[]
        for dojo in results:
            new_dojo = cls(dojo)
            dojos.append(new_dojo)
        return dojos


    @classmethod
    def save_ninja(cls,data):
        query="INSERT into ninjas (first_name,last_name,age,dojos_id) VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojos_id)s)"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)