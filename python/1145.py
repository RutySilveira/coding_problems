a, b = map(int, input().split())
aux = 1

for i in range(1, b + 1):  # Comeca do 1 até o valor de b, incluindo ambos.
    if aux == a:  # Quando aux for igual a a, imprime o ultimo numero da linha.
        print(i)
        # Como foi printando o ultimo numero nesse if, o aux reinicia, para começar uma nova linha.
        aux = 1
    else:
        print(i, end=" ")
        aux += 1  # Incrementa no aux, para continuar printando os numeros.
