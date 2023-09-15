def calculo():
    while True:
        nota_1 = float(input("Insira a primeira nota: "))
        if nota_1 < 0 or nota_1 > 10:
            print("Nota inválida")
        else:
            nota_2 = float(input("Insira a segunda nota: "))
            if nota_2 < 0 or nota_2 > 10:
                print("Nota inválida")
            else:
                media = (nota_1 + nota_2) / 2
                print("Média =", media)

                while True:
                    resposta = input(
                        "Deseja realizar um novo cálculo? (sim/não): ")
                    if resposta.lower() == "sim":
                        break
                    elif resposta.lower() == "não":
                        print("Encerrando o programa.")
                        return
                    else:
                        print("Resposta inválida. Digite 'sim' ou 'não'.")


calculo()
