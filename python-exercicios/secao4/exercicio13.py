def my_map(lista, f):
    return [f(elemento) for elemento in lista]


def potencia_de_2(numero):
    return numero**2


def main():
    lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Teste com a função de potência de 2
    lista_resultado = my_map(lista_original, potencia_de_2)
    print(lista_resultado)


if __name__ == "__main__":
    main()
