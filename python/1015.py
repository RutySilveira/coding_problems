p_1 = input()
p_2 = input()

[a_1, b_1] = p_1.split()
[a_2, b_2] = p_2.split()

x_1 = float(a_1)
y_1 = float(b_1)
x_2 = float(a_2)
y_2 = float(b_2)

eixo_p1 = (x_2 - x_1) ** 2
eixo_2 = (y_2 - y_1) ** 2
distancia = (eixo_p1 + eixo_2) ** (1/2)

print("%.4f" % distancia)
