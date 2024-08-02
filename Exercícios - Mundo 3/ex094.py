# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
# cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
# A) Quantas pessoas cadastradas
# B) A média de idade de todos
# C) Uma lista com mulheres
# D) Uma lista com idades acima da média.

# Iniciando variáveis
usuario = {}
pessoas = []
mulheres = []
velhos = []
ativo = True
mensagem_erro = "\033[31m" + "INFORMAÇÃO INCORRETA, TENTE NOVAMENTE!" + "\033[m\n"

# Laço resgatando informações dos usuários
while ativo:
    # Resgatando nome
    while True:
        nome = input("Nome: ").strip().title()

        # Verificando informação
        if nome.replace(" ", '').isalpha():
            usuario['Nome'] = nome
            break
        else:
            print(mensagem_erro)

    # Resgatando idade
    while True:
        idade = input("Idade: ").strip()

        # Verificando informação
        if idade.isnumeric():
            usuario['Idade'] = int(idade)
            break
        else:
            print(mensagem_erro)

    # Resgatando sexo
    while True:
        sexo = str(input("Sexo [M/F]: ").strip().lower())

        # Verificando informação
        if sexo == 'm' or sexo == 'f':
            usuario['Sexo'] = sexo
            break
        else:
            print(mensagem_erro)
            print("DIGITE APENAS NÚMEROS INTEIROS \n")

    # Adicionando informações na lista
    pessoas.append(usuario.copy())

    # Verificando continuidade
    while True:
        continuar = input("Deseja continuar? [S/N]: ").strip().lower()

        if continuar == 'n':
            print("-" * 20, end="")
            print(" CADASTRO ENCERRADO ", end="")
            print("-" * 20)
            ativo = False
            break
        elif continuar == 's':
            print()     # Pulando linha
            break
        else:
            print(mensagem_erro)

# Mostrando quantas pessoas foram cadastradas
print()     # Pulando linha
print(f"A) No total foram cadastradas {len(pessoas)} pessoas")

# Mostrando a média das idades
idades = 0
for n in pessoas:
    idades += n['Idade']

media = idades / len(pessoas)
print(f"B) A média da idade de todos é {media:.2f} anos")

# Mostrando as mulheres cadastradas
print("C) As mulheres cadastradas são: ", end="")
for n in pessoas:
    if n['Sexo'] == 'f':
        mulheres.append([n['Nome'], n['Idade'], n['Sexo']])

for n in mulheres:
    print(f"{n[0]}; ", end="")

# Mostrando pessoas com idade acima da média
print()     # Pulando linha
print("D) Pessoas com idade acima da média")
for n in pessoas:
    if n['Idade'] > media:
        velhos.append([n['Nome'], n['Idade'], n['Sexo']])

for n in velhos:
    print(f"> Nome: {n[0]}, Idade: {n[1]}, Sexo: {n[2]}")

# Mostrando finalização
print("-" * 20, end="")
print(" FIM DO PROGRAMA ", end="")
print("-" * 20)
