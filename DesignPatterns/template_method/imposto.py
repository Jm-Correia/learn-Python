import abc
class Template(abc.ABC):
    def calcular(self, orcamento):
        if self.maxima(orcamento):
            return self.taxa_maxima(orcamento)
        else:
            return self.taxa_minima(orcamento)

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


