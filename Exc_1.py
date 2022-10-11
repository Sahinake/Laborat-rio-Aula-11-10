"""
Programa que recebe uma lista de 10 inteiros via teclado e
imprime toda a lista em na mesma linha.
"""

from this import d


def imprimir():
    lista = []
    i = 1
    print("Annyeong! Digite 10 números:")
    while i < 11:
        try:
            x = int(input(f"{i}°:"))
            lista.append(x)
            i = i+1
        except:
            print("Não sabe o que é número?")

imprimir()



