par = 0
impar = 0
negativo = 0
positivo = 0

for _ in range(5):
    n = int(input())

    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

    if n > 0:
        positivo = positivo + 1
    elif n < 0:
        negativo = negativo + 1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
