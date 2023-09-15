def calculo():
    while True:
        nota_1 = float(input("Primeira: "))
        if nota_1 < 0 or nota_1 > 10:
            print("nota invalida")
        else:
            nota_2 = float(input("Segunda: "))
            if nota_2 < 0 or nota_2 > 10:
                print("nota invalida")
                nota_2 = float(input("Segunda: "))
                media = (nota_1 + nota_2) / 2
                print("media = %.2f" % media)
                break
            else:
                media = (nota_1 + nota_2) / 2
                print("media = %.2f" % media)
                break

    print("novo calculo (1-sim 2-nao)")
    n = int(input())
    if n < 1 or n > 2:
        print("novo calculo (1-sim 2-nao)")
        n = int(input())

    elif n == 2:
        exit()


while True:
    calculo()
