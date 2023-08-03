import hashlib

while True:
    # Recebe uma string via input
    texto = input("Digite uma palavra para gerar o hash (ou 'sair' para encerrar): ")
    
    if texto.lower() == 'sair':
        break

    # Gerar o hash da string por meio do algoritmo SHA-1
    sha1_hash = hashlib.sha1(texto.encode()).hexdigest()

    # Imprimir o hash em tela, utilizando o método hexdigest
    print(f"Hash SHA-1 da palavra '{texto}': {sha1_hash}")
