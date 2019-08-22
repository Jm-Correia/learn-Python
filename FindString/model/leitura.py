import os
import datetime
from pathlib import Path
import shutil

class Leitura(object):
    def __init__(self, diretorio ,pasta):
        self.__diretorio = diretorio
        self.__pasta = pasta
        self.__path_completo = diretorio + ":/" + pasta
        self.pasta_projeto = diretorio + ":/" + "z__organizador_ws"
        Path(self.pasta_projeto).mkdir(exist_ok=True)

    def concat_path(self, path):
        return self.pasta_projeto + "/" + path

    def __criar_log(self):
        b = self.concat_path("LOG")
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
        self.to_path = self.concat_path(d)
        p = Path(self.to_path)
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
                        _to_path = self.to_path + "/" + a
                        self.__escrever_log(f"Copiando de: {from_path} para {_to_path}")
                        self.copy_folder(from_path, _to_path)
            self.__escrever_log("-=" * 30)
        self.__escrever_log("Fim da criação Pasta TEMPLATE")
        return p

    def convert_date(self, timestamp):
        data = datetime.datetime.utcfromtimestamp(timestamp)
        data_formatada = data.strftime('%d-%m-%Y %H:%M:%S')
        return data_formatada

    def copy_mais_atual(self):
        path = self.create_folder_Eleita()
        self.__escrever_log("Determinando quais diretorios são os mais atuais.......")
        temp = self.create_new_folder()
        #buscar a pasta mais atual entre todas do diretorio principal
        for _path_atual in path.iterdir():
            print(_path_atual.absolute().name)
            lista_diretorios = self.__lista_diretorios()
            for d in lista_diretorios:
                aux = [dc for dc in Path(d.absolute()).iterdir() if dc.is_dir()]
                for sub_dir in aux:
                    if _path_atual.absolute().name == sub_dir.absolute().name:
                        time_atual = _path_atual.stat().st_mtime
                        time_aux = sub_dir.stat().st_mtime
                        print(sub_dir.absolute(), temp.absolute())
                        #COPIAR A PASTA MAIS
                        # ATUAL SOBREESCREVENDO A ANTIGA NO DIRETORIO TEMP do PROJETO
                        if time_atual > time_aux:
                            print(time_atual>time_aux)
                            break
                        elif time_atual < time_aux:
                            print(time_atual<time_aux)
                            break
                        else:
                            print(time_atual==time_aux)
                            break



    def copy_folder(self, from_path, to_path):
        shutil.copytree(from_path, to_path)

    def create_new_folder(self):
        p = Path(self.concat_path("temp"))
        p.mkdir(exist_ok=True)
        return p
if __name__ == '__main__':
    leitura = Leitura("C","Projetos")

    leitura.copy_mais_atual()
