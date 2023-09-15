n = int(input())
tabuleiros = [int(input()) for _ in range(n)]

for tabuleiro in tabuleiros:
    totalGraos = 1
    ultimoCalculado = 1

    for i in range(1, tabuleiro):
        totalGraos += ultimoCalculado * 2
        ultimoCalculado = ultimoCalculado * 2

    totalGramas = totalGraos // 12
    print(f"{totalGramas // 1000} kg")
