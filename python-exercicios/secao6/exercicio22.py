class Pessoa:
    def __init__(self, identificador):
        self.id = identificador
        self.__nome = None

    def nome(self, novo_nome):
        self.__nome = novo_nome

    def get_nome(self):
        return self.__nome


def main():
    pessoa = Pessoa(0)
    pessoa.nome("Fulano De Tal")
    print(pessoa.get_nome())


if __name__ == "__main__":
    main()
