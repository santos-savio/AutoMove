from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Teste integração Smart Commit Jira

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame3"

print(ASSETS_PATH)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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

canvas.place(x = 0, y = 0)
canvas.create_text(
    200.0,
    8.0,
    anchor="nw",
    text="AutoMove 1.0",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    10.0,
    378.0,
    22.0,
    390.0,
    fill="#000000",
    outline="")

canvas.create_text(
    32.0,
    378.0,
    anchor="nw",
    text="Executando, não interromper...",
    fill="#000000",
    font=("Inter", 12 * -1)
)

img_selecionar_pasta_origem = PhotoImage(
    file=relative_to_assets("img_selecionar_pasta_origem.png"))
button_selecionar_pasta_origem = Button(
    image=img_selecionar_pasta_origem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Selecionar pasta de origem"),
    relief="flat"
)
button_selecionar_pasta_origem.place(
    x=153.0,
    y=61.0,
    width=174.0,
    height=26.0
)

img_selecionar_pasta_destino = PhotoImage(
    file=relative_to_assets("img_selecionar_pasta_destino.png"))
button_selecionar_pasta_destino = Button(
    image=img_selecionar_pasta_destino,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Escolher pasta de destino"),
    relief="flat"
)
button_selecionar_pasta_destino.place(
    x=148.0,
    y=138.0,
    width=184.0,
    height=26.0
)

canvas.create_text(
    32.0,
    303.0,
    anchor="nw",
    text="Processando: \nProcessando: \nProcessando: ",
    fill="#818181",
    font=("Inter", 10 * -1)
)

img_help = PhotoImage(
    file=relative_to_assets("img_help.png"))
button_ajuda = Button(
    image=img_help,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Ajuda"),
    relief="flat"
)
button_ajuda.place(
    x=435.0,
    y=15.0,
    width=30.0,
    height=30.0
)

img_executar_script = PhotoImage(
    file=relative_to_assets("img_executar_script.png"))
button_executar = Button(
    image=img_executar_script,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_executar.place(
    x=140.0,
    y=226.0,
    width=200.0,
    height=52.0
)

canvas.create_text(
    250.0,
    96.0,
    anchor="n",
    text="Nenhum diretório selecionado",
    fill="#818181",
    font=("Inter", 12 * -1),
    width=475.0,
)

canvas.create_text(
    250.0,
    173.0,
    anchor="n",
    text="Nenhum diretório selecionado",
    fill="#818181",
    font=("Inter", 12 * -1),
    width=475.0
)
window.resizable(False, False)
window.mainloop()
