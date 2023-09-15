def extrair_ultimos_digitos(numero, c):
    numero_str = str(numero)
    digitos = [int(digito) for digito in numero_str[-c:]]
    numero_inteiro = int("".join(map(str, digitos)))

    return numero_inteiro


n = int(input())
s = 0


while s < n:
    s = s + 1
    a_a, b_b = input().split()

    a, b = int(a_a), int(b_b)

    tamanho_b = len(str(b))
    if extrair_ultimos_digitos(a, tamanho_b) == b:
        print("encaixa")
    else:
        print("nao encaixa")
