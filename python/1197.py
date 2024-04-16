while True:
    try:
        v, t = map(int, input().split())
        tempo_em_dobro = 2 * t
        deslocamenento = v * tempo_em_dobro
        print(deslocamenento)
    except EOFError:
        break
