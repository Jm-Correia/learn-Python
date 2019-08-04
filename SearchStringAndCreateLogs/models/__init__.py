import usuario
import carro

c = carro.Carro("Red", "FLEX", "80v", 5)
print(c.cor)
c.changeColor("Orange")
print(c.cor)
print(c.__str__())
c.potencia = "100v"
print(c.__str__())


list = []
us = usuario.Usuario("João", 34, "Correia")
list.append(us)

print(f"olá, {us.nome} {us.sobrenome}, sua idade é {us.idade}")

pot = 5 % 3
print(pot)

for x in range(1,10):
    y = x
print(x,y)