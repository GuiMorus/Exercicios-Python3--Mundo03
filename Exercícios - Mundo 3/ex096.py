# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
# terreno retangular(largura e comprimento) e mostre a área do terreno.

# --Função para calcular area do terreno
def area(b, h):
    A = b * h
    print(f"{A}m²")


# Variáveis resgatando valores do terreno
print("CALCULADOR DE ÁREAS")
a = float(input("Tamanho da Base (m): "))
b = float(input("Tamanho da Altura (m): "))

print(f"Um terreno de {a} por {b} tem área: ", end="")
area(a, b)
