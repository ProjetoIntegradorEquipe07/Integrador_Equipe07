import pymysql

class Banco():
    def __init__(self):
        # FELIPE
        host = 'localhost'
        user = 'root'
        password = 'root'
        db = 'pastelaria_db_equipe07_integrador'

        # # MARCOS
        # host = 'localhost'
        # user = 'root'
        # password = ''
        # db = 'integrador'

        self.conexao = pymysql.connect(host, user, password, db)