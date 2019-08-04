from array import array

vetor = array("B", [1, 2, 3, 4, 55])

print(vetor)

for i in vetor:
    if i % 2 != 0:
        vetor.remove(i)

print(vetor)