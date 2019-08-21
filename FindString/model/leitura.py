import os
import datetime
from pathlib import Path
import shutil

class Leitura(object):
    def __init__(self, pasta_principal):
        self.__pasta_principal = pasta_principal
        self.__criar_log()

    def __criar_log(self):
        if os.path.exists(self.__pasta_principal + "/LOG"):
            caminho = self.__pasta_principal + "/LOG/log.txt"
        else:
            os.mkdir(self.__pasta_principal + "/LOG", 1)
            self.__criar_log()
        self.__caminho = caminho

    def __escrever_log(self, texto):
        if self.__verificarFile():
            arquivo = open(self.__caminho, 'a')
            arquivo.write(texto + "\n")
            arquivo.close()
        else:
            arquivo = open(self.__caminho, 'w')
            arquivo.write("######################################################################\n")
            arquivo.write("########################### INICIO DO LOG ############################\n")
            arquivo.write("######################################################################\n")
            arquivo.close()
            self.__escrever_log(texto)

    def __verificarFile(self):
        return os.path.isfile(self.__caminho)

    def __lista_diretorios(self, path = None):
        if path is not None:
            return Path(path).iterdir()
        else:
            return Path(self.__pasta_principal).iterdir()

    def listar_projetos(self):
        diretorios = self.__lista_diretorios()
        retorno = list()
        for root in diretorios:
            path = self.__pasta_principal + "/" + root.name
            retorno.append({path: self.__lista_diretorios(path)})

        self.__escrever_log("-=" *15)
        self.__escrever_log("Lendo Diretorios..." + datetime.datetime.now().__str__())
        self.__escrever_log(retorno.__str__())
        self.__escrever_log("-=" *15)

        return retorno

    def convert_date(self, timestamp):
        data = datetime.datetime.utcfromtimestamp(timestamp)
        data_formatada = data.strftime('%d-%m-%Y %H:%M:%S')
        return data_formatada


    def is_mais_atual(self):
        self.__escrever_log("Determinando quais diretorios são os mais atuais.......")
        list_diretorios = self.listar_projetos()

        path_aux_maior = list_diretorios[0].copy()
        print(f"Lista template de Comparação:{path_aux_maior}")
        for i in range(1, len(list_diretorios)):
            print(list_diretorios[i])


    #exemplo
    # lista_final =list(set(lista_1) - set(lista_2)) nao irá retornar elementos repetidos
    # or [x for x in lista_2 if x not in lista_1] caso queria retornar elementos repetidos

    def copy_to_temp(self, from_path, to_path):
        shutil.copytree(from_path, to_path)

if __name__ == '__main__':
    leitura = Leitura("C://Projetos")

    leitura.is_mais_atual()
