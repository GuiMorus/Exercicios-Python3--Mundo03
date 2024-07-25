# Aprimore o desafio anterior, mostre no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

# Iniciando variável
matriz = [[], [], []]

# Repetição resgatando os números da matriz
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f"Valor de [{l}][{c}]: "))
        matriz[l].append(valor)

# Mostrando a matriz no formato 3x3
print("\n" + "Matriz formato 3x3")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")

    # Pular linha
    print("")

# ex087
print("><" * 25)

# Mostrando a soma dos pares
pares = []
soma_par = 0
for n in matriz:    # n -> numeros
    for p in n:     # p -> par
        # Verificando número par
        if p % 2 == 0:
            soma_par += p

print(f"Soma dos pares dentro da matriz: {soma_par}", "\n")

# Mostrando a soma dos valores da 3 coluna
terceira = []
soma_coluna = 0
for n in range(0, 3):
    soma_coluna += matriz[n][2]

print(f"Soma dos valores da 3° coluna: {soma_coluna}", "\n")

# Mostrando maior valor da segunda linha
segunda = matriz[1][:]
print(f"O maior valor da 2° linha: {max(segunda)}")
