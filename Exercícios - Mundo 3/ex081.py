# Crie um programa que vai ler vários números e colocá-los em uma lista. Depois mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista

# Iniciando variável
numeros = []

# Laço lendo os números digitados
while True:
    num = input("\nDigite um número: ").lower()

    # Verificando se o usuário deseja sair
    if num == 'sair':
        break

    # Verificando se o usuário digitou um número
    if num.isnumeric():
        num = int(num)       # Convertendo em número
        numeros.append(num)  # Adicionando na lista

    # Mensagem de erro
    else:
        print("\033[33m" + "INVÁLIDO, TENTE NOVAMENTE", "\033[m")

    # Mensagem para sair do programa
    print("Digite", "\033[31m" + "sair" + "\033[m", "para finalizar o programa")

# Mostrando quantos números digitados
print("\n" + "-=-" * 20)
print(f"Foram digitados {len(numeros)} números")

# Mostrando lista em ordem decrescente
numeros.sort(reverse=True)
print("\nLista em ordem decrescente:")
print(numeros)

# Mostrando se há valor 5 na lista
print("")   # pulando linha
if 5 in numeros:
    vezes = numeros.count(5)
    print(f"Existe número 5 e foi digitado {vezes} vezes")
else:
    print("Não há número 5 dentro da lista")
