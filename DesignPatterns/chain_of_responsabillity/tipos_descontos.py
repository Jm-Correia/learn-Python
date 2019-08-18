class Descontos_by_itens(object):
    def __init__(self, next):
        self.__next = next

    def calcular(self, orcamento):
        if orcamento.total_itens == 5:
            return orcamento.valor * 0.05
        else:
            return self.__next.calcular(orcamento)


class Descontos_above_500(object):
    def __init__(self, next):
        self.__next = next

    def calcular(self, orcamento):
        if orcamento.valor <= 500:
            return orcamento.valor * 0.07
        else:
            return self.__next.calcular(orcamento)


class Desconto_default(object):
    def calcular(self, orcamento):
        return orcamento.valor * 0.1
