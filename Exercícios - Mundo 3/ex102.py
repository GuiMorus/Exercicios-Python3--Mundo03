# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular
# O segundo chamado show, que será um valor lógico(e opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

# --Função fazendo calculo fatorial
def fatorial(x=1, show=False):
    # DOCSTRING
    """
    x: Int
    show: Bool

    Esta função faz o calculo fatorial do valor passado em x e mostra seu resultado.

    show=True: Retorna o valor de 'metodo', resultado onde mostra como foi feito o calculo
    show=False: Retorna o valor de 'fator', resultado do fator definido por 'x'

    """

    # Iniciando variáveis
    fator = 1
    metodo = ''

    # Repetição calculando o fator
    for c in range(x, 0, -1):
        # Valor do fator
        fator *= c

        # Metodo do calculo
        if c != 1:
            metodo += f' {c} X'
        else:
            metodo += f' {c} = {fator}'

    # Definindo valor a ser retornado
    if show:
        # Retornando o valor do metodo
        return metodo.strip()
    else:
        # Retornando somente o resultado do fator
        return fator


# ---Programa Principal---
print(fatorial())
