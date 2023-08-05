def pares_ate(n: int):
    for num in range(2, n + 1, 2):
        yield num


# Obtém o generator
generator = pares_ate(10)

# Itera e imprime os valores pares
for par in generator:
    print(par)
