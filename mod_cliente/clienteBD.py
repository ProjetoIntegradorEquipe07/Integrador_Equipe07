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

    def selectOne(self):
        try:
            banco = Banco()

            c=banco.conexao.cursor()

            c.execute('SELECT id_cliente, nome,cpf, telefone, compra_fiado, senha, dia_fiado FROM tb_cliente WHERE id_cliente = %s ', (self.id_cliente))

            for linha in c:
                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.compra_fiado = linha[4]
                self.senha = linha[5]
                self.dia_fiado = linha[6]

            c.close()

            return 'Busca feita com sucesso!'

        except:
            return 'Erro ao buscar cliente!'
                
    def insert(self):
        try:
            banco = Banco()
            c = banco.conexao.cursor()

            c.execute('INSERT INTO tb_cliente(nome,cpf,telefone,compra_fiado,senha,dia_fiado) VALUES(%s,%s,%s,%s,%s,%s)',(self.nome, self.cpf, self.telefone, self.compra_fiado, self.senha,self.dia_fiado))
            banco.conexao.commit()

            c.close()

            return 'Cliente cadastrado com sucesso!'
        except:
            return 'Erro ao cadastrar cliente!'

    def update(self):
        try:
            banco = Banco()
            c = banco.conexao.cursor()

            c.execute('UPDATE tb_cliente SET nome=%s,cpf=%s,telefone=%s,compra_fiado=%s,senha=%s,dia_fiado=%s WHERE id_cliente = %s',(self.nome, self.cpf, self.telefone, self.compra_fiado,self.senha, self.dia_fiado, self.id_cliente))
            banco.conexao.commit()

            c.close()

            return 'Cliente editado com sucesso!'

        except:
            return 'Erro ao editar cliente!'

    def delete(self):
        try:
            banco = Banco()
            c = banco.conexao.cursor()

            c.execute('DELETE FROM tb_cliente WHERE id_cliente = %s',(self.id_cliente))
            banco.conexao.commit()
            c.close()

            return 'Cliente excluido com sucesso'
        
        except:
            return 'Erro ao tentar excluir cliente'