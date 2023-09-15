teste = int(input())
inn = 0
out = 0

for _ in range(teste):
    n = int(input())

    if n in range(10, 21):
        inn = inn + 1
    else:
        out = out + 1

print(inn, "in")
print(out, "out")
