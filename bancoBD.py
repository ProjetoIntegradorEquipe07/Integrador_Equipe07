import pymysql

class Banco():
    def __init__(self):
        host = 'localhost'
        user = 'root'
        password = 'root'
        db = 'pastelaria_db_equipe07_integrador'
        self.conexao = pymysql.connect(host, user, password, db)