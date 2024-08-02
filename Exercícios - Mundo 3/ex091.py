# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

# Iniciando variável
jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
    }

# Mostrando resultados dos jogadores
for k, v in jogo.items():
    print(f"O {k} jogou o número {v} no dado")
    sleep(0.5)

print("-" * 30)

# Mostrando jogadores em ordem
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("COLOCAÇÃO:")
for k, v in enumerate(rank):
    if k == 0:
        print(f"O Campeão é o {v[0]} que tirou {v[1]}")
    else:
        print(f"{k + 1}º Lugar: {v[0]} tirou {v[1]}")
