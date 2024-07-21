# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
# posições na lista

# Iniciando variável
numeros = []

# Repetição recuperando os números
for c in range(0, 5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Resgatando as posições do maior e menor dos números
maior = max(numeros)
menor = min(numeros)

# Mostrando maior número e posições
c = 1
print(f"O maior número é {maior} e suas posições são: | ", end="")
for n in numeros:
    if n == maior:
        print(f"{c}º", end="| ")
    c += 1

# Mostrando menor número e posições
c = 1
print(f"\nO menor número é {menor} e suas posições são: | ", end="")
for n in numeros:
    if n == menor:
        print(f"{c}°", end="| ")
    c += 1
