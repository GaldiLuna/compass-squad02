def soma_numeros_string(string_numeros):
    numeros = string_numeros.split(",")
    numeros_inteiros = [int(numero) for numero in numeros]
    soma = sum(numeros_inteiros)
    return soma


def main():
    string_numeros = "1,3,4,6,10,76"
    soma_total = soma_numeros_string(string_numeros)
    print("A soma dos valores é:", soma_total)


if __name__ == "__main__":
    main()
