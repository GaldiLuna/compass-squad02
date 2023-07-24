class Aviao:
    cor = "Azul"

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade


def main():
    lista_avioes = []

    modelo1 = "BOIENG456"
    velocidade_maxima1 = "1500 km/h"
    capacidade1 = "400 passageiros"
    aviao1 = Aviao(modelo1, velocidade_maxima1, capacidade1)
    lista_avioes.append(aviao1)

    modelo2 = "Embraer Praetor 600"
    velocidade_maxima2 = "863 km/h"
    capacidade2 = "14 passageiros"
    aviao2 = Aviao(modelo2, velocidade_maxima2, capacidade2)
    lista_avioes.append(aviao2)

    modelo3 = "Antonov An-2"
    velocidade_maxima3 = "258 km/h"
    capacidade3 = "12 passageiros"
    aviao3 = Aviao(modelo3, velocidade_maxima3, capacidade3)
    lista_avioes.append(aviao3)

    for aviao in lista_avioes:
        print(
            f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} e é da cor {Aviao.cor}."
        )


if __name__ == "__main__":
    main()
