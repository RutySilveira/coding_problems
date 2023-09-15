t = int(input())
contador = 0
while t != 0:
    contador = contador + 1
    cinquenta = t // 50
    resto = t % 50
    dez = resto // 10
    resto = resto % 10
    cinco = resto // 5
    resto = resto % 5
    um = resto // 1
    print("Teste", contador)
    print(cinquenta, dez, cinco, um)
    print()

    t = int(input())
