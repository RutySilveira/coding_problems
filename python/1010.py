peca_1 = input()
peca_2 = input()


cod_1 = peca_1.split()
cod_2 = peca_2.split()


(cod_peca, num_peca, valor_peca) = cod_1
(cod_peca_2, num_peca_2, valor_peca_2) = cod_2

valor_a_pagar = int(num_peca) * float(valor_peca) + \
    int(num_peca_2) * float(valor_peca_2)

print("VALOR A PAGAR: R$ %.2f" % valor_a_pagar)
