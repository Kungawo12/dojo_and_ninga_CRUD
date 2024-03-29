from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja
class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @ classmethod 
    def get_dojo(cls):
        query = "SELECT * from dojos"
        results = connectToMySQL('dojo_db').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def show_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('dojo_db').query_db(query,data)
        return cls(results[0])
        
    
    @ classmethod
    def add_dojo(cls, data):
        query= """INSERT INTO dojos(name) 
                    VALUES (%(name)s);
            """
        return connectToMySQL('dojo_db').query_db(query,data)
    
    
    @ classmethod
    def get_one_with_ninjas(cls,data):
        query = """
            SELECT * FROM dojos 
            LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s
        """
        results = connectToMySQL('dojo_db').query_db(query,data)
        
        dojo = cls(results[0])
        for row in results:
            n = {
                "id" : row['ninjas.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "created_at" : row['ninjas.created_at'],
                "updated_at" : row['ninjas.updated_at'],
            }
            dojo.ninjas.append(Ninja(n))
        return dojo