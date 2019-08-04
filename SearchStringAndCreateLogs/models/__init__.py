import usuario
import carro

c = carro.Carro("Red", "FLEX", "80v", 5)
print(c.cor)
c.changeColor("Orange")
print(c.cor)
print(c.__str__())
c.potencia = "100v"
print(c.__str__())

if isinstance(c, usuario.Usuario):
    print("is a user")
else:
    print("Not a user")

list = []
us = usuario.Usuario("João", 34, "Correia")
list.append(us)

print(f"Hi, {us.nome} {us.sobrenome}, your old is {us.idade}")

pot = 5 % 3
print(pot)

for x in range(1,10):
    y = x
print(x,y)