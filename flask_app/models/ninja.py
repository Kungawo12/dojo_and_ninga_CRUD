from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_ninja(cls,data):
        query = """INSERT INTO ninjas(first_name,last_name,age,dojo_id)
                VALUE(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        return connectToMySQL("dojo_db").query_db(query,data)
    
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
    
    @classmethod
    def show_ninja(cls,data):
        query ="SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojo_db').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query= """ UPDATE ninjas
        SET first_name=%(first_name)s,last_name= %(last_name)s, age = %(age)s,
        dojo_id= %(dojo_id)s
        WHERE id = %(id)s
        """
        results = connectToMySQL('dojo_db').query_db(query,data)
        return results
    
    @classmethod
    def delete_ninja(cls,data):
        query = """DELETE FROM ninjas 
                    WHERE id = %(id)s
        """
        return connectToMySQL("dojo_db").query_db(query,data)