from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db_name = 'dojosandninjas2'
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['namme']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojosandninjas2').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(dojo)
        return dojos
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL('dojosandninjas2').query_db(query, data)
        if results:
            return results[0]
        return False