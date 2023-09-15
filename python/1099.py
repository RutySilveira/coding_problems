testes = int(input())

for _ in range(testes):
    x, y = map(int, input().split())
    soma = 0

    if x > y:
        x, y = y, x

    for i in range(x + 1, y):
        if i % 2 != 0:
            soma = soma + i

    print(soma)
