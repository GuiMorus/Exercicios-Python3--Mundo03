# Crie um programa que leia vários números e coloque-os em uma lista.
# Depois, crie duas listas extras que vão conter apenas valores pares e
# valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

# Iniciando variável
numeros = []

# Laço recuperando os números
while True:
    num = input("\nDigite um número: ").lower().strip()

    # Verificando se o usuário deseja sair
    if num == 'sair':
        break

    # Adicionando número na lista
    if num.isnumeric():
        num = int(num)
        numeros.append(num)

    # Mensagem de erro
    else:
        print("\033[33m" + "INVÁLIDO, TENTE NOVAMENTE", "\033[m")

    # Mensagem para sair do programa
    print("Digite", "\033[31m" + "sair" + "\033[m", "para finalizar o programa")

# Mostrando a tabela original
print("")   # pulando linha
print("Seus números:")
print(numeros)

# Mostrando tabela de pares
pares = []
for c in numeros:
    if c % 2 == 0:
        pares.append(c)

print("\nTabela dos pares:")
print(pares)

# Mostrando tabela dos ímpares
impares = []
for c in numeros:
    if c % 2 == 1:
        impares.append(c)

print("\nTabela dos ímpares")
print(impares)
