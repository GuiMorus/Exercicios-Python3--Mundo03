# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra FIM, o programa encerrará
# Use cores

from time import sleep


# --Função mostrar título
def titulo(texto, cor='padrão'):
    # DOCSTRING
    """
    texto: String
    cor: String

    Esta função gera um cabeçalho de título com o seguinte padrão.
    Ex:

    --------------------
       TEXTO DIGITADO
    --------------------

    Por padrão a função escolhe o texto na cor branca, mas é possível mudar
    as cores do texto no 'parâmetro cor'

    Lista das cores:
    'vermelho'
    'verde'
    'amarelo'
    'azul'
    'roxo'
    'ciano'
    'cinza'
    """

    # Dicionário contendo as cores
    cores = {
        'padrão': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
        'azul': '\033[34m', 'roxo': '\033[35m', 'ciano': '\033[36m', 'cinza': '\033[37m'
        }

    # Montando título
    texto = texto.upper()   # Colocando letras em CAPSLOCK

    print(cores[cor])
    print('-' * (len(texto) + 6))
    print(f'   {texto}')
    print('-' * (len(texto) + 6))
    print(cores['padrão'])

    # Tempo de espera
    sleep(0.5)


# ---PROGRAMA PRINCIPAL---

# Laço do programa principal
while True:
    # Introdução
    titulo("SISTEMA DE AJUDA", 'azul')

    # Variável resgatando o nome da função
    comando = input("Função ou Biblioteca: ").strip()

    # Verificando saída
    if comando.lower() == 'sair':
        titulo("SAINDO DO PROGRAMA", 'vermelho')
        break

    # Acessando Interactive Help
    titulo('IMPORTANDO TEXTO', 'amarelo')
    sleep(1)

    # Verificando função interna
    if comando == 'titulo':
        help(titulo)
    else:
        help(comando)
