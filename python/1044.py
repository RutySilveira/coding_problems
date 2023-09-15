n = input().split()

a1, b1 = (n)
a = int(a1)
b = int(b1)

if a > b:
    if a % b == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif b > a:
    if b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    print("Nao sao Multiplos")
