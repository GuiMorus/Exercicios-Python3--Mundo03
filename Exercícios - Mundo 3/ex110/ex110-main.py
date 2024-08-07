# Adicione ao módulo moedas.py criado nos desafios anteriores, uma função chamada resumo()
# que mostre na tela informações geradas pelas funções que já temos no módulo

import moedas

# Variavel resgatando o valor
p = float(input("Digite um preço: R$").strip().replace(',', '.'))

# Mostrando tabela de resumo
moedas.resumo(p, 80, 35)
