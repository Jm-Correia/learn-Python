import os
import datetime
from pathlib import Path
import shutil

class Leitura(object):
    def __init__(self, diretorio ,pasta):
        self.__diretorio = diretorio
        self.__pasta = pasta
        self.__path_completo = diretorio + "://" + pasta
        self.pasta_projeto = diretorio + "://" + "z__organizador_ws"
        Path(self.pasta_projeto).mkdir(exist_ok=True)

    def concat_path(self, path):
        return self.pasta_projeto + "/" + path

    def __criar_log(self):
        b = self.concat_path("LOG")
        print(b)
        p = Path(b)
        p.mkdir(exist_ok=True)
        self.__caminho = self.concat_path("LOG/log.txt")

    def __escrever_log(self, texto):
        if self.__verificarFile():
            arquivo = open(self.__caminho, 'a')
            arquivo.write(texto + "\n")
            arquivo.close()
        else:
            arquivo = open(self.__caminho, 'w')
            arquivo.write("#" * 54 + "\n")
            arquivo.write("#" * 20)
            arquivo.write(" Inicio - LOG ")
            arquivo.write("#" * 20)
            arquivo.write("\n")
            arquivo.write("#" * 54 + "\n")
            arquivo.close()
            self.__escrever_log(texto)

    def __verificarFile(self):
        return os.path.isfile(self.__caminho)

    def __lista_diretorios(self, path = None):
        if path is not None:
            return Path(path).iterdir()
        else:
            return Path(self.__path_completo).iterdir()

    def create_folder_Eleita(self):
        list = self.__lista_diretorios()
        self.__criar_log()
        now = datetime.datetime.now()
        d = now.strftime('%Y%m%d%H%M%S') + "_ELEITA"
        to_path = self.concat_path(d)
        p = Path(to_path)
        p.mkdir(exist_ok=True)
        winner = []
        self.__escrever_log("-=" * 30)
        self.__escrever_log("Lendo Diretorios..." + datetime.datetime.now().__str__())
        self.__escrever_log("-=" * 30)
        for d in list:
            self.__escrever_log(f"Lendo sub_diretorio: {d.absolute()} ")
            if d.is_dir():
                aux = [dc for dc in os.listdir(d.absolute()) if not os.path.isfile(os.path.join(d.absolute(), dc))]
                self.__escrever_log(f"Lista: {aux} ")
                for a in aux:
                    if a not in winner:
                        winner.append(a)
                        from_path = self.__path_completo + "/" + d.absolute().name + "/"+ a
                        _to_path = to_path + "/" + a
                        self.__escrever_log(f"Copiando de: {from_path} para {_to_path}")
                        self.copy_folder(from_path, _to_path)
            self.__escrever_log("-=" * 30)
        return to_path

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

    def copy_folder(self, from_path, to_path):
        shutil.copytree(from_path, to_path)

if __name__ == '__main__':
    leitura = Leitura("C","Projetos")

    leitura.create_folder_Eleita()
