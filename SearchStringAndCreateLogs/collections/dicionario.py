dicionario = {1: "João", 2: "Correia"}

print(dicionario)

retorno = dicionario.pop(1)

print(retorno, dicionario)
dicionario[3] = "Marcos"
for i, r in dicionario.items():
    print(i, r)

