teste = int(input())

for _ in range(teste):
    a1, b1 = input().split()
    a, b = int(a1), int(b1)

    if b == 0:
        print("divisao impossivel")
    else:
        divisao = a / b
        print("%.1f" % divisao)
