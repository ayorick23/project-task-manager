import customtkinter as ctk
from PIL import Image

# Inicializar ventana principal
root = ctk.CTk()
root.title("Pantalla Principal")
root.geometry("1000x650")
root.resizable(False, False)

# Frame del menú lateral
menu_frame = ctk.CTkFrame(root, width=250, fg_color=("white", "#141414"), corner_radius=0)
menu_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")  # Se expande en toda la altura

# Configurar el `grid` para que ocupe toda la altura
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=0)  # Fijar ancho del menú lateral
root.grid_columnconfigure(1, weight=3)  # Contenido principal
root.grid_columnconfigure(2, weight=1)  # Panel derecho
#root.grid_columnconfigure(1, weight=1)  # Espacio para contenido principal

# Logo centrado
logo_image = ctk.CTkImage(light_image=Image.open("src/assets/UEES_logo.png"), size=(125, 125))
logo_label = ctk.CTkLabel(menu_frame, image=logo_image, text="")
logo_label.grid(row=0, column=0, pady=30, sticky="n")  # Centrado en la parte superior

# Opciones del menú (6 botones)
botones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5", "Opción 6"]

for i, texto in enumerate(botones):
    boton = ctk.CTkButton(menu_frame, text=texto, width=200)
    boton.grid(row=i + 1, column=0, pady=5, padx=10, sticky="ew")  # Se alinean verticalmente

# Mantener ventana abierta
root.mainloop()