from bancoBD import Banco

class Funcionario():
    def __init__(self, id_funcionario=0, nome="", cpf="", telefone="", senha="", matricula="", grupo=2):
        self.id_funcionario = id_funcionario
        self.nome= nome
        self.cpf = cpf
        self.telefone = telefone
        self.senha = senha
        self.matricula = matricula
        self.grupo = grupo

    def selectAll(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT id_funcionario, nome, matricula, grupo FROM tb_funcionario')

            result = c.fetchall()
            c.close()
            return result
        except Exception as e:
            return 'Erro ao buscar funcionários!'

    def selectOne(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()
            c.execute('SELECT id_funcionario, nome, cpf, telefone, senha, matricula, grupo FROM tb_funcionario where id_funcionario = %s',(self.id_funcionario))

            for linha in c:
                self.id_funcionario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.senha = linha[4]
                self.matricula = linha[5]
                self.grupo = linha[6]

            c.close()

            return 'Busca feita com sucesso!'

        except:
            return 'Erro ao buscar cliente!'

    def insert(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('INSERT INTO tb_funcionario(nome,cpf,telefone,senha,matricula,grupo) VALUES(%s,%s,%s,%s,%s,%s)',(self.nome,self.cpf,self.telefone,self.senha,self.matricula,self.grupo))
            banco.conexao.commit()
            c.close()

            return 'Funcionário cadastrado com sucesso!'

        except Exception as e:
            
            raise Exception('Erro ao cadastrar funcionario!', str(e))
    
    def update(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('UPDATE tb_funcionario SET nome=%s,cpf=%s,telefone=%s,senha=%s,matricula=%s,grupo=%s WHERE id_funcionario=%s',(self.nome,self.cpf,self.telefone,self.senha,self.matricula,self.grupo,self.id_funcionario))
            banco.conexao.commit()
            c.close()

            return 'Funcionário editado com sucesso!'

        except Exception as e:
            raise Exception('Erro ao editar funcionário!', str(e))

    def delete(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('DELETE FROM tb_funcionario WHERE id_funcionario = %s',(self.id_funcionario))

            banco.conexao.commit()
            c.close()

            return 'Funcionário excluído com sucesso'

        except Exception as e:
            raise Exception('Erro ao excluir funcionário', str(e))

    
    def selectLogin(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT id_funcionario, nome, grupo FROM tb_funcionario WHERE nome=%s and senha=%s', (self.nome, self.senha))

            result = c.fetchall()
            if len(result) > 0:
                for linha in result:                    
                    self.id_funcionario = linha[0]
                    self.nome = linha[1]
                    self.grupo = linha[2]
                c.close()
                return True

            else:
                c.close()
                return False

            
            

        except Exception as e:
            raise Exception('Erro ao tentar validar login!', str(e))

    def validaMatriculaExistente(self):
        try:
            banco = Banco()
            c = banco.conexao.cursor()

            c.execute('SELECT id_funcionario FROM tb_funcionario WHERE matricula=%s',(self.matricula))

            result = c.fetchall()

            c.close()
            return result

        except Exception as e:
            raise Exception('Erro ao tentar validar matricula', str(e))