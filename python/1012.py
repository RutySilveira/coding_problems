n = input()


(a, b, c) = n.split()

pi = 3.14159
area_triangulo = float(a) * float(c) / 2
area_circulo = pi * float(c) ** 2
area_trapezio = ((float(a) + float(b)) * float(c)) / 2
area_quadrado = float(b) ** 2
area_retangulo = float(a) * float(b)


print("TRIANGULO: %.3f" % area_triangulo)
print("CIRCULO: %.3f" % area_circulo)
print("TRAPEZIO: %.3f" % area_trapezio)
print("QUADRADO: %.3f" % area_quadrado)
print("RETANGULO: %.3f" % area_retangulo)
