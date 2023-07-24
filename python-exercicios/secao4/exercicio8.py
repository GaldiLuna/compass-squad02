def eh_palindromo(palavra):
    return palavra == palavra[::-1]


def main():
    palavras = ["maça", "arara", "audio", "radio", "radar", "moto"]

    for palavra in palavras:
        if eh_palindromo(palavra):
            print(f"A palavra: {palavra} é um palíndromo")
        else:
            print(f"A palavra: {palavra} não é um palíndromo")


if __name__ == "__main__":
    main()
