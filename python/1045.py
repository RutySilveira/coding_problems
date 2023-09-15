# Os valores serão em ordem crescente, com o maior deles sendo a, depois b, e entao c.
c, b, a = sorted([float(i) for i in input().split()])

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == ((b ** 2) + (c ** 2)):
        print("TRIANGULO RETANGULO")
    elif a ** 2 > ((b ** 2) + (c ** 2)):
        print("TRIANGULO OBTUSANGULO")
    elif a ** 2 < ((b ** 2) + (c ** 2)):
        print("TRIANGULO ACUTANGULO")

if a == b and b == c:
    print("TRIANGULO EQUILATERO")
else:
    if (a == b and b != c) or (a != b and b == c):
        print("TRIANGULO ISOSCELES")
