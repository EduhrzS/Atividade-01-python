# Leitura dos dados
inicio_dia = int(input().split()[1])
inicio_h, inicio_m, inicio_s = map(int, input().split(' : '))
fim_dia = int(input().split()[1])
fim_h, fim_m, fim_s = map(int, input().split(' : '))

# Converte tudo para segundos
total_inicio = inicio_dia * 24 * 3600 + inicio_h * 3600 + inicio_m * 60 + inicio_s
total_fim = fim_dia * 24 * 3600 + fim_h * 3600 + fim_m * 60 + fim_s
duracao = total_fim - total_inicio

# Calcula dias, horas, minutos, segundos
w = duracao // (24 * 3600)
duracao %= (24 * 3600)
x = duracao // 3600
duracao %= 3600
y = duracao // 60
z = duracao % 60

print(f"{w} dia(s)")
print(f"{x} hora(s)")
print(f"{y} minuto(s)")
print(f"{z} segundo(s)")
