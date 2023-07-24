def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


def main():
    numeros = []

    # Solicita os três números ao usuário
    for i in range(3):
        numero = int(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)

    # Verifica e imprime se cada número é par ou ímpar
    for numero in numeros:
        resultado = verificar_par_ou_impar(numero)
        print(f"{resultado}: {numero}")


if __name__ == "__main__":
    main()
