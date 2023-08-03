# Função que verifica se um número é par
is_even = lambda x: x % 2 == 0

# Abre o arquivo e lê os números inteiros
with open("./number.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

# Filtra apenas os números pares
even_numbers = filter(is_even, numbers)

# Ordena os números pares em ordem decrescente
sorted_numbers = sorted(even_numbers, reverse=True)

# Pega os 5 maiores números pares
five_largest = sorted_numbers[:5]

# Calcula a soma dos 5 maiores números pares
sum_of_five_largest = sum(map(int, five_largest))

# Exibe os resultados na saída
print(five_largest)
print(sum_of_five_largest)
