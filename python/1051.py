n = float(input())

oito = (n - 2000) * 8 / 100
dezoito = (1000 * 8) / 100 + (18 * (n - 3000.01)) / 100
vinte_oito = (1000 * 8) / 100 + (1500 * 18) / 100 + (28 * (n - 4500)) / 100

if n >= 0.00 and n <= 2000.00:
    print("Isento")
elif n >= 2000.01 and n <= 3000.00:
    print("R$ %.2f" % oito)
elif n >= 3000.01 and n <= 4500.00:
    print("R$ %.2f" % dezoito)
else:
    print("R$ %.2f" % vinte_oito)
