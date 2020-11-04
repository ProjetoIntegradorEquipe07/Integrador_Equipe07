from bancoBD import Banco

class Empresa():
    def __init__(self, multa_atraso=0, taxa_juro_diario=0):
        self.multa_atraso = multa_atraso
        self.taxa_juro_diario = taxa_juro_diario

    def select(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT multa_atraso, taxa_juro_diario FROM tb_empresa')

            result = c.fetchall()

            return result
        
        except Exception as e:
            raise Exception('Falha ao consultar as configurações', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()
            