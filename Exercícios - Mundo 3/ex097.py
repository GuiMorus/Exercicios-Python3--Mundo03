# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com o tamanho adaptável.

# --Função adaptando texto
def escreva(texto):
    tamanho = len(texto)
    print("~" * (tamanho + 6))
    print(f"   {texto}")
    print("~" * (tamanho + 6))


# ---PROGRAMA PRINCIPAL
escreva("Título Maker")
print()     # Pulando linha

while True:
    # Variável resgatando texto
    txt = input("Digite seu texto: ").strip().title()

    # Verificando saida
    if txt == 'Sair':
        break

    # Mostrando o texto formatado
    escreva(txt)
    print("\033[33m" + "para sair digite: sair", "\033[m")
    print()     # Pulando linha
