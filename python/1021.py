valor = float(input())

cem = int(valor // 100)
cinquenta = int(valor % 100) // 50
vinte = int(valor % 100) % 50 // 20
dez = int(valor % 100) % 50 % 20 // 10
cinco = int(valor % 100) % 50 % 20 % 10 // 5
dois = int(valor % 100) % 50 % 20 % 10 % 5 // 2

um = int(valor % 100) % 50 % 20 % 10 % 5 % 2 // 1
cent_cinquenta = int((valor % 100) % 50 % 20 % 10 % 5 % 2 % 1 // 0.50)
cent_vinte_e_cinco = int((valor % 100) % 50 % 20 %
                         10 % 5 % 2 % 1 % 0.50 // 0.25)
cent_dez = int((valor % 100) % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 // 0.10)
cent_cinco = int((valor %
                 100) % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 // 0.05)
cent_um = int(round((valor %
              100) % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 % 0.05 / 0.01))

if valor > 0 and valor < 1000000:
    print("NOTAS:")
    print(cem, "nota(s) de R$ 100.00")
    print(cinquenta, "nota(s) de R$ 50.00")
    print(vinte, "nota(s) de R$ 20.00")
    print(dez, "nota(s) de R$ 10.00")
    print(cinco, "nota(s) de R$ 5.00")
    print(dois, "nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(um, "moeda(s) de R$ 1.00")
    print(cent_cinquenta, "moeda(s) de R$ 0.50")
    print(cent_vinte_e_cinco, "moeda(s) de R$ 0.25")
    print(cent_dez, "moeda(s) de R$ 0.10")
    print(cent_cinco, "moeda(s) de R$ 0.05")
    print(cent_um, "moeda(s) de R$ 0.01")
