# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função

# --Função calculando notas
def notas(*notas, sit=False):
    # Formatando informações
    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = 0

    # Calculando média
    for n in notas:
        media += n
    media = media / total

    # Definindo situação do aluno
    if media < 5:
        status = 'Ruim'
    elif 5 <= media <= 6:
        status = 'Razoável'
    else:
        status = 'Bom'

    # Iniciando dicionário
    info = {'Total': total, 'Maior': maior, 'Menor': menor, 'Média': float(f"{media:.2f}")}

    # Colocando situação caso o usuário deseja mostrar
    if sit:
        info['Situação'] = status

    return info


# ---PROGRAMA PRINCIPAL---
resp = notas(8.3, 7, 6, 5, sit=True)
print(resp)
