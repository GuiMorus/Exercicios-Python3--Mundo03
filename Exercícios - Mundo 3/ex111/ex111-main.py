# Crie um pacote chamado utilidades que tenha dois módulos internos chamados moedas e dados.
# Transfira todas as funções utilizadas nos desafios 107, 108, 109, 110 para o primeiro pacote e mantenha
# tudo funcionando

from utilidades import moedas

# Variavel resgatando o valor
p = float(input("Digite um preço: R$").strip().replace(',', '.'))

# Mostrando tabela de resumo
moedas.resumo(p, 20, 12)
