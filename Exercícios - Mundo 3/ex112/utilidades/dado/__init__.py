# --Função verificando se o número é float
def isfloat(n):
    try:
        n = float(n)
        return True
    except ValueError:
        return False


# --Função tratando dados
def leiaDinheiro(msg=''):
    # Loop recuperando informação
    while True:
        # Variável resgatando o valor
        valor = input(msg)

        # Tratando informação
        valor = valor.strip().replace(',', '.')

        # Verificando se o número é float
        if isfloat(valor):
            valor = float(valor)
            return valor
        else:
            print("\033[31m" + f"ERRO: '{valor}' é um preço inválido", "\033[m \n")
