# Teste de Seleção 1
entrada = input().split()
a, b, c, d = entrada

a = int(a)
b = int(b)
c = int(c)
d = int(d)

soma1 = c + d
soma2 = a + b

if b > c and d > a and soma1 > soma2 and c > 0 and d > 0 and a % 2 == 0:
    print(f'Valores aceitos')
else:
    print(f'Valores nao aceitos')