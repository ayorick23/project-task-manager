import customtkinter as ctk
from PIL import Image, ImageTk
import datetime
from models.task_manager import *
from views.editor import MarkdownEditor

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class SidebarButton(ctk.CTkButton):
    def __init__(self, master, text, icon_path, command=None, **kwargs):
        icon = ctk.CTkImage(light_image=Image.open(icon_path), size=(24, 24))
        super().__init__(
            master,
            text=text,
            image=icon,
            anchor="w",
            compound="left",
            fg_color="white",
            text_color="black",
            hover_color="#e0e0e0",
            corner_radius=8,
            command=command,
            **kwargs
        )
        self.icon = icon

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("UEESential")
        self.geometry("1080x720")
        self.after(0, lambda: self.state('zoomed'))

        # Layout principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.minsize(1080, 720)
        
        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=340, fg_color="white", corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Logo
        logo_img = ctk.CTkImage(light_image=Image.open("src/assets/UEES_logo.png"), size=(120, 120))
        self.logo_label = ctk.CTkLabel(self.sidebar, image=logo_img, text="", fg_color="white")
        self.logo_label.image = logo_img
        self.logo_label.pack(pady=(50, 50))

        # Opciones del menú
        self.menu_options = [
            ("Inicio", "src/assets/inicio.png"),
            ("Materias", "src/assets/materias.png"),
            ("Notas de clases", "src/assets/apunte.png"),
            ("Actividades", "src/assets/actividades.png"),
            ("Pensum", "src/assets/pensum.png"),
            ("Estadisticas", "src/assets/estadistica.png"),
            ("Recordatorios", "src/assets/recordatorio.png"),
        ]
        self.menu_buttons = []
        for idx, (text, icon) in enumerate(self.menu_options):
            btn = SidebarButton(
                self.sidebar,
                text=text,
                icon_path=icon,
                command=lambda i=idx: self.select_option(i),
                height=40,
                width=260
            )
            btn.pack(pady=10, padx=40, fill="x")
            self.menu_buttons.append(btn)

        # Contenido principal
        self.content_frame = ctk.CTkFrame(self, fg_color="#f5f6fa", corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.grid_propagate(True)

        # Lateral derecho
        self.right_frame = ctk.CTkFrame(self, width=340, fg_color="white", corner_radius=0)
        self.right_frame.grid(row=0, column=2, sticky="nsew")
        self.right_frame.grid_propagate(False)
        
        self.selected_index = None
        self.select_option(0)

    def select_option(self, index):
        # Cambia el color del botón seleccionado
        for i, btn in enumerate(self.menu_buttons):
            if i == index:
                btn.configure(fg_color="#e3f2fd")
            else:
                btn.configure(fg_color="white")
        self.selected_index = index
        
        # Cambia el contenido principal según la opción
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # INICIO
        if index == 0:
            # Obtener la hora actual
            now = datetime.datetime.now().hour
            if 5 <= now < 12:
                saludo = "¡Buenos días"
            elif 12 <= now < 19:
                saludo = "¡Buenas tardes"
            else:
                saludo = "¡Buenas noches"

            # Nombre del usuario (puedes cambiarlo por una variable si lo deseas)
            nombre_usuario = "Dereck"

            # Saludo principal
            saludo_label = ctk.CTkLabel(
            self.content_frame,
            text=f"{saludo}, {nombre_usuario}!",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#222"
            )
            saludo_label.pack(anchor="w", padx=40, pady=(30, 0))

            # Subtítulo
            subtitulo_label = ctk.CTkLabel(
            self.content_frame,
            text="¿En qué vamos a avanzar hoy?",
            font=ctk.CTkFont(size=20),
            text_color="#555"
            )
            subtitulo_label.pack(anchor="w", padx=40, pady=(10, 30))

            # Título "Mis Materias"
            materias_titulo = ctk.CTkLabel(
            self.content_frame,
            text="Mis Materias",
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color="#222"
            )
            materias_titulo.pack(anchor="w", padx=40, pady=(0, 20))

            # Lista de materias (puedes personalizar estos nombres)
            materias = [
            "Matemáticas",
            "Física",
            "Química",
            "Programación",
            "Historia",
            "Inglés"
            ]

            # Contenedor para los botones de materias
            materias_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
            materias_frame.pack(anchor="w", padx=40, pady=(0, 0))

            def materia_callback(idx):
                self.select_option(1)  # Cambia esto si tienes una vista específica para cada materia

            # Crear los botones de materias en dos filas de tres
            for i, materia in enumerate(materias):
                btn = ctk.CTkButton(
                    materias_frame,
                    text=materia,
                    width=374,
                    height=154,
                    fg_color="blue",
                    text_color="#222",
                    font=ctk.CTkFont(size=18, weight="bold"),
                    corner_radius=20,
                    command=lambda idx=i: materia_callback(idx)
                )
                row = i // 3
                col = i % 3
                btn.grid(row=row, column=col, padx=(5, 10), pady=10, sticky="nsew")
                materias_frame.grid_columnconfigure(col, weight=1)
        # MATERIAS
        if index == 1:
            print("Materias")
        # NOTAS DE CLASES
        if index == 2:
            editor = MarkdownEditor(self.content_frame)
            editor.pack(fill="both", expand=True)
        # ACTIVIDADES
        if index == 3:
            print("Actividades")
        # PENSUM
        if index == 4:
            print("Pensum")
        # ESTADISTICAS
        if index == 5:
            print("Estadísticas")
        # RECORDATORIOS
        if index == 6:
            print("Recordatorios")
        else:
            """
            # Vista por defecto para otras opciones
            label = ctk.CTkLabel(
            self.content_frame,
            text=f"Vista: {self.menu_options[index][0]}",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#222"
            )
            label.pack(pady=40)
            """
            pass