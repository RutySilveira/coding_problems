def calcula(n):
    t = 0
    for s in range(n + 1):
        t += s ** 2

    return t


while True:
    n = int(input())

    if n == 0:
        break

    print(calcula(n))

