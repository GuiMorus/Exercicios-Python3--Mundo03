# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois, você deve mostrar, para cada palavra, quais são as suas vogais.

# Variavel inicial
palavras = ("pedra", "arvore", "casa", "rua", "cidade", "predio", "aviao", "carro", "espada", "fogo")

# Repetição mostrando o resultado
for c in palavras:
    print(f"\nNa palavra {c.upper()} temos:", end="")

    if 'a' in c:
        print(" a" * c.count('a'), end="")
    if 'e' in c:
        print(" e" * c.count('e'), end="")
    if 'i' in c:
        print(" i" * c.count('i'), end="")
    if 'o' in c:
        print(" o" * c.count('o'), end="")
    if 'u' in c:
        print(" u" * c.count('u'), end="")
