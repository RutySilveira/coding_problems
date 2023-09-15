a1, b1 = input().split()

a = int(a1)
b = int(b1)

duracao = (24 - a + b) % 24

d = 24 if duracao == 0 else duracao

print("O JOGO DUROU", d, "HORA(S)")
