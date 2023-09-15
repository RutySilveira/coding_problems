contador = 0
soma = 0
intervalo = [0, 10]

while contador < 2:
    notas = float(input())
    if notas >= intervalo[0] and notas <= intervalo[1]:
        contador = contador + 1
        soma = soma + notas
    else:
        print("nota invalida")

print("media = %.2f" % (soma / 2))
