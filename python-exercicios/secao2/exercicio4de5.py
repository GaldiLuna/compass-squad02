def calcular_valor_maximo(operadores, operandos):
    # Aplicar as operações aos pares de operandos usando a função zip e map
    resultados = map(
        lambda op, opd: eval(f"{opd[0]} {op} {opd[1]}"), operadores, operandos
    )

    # Obter o maior valor dentre eles
    return max(resultados)


# Exemplo de uso:
operadores = ["+", "-", "*", "/", "+"]
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)  # Output: 12

conta = zip(operadores, operandos)
conta = list(conta)
print(conta)
