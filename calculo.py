import customtkinter as ctk #Interfaz gráfica
import matplotlib.pyplot as plt #Libreria para graficar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

# CustomTkinter (interfaz)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") # color de los botones

ventana = ctk.CTk() #Crea la ventana
ventana.title("Graficador de Límites - EID")
ventana.geometry("950x650")

canvas = None  #Se guarda el gráfico acá??

def insertar_texto(texto):
    """Esta función ya funciona: escribe en la casilla lo que aprietas en los botones"""
    entrada_funcion.insert(ctk.END, texto)

def calcular_y_graficar():
    """El botón verde llamará a esto. Por ahora está vacío con 'pass' 
    para que puedas probar la interfaz sin romper nada."""
    pass
 
# ----------- Diseño de INTEFAZ ----------- (Panel para los botones)
frame_izquierdo = ctk.CTkFrame(ventana, width=350, corner_radius=10)   #Deja una parte asignada para los botones del lado izquierdo (gris)
frame_izquierdo.pack(side="left", fill="both", expand=False, padx=15, pady=15)

frame_derecho = ctk.CTkFrame(ventana, corner_radius=10)
frame_derecho.pack(side="right", fill="both", expand=True, padx=15, pady=15)  #El expand hace que use toda el área restante (?)

# ----------- Cosas dentro del panel -----------
lbl_titulo = ctk.CTkLabel(frame_izquierdo, text="Graficador de Límites", font=("Arial", 20, "bold"))  
lbl_titulo.pack(pady=15)

# ----------- Espacio 1: f(x) ----------- (Va añadiéndose abajo de la siguiente)
lbl_funcion = ctk.CTkLabel(frame_izquierdo, text="Ingresa f(x):", font=("Arial", 12))   
lbl_funcion.pack(anchor="w", padx=20) # POS X
entrada_funcion = ctk.CTkEntry(frame_izquierdo, placeholder_text="Ej: (x**2 - 1)/(x - 1)", width=2800)
entrada_funcion.pack(pady=5, padx=20)


# ----------- Espacio 2: Valores tiende x -----------
lbl_punto = ctk.CTkLabel(frame_izquierdo, text="¿A qué valor tiende x? (x -> c):", font=("Arial", 12))
lbl_punto.pack(anchor="w", padx=20)
entrada_punto = ctk.CTkEntry(frame_izquierdo, placeholder_text="Ej: 1", width=280)
entrada_punto.pack(pady=5, padx=20)










ventana.mainloop()




