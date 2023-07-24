def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # Compreensão de lista para gerar uma nova lista contendo
    # apenas números ímpares
    numeros_impares = [numero for numero in a if numero % 2 != 0]

    # Imprimir a nova lista na saída padrão
    print(numeros_impares)


if __name__ == "__main__":
    main()
