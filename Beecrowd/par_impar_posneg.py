cont_par = 0
cont_impar = 0
cont_pos = 0
cont_neg = 0
for x in range(5):
    num = int(input())
    if num > 0:
        cont_pos += 1
    if num < 0:
        cont_neg += 1
    if num % 2 == 0:
        cont_par += 1
    if num % 2 != 0:
        cont_impar += 1
print(f'{cont_par} valor(es) par(es)')
print(f'{cont_impar} valor(es) impar(es)')
print(f'{cont_pos} valor(es) positivo(s)')
print(f'{cont_neg} valor(es) negativo(s)')
