def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def main():
    numeros_primos = []
    for numero in range(1, 101):
        if eh_primo(numero):
            numeros_primos.append(numero)

    print("Números primos entre 1 e 100:")
    for primo in numeros_primos:
        print(primo)


if __name__ == "__main__":
    main()
