from abc import abstractmethod, ABC, ABCMeta
import hashlib

class Funcoes(metaclass=ABCMeta):#Cria classe abstrata

    #método abstrato
    @abstractmethod
    def criptografaSenha(senha):
        return hashlib.sha3_256(senha.encode('utf-8')).hexdigest()