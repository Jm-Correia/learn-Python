import os
from datetime import datetime, date
from pathlib import Path
import collections

class migracaoIP(object):
    def __init__(self, caminho):
        self.__caminho = caminho
        self.dicionario = {}
        self.list_p = []
        self.ip_1 = "172.30.1.6"
        self.ip_2 = '129.144.51.232'

    def listar_diretorios(self):
        return Path(self.__caminho).iterdir()

    def listar_sub_diretorios(self, basePath):
        return os.listdir(basePath)


    def criar_dicionario(self, lista):
        for row in lista:
            base = f"{row.absolute()}/src/"
            a = self.listar_sub_diretorios(base)

            self.dicionario[base] = a
            self.list_p = []
        self.verficar_jar()

    def verficar_jar(self):
       primeiro_nivel = []
       for key in self.dicionario.keys():
            lista_aux = self.dicionario.get(key)

            for sub in lista_aux:
                base = f"{key}\{sub}"
                if os.path.isdir(base):

                    file = [dc for dc in os.listdir(base) if os.path.isfile(os.path.join(base, dc))]

                    if sub == "java":
                        primeiro_nivel = [dc for dc in os.listdir(base) if os.path.isdir(os.path.join(base, dc))]


                        for row_aux in primeiro_nivel:

                            if f'{row_aux}' in ('bean', 'dao', 'negocio', 'fachada', 'seguranca', 'basicas'):
                                path = f"{key}{sub}/{row_aux}"

                                file_aux = [dc for dc in os.listdir(path) if os.path.isfile(os.path.join(path, dc))]
                                print(file_aux)
                                for row in file_aux:


                                    if row.find(".java") != -1:

                                        arquivo = open(f'{path}/{row}', "r")
                                        count = 0
                                        for linha_a in arquivo:
                                            count += 1
                                            if linha_a.find(self.ip_1) != -1 or linha_a.find(self.ip_2) != -1:
                                                log = open(f"{row}.log", "w")
                                                log.write(path + "\n")
                                                log.write(f"{count} {linha_a}\n")



                    for row in file:
                        path = f"{key}{sub}\{row}"


                        if row.find(".java") != -1:

                            arquivo = open(path, "r")
                            count =0
                            for linha_a in arquivo:
                               count += 1
                               if linha_a.find(self.ip_1) != -1 or linha_a.find(self.ip_2) != -1:
                                   log = open(f"{row}.log", "w")
                                   log.write(path+"\n")
                                   log.write(f"{count} {linha_a}\n")



if __name__ == "__main__":
    projeto = migracaoIP("E:\#ProjetosGit")
    lista = projeto.listar_diretorios()

    projeto.criar_dicionario(lista)
