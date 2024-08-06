# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições

from datetime import datetime


# --Função verificando voto
def voto(ano):
    # Verificando idade com base no ano atual
    idade = ano_atual - ano

    if idade < 18:
        return "VOTO NEGADO"
    elif 18 <= idade <= 70:
        return "VOTO OBRIGATÓRIO"
    else:
        return "VOTO OPCIONAL"


# ---PROGRAMA PRINCIPAL---

# Iniciando variável
ano_atual = datetime.today().year

# Variável resgatando nascimento do usuário
nascimento = int(input("Digite seu ano de nascimento: "))

# Mostrando resultado
print(f"Com {ano_atual - nascimento} anos. Situação: {voto(nascimento)}")
