# Definição da função que converte dias, horas, minutos e segundos para segundos
def segundos_totais(d, h, m, s):
    total = 0
    # 86400 segundos em um dia (24 horas * 60 minutos * 60 segundos)
    total += d * 86400
    total += h * 3600  # 3600 segundos em uma hora (60 minutos * 60 segundos)
    total += m * 60  # 60 segundos em um minuto
    total += s   # segundos

    return total


_, data_inicio = input().split()
d_inicio = int(data_inicio)
horas1, minutos1, segundos1 = [int(i) for i in input().split(" :")]
_, data_termino = input().split()
d_termino = int(data_termino)
horas2, minutos2, segundos2 = [int(i) for i in input().split(" :")]

# Converte o momento inicial e final para segundos
total_segundos_inicio = segundos_totais(d_inicio, horas1, minutos1, segundos1)
total_segundos_final = segundos_totais(d_termino, horas2, minutos2, segundos2)

# Calcula a diferenca entre o momento inicial e o final em segundos
diferenca = total_segundos_final - total_segundos_inicio

# Cálculo da duração em dias, horas, minutos e segundos
# Cálculo dos dias a partir dos segundos (86400 segundos em um dia)
dias = diferenca // 86400
# Resto da divisão para calcular o tempo restante após subtrair os dias
diferenca = diferenca % 86400

# Cálculo das horas a partir dos segundos restantes (3600 segundos em uma hora)
horas = diferenca // 3600
# Resto da divisão para calcular o tempo restante após subtrair as horas
diferenca = diferenca % 3600

# Cálculo dos minutos a partir dos segundos restantes (60 segundos em um minuto)
minutos = diferenca // 60
# Resto da divisão para calcular o tempo restante após subtrair os minutos
segundos = diferenca % 60
# O valor atual de 'r' contém os segundos restantes

# Print da impressão da duração em dias, horas, minutos e segundos
print(dias, "dia(s)")  # Imprime os dias
print(horas, "hora(s)")  # Imprime as horas
print(minutos, "minuto(s)")  # Imprime os minutos
print(segundos, "segundo(s)")  # Imprime os segundos
