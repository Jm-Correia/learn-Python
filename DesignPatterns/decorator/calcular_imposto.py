class Calcular_importo(object):
    def calcular_imposto(self, orcamento, imposto):
        return imposto.calcular(orcamento)


if __name__ == '__main__':

    from decorator.orcamento import Orcamento
    from decorator.imposto import ICMS, ISS, ICD

    calcular_imposto = Calcular_importo()

    orcamento = Orcamento(1500)

    devido_icms = calcular_imposto.calcular_imposto(orcamento, ICMS())
    devido_iss = calcular_imposto.calcular_imposto(orcamento, ISS())
    devido_icd = calcular_imposto.calcular_imposto(orcamento, ICD(ISS()))
    print(f"ICMS: {devido_icms}, ISS: {devido_iss}, ICD {devido_icd}")