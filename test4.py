import customtkinter as ctk

root = ctk.CTk()
root.title("Ventana Maximizada y No Redimensionable")

# Maximizar la ventana sin ocultar la barra de herramientas
root.state("zoomed")

# Bloquear el cambio de tamaño
root.resizable(False, False)

root.mainloop()