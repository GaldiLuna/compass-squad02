def imprimir_parametros(*args, **kwargs):
    print("Parâmetros não nomeados (args):")
    for arg in args:
        print(arg)

    print("\nParâmetros nomeados (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main():
    imprimir_parametros(1, 3, 4, "hello", parametro_nomeado="alguma coisa", x=20)


if __name__ == "__main__":
    main()
