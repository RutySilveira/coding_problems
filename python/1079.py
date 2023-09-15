teste = int(input())

for _ in range(teste):
    a1, b1, c1 = input().split()
    a, b, c = float(a1), float(b1), float(c1)

    media = (a * 2 + b * 3 + c * 5) / 10
    print("%.1f" % media)
