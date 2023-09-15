valores = input()

[a1, b1, c1, d1] = valores.split()

a = int(a1)
b = int(b1)
c = int(c1)
d = int(d1)

if (b > c) and (d > a) and (c + d) > (a + b) and c and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
