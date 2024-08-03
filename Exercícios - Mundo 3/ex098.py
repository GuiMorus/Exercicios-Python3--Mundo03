# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

from time import sleep


# --Função realizando contagens
def contagem(inicio, fim, passo):
    # Introdução
    print("-" * 40)
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}")

    # Verificando informações
    if passo == 0:      # Caso passo for nulo
        passo = 1

    if inicio < fim:                   # Caso valores positivos em ordem crescente
        fim += 1
    elif inicio > fim:                 # Caso valores positivos em ordem decrescente
        fim -= 1

        # Invertendo valor do passo
        if passo > 0:
            passo *= -1

    # Repetição fazendo a contagem
    for n in range(inicio, fim, passo):
        print(f"{n} ", end="")
        sleep(0.5)
    print("FIM! \n")  # Mensagem final


# ---PROGRAMA PRINCIPAL

# Mostrando primeira contagem
contagem(1, 10, 1)

# Mostrando segunda contagem
contagem(10, 0, 2)

# Mostrando contagem personalizada
print("Contagem personalizada")
a = int(input("Digite o início: "))
b = int(input("Digite o fim: "))
c = int(input("Digite o passo: "))

# Chamando função
contagem(a, b, c)
