cont = 0
for x in range(5):
    num = float(input())
    if num > 0 and num % 2 == 0:
        cont += 1
print(f'{cont} valores pares')

