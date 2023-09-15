e, f, custo = map(int, input().split())

totalGarrafas = e + f
totalRefrigerantes = totalGarrafas // custo
restoGarrafas = (totalGarrafas % custo) + totalRefrigerantes

while restoGarrafas >= custo:
    totalRefrigerantesDoResto = restoGarrafas // custo
    totalRefrigerantes += totalRefrigerantesDoResto
    restoGarrafas = (restoGarrafas % custo) + totalRefrigerantesDoResto

print(totalRefrigerantes)
