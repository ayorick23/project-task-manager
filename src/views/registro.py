import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image

#Configuración inicial
ctk.set_appearance_mode("light")
#ctk.set_default_color_theme("blue")

def CenterWindowToDisplay(Screen: ctk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/1.5))
    return f"{width}x{height}+{x}+{y}"

def switch_window(current_window, target_window_class):
    """
    Cierra la ventana actual y abre la ventana destino.
    
    Parámetros:
    - current_window: La ventana actual que será destruida
    - target_window_class: La clase de la ventana a la que se quiere navegar
    """
    # Guardar la posición de la ventana actual
    x = current_window.winfo_x()
    y = current_window.winfo_y()
    
    # Destruir la ventana actual
    current_window.destroy()
    
    # Crear y mostrar la nueva ventana
    new_window = target_window_class()
    
    # Posicionar la nueva ventana en la misma ubicación que la anterior
    new_window.geometry(f"+{x}+{y}")
    
    return new_window

def ventana_registro():
    from log_in import ventana_log_in
    #Ventana principal
    registro = ctk.CTk()
    registro.title("Registro")
    registro.geometry(CenterWindowToDisplay(registro, 1000, 650, registro._get_window_scaling()))
    registro.resizable(False, False)
    #registro.iconbitmap("src/assets/UEESential_logo.ico")

    #Frame contenedor principal
    main_frame = ctk.CTkFrame(registro, fg_color=None)
    main_frame.pack(fill="both", expand=True)

    #Contenedor para imagen derecha
    image_container = ctk.CTkFrame(main_frame, width=500, height=650, fg_color="white")
    image_container.place(relx=0.25, rely=0.5, anchor="center")

    background_image = ctk.CTkImage(
        light_image=Image.open("src/assets/registro-light-mode.png"), 
        dark_image=Image.open("src/assets/registro-dark-mode.png"), 
        size=(500, 650))
    background_label = ctk.CTkLabel(image_container, image=background_image, text="")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Frame formulario
    form_frame = ctk.CTkFrame(main_frame, width=500, height=650, fg_color=("white", "#141414"), corner_radius=0)
    form_frame.place(relx=0.75, rely=0.5, anchor="center")  #centrado dentro del frame
    form_frame.grid_propagate(False)  #desactiva el ajuste automático de tamaño del frame
                            
    # --- CONTENIDO LADO DERECHO ---
    #Logo
    logo_image = ctk.CTkImage(light_image=Image.open("src/assets/UEES_logo.png"), size=(125, 125))
    logo_label = ctk.CTkLabel(form_frame, image=logo_image, text="")
    logo_label.grid(row=0, column=0, columnspan=2, pady=30)

    #Campos de usuario, correo y contraseña
    label_user = ctk.CTkLabel(form_frame, text="Nombre de usuario", font=("Roboto", 14, "bold"), text_color=("#2F2F77", "white"))
    label_user.grid(row=1, column=0, columnspan=2, pady=2, padx=100, sticky="w")

    entry_user = ctk.CTkEntry(form_frame, placeholder_text="Dereck Méndez", width=300, height=30)
    entry_user.configure(border_color="#B3B3B3", border_width=1, corner_radius=8)
    entry_user.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=100)

    label_mail = ctk.CTkLabel(form_frame, text="Correo electrónico", font=("Roboto", 14, "bold"), text_color=("#2F2F77", "white"))
    label_mail.grid(row=3, column=0, columnspan=2, pady=2, padx=100, sticky="w")

    entry_mail = ctk.CTkEntry(form_frame, placeholder_text="ejemplo@mail.com", width=300, height=30)
    entry_mail.configure(border_color="#B3B3B3", border_width=1, corner_radius=8)
    entry_mail.grid(row=4, column=0, columnspan=2, pady=(0, 10), padx=100)

    label_password = ctk.CTkLabel(form_frame, text="Contraseña", font=("Roboto", 14, "bold"), text_color=("#2F2F77", "white"))
    label_password.grid(row=5, column=0, columnspan=2, pady=2, padx=100, sticky="w")

    entry_password = ctk.CTkEntry(form_frame, placeholder_text="*********", show="*", width=300, height=30)
    entry_password.configure(border_color="#B3B3B3", border_width=1, corner_radius=8)
    entry_password.grid(row=6, column=0, columnspan=2, pady=(0, 10), padx=100)

    #Checkbox
    #remember = ctk.CTkCheckBox(form_frame, text="Recordar mi usuario", width=300, height=30)
    #remember.grid(row=7, column=0, columnspan=2, pady=10, padx=50)

    #Botón de registrar
    register_btn = ctk.CTkButton(form_frame, text="Crear cuenta")
    register_btn.configure(font=("Roboto", 14, "bold"), fg_color="#F6DC00", hover_color="#0033FF", text_color="#2F2F77", corner_radius=8, cursor="hand2")
    register_btn.bind("<Button-1>", lambda e: register_btn.configure(fg_color="#0033FF", text_color="white"))
    register_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=100, sticky="ew")

    #Separador
    separator = ttk.Separator(form_frame, orient=tk.HORIZONTAL)
    separator.grid(row=8, column=0, columnspan=2, pady=10, padx=100, sticky="ew")

    #Continuar con Google
    continue_label = ctk.CTkLabel(form_frame, text="O continúa con:", font=("Roboto", 12), text_color=("#2F2F77", "white"))
    continue_label.grid(row=9, column=0, columnspan=2, pady=(10, 0), padx=50)

    google_btn = ctk.CTkButton(form_frame, text="Continuar con Google", image=ctk.CTkImage(Image.open("src/assets/logo-google-48.png"), size=(25, 25)))
    google_btn.configure(fg_color=("white", "#141414"), font=("Roboto", 12, "bold"), text_color=("#2F2F77", "white"), hover_color="#0033FF", border_color="#B3B3B3", border_width=1, corner_radius=8, cursor="hand2")
    google_btn.bind("<Button-1>", lambda e: google_btn.configure(fg_color="#0033FF", text_color="white"))
    google_btn.grid(row=10, column=0, columnspan=2, pady=(0, 10), padx=100, sticky="ew")

    #Labels vacios
    label_empty = ctk.CTkLabel(form_frame, text="", font=("Roboto", 12), text_color=("#2F2F77", "white"))
    label_empty.grid(row=11, column=0, pady=(0, 0), padx=(160, 0))

    #Cambiar a iniciar sesión
    label_login = ctk.CTkLabel(form_frame, text="¿Ya tienes cuenta?", font=("Roboto", 12), text_color=("#2F2F77", "white"))
    label_login.grid(row=12, column=0, pady=(10, 0), padx=(160, 0))
    link_login = ctk.CTkLabel(form_frame, text="Iniciar sesión", font=("Roboto", 12, "bold"), text_color="#0033FF", cursor="hand2")
    link_login.bind("<Button-1>", lambda e: link_login.configure(text_color="#6C0000"))
    link_login.bind("<Button-1>", lambda e: switch_window(ventana_registro, ventana_log_in))
    link_login.grid(row=12, column=1, pady=(10, 0), padx=(0, 160))

    registro.mainloop()
    
ventana_registro()