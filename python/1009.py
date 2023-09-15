nome = input()
salario = float(input())
total_vendas = float(input())

total = (total_vendas * 15 / 100) + salario

print("TOTAL = R$ %.2f" % total)
