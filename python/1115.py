a, b = input().split()
x, y = int(a), int(b)
while x and y != 0:
    if x < 0 and y > 0:
        print("segundo")
    elif x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y < 0:
        print("terceiro")
    else:
        print("quarto")
    a, b = input().split()
    x, y = int(a), int(b)
