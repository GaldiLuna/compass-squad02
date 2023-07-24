def dividir_lista_em_tres_partes(lista):
    tamanho_parte = len(lista) // 3
    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte : 2 * tamanho_parte]
    parte3 = lista[2 * tamanho_parte :]
    return parte1, parte2, parte3


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    parte1, parte2, parte3 = dividir_lista_em_tres_partes(lista)
    print("Parte 1:", parte1)
    print("Parte 2:", parte2)
    print("Parte 3:", parte3)


if __name__ == "__main__":
    main()
