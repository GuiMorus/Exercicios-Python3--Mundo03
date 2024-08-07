# Crie um módulo chamado moedas.py que tenha as funções incorporadas:
# aumentar(), diminuir(), dobro() e metade().

# Faça também um programa que importe esse módulo e use algumas dessas funções

import moedas

p = float(input('Digite o preço: R$').strip().replace(',', '.'))
print(f"A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}")
print(f"O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}")
print(f"Aumentando {moedas.moeda(p)} em 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}")
print(f"Reduzindo {moedas.moeda(p)} em 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}")
