"""
Programa que receba uma lista de de 10 inteiros via teclado, em
seguida o programa deve solicitar um número e informar se o número
também está na lista ou não.
"""

def imprimir_e_informar():
    lista = []
    print("Annyeong! Digite 10 números:")
    i = 1
    while i < 11:
        try:
            x = int(input(f"{i}°:"))
            lista.append(x)
            i = i+1
        except:
            print("Não sabe o que é número?")
    
    print("Agora, que número você está procurando?")
    a = 0
    while a == 0:
        try:
            x = int(input())
            a = 1
        except:
            print("Não sabe o que é número? Digite um número:")

    if x not in lista:
        print(f"Mianhae! O número {x} não está na sua lista {lista}")
    else:
        print(f"Yeah! O número {x} está na sua lista {lista}")

imprimir_e_informar()
