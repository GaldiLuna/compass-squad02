def remover_elementos_duplicados(lista):
    lista_sem_duplicados = list(set(lista))
    return lista_sem_duplicados


def main():
    lista_original = ["abc", "abc", "abc", "123", "abc", "123", "123"]
    lista_sem_duplicados = remover_elementos_duplicados(lista_original)
    print(lista_sem_duplicados)


if __name__ == "__main__":
    main()
