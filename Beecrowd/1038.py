# Média 3

entrada = input().split()
a, b, c, d = entrada

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = a * 2 + b * 3 + c * 4 + d * 1 / 10
print(f'Media: {media:.1f}')

if media >= 7:
    print(f'Aluno aprovado')
if media < 5:
    print(f'Aluno reprovado')

if media >= 5 and media < 7:
    print(f'Aluno em exame')
    nota = float(input())
    print(f'Nota do exame: {nota:.1f}')
    nv_media = (media + nota) / 2
    if nv_media >= 5:
        print(f'Aluno aprovado')
        print(f'Media final: {nv_media:.1f}')
    else:
        print(f'Aluno reprovado')
        print(f'Media final: {nv_media:.1f}')

x = input().split()
n1, n2, n3, n4 = x
m = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
if m < 5.0:
    print('Aluno reprovado.')
if 5.0 <= m <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {}'.format(y))
    m2 = (y + m) / 2
    if m2 >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(m2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(m2))