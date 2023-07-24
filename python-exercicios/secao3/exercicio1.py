def calcular_ano_completara_100_anos(nome, idade_atual):
    from datetime import datetime

    # Obtém o ano atual
    ano_atual = datetime.now().year

    # Calcula o ano em que a pessoa completará 100 anos
    ano_completara_100 = ano_atual + (100 - idade_atual)

    return ano_completara_100


def main():
    # Solicita nome e idade ao usuário
    nome = input("Digite o seu nome: ")
    idade_atual = int(input("Digite a sua idade atual: "))

    # Calcula o ano em que a pessoa completará 100 anos
    ano_completara_100 = calcular_ano_completara_100_anos(nome, idade_atual)

    # Exibe o resultado
    print(f"{nome} completará 100 anos no ano de {ano_completara_100}.")


if __name__ == "__main__":
    main()
