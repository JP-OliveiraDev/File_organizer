#Organizador de arquivos

import os
#Biblioteca para abrir um pop
from tkinter.filedialog import askdirectory
#caminho para selecionar a pasta que deseja e abrir o pop
caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)
#pasta para cada tipo de arquivo
locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx", ".csv"],
    "pdfs": [".pdf"],
}
#criação da pasta e movimentação dos arquivos
for arquivo in lista_arquivos:
    Nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")