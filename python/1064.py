n = 0
contador = 0
soma = 0

while n <= 5:
    valores = float(input())
    n = n + 1
    if valores > 0:
        contador = contador + 1
        soma = valores + soma

media = soma / contador
print(contador, "valores positivos")
print('{:.1f}'.format(media))
