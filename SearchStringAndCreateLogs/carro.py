import veiculo
class Carro(veiculo.Veiculo):
    def __init__(self,cor, tipoCombustivel, potencia, qtdPortas):
        super().__init__(cor, tipoCombustivel, potencia)
        self.qtdPortas = qtdPortas

    def __str__(self):
        return f"Cor:{self.cor}, Qtd de Portas: {self.qtdPortas}, Tipo de Combustivel: {self.tipoCombustivel} , " \
               f"Potencia: {self.potencia}"

    def changeColor(self, cor):
        self.cor = "<< " + cor + " >>"

