hora_i, minuto_i, hora_f, minuto_f = [int(i) for i in input().split()]

horas = 24 - hora_i + hora_f
h = 24 if horas == 24 and minuto_i >= minuto_f else horas % 24

minutos = 60 - minuto_i + minuto_f
m = minutos % 60

# Correção da duração em horas caso os minutos ultrapassem 60

if minutos < 60 and minuto_i > minuto_f:
    h = h - 1
elif minutos >= 60 and minuto_i > minuto_f:
    h = h + 1


print("O JOGO DUROU", h, "HORA(S) E", m, "MINUTO(S)")
