n = 0
contador = 0
while n <= 5:
    valores = float(input())
    n = n + 1
    if valores > 0:
        contador = contador + 1
print(contador, "valores positivos")
