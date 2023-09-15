n = int(input())
secoes = list(map(int, input().split()))

somaEsquerda = 0
somaDireita = sum(secoes)
divisao = -1

for idx, secao in enumerate(secoes):
    if somaEsquerda < somaDireita:
        somaDireita -= secao
        somaEsquerda += secao
    else:
        divisao = idx
        break

print(divisao)
