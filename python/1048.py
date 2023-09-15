n = float(input())

quinze = n * 15 / 100
doze = n * 12 / 100
dez = n * 10 / 100
sete = n * 7 / 100
quatro = n * 4 / 100

if n >= 0 and n <= 400.00:
    print("Novo salario: {:.2f}".format(n + quinze))
    print("Reajuste ganho: %.2f" % quinze)
    print("Em percentual: 15 %")

elif n >= 400.01 and n <= 800.00:
    print("Novo salario: {:.2f}".format(n + doze))
    print("Reajuste ganho: %.2f" % doze)
    print("Em percentual: 12 %")

elif n >= 800.01 and n <= 1200.00:
    print("Novo salario: {:.2f}".format(n + dez))
    print("Reajuste ganho: %.2f" % dez)
    print("Em percentual: 10 %")

elif n >= 1200.01 and n <= 2000.00:
    print("Novo salario: {:.2f}".format(n + sete))
    print("Reajuste ganho: %.2f" % sete)
    print("Em percentual: 7 %")

else:
    print("Novo salario: {:.2f}".format(n + quatro))
    print("Reajuste ganho: %.2f" % quatro)
    print("Em percentual: 4 %")
