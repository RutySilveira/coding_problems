n = int(input())
contador = 0
rato = 0
sapo = 0
coelho = 0
total_cobaias = 0


while contador < n:
    contador = contador + 1
    a, b = input().split()
    quant, tipo = int(a), str(b)
    total_cobaias = total_cobaias + quant
    if tipo == 'C':
        coelho = coelho + quant
    elif tipo == 'R':
        rato = rato + quant
    elif tipo == 'S':
        sapo = sapo + quant

perc_coelhos = (coelho * 100) / total_cobaias
perc_ratos = (rato * 100) / total_cobaias
perc_sapos = (sapo * 100) / total_cobaias

print("Total:", total_cobaias, "cobaias")
print("Total de coelhos:", coelho)
print("Total de ratos:", rato)
print("Total de sapos:", sapo)
print("Percentual de coelhos: %.2f" % perc_coelhos, "%")
print("Percentual de ratos: %.2f" % perc_ratos, "%")
print("Percentual de sapos: %.2f" % perc_sapos, "%")
