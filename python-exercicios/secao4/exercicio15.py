class Lampada:
    def __init__(self, estado=False):
        self.esta_ligada = estado

    def liga(self):
        self.esta_ligada = True

    def desliga(self):
        self.esta_ligada = False

    def esta_ligada(self):
        return self.esta_ligada


def main():
    # Teste da classe Lampada
    lampada = Lampada()

    # Ligue a Lampada
    lampada.liga()

    # Imprima: A lâmpada está ligada? True
    print("A lâmpada está ligada?", lampada.esta_ligada)

    # Desligue a Lampada
    lampada.desliga()

    # Imprima: A lâmpada ainda está ligada? False
    print("A lâmpada ainda está ligada?", lampada.esta_ligada)


if __name__ == "__main__":
    main()
