cod_1, num_p1, valor_p1 = int(input()), int(input()), float(input())
cod_2, num_p2, valor_p2 = int(input()), int(input()), float(input())

valor_pagar = (num_p1 * valor_p1) + (num_p2 * valor_p2)

print(f'VALOR A PAGAR: R$ {valor_pagar:.2f}')


linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)