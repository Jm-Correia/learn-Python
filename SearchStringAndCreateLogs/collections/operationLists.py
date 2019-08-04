listSimples = [1, 2, 3, 4, 5]
listSimplesTxt = ["Olá", "Mundo"]
listMescla = [1, 2, [1, 2, 3], "Olá", "Fulano"]

print(sum(listSimples))
print(listSimplesTxt)

#len()
print(len(listSimples))
for x in listSimples:
    print(x)

#count()
qtd = listMescla.count(2)
print(qtd)

#copy()
listBack = listSimples.copy()
listBack[0] = 12
#pop()
listSimples.pop(2)

print(listSimples, listBack)

#lists comprehension
listQuadrado = [i**2 for i in listSimples]
print(listQuadrado)

#slice
listMetade = listSimples[:2]
print(listMetade)

