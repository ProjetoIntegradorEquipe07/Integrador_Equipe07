import datetime

from bancoBD import Banco
from funcoes import Funcoes, LOG


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

            Funcoes.criaLOG(f'Insere produtos comanda, id_comanda: {self.comanda_id}, id_produto: {self.produto_id}', LOG.info)            

            return 'Produto adicionado com sucesso!'

        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
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

            c.execute('SELECT id_comanda, produto_id, quantidade, valor_unitario, comanda, data_hora, CONVERT(SUM(valor_unitario * quantidade), CHAR) FROM tb_comanda_produto RIGHT JOIN tb_comanda ON id_comanda = comanda_id  WHERE id_comanda = %s ',(self.comanda_id))

            for linha in c:
                comanda = {

                    'id_comanda': linha[0],
                    'id_produto': linha[1],
                    'quantidade': linha[2],
                    'valor_unitario': linha[3],
                    'comanda': linha[4],
                    'data_hora': linha[5].strftime("%d/%m/%Y"),#Converte de mes-dia-ano para dia/mes/ano
                    'valor_total': linha[6]
                }

            

            c.close()

            return comanda

        except Exception as e:
            raise Exception('Erro ao buscar comanda!', str(e))

    def selectValorTotalComanda(self, status_comanda):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT SUM(valor_unitario * quantidade) FROM tb_comanda_produto INNER JOIN tb_comanda ON id_comanda = comanda_id WHERE comanda_id = %s AND status_comanda = %s ',(self.comanda_id, status_comanda))

            valor_total = c.fetchone()

            c.close()

            return valor_total

        except Exception as e:
            raise Exception('Erro ao retornar valor total', str(e))

    def deleteProdutoComanda(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('DELETE FROM tb_comanda_produto WHERE id_comanda_produto = %s', (self.id_comanda_produto))
            banco.conexao.commit()
            Funcoes.criaLOG('Delete produto comanda', LOG.info)
            return 'Produto deletado da comanda'

        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception('Erro ao deletar produto da comanda', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()