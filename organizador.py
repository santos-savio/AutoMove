# organizador.py
import os
import shutil
from tkinter import filedialog
from tkinter import Tk
from pathlib import Path

def selecionar_diretorio_inicial():
    """Abre um seletor de diretório para escolher o diretório inicial."""
    root = Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    diretorio_inicial = filedialog.askdirectory(
        title="Selecione o diretório inicial"
    )
    return diretorio_inicial

def renomear_arquivos(diretorio_inicial, diretorio_saida):
    data = Path(diretorio_inicial).name
    print(data)
    if diretorio_inicial:
        # Itera sobre a pasta raiz e suas subpastas
        for pasta_atual, subpastas, arquivos in os.walk(diretorio_inicial):
            # Itera sobre os arquivos da pasta atual e subpastas, adicionando o nome do diretório inicial ao nome do arquivo
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                if os.path.isfile(caminho_arquivo):
                    novo_nome = f"{data}_{arquivo}"
                    novo_caminho = os.path.join(diretorio_saida, novo_nome)
                    print("Processando arquivo: ", novo_caminho)
                    shutil.move(caminho_arquivo, novo_caminho)
    else:
        print("Nenhum diretório selecionado")


def mover_arquivos(pasta):
    for raiz, subdirs, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, arquivo)
            shutil.move(caminho_arquivo, pasta)
        for subdir in subdirs:
            caminho_subdir = os.path.join(raiz, subdir)
            if not os.listdir(caminho_subdir):
                os.rmdir(caminho_subdir)

def main():
    renomear_arquivos()
