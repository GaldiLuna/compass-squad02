def conta_vogais(string):
    vogais = "aeiou"
    string_sem_acentos = "".join(filter(lambda x: x.lower() in vogais, string))
    return len(string_sem_acentos)


# Teste da função
texto = "Olá, esta é uma string de teste contando vogais"
resultado = conta_vogais(texto)
print(resultado)  # Saída esperada: 14
