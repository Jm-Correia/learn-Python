import abc

class interfaceVeiculo(abc.ABC):

    @abc.abstractmethod
    def changeColor(self, cor):
        pass
