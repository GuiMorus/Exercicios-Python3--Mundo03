# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos.
# No final, mostre a matriz na tela, com a formatação de correta 3x3

# Iniciando variável
matriz = [[], [], []]

# Repetição resgatando os números da matriz
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f"Valor de [{l}][{c}]: "))
        matriz[l].append(valor)

# Mostrando matriz formatado 3x3
print("\n" + "Matriz formato 3x3")
for n in range(0, 3):
    print(matriz[n])


