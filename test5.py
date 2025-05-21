import customtkinter as ctk
from PIL import Image

# Inicializar ventana principal
root = ctk.CTk()
root.title("Pantalla Principal")
root.geometry("1000x650")
root.resizable(False, False)

# Frame del menú lateral
menu_frame = ctk.CTkFrame(root, fg_color=("white", "#141414"), corner_radius=0, width=250, height=650)
menu_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")

# Configuración de la cuadrícula
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)

# Logo centrado
logo_image = ctk.CTkImage(light_image=Image.open("src/assets/UEES_logo.png"), size=(125, 125))
logo_label = ctk.CTkLabel(menu_frame, image=logo_image, text="")
logo_label.grid(row=0, column=0, pady=30, sticky="n")

# Botones del menú
botones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5", "Opción 6"]
for i, texto in enumerate(botones):
    boton = ctk.CTkButton(menu_frame, text=texto, width=200)
    boton.grid(row=i + 1, column=0, pady=5, padx=10, sticky="ew")

# Función para mostrar/ocultar el menú
def toggle_menu():
    global menu_visible
    if menu_visible:
        slide_out()  # Desliza el menú fuera de la pantalla
        #menu_frame.grid_forget()  # Oculta el menú
        toggle_btn.configure(text="☰")
    else:
        slide_in()  # Desliza el menú dentro de la pantalla
        #menu_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")  # Muestra el menú
        toggle_btn.configure(text="☰")
    menu_visible = not menu_visible

# Botón de alternancia
menu_visible = True  # Estado inicial del menú (visible)
toggle_btn = ctk.CTkButton(root, text="☰", command=toggle_menu, width=40)
toggle_btn.grid(row=0, column=0, pady=10, padx=10, sticky="nw")
#toggle_btn = ctk.CTkButton(root, text="Ocultar menú", command=toggle_menu)
#toggle_btn.grid(row=0, column=1, pady=10, padx=10, sticky="ne")

def fade_out():
    global menu_opacity
    if menu_opacity > 0:
        menu_opacity -= 0.1
        menu_frame.configure(fg_color=(f"#{int(menu_opacity * 255):02x}2F2F77", f"#{int(menu_opacity * 255):02x}141414"))
        #menu_frame.configure(fg_color=f"#{int(menu_opacity * 255):02x}141414")  # Ajusta el color dinámicamente
        root.after(50, fade_out)  # Llama a la función de nuevo tras 50ms
    else:
        menu_frame.grid_forget()

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def fade_out():
    global menu_opacity
    if menu_opacity > 0:
        menu_opacity -= 0.1
        color = rgb_to_hex(int(menu_opacity * 47), int(menu_opacity * 47), int(menu_opacity * 119))  # Ajuste progresivo
        menu_frame.configure(fg_color=(color, "#141414"))  # Alterna entre colores claros y oscuros
        root.after(50, fade_out)
    else:
        menu_frame.grid_forget()

def fade_in():
    menu_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
    global menu_opacity
    menu_opacity = 0

    def increase_opacity():
        global menu_opacity
        if menu_opacity < 1:
            menu_opacity += 0.1
            color = rgb_to_hex(int(menu_opacity * 47), int(menu_opacity * 47), int(menu_opacity * 119))
            menu_frame.configure(fg_color=(color, "#141414"))
            root.after(50, increase_opacity)

    increase_opacity()
    
def slide_out():
    x = menu_frame.winfo_x()
    if x > -250:
        menu_frame.place(x=x - 10)  # Mueve el menú fuera de la pantalla lentamente
        root.after(10, slide_out)
    else:
        menu_frame.place_forget()

def slide_in():
    menu_frame.place(x=-250, y=0)  # Comienza fuera de la pantalla

    def animate():
        x = menu_frame.winfo_x()
        if x < 0:
            menu_frame.place(x=x + 10, y=0)  # Solo modificar `x`, sin tocar `width` ni `height`
            root.after(10, animate)

    animate()

# Mantener ventana abierta
root.mainloop()