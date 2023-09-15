def toMinutes(h, m):
    h = 24 if h == 0 else h
    hm = h * 60
    return hm + m


while True:
    hi, mi, hf, mf = map(int, input().split())

    if hi == 0 and mi == 0 and hf == 0 and mf == 0:
        break

    tmi = toMinutes(hi, mi)
    tmf = toMinutes(hf, mf)

    if tmi > tmf:
        tmf += 60 * 24

    print(tmf - tmi)
