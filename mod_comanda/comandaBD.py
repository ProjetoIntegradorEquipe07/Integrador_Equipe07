from bancoBD import Banco

class Comanda():
    def __init__(self, id_comanda=0, comanda=0, dada_assinatura_fiado="", data_hora="", status_pagamento=0, status_comanda=0, funcionario_id="", cliente_id=""):
        self.id_comanda = id_comanda
        self.comanda = comanda
        self.data_assinatura_fiado = dada_assinatura_fiado
        self.data_hora = data_hora
        self.status_pagamento = status_pagamento
        self.status_comanda = status_comanda
        self.funcionario_id = funcionario_id
        self.cliente_id = cliente_id


    def selectAllComandaDashboard(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT id_comanda , comanda, data_hora, status_pagamento, status_comanda, SUM(valor_unitario * quantidade) FROM tb_comanda LEFT JOIN tb_comanda_produto ON comanda_id = id_comanda GROUP BY id_comanda')

            result = c.fetchall()

            c.close()

            return result
        except Exception as e:
            return str(e)

    def selectOne(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT id_comanda, comanda, data_hora FROM tb_comanda WHERE id_comanda = %s ',(self.id_comanda))

            for linha in c:
                self.id_comanda = linha[0]
                self.comanda = linha[1]
                self.data_hora = linha[2]

            c.close()

            return comanda

        except Exception as e:
            return str(e)

    def insertNumeroComanda(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('INSERT INTO tb_comanda(comanda, data_hora, status_pagamento, status_comanda, funcionario_id) VALUES(%s, %s, %s, %s, %s)', (self.comanda, self.data_hora, self.status_pagamento, self.status_comanda, self.funcionario_id))

            banco.conexao.commit()

            c.close()
            return 'Comanda criada com sucesso!'

        except Exception as e:
            raise Exception('Erro ao criar comanda', str(e))

    def verificaSeComandaExiste(self):
        try:
            banco = Banco()

            c= banco.conexao.cursor()

            c.execute('SELECT id_comanda FROM tb_comanda WHERE comanda = %s AND status_comanda = %s', (self.comanda, self.status_comanda))

            result = c.fetchall()

            return result
        except Exception as e:
            raise Exception('Erro ao buscar número da comanda', str(e))

    def selectComandaByNumero(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute("SELECT id_comanda , comanda, status_comanda, data_hora,  CONVERT(SUM(valor_unitario*quantidade), CHAR) FROM tb_comanda LEFT JOIN tb_comanda_produto ON comanda_id = id_comanda  WHERE comanda = %s AND status_comanda = %s",(self.comanda, self.status_comanda))

            result = c.fetchone()

            c.close()

            return result
        
        except Exception as e:
            raise Exception('Erro ao buscar numero', str(e))

    def selectComandaByStatus(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT id_comanda , comanda, data_hora, status_pagamento, status_comanda, SUM(valor_unitario * quantidade) FROM tb_comanda LEFT JOIN tb_comanda_produto ON comanda_id = id_comanda GROUP BY id_comanda HAVING status_comanda = %s ',(self.status_comanda) )

            result = c.fetchall()

            return result

        except Exception as e:
             raise Exception('Erro ao buscar comandas', str(e))

    def contaComandasPorStatus(self, status_comanda):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT COUNT(id_comanda) FROM tb_comanda WHERE status_comanda = %s ',(status_comanda) )

            result = c.fetchone()

            return result

        except Exception as e:
             raise Exception('Erro ao buscar comandas', str(e))

    def selectProdutosPorNumeroComanda(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT nome, quantidade, CONVERT(tbp.valor_unitario, CHAR) FROM tb_produto tbp LEFT JOIN tb_comanda_produto tbpc ON id_produto = produto_id INNER JOIN tb_comanda ON id_comanda = comanda_id WHERE comanda = %s AND status_comanda = %s', (self.comanda, self.status_comanda))

            

            result = c.fetchall()
            c.close()

            return result

        except Exception as e:
             raise Exception('Erro ao buscar produtos das comandas', str(e))

    def fechaComanda(self, total_comandas, valor_total, desconto, data_hora, tipo):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('UPDATE tb_comanda SET status_comanda = %s, status_pagamento = %s WHERE id_comanda = %s', (self.status_comanda, self.status_pagamento, self.id_comanda))

            c.execute('INSERT INTO tb_recebimento(total_comandas, valor_total, desconto, data_hora, tipo) VALUES(%s, %s, %s, %s, %s)', (total_comandas, valor_total, desconto, data_hora, tipo))

            id_recebimento = c.lastrowid #pega o ultimo id inserido no cursor
            c.execute('INSERT INTO tb_comanda_recebimento(recebimento_id, comanda_id) VALUES(%s, %s)', (id_recebimento, self.id_comanda))

            banco.conexao.commit()

           

            return 'Comanda fechada com sucesso!'
        except Exception as e:
             raise Exception('Erro fechar comanda banco', str(e))

        finally:
            c.close()

    def registraComandaFiado(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('UPDATE tb_comanda SET status_comanda = %s, data_assinatura_fiado = %s, cliente_id = %s WHERE id_comanda = %s', (self.status_comanda, self.data_assinatura_fiado, self.cliente_id, self.id_comanda))
            banco.conexao.commit()
            

            return 'Fiado registrado!'

        except Exception as e:
             raise Exception('Erro registra comanda fiado banco', str(e))

        finally:
            c.close()