n = int(input())

for i in range(2, n + 1):
    if i % 2 == 0:
        print("%d^2 = %d" % (i, i ** 2))
