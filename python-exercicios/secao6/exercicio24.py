class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)


def main():
    lista_crescente = [3, 4, 2, 1, 5]
    lista_decrescente = [9, 7, 6, 8]

    crescente = Ordenadora(lista_crescente)
    decrescente = Ordenadora(lista_decrescente)

    resultado_crescente = crescente.ordenacaoCrescente()
    resultado_decrescente = decrescente.ordenacaoDecrescente()

    print(resultado_crescente)
    print(resultado_decrescente)


if __name__ == "__main__":
    main()
