a, b = input().split()
a1 = int(a)
tamanho = [int(i) for i in input().split()]
resultado = a1


for i in tamanho:
    if i > 0:
        if i + resultado > 100:
            resultado = 100
        else:
            resultado = resultado + i

    elif i < 0:
        if i + resultado < 0:
            resultado = 0
        else:
            resultado = resultado + i

print(resultado)
