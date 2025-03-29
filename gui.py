import tkinter as tk
from tkinter import Entry, Label, Button, Frame, Canvas
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("800x500")
root.resizable(False, False)

# Crear un Canvas para dividir el fondo
canvas = Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)

# Crear la parte del fondo con degradado (se simula con una imagen o color sólido)
canvas.create_rectangle(0, 0, 400, 500, fill="#FFD700", outline="")  # Amarillo
canvas.create_rectangle(400, 0, 800, 500, fill="white", outline="")

# Cargar la imagen del icono (Asegúrate de tener una imagen en el directorio)
# Se necesita una imagen en formato PNG para que funcione correctamente
try:
    img = Image.open("icono.png")  # Ruta de la imagen
    img = img.resize((100, 100), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(600, 100, image=img_tk)
except:
    pass

# Crear el Frame para el formulario
frame = Frame(root, bg="white")
frame.place(x=450, y=200, width=300, height=200)

# Etiqueta y campo de usuario
Label(frame, text="Usuario", bg="white", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10, 0))
Entry(frame, font=("Segoe UI", 12), bd=2, relief="groove").pack(fill="x", padx=10, pady=5)

# Etiqueta y campo de contraseña
Label(frame, text="Contraseña", bg="white", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10, 0))
Entry(frame, font=("Segoe UI", 12), bd=2, relief="groove", show="*").pack(fill="x", padx=10, pady=5)

# Botón de acceso
Button(frame, text="Acceder", font=("Segoe UI", 12), bg="black", fg="white", cursor="hand2").pack(fill="x", padx=10, pady=20)

root.mainloop()