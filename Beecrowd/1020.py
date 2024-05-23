# Conversão de dias

dias = int(input())

ano = dias // 365
resto = dias - ano * 365

mes = resto // 30
resto = dias - mes * 30

dias = resto

print(f'{ano} ano(s)')
print(f'{mes} mês(es)')
print(f'{dias} dia(s)')

n = int(input())

a = n // 365
n = n - a*365

m = n // 30
n = n - m*30

d = n

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))