from collections import deque

fila = deque(["Joao", "Marcos", "Correia"])

print(fila)

#primeiro por favor
pessoa = fila.popleft();

print(pessoa)
print(fila)
#Segundo por favor
pessoa = fila.popleft();

print(pessoa)
print(fila)