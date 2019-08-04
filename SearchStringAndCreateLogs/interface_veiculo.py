import abc

class interface_Veiculo(abc.ABC):

    @abc.abstractmethod
    def changeColor(self, cor):
        pass
