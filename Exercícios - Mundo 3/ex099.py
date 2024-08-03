# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

# --Função mostrando maior valor
def maior(*num):
    # Introdução
    print("Analisando os valores passados...")

    # Mostrando valores
    for n in num:
        print(f"{n} ", end="")

    # Mensagem final
    print(f"Foram informados {len(num)} valores ao todo")

    # Verificando se a função não está vazia
    if len(num) > 0:
        print(f"O maior valor foi {max(num)}.")
        print("-" * 45)


# Analisando valores
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
