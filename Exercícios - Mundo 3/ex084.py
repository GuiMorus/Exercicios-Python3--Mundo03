# Faça um programa que leia nome e peso de várias pessoas, guardando em uma única lista.
# No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves

# Iniciando variável
pessoas = []

# Laço resgatando nome e peso
while True:
    nome = str(input("Digite seu nome: ").strip())
    peso = float(input("Digite seu peso: ").strip())

    # Cadastrando informações na lista
    pessoas.append([nome, peso])

    # Verificando continuidade
    sair = str(input("\nDeseja continuar? [S/N]: ").strip().lower())

    # Tratando informação
    sair.replace('sim', 's')
    sair.replace('não', 'n')
    sair.replace('nao', 'n')

    if sair == 'n':
        print("\033[32m" + "Pessoas cadastradas com sucesso", "\033[m \n")
        break

# Introdução
print("-" * 15)

# QUESTÃO A

# Mostrando quantas pessoas foram cadastradas
print(f"No total foram cadastradas {len(pessoas)} pessoas")

# QUESTÃO B

pesos = []
# Repetição agrupando os pesos
for n in pessoas:
    pesos.append(n[1])

# Verificando o maior peso
maior = max(pesos)
menor = min(pesos)  # Para Questão C

# Mostrando os mais pesados
print(f"\nO maior peso registrado foi {maior}Kg e são eles:")

for n in pessoas:
    if n[1] == maior:
        print(n[0].title(), end=", ")

# QUESTÃO C

# Mostrando os mais leves
print(f"\nO menor peso registrado foi {menor} e são eles:")

for n in pessoas:
    if n[1] == menor:
        print(n[0].title(), end=", ")
