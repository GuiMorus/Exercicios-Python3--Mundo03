# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, todas as informações serão guardadas
# em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Iniciando variáveis
jogador = {}
gols = []

# Resgatando informações do usuário
nome = input("Nome do jogador: ").strip().title()
partidas = int(input("Quantas partidas jogou: ").strip())

# Repetição recuperando quantidade de gols por partida
for n in range(0, partidas):
    gol = int(input(f"Quantos GOLS na {n + 1}° partida: ").strip())
    gols.append(gol)

total = sum(gols)   # Somando total de partidas

# Colocando informações no dicionário
jogador['Nome'] = nome
jogador['Gols'] = gols[:]
jogador['Total de gols'] = total

# Mostrando informções de 3 modos diferentes
print("-" * 30)     # PRIMEIRO MODO
print(jogador)

print("-" * 30)     # SEGUNDO MODO
for k, v in jogador.items():
    print(f"{k} do jogador: {v}")

print("-" * 30)     # TERCEIRO MODO
print(f"O jogador {jogador['Nome']} jogou {partidas} partidas")
for i, v in enumerate(jogador['Gols']):
    print(f"Na {i + 1}° partida: {v} gols.")

print(f"Fez um total de {jogador['Total de gols']} GOLS!!")
