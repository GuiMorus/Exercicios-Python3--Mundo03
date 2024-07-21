# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
# No final mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.

# Iniciando variável
numeros = []

# Repetição recuperando números
for c in range(0, 4):
    numero = int(input("Digite um valor: "))
    numeros.append(numero)

# Criando a tupla
valores = tuple(numeros)

# Mostrando quantas vezes aparece o 9
print(f"O número 9 apareceu {valores.count(9)} vezes")

# Mostrando posição do número 3
if valores.count(3) != 0:
    print(f"O primeiro valor 3 encontrado está na {valores.index(3) + 1}° posição")
else:
    print("O valor 3 não consta dentro da tupla")

# Mostrando valores pares
print("Os valores pares digitados foram: ", end="")
for p in valores:
    if p % 2 == 0:
        print(p, end=", ")
