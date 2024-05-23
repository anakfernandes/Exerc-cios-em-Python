cont = 0
soma = 0
for x in range(6):
    n = float(input())
    if n > 0:
        cont += 1
        soma += n
media = soma / cont
print(f'{cont} valores positivos')
print(f'{media:.1f}')


