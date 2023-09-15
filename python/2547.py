while True:
    try:
        numeroVisitante, alturaMinima, alturaMaxima = map(int, input().split())
        alturaVisitantes = [int(input()) for _ in range(numeroVisitante)]

        quantidade = 0

        for altura in alturaVisitantes:
            if alturaMinima <= altura <= alturaMaxima:
                quantidade += 1

        print(quantidade)
    except EOFError:
        break
