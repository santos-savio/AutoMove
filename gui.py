# This code was developed by Savio G. Santos
# The purpose of this code is to create a GUI for the AutoMove script
# The script is used to organize the images generated by the Intebras VIP camera
# The script renames the images with the date of the record and moves them to a new folder

from pathlib import Path
from tkinter import filedialog
import textwrap
import organizador

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage

# Define o caminho relativo para os assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"
diretorio_inicial = ""
diretorio_saida = ""
text_diretorio_inicial = "Nenhum diretório selecionado"
text_diretorio_saida = "Nenhum diretório selecionado"

status_color = "#FFFF00"  # Define a cor para amarelo
status = "Selecione os diretórios"  # Define o status inicial

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Função para atualizar a cor e status de operação
def update_status_color():
    """Atualiza a cor do círculo com base na variável global."""
    global status_color
    global status
    canvas.itemconfig(rectangle, fill=status_color)
    canvas.itemconfig(frase_status, text=status)

# Funções para alterar a cor e status de operação
def change_color_to_green():
    global status_color
    global status
    status_color = "#00FF00"  # Define a cor para verde
    status = "Pronto para executar"
    button_5.config(state="normal")
    update_status_color()

def change_color_to_red():
    global status_color
    global status
    status_color = "#FF0000"  # Define a cor para vermelho
    status = "Executando, não interromper..."
    button_5.config(state="disabled")
    update_status_color()

def change_color_to_yellow():
    global status_color
    global status
    status_color = "#FFFF00"  # Define a cor para amarelo
    status = "Selecione os diretórios"
    button_5.config(state="disabled")
    update_status_color()

def atualizar_label_log(mensagem):
    """Atualiza a label de log na interface gráfica."""
    log_formatado = textwrap.fill(mensagem, width=95) # Formata o texto para quebrar a linha
    canvas.itemconfig(label_log, text=log_formatado)
    canvas.update_idletasks()  # Força a atualização da interface gráfica

# Funções correspondentes aos botões
def selecionar_diretorio_inicial():
    global diretorio_inicial
    global status
    global status_color
    global text_diretorio_saida
    """Abre um seletor de diretório para escolher o diretório inicial."""
    root = Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    diretorio_inicial = filedialog.askdirectory(
        title="Selecione o diretório inicial"
    )
    if not diretorio_inicial:  # Verifica se o usuário cancelou a seleção
        diretorio_inicial = ""
        text_diretorio_inicial = "Nenhum diretório selecionado"
        texto_formatado = textwrap.fill(text_diretorio_inicial, width=60) # Formata o texto para quebrar a linha
        canvas.itemconfig(label_diretorio_inicial, text=texto_formatado)
        status = "Selecione o diretório inicial"
        status_color = "#FFFF00"  # Define a cor para amarelo
        update_status_color()
        print("Seleção de diretório inicial cancelada")
    else:
        text_diretorio_inicial = diretorio_inicial
        texto_formatado = textwrap.fill(text_diretorio_inicial, 60) # Formata o texto para quebrar a linha
        canvas.itemconfig(label_diretorio_inicial, text=texto_formatado)
        status = "Diretório inicial selecionado"
        update_status_color()
        if diretorio_saida:
            change_color_to_green()
        else:
            status = "Selecione o diretório de saída"
            status_color = "#FFFF00"  # Define a cor para amarelo
            update_status_color()

        print("Botão 'Selecionar diretório inicial' pressionado")
        print(f"Diretório inicial: {diretorio_inicial}")

def selecionar_diretorio_saida():
    global diretorio_saida
    global status
    global status_color
    global text_diretorio_inicial
    """Abre um seletor de diretório para escolher o diretório de saída."""
    root = Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    diretorio_saida = filedialog.askdirectory(
        title="Selecione o diretório de saída"
    )
    if not diretorio_saida:  # Verifica se o usuário cancelou a seleção
        diretorio_saida = ""
        text_diretorio_saida = "Nenhum diretório selecionado"
        texto_formatado = textwrap.fill(text_diretorio_saida, 60) # Formata o texto para quebrar a linha
        canvas.itemconfig(label_diretorio_saida, text=texto_formatado)
        status = "Selecione o diretório de saída"
        status_color = "#FFFF00"  # Define a cor para amarelo
        update_status_color()
        print("Seleção de diretório de saída cancelada")
    else:
        text_diretorio_saida = diretorio_saida
        texto_formatado = textwrap.fill(text_diretorio_saida, 60) # Formata o texto para quebrar a linha
        canvas.itemconfig(label_diretorio_saida, text=texto_formatado)
        status = "Diretório de saída selecionado"
        update_status_color()
        if diretorio_inicial:
            change_color_to_green()
        else:
            status = "Selecione o diretório inicial"
            status_color = "#FFFF00"  # Define a cor para amarelo
            update_status_color()

        print("Botão 'Selecionar diretório de saída' pressionado")
        print(f"Diretório saída: {diretorio_saida}")

def porque_usar():
    print("Botão 'Porque usar' pressionado")

def qual_e_o_padrao():
    print("Botão 'Qual é o padrão' pressionado")

def executar_script():
    # print("Botão 'Executar script' pressionado")
    change_color_to_red()
    organizador.renomear_arquivos(diretorio_inicial, diretorio_saida, atualizar_label_log)
    change_color_to_yellow()
    
window = Tk()

window.title("savio.dev.br")
window.geometry("700x500")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Título
canvas.place(x = 0, y = 0)
canvas.create_text(
    302.0,
    8.0,
    anchor="nw",
    text="AutoMove 1.0",
    fill="#000000",
    font=("Inter", 12 * -1)
)

# Sinal do status
rectangle = canvas.create_rectangle(
    10.0,
    478.0,
    22.0,
    490.0,
    fill=status_color,
    outline="")

# Texto do status
frase_status = canvas.create_text(
    32.0,
    478.0,
    anchor="nw",
    text="Status: Selecione os diretórios",
    fill="#000000",
    font=("Inter", 12 * -1)
)

# Log de operação
label_log = canvas.create_text(
    225.0,
    458.0,
    anchor="nw",
    text="",
    fill="#818181",
    font=("Inter", 10 * -1)
)

# Botões

# Botão 1 - Selecionar diretório inicial
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_diretorio_inicial(),
    relief="flat"
)
button_1.place(
    # x=60.0,
    x=100.0,
    y=246.0,
    width=174.0,
    height=26.0
)

# Botão 2 - Selecionar diretório de saída
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selecionar_diretorio_saida(),
    relief="flat"
)
button_2.place(
    # x=60.0,
    x=100.0,
    y=323.0,
    width=184.0,
    height=26.0
)

# Botão 3 - Porque usar
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: porque_usar(),
    relief="flat"
)
button_3.place(
    x=373.0,
    y=78.0,
    width=101.0,
    height=26.0
)

# Botão 4 - Qual é o padrão
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: qual_e_o_padrao(),
    relief="flat"
)
button_4.place(
    x=369.0,
    y=165.0,
    width=109.0,
    height=26.0
)

# Botão 5 - Executar script
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: executar_script(),
    relief="flat",
    state= "disabled"
)
button_5.place(
    x=245.0,
    y=393.0,
    width=209.0,
    height=52.0
)

# Textos

# Texto do caminho do diretório inicial
label_diretorio_inicial = canvas.create_text(
    295.0,
    252.0,
    # 51.0,
    # 281.0,
    anchor="nw",
    text=text_diretorio_inicial,
    fill="#818181",
    font=("Inter", 12 * -1)
)

# Texto do caminho do diretório de saída
label_diretorio_saida = canvas.create_text(
    295.0,
    329.0,    
    # 51.0,
    # 358.0,
    anchor="nw",
    text=text_diretorio_saida,
    fill="#818181",
    font=("Inter", 12 * -1)
)

# Texto de instrução
canvas.create_text(
    51.0,
    64.0,
    anchor="nw",
    text="Esta ferramenta tem o propósito de \n"
    "facilitar a organização dos arquivos de \n"
    "imagem gerados para Timelapse pela \n"
    "câmera Intebras VIP.",
    fill="#000000",
    font=("Inter", 14 * -1)
)

# Texto de instrução
canvas.create_text(
    51.0,
    157.0,
    anchor="nw",
    text="O script move as imagens contidas nas\n"
    "pastas e subpastas que correspondem ao\n"
    "padrão e renomeia com a data do registro.",
    fill="#000000",
    font=("Inter", 14 * -1)
)

window.resizable(False, False)
window.mainloop()
