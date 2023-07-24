def main():
    a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Criar conjuntos sem duplicatas para ambas as listas
    set_a = set(a)
    set_b = set(b)

    # Encontrar a interseção dos conjuntos
    intersecao = set_a.intersection(set_b)

    # Converter a interseção de volta para lista
    lista_intersecao = list(intersecao)

    # Imprimir a lista de valores da interseção na saída padrão
    print(lista_intersecao)


if __name__ == "__main__":
    main()
