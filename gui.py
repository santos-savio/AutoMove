from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "buttons"

print(ASSETS_PATH)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("savio.dev.br")
window.geometry("480x400")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 480,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Título
canvas.place(x = 0, y = 0)
canvas.create_text(
    200.0,
    8.0,
    anchor="nw",
    text="AutoMove 1.0",
    fill="#000000",
    font=("Inter", 12 * -1)
)

# Sinal do status
cor_status = canvas.create_oval(
    10.0,
    378.0,
    22.0,
    390.0,
    fill="#FF0000",
    outline="")

# Texto do status
frase_status = canvas.create_text(
    32.0,
    378.0,
    anchor="nw",
    text="Status: Selecione os diretórios",
    fill="#000000",
    font=("Inter", 12 * -1)
)

# Botão de selecionar pasta de origem
img_selecionar_pasta_origem = PhotoImage(
    file=relative_to_assets("img_selecionar_pasta_origem.png"))
button_selecionar_pasta_origem = Button(
    image=img_selecionar_pasta_origem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: controller.selecionar_pasta_origem(),
    relief="flat"
)
button_selecionar_pasta_origem.place(
    x=153.0,
    y=61.0,
    width=174.0,
    height=26.0
)

# Botão de selecionar pasta de destino
img_selecionar_pasta_destino = PhotoImage(
    file=relative_to_assets("img_selecionar_pasta_destino.png"))
button_selecionar_pasta_destino = Button(
    image=img_selecionar_pasta_destino,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: print("Escolher pasta de destino"),
    command=lambda: controller.selecionar_pasta_destino(),
    relief="flat"
)
button_selecionar_pasta_destino.place(
    x=148.0,
    y=138.0,
    width=184.0,
    height=26.0
)

# Log de processamento
label_log = canvas.create_text(
    32.0,
    303.0,
    anchor="nw",
    text="",
    fill="#818181",
    font=("Inter", 10 * -1)
)

# Botão de ajuda
img_help = PhotoImage(
    file=relative_to_assets("img_help.png"))
button_ajuda = Button(
    image=img_help,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: print("Ajuda"),
    command=lambda: controller.ajuda(),
    relief="flat"
)
button_ajuda.place(
    x=435.0,
    y=15.0,
    width=30.0,
    height=30.0
)

# Botão de executar script
img_executar_script = PhotoImage(
    file=relative_to_assets("img_executar_script.png"))
button_executar = Button(
    image=img_executar_script,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: print("executar script"),
    command=lambda: controller.executar_script(),
    relief="flat"
)
button_executar.place(
    x=140.0,
    y=226.0,
    width=200.0,
    height=52.0
)

# Texto do caminho do diretório inicial
label_diretorio_inicial = canvas.create_text(
    250.0,
    96.0,
    anchor="n",
    text="Nenhuma pasta selecionada",
    fill="#818181",
    font=("Inter", 12 * -1),
    width=475.0,
)

# Texto do caminho do diretório de saída
label_diretorio_saida = canvas.create_text(
    250.0,
    173.0,
    anchor="n",
    text="Nenhuma pasta selecionada",
    fill="#818181",
    font=("Inter", 12 * -1),
    width=475.0
)
window.resizable(False, False)
window.mainloop()
