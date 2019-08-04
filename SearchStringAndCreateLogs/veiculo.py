import abc, interface_veiculo

class Veiculo(interface_veiculo.interface_Veiculo, abc.ABC):

    def __init__(self, cor, tipoCombustivel, potencia):
        self.cor = cor
        self.tipoCombustivel = tipoCombustivel
        self.__potencia = potencia

    def changeColor(self, cor):
        self.cor = cor

    @property
    def potencia(self):
        self.__changePotencia(" PRIVATE METHOD? ")
        return self.__potencia

    @potencia.setter
    def potencia(self, portencia):
        self.__potencia = portencia

    def __changePotencia(self,pot):
        self.__potencia = pot

    def __str__(self):
        return f"Cor:{self.cor}, Tipo de Combustivel {self.tipoCombustivel} , " \
               f"Potencia {self.potencia}"


