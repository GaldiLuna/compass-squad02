from functools import reduce


def calcula_saldo(lancamentos):
    # Define a função lambda para mapear os valores de acordo com o tipo (C para crédito, D para débito)
    mapear_valores = lambda lanc: lanc[0] if lanc[1] == "C" else -lanc[0]

    # Mapeia os valores para uma nova lista usando a função lambda acima
    valores = map(mapear_valores, lancamentos)

    # Reduz a lista de valores para um único valor somando todos os elementos
    saldo_final = reduce(lambda x, y: x + y, valores)

    return saldo_final


# Teste da função
lancamentos = [(200, "D"), (300, "C"), (100, "C")]

resultado = calcula_saldo(lancamentos)
print(resultado)  # Saída esperada: 200
