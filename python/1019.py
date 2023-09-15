n = int(input())


def conversão(numero_segundos):
    horas = numero_segundos // 3600
    minutos = (numero_segundos % 3600) // 60
    segundos = (numero_segundos % 3600) % 60

    return "%d:%01d:%01d" % (horas, minutos, segundos)


print(conversão(n))
