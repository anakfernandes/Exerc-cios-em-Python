# Conversão de Tempo

tempo = int(input())

conversao_hora = tempo // 60 ** 2
tempo = tempo - conversao_hora * 60**2

conversao_min = tempo // 60
tempo = tempo - conversao_min * 60

segundos = tempo

print(f'{conversao_hora}:{conversao_min}:{segundos}')


