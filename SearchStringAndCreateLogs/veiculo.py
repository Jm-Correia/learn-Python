import abc

class Veiculo(abc.ABC):

    def __init__(self, cor, tipoCombustivel, potencia):
        self.cor = cor
        self.tipoCombustivel = tipoCombustivel
        self.__potencia = potencia

    @abc.abstractmethod
    def changeColor(self, cor):
        self.cor = cor

    def __str__(self):
        return f"Cor:{self.cor}, Tipo de Combustivel {self.tipoCombustivel} , " \
               f"Potencia {self.potencia}"

    def get_potencia(self):
        return self.__potencia

    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, portencia):
        self.__potencia = portencia