# Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro
# da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados
# pela função anterior.

from random import randint

# Iniciando variável
numeros = []


# --Função sorteando 5 números
def sorteia():
    for n in range(0, 5):
        # Adicionando número aleatório dentro da lista
        numeros.append(randint(0, 15))


# --Função somando pares
def somaPar(lista):
    # Iniciando variável
    soma = 0

    # Repetição verificando lista
    for n in lista:
        # Verificando se o número é par
        if n % 2 == 0:
            soma += n

    # Mostrando soma
    print(soma)


# ---PROGRAMA PRINCIPAL

# Mostrando os números sorteados
sorteia()
print(f"Os números sorteados foram: {numeros}")
print(f"A soma entre os pares é igual a: ", end="")
somaPar(numeros[:])
