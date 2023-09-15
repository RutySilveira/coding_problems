teste = int(input())

for _ in range(teste):
    n = int(input())
    resultado = ''

    if n == 0:
        resultado = "NULL"
    else:
        if n % 2 == 0:
            resultado = "EVEN"
        else:
            resultado = "ODD"

        if n > 0:
            resultado += " POSITIVE"
        elif n < 0:
            resultado += " NEGATIVE"

print(resultado)
