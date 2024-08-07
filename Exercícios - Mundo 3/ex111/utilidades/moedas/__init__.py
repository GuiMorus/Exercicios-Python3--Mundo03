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


# --Função diminuindo valor em porgentagem
def diminuir(valor, porcent, formatar=False):
    calc = valor - (valor * porcent / 100)
    return calc if not formatar else moeda(calc)


# --Função formatando a moedas
def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


# --Função resumindo os dados
def resumo(valor, porcentagem_aumentar, porcentagem_reduzir):
    # Introdução
    print("-" * 50)
    print(f"{'RESUMO DO VALOR':^50}")
    print("-" * 50)

    # Montando tabela
    print(f"{'Preço analisado: ':<40}{moeda(valor)}")
    print(f"{'Dobro do preço: ':<40}{dobro(valor, True)}")
    print(f"{'Metade do preço: ':<40}{metade(valor, True)}")
    print(f"{porcentagem_aumentar:<2}% " + f"{'de aumento: ':<36}{aumentar(valor, porcentagem_aumentar, True)}")
    print(f"{porcentagem_reduzir:<2}% " + f"{'de redução: ':<36}{diminuir(valor, porcentagem_reduzir, True)}")
