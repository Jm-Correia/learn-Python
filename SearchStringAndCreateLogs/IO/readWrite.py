import random

arquivo = open("palavra.txt", "w")
arquivo.write("Banana\n")
arquivo.write("Morango\n")
arquivo.write("Melancia\n")
arquivo.close()

search = open("palavra.txt", "r")
list =[]
for s in search:
    s = s.strip()
    list.append(s)
search.close()
n = random.randrange(0, len(list))

print(list[n])