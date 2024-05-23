# Fórmula de Bhaskara

entrada = input().split()
a, b, c = entrada

a = float(a)
b = float(b)
c = float(c)

if a == 0.0  or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    x2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')