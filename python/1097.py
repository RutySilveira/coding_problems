i = 0
contador = 0


for i in range(0, 10, 2):
    i = i + 1
    contador = 0
    j = i + 7
    while contador < 3:
        contador = contador + 1
        j = j - 1
        print("I=%d J=%d" % (i, j))
