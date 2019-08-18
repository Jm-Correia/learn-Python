class Calcular_importo(object):
    def calcular_imposto(self, orcamento, imposto):
        return imposto.calcular(orcamento)


if __name__ == '__main__':

    from strategy.orcamento import Orcamento
    from strategy.imposto import ICMS, ISS, ICD

    calcular_imposto = Calcular_importo()

    orcamento = Orcamento(500)

    devido_icms = calcular_imposto.calcular_imposto(orcamento, ICMS())
    print(devido_icms)
    devido_iss = calcular_imposto.calcular_imposto(orcamento, ISS())
    print(devido_iss)
    devido_icd = calcular_imposto.calcular_imposto(orcamento, ICD())
    print(devido_icd)