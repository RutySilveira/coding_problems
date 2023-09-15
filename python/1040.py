n = input()

(n1, n2, n3, n4) = n.split()

nota1 = float(n1)
nota2 = float(n2)
nota3 = float(n3)
nota4 = float(n4)

media = (2 * nota1 + 3 * nota2 + 4 * nota3 + 1 * nota4) / 10
aluno_em_exame = True

print("Media: %.1f" % media)
if media >= 7.0:
    print("Aluno aprovado.")
if media < 5.0:
    print("Aluno reprovado.")
if media >= 5.0 and media <= 6.9 and aluno_em_exame:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: %.1f" % nota_exame)
    nova_media = (nota_exame + media) / 2
    if nova_media >= 5.0:
        print("Aluno aprovado.")
    if nova_media <= 4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f" % nova_media)
