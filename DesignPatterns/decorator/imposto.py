import abc
class Decorator(abc.ABC):
    def __init__(self, roubo = None):
        self.__roubo = roubo

    def somar_importos(self, orcamento):
        if self.__roubo is not None:
            return self.__roubo.calcular(orcamento)
        else:
            return 0

    @abc.abstractmethod
    def calcular(self, orcamento):
        pass

class Template(Decorator):
    def calcular(self, orcamento):
        if self.maxima(orcamento):
            return self.taxa_maxima(orcamento) + self.somar_importos(orcamento)
        else:
            return self.taxa_minima(orcamento) + self.somar_importos(orcamento)

    @abc.abstractmethod
    def maxima(self, orcamento):
        pass

    @abc.abstractmethod
    def taxa_maxima(self, orcamento):
        pass

    @abc.abstractmethod
    def taxa_minima(self, orcamento):
        pass


class ICMS(Template):

    def maxima(self,orcamento):
        return orcamento.valor > 600

    def taxa_maxima(self, orcamento):
        print(f"ICMS Maximo")
        return orcamento.valor * 0.17

    def taxa_minima(self, orcamento):
        print(f"ICMS Minimo")
        return orcamento.valor * 0.15

class ISS(Template):
    def maxima(self, orcamento):
        return orcamento.valor > 300


    def taxa_maxima(self, orcamento):
        print(f"ISS Maximo")
        return orcamento.valor * 0.06

    def taxa_minima(self, orcamento):
        print(f"ISS Minimo")
        return orcamento.valor * 0.05


class ICD(Template):
    def maxima(self, orcamento):
        return orcamento.valor < 500

    def taxa_maxima(self, orcamento):
        print(f"ICD Maximo")
        return orcamento.valor * 0.04

    def taxa_minima(self, orcamento):
        print(f"ICD Minimo")
        return 0


