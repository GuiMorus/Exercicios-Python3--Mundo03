# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o
# maior valor que estão na tupla

from random import randrange

# Iniciando variável
aleatorios = []

# Repetição gerando números aleatórios
for c in range(0, 5):
    aleatorios.append(randrange(100))

# Gerando tupla com resultados da lista
resultado = tuple(aleatorios)
print("Números aleatórios gerados:", resultado)

# Indicando menor e maior valor
print(f"Menor valor: {sorted(resultado)[0]}")
print(f"Maior valor: {sorted(resultado)[-1]}")
