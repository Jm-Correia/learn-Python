import usuario
import carro

c = carro.Carro("Red", 4, "FLEX", "80v")
print(c.cor)
c.changeColor("BLACK")
print(c.cor)
print(c.__str__())

list = []
us = usuario.Usuario("João", 34, "Correia")
list.append(us)

print(f"olá, {us.nome} {us.idade}, sua idade é {us.sobrenome}")

potencia = 5%3
print(potencia)

for x in range(1,10):
    y = x
print(x,y)
