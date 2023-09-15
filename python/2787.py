linha = int(input())
coluna = int(input())

linha_par = (linha % 2) == 0
coluna_par = (coluna % 2) == 0


if linha_par is False and coluna_par is False:
    print("1")
elif linha_par is False and coluna_par is True:
    print("0")
elif linha_par is True and coluna_par is True:
    print("1")
elif linha_par is True and coluna_par is False:
    print("0")
