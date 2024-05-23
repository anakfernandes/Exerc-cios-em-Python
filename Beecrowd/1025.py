# Lanche

entrada = input().split()
a, b = entrada

a = str(a)
b = float(b)

cachorro = 4
x_sal = 4.5
x_bac = 5.0
torrada = 2.0
refri = 1.5

if a == '1':
    resul = b * cachorro
    print(f'Total R$ {resul:.2f}')
if a == '2':
    resul = b * x_sal
    print(f'Total R$ {resul:.2f}')
if a == '3':
    resul = b * x_bac
    print(f'Total R$ {resul:.2f}')
if a == '4':
    resul = b * torrada
    print(f'Total R$ {resul:.2f}')
if a == '5':
    resul = b * refri
    print(f'Total R$ {resul:.2f}')