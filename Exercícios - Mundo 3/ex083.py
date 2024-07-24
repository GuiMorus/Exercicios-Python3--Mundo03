# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplivativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

# Variável recuperando a expressão
calculo = str(input("Digite a expressão: "))

# Lista contendo os parênteses
pilha = []

# Repetição verificando parênteses da expressão
for s in calculo:
    if s == '(':
        pilha.append(s)
    elif s == ')':
        # Verificando se a pilha não está vazia
        if len(pilha) > 0:
            pilha.pop()  # Apagando último parênteses aberto
        else:
            pilha.append(s)  # Adicionando parênteses fechado
            break

if len(pilha) == 0:
    print("Sua expressão é válida")
else:
    print("Expressão inválida")
