# Crie um módulo chamado moedas.py que tenha as funções incorporadas:
# aumentar(), diminuir(), dobro() e metade().

# Faça também um programa que importe esse módulo e use algumas dessas funções

from ex107 import moedas

p = float(input('Digite o preço: R$').strip().replace(',', '.'))
print(f"A metade de R${p:.2f} é R${moedas.metade(p):.2f}")
print(f"O dobro de R${p:.2f} é R${moedas.dobro(p):.2f}")
print(f"Aumentando R${p:.2f} em 10%, temos R${moedas.aumentar(p, 10):.2f}")
print(f"Reduzindo R${p:.2f} em 13%, temos R${moedas.diminuir(p, 13):.2f}")
