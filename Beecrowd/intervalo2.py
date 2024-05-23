soma_in = 0
soma_out = 0

N = int(input())

for i in range(N):
        numeros = int(input())
        if numeros >= 10 and numeros <=20:
            soma_in += 1
        else:
            soma_out += 1
print(f'{soma_in} in')
print(f'{soma_out} out')



