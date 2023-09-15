n = input()

[codigo, quantidade] = n.split()

cod = int(codigo)
quant = int(quantidade)
cachorroq = float(quant * 4.00)
x_salada = float(quant * 4.50)
x_bacon = float(quant * 5.00)
torrada = float(quant * 2.00)
refri = float(quant * 1.50)


if cod == 1:
    print("Total: R$ %.2f" % cachorroq)
if cod == 2:
    print("Total: R$ %.2f" % x_salada)
if cod == 3:
    print("Total: R$ %.2f" % x_bacon)
if cod == 4:
    print("Total: R$ %.2f" % torrada)
if cod == 5:
    print("Total: R$ %.2f" % refri)
