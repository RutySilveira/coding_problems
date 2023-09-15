valores = input()

(a, b, c) = valores.split()

a_1 = int(a)
b_2 = int(b)
c_2 = int(c)

maior = (a_1 + b_2 + abs(a_1 - b_2)) // 2
maior_dos3 = (maior + c_2 + abs(maior - c_2)) // 2

print(maior_dos3, "eh o maior")
