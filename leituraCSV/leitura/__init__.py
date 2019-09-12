import csv
from collections import OrderedDict
from datetime import date

arquivo_texto = open("arquivo_saida.txt", "w")
with open("SO.CSV") as cvs_file:
    cvs_arquivo = csv.DictReader(cvs_file, delimiter=";")
    count = 0;

    for row in cvs_arquivo:

        if count == 0:
            count += 1
            continue
        else:
            lista = list(row.items())
            dic = dict(lista)
            sistema = dic.pop("ID")
            dic_2 = dic.copy()
            for key in dic_2.keys():
                if dic.get(key) == "":
                    dic.pop(key)
            #ultimo = OrderedDict(sorted(dic.items(), key=lambda t: (t[1])))
            print(dic)
            if dic.__len__() == 0:
                continue
            ultimo = OrderedDict(
                sorted(dic.items(), key=lambda t: date(int(t[1][6:10]), int(t[1][3:5]), int(t[1][:2])))).popitem()


            texto = f"Sistema: {sistema}  computador de" \
                    f" {ultimo.__str__()} \n"
            arquivo_texto.write(texto)
            print(texto)

        count += 1

    print(f'Linhas {count} Processadas')

arquivo_texto.close()