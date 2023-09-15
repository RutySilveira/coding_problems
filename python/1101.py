while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break

    if m > n:
        m, n = n, m

    soma = 0
    numeros = []

    for i in range(m, n + 1):
        soma += i
        numeros.append(i)

    print(' '.join(map(str, numeros)) + " Sum=" + str(soma))
