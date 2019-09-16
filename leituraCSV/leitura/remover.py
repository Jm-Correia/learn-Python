from datetime import date

data_com = date(int(2018),int(9),int(1))

arquivo = open("arquivo_saida.txt", "r").readlines()
arquivo_final = open("arquivo_final.txt", "w")
count_p = 0
count_l =0
lista_t, lista_g, lista_m, lista_l, lista_n, lista_v = []

for linha in arquivo:
    i = linha.index("/")
    i -=2
    f = len(linha)-4
    aux = linha[i:f].__str__()

    ano, mes, dia = int(aux[6:]), int(aux[3:5]),int(aux[:2])
    print(ano, mes, dia)
    data_aux = date(ano, mes, dia)

    print(data_aux)
    if data_aux > data_com:
        arquivo_final.write(linha)
        count_l +=1

    count_p +=1

arquivo_final.write(f"Linhas Adicionadas ao Arquivo{count_l}")

arquivo_final.write(f"Linhas processadas do arquivo de origem {count_p}")
arquivo_final.close()