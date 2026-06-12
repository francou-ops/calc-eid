import customtkinter as ctk
import matplotlib.figure as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

cEID = ctk.CTk()
cEID.geometry("1080x720")
cEID.title("Programa Cálculo EID")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
cEID.grid_columnconfigure(0, weight=1)
cEID.grid_rowconfigure(0, weight=1)


cajatexto = ctk.CTkTextbox(cEID, width=400, height=100)
cajatexto.pack(pady=20, padx=47, anchor="nw")

frame_botones = ctk.CTkFrame(cEID, fg_color="transparent")
frame_botones.pack(pady=20, padx=20, anchor="nw")

#grafico = ctk.CTkFrame(cEID)
#grafico.pack(side="right", fill="both", expand=True, padx=10, pady=10)


x = sp.Symbol('x')

def Calcular():
    pass

def Graficar():
    pass

def Limpiar():
    cajatexto.delete("0.0", ctk.END)

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


boton_calcular = ctk.CTkButton(master=frame_botones, text="Calcular", command=Calcular, width=100)
boton_calcular.grid(row=0, column=0, padx=5, pady=5)

boton_graficar = ctk.CTkButton(master=frame_botones, text="Graficar", command=Graficar, width=100)
boton_graficar.grid(row=0, column=1, padx=5, pady=5)

boton_limpiar = ctk.CTkButton(master=frame_botones, text="Limpiar", command=Limpiar, width=100)
boton_limpiar.grid(row=0, column=2, padx=5, pady=5)

boton_infinito_negativo = ctk.CTkButton(master=frame_botones, text="-oo", command=InfinitoNegativo)
boton_infinito_negativo.grid(row=1, column=0, padx=5, pady=5)

boton_infinito_positivo = ctk.CTkButton(master=frame_botones, text="+oo", command=InfinitoPositivo)
boton_infinito_positivo.grid(row=1, column=2, padx=5, pady=5)

boton_sin = ctk.CTkButton(master=frame_botones, text="sen(x)", command=Sin)
boton_sin.grid(row=2, column=0, padx=5, pady=5)

boton_cos = ctk.CTkButton(master=frame_botones, text="cos(x)", command=Cos)
boton_cos.grid(row=2, column=1, padx=5, pady=5)

boton_tg = ctk.CTkButton(master=frame_botones, text="tan(x)", command=Tg)
boton_tg.grid(row=2, column=2, padx=5, pady=5)

boton_raiz = ctk.CTkButton(master=frame_botones, text="√x", command=Raiz)
boton_raiz.grid(row=1, column=1, pady=5, padx=5)




cEID.mainloop()
