x = int(input())
y = int(input())
lista = []


if x <= y:
    for i in range(x + 1, y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
else:
    for i in range(x - 1, y, -1):
        if i % 5 == 2 or i % 5 == 3:
            lista.append(i)
    lista.reverse()
    for i in lista:
        print(i)
