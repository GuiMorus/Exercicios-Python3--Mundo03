# Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela

# Iniciando variável
aluno = {}

# Recuperando informações do aluno
nome = input("Nome do aluno: ").strip().title()
media = float(input("Qual a média: "))

# Definindo situação do aluno com base na média
if media < 5:
    situação = 'Reprovado'
elif 5 <= media < 7:
    situação = 'Recuperação'
else:
    situação = 'Aprovado'

# Introduzindo valores no dicionário
aluno = {'nome': nome, 'média': media, 'situação': situação}

# Mostrando informações
print("-" * 30)
print(f"Aluno: {aluno['nome']}")
print(f"Média: {aluno['média']}")
print(f"Situação do aluno: {aluno['situação']}")
