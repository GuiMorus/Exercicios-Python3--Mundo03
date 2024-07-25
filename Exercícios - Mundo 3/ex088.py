# Faça um programa que ajude um jogador da Mega Sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

# Iniciando variável
sorteados = []

# Variável resgatando quantidade de jogos a gerar
print("=" * 15, end="")
print("[ MEGA-SENA GENERATOR ]", end="")
print("=" * 15)
jogos = int(input("Quer gerar quantos jogos?: "))

# Repetição gerando números aleatórios
for c in range(0, jogos):
    while len(sorteados) < 6:
        num = randint(1, 60)

        # Verificando se o número não existe
        if num not in sorteados:
            sorteados.append(num)

    # Mostrando números sorteados
    sorteados.sort()
    print(f"{c + 1}° jogo: {sorteados}")

    # Reiniciando lista dos números sorteados
    sorteados.clear()
    sleep(0.8)  # Pausa da animação

