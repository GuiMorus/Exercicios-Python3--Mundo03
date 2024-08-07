# Crie um módulo chamado moedas.py que tenha as funções incorporadas:
# aumentar(), diminuir(), dobro() e metade().

# Faça também um programa que importe esse módulo e use algumas dessas funções

import moedas

p = float(input('Digite o preço: R$').strip().replace(',', '.'))
print(f"A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}")
print(f"O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}")
print(f"Aumentando {moedas.moeda(p)} em 10%, temos {moedas.aumentar(p, 10, True)}")
print(f"Reduzindo {moedas.moeda(p)} em 13%, temos {moedas.diminuir(p, 13, True)}")
