import customtkinter as ctk
import matplotlib.figure as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

cEID = ctk.CTk()
cEID.geometry("1280x720")
cEID.title("Programa Cálculo EID")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
cEID.grid_columnconfigure(0, weight=1)
cEID.grid_rowconfigure(0, weight=1)

x = sp.Symbol('x')

cEID.grid_columnconfigure(0, weight=1) # Panel izquierdo
cEID.grid_columnconfigure(1, weight=4) # Panel derecho 
cEID.grid_rowconfigure(0, weight=1)

frame_izquierdo = ctk.CTkFrame(cEID, fg_color="transparent")
frame_izquierdo.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

frame_derecho = ctk.CTkFrame(cEID, fg_color="#1a1a1a")
frame_derecho.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

titulo = ctk.CTkLabel(master=frame_izquierdo, text="Calculadora EID", font=("ARIAL", 24, "bold"), text_color="#D92B4F")
titulo.pack(pady=20, padx=20, anchor="nw")
ingfunc = ctk.CTkLabel(master=frame_izquierdo, text="Ingrese la función:", font=("ARIAL", 16), text_color="#C2294C")
ingfunc.pack(pady=10, padx=20, anchor="nw")
cajatexto = ctk.CTkTextbox(frame_izquierdo, width=400, height=50)
cajatexto.pack(pady=10, padx=47, anchor="nw")
ingtend = ctk.CTkLabel(master=frame_izquierdo, text="Ingrese la tendencia:", font=("ARIAL", 16), text_color="#C2294C")
ingtend.pack(pady=10, padx=20, anchor="nw")
cajatextoten = ctk.CTkTextbox(frame_izquierdo, width=400, height=50)
cajatextoten.pack(pady=10, padx=47, anchor="nw")
atajos = ctk.CTkLabel(master=frame_izquierdo, text="Atajos y opciones:", font=("ARIAL", 16), text_color="#C2294C")
atajos.pack(pady=10, padx=20, anchor="nw")
frame_botones = ctk.CTkFrame(frame_izquierdo, fg_color="transparent")
frame_botones.pack(pady=10, padx=20, anchor="nw")
resultados = ctk.CTkLabel(master=frame_izquierdo, text="Resultados:", font=("ARIAL", 16), text_color="#C2294C")
resultados.pack(pady=10, padx=20, anchor="nw")
label_resultado = ctk.CTkLabel(frame_izquierdo, text="Resultado del cálculo:", font=("ARIAL", 16), text_color="#CAC4C5",fg_color="#2B2B2B",corner_radius=8,width=400,height=50)
label_resultado.pack(pady=10, padx=45, anchor="nw")

fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=frame_derecho)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

def Calcular():
    pass

def Graficar():
    ax.clear()

def Limpiar():
    cajatexto.delete("0.0", ctk.END)
    cajatextoten.delete("0.0", ctk.END)

def InfinitoNegativo():
    pass

def InfinitoPositivo():
    pass

def Sin():
    cajatexto.insert(ctk.END, "sin(x)")

def Cos():
    cajatexto.insert(ctk.END, "cos(x)")

def Tg():
    cajatexto.insert(ctk.END, "tan(x)")

def Raiz():
    pass

boton_calcular = ctk.CTkButton(master=frame_botones, text="Calcular", command=Calcular, width=100, fg_color="#D92B4F", hover_color="#C2294C")
boton_calcular.grid(row=0, column=0, padx=5, pady=5)
boton_graficar = ctk.CTkButton(master=frame_botones, text="Graficar", command=Graficar, width=100, fg_color="#D92B4F", hover_color="#C2294C")
boton_graficar.grid(row=0, column=1, padx=5, pady=5)
boton_limpiar = ctk.CTkButton(master=frame_botones, text="Limpiar", command=Limpiar, width=100, fg_color="#D92B4F", hover_color="#C2294C")
boton_limpiar.grid(row=0, column=2, padx=5, pady=5)

boton_infinito_negativo = ctk.CTkButton(master=frame_botones, text="-oo", command=InfinitoNegativo, fg_color="#D92B4F", hover_color="#C2294C")
boton_infinito_negativo.grid(row=1, column=0, padx=5, pady=5)
boton_infinito_positivo = ctk.CTkButton(master=frame_botones, text="+oo", command=InfinitoPositivo, fg_color="#D92B4F", hover_color="#C2294C")
boton_infinito_positivo.grid(row=1, column=2, padx=5, pady=5)

boton_sin = ctk.CTkButton(master=frame_botones, text="sen(x)", command=Sin, fg_color="#D92B4F", hover_color="#C2294C")
boton_sin.grid(row=2, column=0, padx=5, pady=5)
boton_cos = ctk.CTkButton(master=frame_botones, text="cos(x)", command=Cos, fg_color="#D92B4F", hover_color="#C2294C")
boton_cos.grid(row=2, column=1, padx=5, pady=5)
boton_tg = ctk.CTkButton(master=frame_botones, text="tan(x)", command=Tg, fg_color="#D92B4F", hover_color="#C2294C")
boton_tg.grid(row=2, column=2, padx=5, pady=5)

boton_raiz = ctk.CTkButton(master=frame_botones, text="√x", command=Raiz, fg_color="#D92B4F", hover_color="#C2294C")
boton_raiz.grid(row=1, column=1, pady=5, padx=5)

cEID.mainloop()