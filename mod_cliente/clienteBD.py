from bancoBD import Banco

class Cliente():
    def __init__(self, id_cliente=0, nome="", cpf="", telefone="", compra_fiado=0, senha="", dia_fiado=1):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.senha = senha
        self.dia_fiado = dia_fiado

    def selectAll(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()
            c.execute('SELECT id_cliente, nome, telefone, compra_fiado FROM tb_cliente')

            result = c.fetchall()
            c.close()

            
            return result
           

        except:
            return 'Erro ao buscar clientes!'