from strategy.orcamento import Orcamento

class ICMS(object):
    def calcular(self, orcamento):
        return orcamento.valor * 0.17

class ISS(object):
    def calcular(self, orcamento):
        return orcamento.valor * 0.06

class ICD(object):
    def calcular(self, orcamento):
        return orcamento.valor * 0.4