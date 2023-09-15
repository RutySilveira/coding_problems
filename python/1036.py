import math
n = input()

[a1, b1, c1] = n.split()

a = float(a1)
b = float(b1)
c = float(c1)

divisor = 2 * a

delta = (b ** 2 - 4 * a * c)

if delta <= 0 or a == 0:
    print("Impossivel calcular")
else:
    raiz_1 = ((-b + math.sqrt(delta)) / (divisor))
    raiz_2 = ((-b - math.sqrt(delta)) / (divisor))
    print("R1 = %.5f" % raiz_1)
    print("R2 = %.5f" % raiz_2)
