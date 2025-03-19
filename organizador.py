# organizador.py
import os
import shutil

def renomear_arquivos(pasta):
    nome_pasta = os.path.basename(pasta)
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            novo_nome = f"{nome_pasta}_{arquivo}"
            novo_caminho = os.path.join(pasta, novo_nome)
            shutil.move(caminho_arquivo, novo_caminho)

def mover_arquivos(pasta):
    for raiz, subdirs, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, arquivo)
            shutil.move(caminho_arquivo, pasta)
        for subdir in subdirs:
            caminho_subdir = os.path.join(raiz, subdir)
            if not os.listdir(caminho_subdir):
                os.rmdir(caminho_subdir)
                