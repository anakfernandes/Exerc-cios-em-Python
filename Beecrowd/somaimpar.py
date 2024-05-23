soma = 0

X = int(input())
Y = int(input())

if X > Y:
    start = Y 
    stop = X
else:
    start = X
    stop = Y

for elemento in range(start + 1, stop):
    if elemento % 2 != 0:
        soma += elemento 
print(soma)



