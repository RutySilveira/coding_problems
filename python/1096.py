i = 0
j = 8
contador = 0


for i in range(0, 10, 2):
    i = i + 1
    contador = 0
    j = 8
    while contador < 3:
        contador = contador + 1
        j = j - 1
        print("I=%d J=%d" % (i, j))
