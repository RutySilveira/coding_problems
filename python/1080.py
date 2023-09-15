valor = -1
p = 1

numeros = [int(input()) for _ in range(1, 101)]

for i, n in enumerate(numeros, start=1):
    if n > valor:
        valor = n
        p = i

print(valor)
print(p)
