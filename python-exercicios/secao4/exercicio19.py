import random

# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500), 50)

# Ordena a lista para calcular a mediana
random_list.sort()

# Calcula o valor mínimo, valor máximo e valor médio
valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)

# Calcula a mediana
if len(random_list) % 2 == 0:
    mediana = (
        random_list[len(random_list) // 2 - 1] + random_list[len(random_list) // 2]
    ) / 2
else:
    mediana = random_list[len(random_list) // 2]

print("Mediana:", mediana)
print("Média:", media)
print("Valor Mínimo:", valor_minimo)
print("Valor Máximo:", valor_maximo)
