from abc import abstractmethod, ABC, ABCMeta
from enum import Enum
import logging
import hashlib
from flask import session

class LOG(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'


class Funcoes(metaclass=ABCMeta):#Cria classe abstrata

    #método abstrato
    @abstractmethod
    def criptografaSenha(senha):
        return hashlib.sha3_256(senha.encode('utf-8')).hexdigest()

    @abstractmethod
    def criaLOG(mensagem, tipo):
        logging.basicConfig(filename='pastelariaDoZe.log', format='%(levelname)s| %(name)s | %(asctime)s | %(message)s ', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
        print(tipo)        
        if tipo == LOG.info:            
            logging.info(f'{mensagem} Usuario: {session["id"]}')
        elif tipo == LOG.warning:            
            logging.warning(f'{mensagem} Usuario: {session["id"]}')
        elif tipo == LOG.error:
            logging.error(f'{mensagem} Usuario: {session["id"]}')
    