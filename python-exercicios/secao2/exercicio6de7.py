def maiores_que_media(conteudo):
    # Calcula a média dos valores dos produtos
    valores = list(conteudo.values())
    media = sum(valores) / len(valores)

    # Filtra os produtos cujo valor é superior à média
    produtos_acima_da_media = [
        (produto, preco) for produto, preco in conteudo.items() if preco > media
    ]

    # Ordena o resultado pelo preço do item em ordem crescente
    produtos_acima_da_media.sort(key=lambda item: item[1])

    return produtos_acima_da_media


conteudo = {"arroz": 4.99, "feijão": 3.49, "macarrão": 2.99, "leite": 3.29, "pão": 1.99}

resultado = maiores_que_media(conteudo)
print(resultado)
