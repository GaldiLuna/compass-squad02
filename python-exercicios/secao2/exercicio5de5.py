def processar_notas(estudantes):
    # Converte as notas em números (int ou float) e calcula a média das três maiores notas
    return [
        (
            nome,
            sorted(map(float, notas), reverse=True)[:3],
            round(sum(sorted(map(float, notas), reverse=True)[:3]) / 3, 2),
        )
        for nome, *notas in estudantes
    ]


def formatar_relatorio(estudantes):
    # Formata o relatório e retorna como string
    relatorio = ""
    for nome, notas, media in estudantes:
        # Converte os valores da lista de notas de float para int e arredonda
        notas_inteiras = [round(float(nota)) for nota in notas]
        relatorio += f"Nome: {nome} Notas: {notas_inteiras} Média: {media}\n"
    return relatorio


# Leitura do arquivo e processamento das notas
nome_arquivo = "./estudantes.csv"
with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()

# Remove caracteres especiais e quebra cada linha em uma lista de valores
estudantes = [linha.strip().split(",") for linha in linhas]

# Processa as notas e calcula as informações para o relatório
relatorio = processar_notas(estudantes)

# Ordena o relatório pelo nome do estudante
relatorio_ordenado = sorted(relatorio, key=lambda x: x[0])

# Formata o relatório final
relatorio_final = formatar_relatorio(relatorio_ordenado)

# Imprime o relatório
print(relatorio_final)
