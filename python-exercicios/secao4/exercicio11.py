def main():
    nome_arquivo = "arquivo_texto.txt"

    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


if __name__ == "__main__":
    main()
