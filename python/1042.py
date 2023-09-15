a, b, c = input().split()

ao = int(a)
bo = int(b)
co = int(c)

if ao > bo:
    aux = ao
    ao = bo
    bo = aux

if ao > co:
    aux = ao
    ao = co
    co = aux

if bo > co:
    aux = bo
    bo = co
    co = aux

print(ao)
print(bo)
print(co)
print()
print(a)
print(b)
print(c)
