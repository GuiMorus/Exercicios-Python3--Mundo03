# Crie um programa que tenha a função leiaint(), que vai funcionar de forma
# semelhante à função input() do Python, só que fazendo a validação para aceitar
# apenas um valor númerico

# --Função lendo números inteiros
def leiaInt(string=''):
    # DOCSTRING
    """
    string: String

    Está função verifica se o valor digitado é um número inteiro.
    Enquanto o usuário não passar um valor que seja Int() a função continuará
    exibindo uma mensagem de erro.

    """

    # Repetição verificando valor
    while True:
        valor = input(string)

        # Verificando se o valor é um número
        if valor.isnumeric():
            return valor
        else:
            print("\033[31m" + "ERRO! Digite um número inteiro válido", "\033[m\n")


# ---PROGRAMA PRINCIPAL---

# Variável lendo valor int
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
