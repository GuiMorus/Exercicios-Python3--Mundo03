# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

# Variáveis Iniciais
tabela = (
    "Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00,
    "Regua", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30,
    "Livro", 34.90, "Apontador", 1.99
    )

tamanho = len(tabela)   # Pegando tamanho da tupla

# Mostrando tabela

# Mensagem inicial
print("_" * 40)
print("{:^40}".format("LISTA DE PREÇOS"))
print("_" * 40)

# Repetição mostrando a tabela
for c in range(0, tamanho, 2):
    # Mostrando os itens
    print("{:.<31}".format(tabela[c]), end="")
    # Mostrando valores
    print("R${:>7.2f}".format(tabela[c+1]))

# Final da tabela
print("_" * 40)
