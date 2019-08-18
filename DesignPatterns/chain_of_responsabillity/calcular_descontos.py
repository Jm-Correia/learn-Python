from chain_of_responsabillity.tipos_descontos import Descontos_by_itens,Descontos_above_500,Desconto_default

class Calcular_descontos(object):

    def calcular(self, orcamento):
        desconto = Descontos_by_itens(Descontos_above_500(Desconto_default())).calcular(orcamento)
        print(desconto)


if __name__ == '__main__':

    from chain_of_responsabillity.orcamento import Orcamento,Item

    orc = Orcamento()
    orc.adicionar_itens(Item('1', 100))
    orc.adicionar_itens(Item('2', 100))
    orc.adicionar_itens(Item('3', 200))
    orc.adicionar_itens(Item('4', 700))
    print(orc.valor)
    calc_desconto = Calcular_descontos()
    calc_desconto.calcular(orc)