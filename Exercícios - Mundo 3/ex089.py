# Crie um programa que leia nome e duas notas de vários alunos e gaurde
# tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada aluno e permita que o usuário possa mostrar as notas de cada aluno individualmente

# Iniciando variável
alunos = []
nome = '0'
info = ''

# Introdução
print("|" + "=" * 18, end="")
print("[ SISTEMA DE BOLETIM ESCOLAR ]", end="")
print("=" * 18 + "|")

# Laço cadastrando os alunos
while True:
    # Verificando se o campo foi preenchido com um nome
    while nome.isnumeric():
        # Resgatando nome do aluno
        nome = str(input("Nome do aluno(a): "))
        nome = nome.strip().title()

    # Parando sistema
    if nome == 'Sair':
        break

    # Resgatando notas do aluno
    nota1 = float(input("1° Nota: ").strip().replace(',', '.'))
    nota2 = float(input("2° Nota: ").strip().replace(',', '.'))

    # Cadastrando aluno e notas
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])

    # Mensagem de saida do sistema
    print("\033[33m" + "Para encerrar o sistema digite: sair", "\033[m\n")
    nome = '0'  # Reiniciando nome

# Mostrando boletim
print("><" * 20)
print()  # Pulando linha
print(f"{'Nº':<3} {'NOME':<30} {'MÉDIA':<3}")
print("-" * 40)

# Criando lista do boletim
for n in range(0, len(alunos)):
    aluno_nome = alunos[n][0]
    aluno_media = alunos[n][3]
    print(f"{n:<3} {aluno_nome:<30} {aluno_media:<3.2f}")

# Mostrando informações detalhadas
print()  # Pulando linha
while info != 'sair':
    info = input("Deseja ver as notas do aluno(a) Nº: ").strip().lower()

    # Verificando se o campo info é um número
    if info.isnumeric():
        info = int(info)

        # Verificando se o aluno existe na lista
        if info <= len(alunos) - 1:
            print("=" * 35)
            print(f"Aluno(a): {alunos[info][0]}")
            print(f"1º Nota: {alunos[info][1]:.1f} | 2° Nota: {alunos[info][2]:.1f}")
        else:
            print("\033[31m" + "Aluno não encontrado, tente novamente!", "\033[m")

    # Parando o sistema
    if info == 'sair':
        break

    # Mensagem de saida do sistema
    print("\033[33m" + "Para encerrar o sistema digite: sair", "\033[m\n")

# Encerramento
print("|" + "=" * 18, end="")
print("[ ENCERRANDO BOLETIM ESCOLAR ]", end="")
print("=" * 18 + "|")
