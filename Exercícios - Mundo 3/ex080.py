# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta da inserção(sem usar o sort()).
# No final, mostre a lista ordenada na tela

# Iniciando variável
lista = []

# Adicionando e mostrando primeiro valor
x = int(input("Digite o 1° valor: "))
lista.append(x)

print(f"O número {x} foi adicionado à lista")
del x   # Deletando variável temporária

# Repetição resgatando outros valores
for c in range(0, 4):
    num = int(input(f"\nDigite o {c + 2}° valor: "))
    cont = 0    # Reiniciando contagem

    # Definindo posição
    # Verificando se o valor já existe na lista
    if num in lista:
        pos = lista.index(num)
        lista.insert(pos, num)
        print(f"O número {num} foi adicionado atrás do seu existente")
    else:
        # Repetição para inserir o valor no lugar correto
        for n in lista:
            cont += 1   # Contagem para chegar ao final da lista
            pos = lista.index(n)    # Resgatando index do valor atual

            # Verificando número inserido e resultados da lista
            if num < n:
                # Inserindo número na posição do maior para ordena-lo
                lista.insert(pos, num)
                print(f"O número {num} foi adicionado na {pos + 1}° posição")
                break
            # Adicionando o número inserido caso chegue ao final da lista
            # sem ter passado por nenhuma condição acima
            elif cont == len(lista):
                lista.append(num)
                print(f"O número {num} foi adicionado ao final da lista")
                break

# Mostrando resultado final da lista
print("\nLISTA ORDENADA: ")
print(lista)
