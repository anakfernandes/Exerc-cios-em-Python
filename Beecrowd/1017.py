from re import T


tempo_hrs = int(input())
velocidade_med = int(input())

calc_gasolina = tempo_hrs * velocidade_med / 12

print(f'{calc_gasolina:.3f}')