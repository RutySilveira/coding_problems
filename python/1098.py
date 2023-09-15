i = 0

while i <= 2:
    for j in range(1, 4):
        i = int(i) if i == int(i) else i

        j = j + i
        j = int(j) if j == int(j) else j

        print("I={} J={}".format(i, j))

    i = round(i + 0.2, 2)
