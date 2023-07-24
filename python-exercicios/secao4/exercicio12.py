import json


def main():
    nome_arquivo = "person.json"

    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo_json = json.load(arquivo)
            print(conteudo_json)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError as e:
        print(f"Erro de parsing JSON: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
