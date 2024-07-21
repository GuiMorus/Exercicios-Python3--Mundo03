# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Vasco.

# Variável contendo os times
times = (
    "Botafogo", "Palmeiras", "Flamengo", "São Paulo", "Bahia",
    "Cruzeiro", "Fortaleza", "Athletico-PR", "Vasco", "Bragantino",
    "Atlético-MG", "Juventude", "Internacional", "Criciúma", "Cuiabá",
    "Vitória", "Corinthians", "Grêmio", "Atlético-GO", "Fluminense"
    )

# Mostrando os colocados
print("Colocados do Brasileirão - Série A 2024\n", times)

# Mostrando os 5 primeiros colocados
print("Os 5 primeiros colocados:\n", times[0:5])

# Mostrando os últimos 4 da tupla
print("Os 4 últimos colocados:\n", times[-4:])

# Mostrando times em ordem alfabética
print("Os times em Ordem Alfabética:\n", sorted(times))

# Mostrando a posição do time do Vasco
print("O Vasco está na posição:", times.index("Vasco") + 1)
