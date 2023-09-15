while True:
    n = int(input())
    if n == 0:
        break

    if n % 2 != 0:
        n = n + 1

    soma = 0
    for i in range(5):
        soma = soma + n
        n = n + 2
    print(soma)
