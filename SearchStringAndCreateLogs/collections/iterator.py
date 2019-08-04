listSimples = [1, 2, 3, 15, 78, 100, 105, 101, 2556, 225698, 111111, 25655887944513]

iter = iter(listSimples)

print(next(iter))

def elava_dois(max=0):
    n = 0
    while n <= max:
        yield 2 ** n
        n += 1
for y in elava_dois(10):
    print(y)

class Iterator:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n =0
        return self

    def __next__(self):
        if self.n <= self.max:
            resultado = 2 ** self.n
            self.n += 1
            return resultado
        else:
            raise StopIteration

for i in Iterator(5):
    print(i)