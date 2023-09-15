n = int(input())
alcool = 0
gasolina = 0
diesel = 0
while n != 1 or 2 or 3:
    n = int(input())
    if n == 1:
        alcool = alcool + 1
    elif n == 2:
        gasolina = gasolina + 1
    elif n == 3:
        diesel = diesel + 1
    elif n == 4:
        break
print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)
