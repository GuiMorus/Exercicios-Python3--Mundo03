# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais
# O nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que nenhum dado tenha
# sido informado corretamente

# --Função mostrando ficha do jogador
def ficha(nome='', pontos=''):
    # Verificando se o nome está vazio
    if nome == '':
        nome = '<desconhecido>'

    # Verificando valor de pontos
    if pontos == '' or pontos.isalpha():
        pontos = int(0)
    elif pontos.isnumeric():
        pontos = int(pontos)

    # Mostrando mensagem
    return print(f"Jogador(a) {nome} fez {pontos} gol(s).")


# ---PROGRAMA PRINCIPAL---

# Variáveis recolhendo informações
jogador = input("Nome do jogador: ").strip().title()
gols = input("Quantos gols marcados: ")

# Mostrando a ficha
ficha(jogador, gols)
