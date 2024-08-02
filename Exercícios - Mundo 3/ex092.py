# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário. Se por acaso tiver CTPS, o dicionário receberá também o ano de contratação e
# o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

# Iniciando variável
usuario = {}
ano_atual = datetime.today().year

# Variáveis resgatando informações iniciais
nome = input("Digite seu nome: ").strip().title()
nascimento = int(input("Ano de nascimento: ").strip())
ctps = input("Digite sua carteira de trabalho(coloque 0 caso não tenha): ").strip()
ctps = int(ctps) if ctps.isnumeric() else 0     # Tratando informação

# Adicionando informações no dicionário
usuario["Nome"] = nome
usuario["Idade"] = ano_atual - nascimento
usuario["Carteira"] = ctps

# Adicionando informações caso o usuário tenha CTPS
if usuario["Carteira"] > 0:
    usuario["Contratação"] = int(input("Digite o seu ano de contratação: ").strip())
    usuario["Salário"] = float(input("Digite seu salário: R$").strip().replace(",", "."))

    # Calculo da aposentadoria
    trabalho = 35 - (ano_atual - usuario['Contratação'])
    usuario["Aposentadoria"] = ano_atual + trabalho

# Mostrando informações
print("-" * 30)
for k, v in usuario.items():
    if k != 'Aposentadoria':
        print(f"{k} do usuário: {v}")
    else:
        print(f"{k} do usuário: {v}, se aposentará com {usuario['Idade'] + trabalho} anos")
