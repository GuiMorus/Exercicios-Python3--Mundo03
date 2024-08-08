# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.

# --Função verificando número int
def leiaInt(msg=''):
    # Loop do comando principal
    while True:

        # Verificando se o número passado é inteiro
        try:
            # Resgatando e tratando informação
            n = int(input(msg).strip())
        except KeyboardInterrupt:
            # Caso o usuário interrompa o programa
            print("\033[31m" + "ERRO, programa interrompido", "\033[m \n")
            exit()
        except (ValueError, TypeError):
            # Caso seja um erro de tipo ou valor
            print("\033[31m" + "ERRO, digite um número inteiro", "\033[m \n")
        else:
            return n


# --Função verificando número float
def leiaFloat(msg=''):
    # Loop do programa principal
    while True:
        # Verificando possíveis erros
        try:
            # Recolhendo e tratando informação
            n = float(input(msg).strip())
        except KeyboardInterrupt:
            # Caso o usuário interrompa o programa
            print("\033[31m" + "ERRO, programa interrompido", "\033[m \n")
            exit()
        except (ValueError, TypeError):
            # Caso seja um erro de tipo ou valor
            print("\033[31m" + "ERRO, digite um número decimal", "\033[m \n")
        else:
            return n


# Variáveis resgatando números digitados
n1 = leiaInt("Digite um número inteiro: ")
n2 = leiaFloat("Digite um número decimal: ")
print(f"O número inteiro digitado foi {n1}")
print(f"O número float digitado foi {n2}")
