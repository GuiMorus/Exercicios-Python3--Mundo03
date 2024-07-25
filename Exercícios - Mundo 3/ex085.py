# Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em
# uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente

# Iniciando variável
numeros = [[], []]

# Laço recuperando os números
c = 1
while c <= 7:
    num = int(input(f"Digite o {c}° número: "))
    c += 1  # Aumentando contador

    # Adicionando pares na lista
    if num % 2 == 0:
        numeros[0].append(num)

    # Adicionando ímpares na lista
    if num % 2 == 1:
        numeros[1].append(num)

# Mostrando pares
print("\n" + "-" * 30)  # Introdução
print("Os pares em ordem crescente são:")
print(sorted(numeros[0]))

# Mostrando ímpares
print("")   # Pulando linha
print("Os ímpares em ordem crescente são:")
print(sorted(numeros[1]))
