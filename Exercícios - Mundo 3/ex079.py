# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

# Iniciando variáveis
numeros = []

# Laço resgatando números digitados
while True:
    numero = int(input("Digite um número: "))

    # Parando repetição
    print("\033[31m" + "Digite -1 para sair \n", "\033[m")
    if numero <= 0:
        break

    # Adicionando número na lista caso não exista
    if numero not in numeros:
        numeros.append(numero)
    else:
        print(f"O número {numero} já está cadastrado")

# Mostrando resultado
numeros.sort()
print("Os números digitados em ordem crescente foram:")
print(numeros)
