import os

caminho_pasta = "/home/denis/Documentos/testepython"

novo_nome = "arquivos"
contador = 1

for arquivo in os.listdir(caminho_pasta):
    caminho_completo = os.path.join(caminho_pasta, arquivo)

    if os.path.isfile(caminho_completo):
        extensão = os.path.splitext(arquivo)[1]
        novo_arquivo =f"{novo_nome}_{contador} {extensão}"

        os.rename(caminho_completo, os.path.join(caminho_pasta, novo_arquivo))
        contador +=1

print("arquivos renomeados com sucesso")