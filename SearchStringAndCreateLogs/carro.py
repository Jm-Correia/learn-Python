class Carro(object):

    def __init__(self, cor, qtdPortas, tipoCombustivel, potencia):
        self.cor = cor
        self.qtdPortas = qtdPortas
        self.tipoCombustivel = tipoCombustivel
        self.potencia = potencia

    def changeColor(self, cor):
        self.cor = cor

    def __str__(self):
        return f"Cor:{self.cor}, Qtd de Portas {self.qtdPortas}, Tipo de Combustivel {self.tipoCombustivel} , " \
               f"Potencia {self.potencia}"