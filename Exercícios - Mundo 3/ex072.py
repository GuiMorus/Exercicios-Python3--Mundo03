# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo
# por extenso.

# Váriável contendo os números
numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "quatorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove", "vinte"
    )

# Laço recuperando número do usuário
while True:
    num = int(input("Digite um número entre 0 e 20: ").strip())
    # Verificando número recuperado
    if 0 <= num <= 20:
        break

    # Mensagem de erro
    print("\033[31m" + "Erro, tente novamente" + "\033[m")

# Mostrando resultado
print(f"Você digitou o número {numeros[num]}")
