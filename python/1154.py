n = int(input())
soma = 0
contador = 0


while n > 0:
    contador = contador + 1
    soma = soma + n
    n = int(input())
media = soma / contador
print("%.2f" % media)
