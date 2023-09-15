n = 0
contador = 0
while n <= 4:
    valores = int(input())
    n = n + 1
    if valores % 2 == 0:
        contador = contador + 1
print(contador, "valores pares")
