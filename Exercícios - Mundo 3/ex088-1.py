# Fazendo um gerador de números da Lotofácil

from random import randint
from time import sleep

# Iniciando variável
sorteados = []

# Variável resgatando a quantidade de jogos
print("=" * 20, end="")
print("[ LOTOFÁCIL GENERATOR ]", end="")
print("=" * 20)

jogos = int(input("Quantos jogos quer gerar?: "))

# Repetição gerando números aleatórios
for c in range(0, jogos):
    while len(sorteados) < 15:
        num = randint(1, 25)

        # Verificando números sorteados
        if num not in sorteados:
            sorteados.append(num)

    # Mostrando números sorteados
    sorteados.sort()
    print(f"{c + 1}° sorteio: {sorteados}")

    # Reiniciando lista
    sorteados.clear()
    sleep(0.5)  # Tempo da animação
