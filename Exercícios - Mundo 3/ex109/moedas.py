# --Função fazendo o dobro do valor
def dobro(valor, formatar=False):
    calc = valor * 2
    return calc if not formatar else moeda(calc)


# --Função fazendo a metade do valor
def metade(valor, formatar=False):
    calc = valor / 2
    return calc if not formatar else moeda(calc)


# --Função aumentando valor em porcentagem
def aumentar(valor, porcent, formatar=False):
    calc = valor + (valor * porcent / 100)
    return calc if not formatar else moeda(calc)


def diminuir(valor, porcent, formatar=False):
    calc = valor - (valor * porcent / 100)
    return calc if not formatar else moeda(calc)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')