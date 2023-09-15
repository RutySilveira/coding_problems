valor = int(input())

cem = valor // 100
cinquenta = (valor % 100) // 50
vinte = (valor % 100) % 50 // 20
dez = (valor % 100) % 50 % 20 // 10
cinco = (valor % 100) % 50 % 20 % 10 // 5
dois = (valor % 100) % 50 % 20 % 10 % 5 // 2
um = (valor % 100) % 50 % 20 % 10 % 5 % 2 // 1

if valor > 0 and valor < 1000000:
    print(valor)
    print(cem, "nota(s) de R$ 100,00")
    print(cinquenta, "nota(s) de R$ 50,00")
    print(vinte, "nota(s) de R$ 20,00")
    print(dez, "nota(s) de R$ 10,00")
    print(cinco, "nota(s) de R$ 5,00")
    print(dois, "nota(s) de R$ 2,00")
    print(um, "nota(s) de R$ 1,00")
