# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

# Variável recuperando expressão
calculo = str(input("Digite a expressão: "))

# Identificando quantidade de parênteses
aberto = calculo.count('(')
fechado = calculo.count(')')

# Verificando expressão
if aberto == fechado:
    print("Expressão válida")
else:
    print("Expressão inválida")
