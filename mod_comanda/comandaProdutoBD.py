from bancoBD import Banco
import datetime

class ComandaProduto():
    def __init__(self, id_comanda_produto=0, funcionario_id=0, produto_id=0, comanda_id=0, quantidade=0, valor_unitario=0):
        self.id_comanda_produto = id_comanda_produto
        self.funcionario_id = funcionario_id
        self.produto_id = produto_id
        self.comanda_id = comanda_id
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def insertProdutoComanda(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute("INSERT INTO tb_comanda_produto(funcionario_id, produto_id, comanda_id, quantidade, valor_unitario) VALUES(%s, %s, %s, %s, %s)",(self.funcionario_id, self.produto_id, self.comanda_id, self.quantidade, self.valor_unitario))

            banco.conexao.commit()

            c.close()

            return 'Produto adicionado com sucesso!'

        except Exception as e:
            raise Exception('Erro ao adicionar produto!', str(e))

    def selectOne(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT comanda_id, produto_id, quantidade, valor_unitario FROM tb_comanda_produto  WHERE comanda_id = %s ',(self.comanda_id))

            for linha in c:
                self.comanda_id = linha[0]
                self.produto_id = linha[1]
                self.quantidade = linha[2]
                self.valor_unitario = linha[3]

            c.close()

            return 'Sucesso ao buscar comanda!'

        except Exception as e:
            raise Exception('Erro ao buscar comanda!', str(e))

    def selectOneComanda(self):
        try:
            banco = Banco()
            comanda = dict()

            c = banco.conexao.cursor()

            c.execute('SELECT comanda_id, produto_id, quantidade, valor_unitario, comanda, data_hora FROM tb_comanda_produto RIGHT JOIN tb_comanda ON id_comanda = comanda_id  WHERE id_comanda = %s ',(self.comanda_id))

            for linha in c:
                comanda = {

                    'id_comanda': linha[0],
                    'id_produto': linha[1],
                    'quantidade': linha[2],
                    'valor_unitario': linha[3],
                    'comanda': linha[4],
                    'data_hora': linha[5].strftime("%d/%m/%Y")
                }

            

            c.close()

            return comanda

        except Exception as e:
            raise Exception('Erro ao buscar comanda!', str(e))