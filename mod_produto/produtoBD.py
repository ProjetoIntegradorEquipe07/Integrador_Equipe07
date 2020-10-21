from bancoBD import Banco

class Produto():
    def __init__(self, id_produto = 0,	nome="",	descricao="",	foto="",	valor_unitario=0):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario
    
    def selectAll(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT id_produto, nome, descricao, foto, valor_unitario FROM tb_produto')

            result = c.fetchall()
            c.close()
            return result
        except Exception as e:
            return 'Erro ao buscar produtos!'

    def insert(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('INSERT INTO tb_produto(nome,descricao,valor_unitario) VALUES(%s,%s,%s)',(self.nome,self.descricao,self.valor_unitario))
            banco.conexao.commit()
            c.close()

            return 'Produto cadastrado com sucesso!'

        except Exception as e:
            
            raise Exception('Erro ao cadastrar produto!', str(e))
    
    def update(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('UPDATE tb_produto SET nome=%s,descricao=%s,foto=%s,valor_unitario=%s WHERE id_produto=%s',(self.nome,self.descricao,self.foto,self.valor_unitario,self.id_produto))
            banco.conexao.commit()
            c.close()

            return 'Produto editado com sucesso!'

        except Exception as e:
            raise Exception('Erro ao editar produto!', str(e))

    def delete(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('DELETE FROM tb_produto WHERE id_produto = %s',(self.id_produto))

            banco.conexao.commit()
            c.close()

            return 'Produto excluído com sucesso'

        except Exception as e:
            raise Exception('Erro ao excluir produto', str(e))

        
