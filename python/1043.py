a1, b1, c1 = input().split()

a = float(a1)
b = float(b1)
c = float(c1)
perimetro = a + b + c
area = (a + b) * c / 2

if a + b > c and b + c > a and c + a > b:
    print("Perimetro = %.1f" % perimetro)
else:
    print("Area = %.1f" % area)
