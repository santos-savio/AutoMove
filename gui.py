from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=153.0,
    y=61.0,
    width=174.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
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

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=435.0,
    y=15.0,
    width=30.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
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
# window.mainloop()
