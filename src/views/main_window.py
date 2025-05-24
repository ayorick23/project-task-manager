import customtkinter as ctk
from PIL import Image, ImageTk
import datetime
from models.task_manager import *
from views.editor import MarkdownEditor
from views.pensum import PensumWindow
from PIL import ImageDraw
from views.widgets import WeekWidget
import textwrap
from models.task_manager import primeras_info_materias
from views.inicio import InicioView

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
        
        self.selected_index = None
        self.select_option(0)
        
        # Lateral derecho
        self.right_frame = ctk.CTkFrame(self, width=340, fg_color="white", corner_radius=0)
        self.right_frame.grid(row=0, column=2, sticky="nsew")
        self.right_frame.grid_propagate(False)
        
        # Título "Perfil" en la parte superior izquierda del right_frame
        perfil_label = ctk.CTkLabel(
            self.right_frame,
            text="Perfil",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#222",
            fg_color="white",
            anchor="w",
            justify="left"
        )
        perfil_label.pack(anchor="nw", padx=30, pady=(30, 0))
        
        # Foto de perfil circular
        profile_img = Image.open("src/assets/profile.jpg").resize((120, 120))
        mask = Image.new("L", (120, 120), 0)
        draw = Image.new("RGBA", (120, 120))
        mask_draw = Image.new("L", (120, 120), 0)
        ImageDraw.Draw(mask_draw).ellipse((0, 0, 120, 120), fill=255)
        profile_img.putalpha(mask_draw)
        profile_ctk_img = ctk.CTkImage(light_image=profile_img, size=(120, 120))
        profile_label = ctk.CTkLabel(self.right_frame, image=profile_ctk_img, text="", fg_color="white")
        profile_label.image = profile_ctk_img
        profile_label.pack(pady=(20, 20))

        # Nombre del usuario
        user_name_label = ctk.CTkLabel(
            self.right_frame,
            text="Dereck Mendez",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#222",
            fg_color="white"
        )
        user_name_label.pack(pady=(0, 20))
        
        # Ajustar el texto de la carrera para que tenga saltos de línea si es muy largo
        career_text = "Futuro Ingenierio en Desarrollo de Software y Ciencia de Datos"
        # Puedes ajustar el ancho máximo de caracteres por línea según tu preferencia
        wrapped_career = "\n".join(textwrap.wrap(career_text, width=32))
        
        # Carrera universitaria
        user_career_label = ctk.CTkLabel(
            self.right_frame,
            text=wrapped_career,
            font=ctk.CTkFont(size=20),
            text_color="#555",
            fg_color="white"
        )
        user_career_label.pack(pady=(0, 30))

        # Espacio para el widget de calendario
        calendar_widget = WeekWidget(self.right_frame)
        calendar_widget.pack(pady=20, padx=20, fill="x")

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
            inicio = InicioView(self.content_frame, self.select_option)
            inicio.pack(fill="both", expand=True)
            """
            # Obtener la hora actual
            now = datetime.datetime.now().hour
            if 5 <= now < 12:
                saludo = "¡Buenos días"
            elif 12 <= now < 19:
                saludo = "¡Buenas tardes"
            else:
                saludo = "¡Buenas noches"

            # Nombre del usuario (cambiar por usuario real
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

            ## Contenedor para los botones de materias
            materias_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
            materias_frame.pack(anchor="w", padx=40, pady=(0, 0))

            materias_db = primeras_info_materias()  # Debe retornar una lista de dicts o tuplas con los datos

            # Cargar un icono por defecto para las materias
            default_icon_path = "src/assets/programacion.png"
            try:
                default_icon = ctk.CTkImage(light_image=Image.open(default_icon_path), size=(90, 90))
            except Exception:
                default_icon = None

            # Redefinir la lista de materias para usar los datos de la base
            materias = materias_db[:6]

            # Crear los botones de materias en dos filas de tres
            for i, materia in enumerate(materias):
                # materia es un diccionario con claves como: nombre, profesor, seccion, horario, icon_path (opcional)
                nombre = materia.get("Materia", "Materia")
                profesor = materia.get("Profesor", "Profesor")
                seccion = materia.get("Seccion", "Sección")
                ciclo = materia.get("Ciclo", "Ciclo")
                icon_path = materia.get("Icono", "Icono")
                try:
                    icon = ctk.CTkImage(light_image=Image.open(icon_path), size=(90, 90))
                except Exception:
                    icon = default_icon

                btn_frame = ctk.CTkFrame(materias_frame, fg_color="white", corner_radius=20, width=374, height=154)
                btn_frame.grid_propagate(False)

                # Icono a la izquierda
                icon_label = ctk.CTkLabel(btn_frame, image=icon, text="", width=90)
                icon_label.grid(row=0, column=0, rowspan=4, padx=(20, 10), pady=30, sticky="n")

                # Nombre de la materia
                nombre_label = ctk.CTkLabel(
                    btn_frame,
                    text=nombre,
                    font=ctk.CTkFont(size=24, weight="bold"),
                    text_color="#222",
                    anchor="w"
                )
                nombre_label.grid(row=0, column=1, sticky="w", padx=15, pady=(20, 10))

                # Profesor, sección y ciclo
                profesor_label = ctk.CTkLabel(
                    btn_frame,
                    text=f"{profesor}",
                    font=ctk.CTkFont(size=16),
                    text_color="#555",
                    anchor="w"
                )
                profesor_label.grid(row=1, column=1, sticky="we", padx=15, pady=0)
                
                seccion_label = ctk.CTkLabel(
                    btn_frame,
                    text=f"Sección {seccion}",
                    font=ctk.CTkFont(size=16),
                    text_color="#555",
                    anchor="w"
                )
                seccion_label.grid(row=2, column=1, sticky="we", padx=15, pady=0)
                
                ciclo_label = ctk.CTkLabel(
                    btn_frame,
                    text=f"{ciclo}",
                    font=ctk.CTkFont(size=16),
                    text_color="#555",
                    anchor="w"
                )
                ciclo_label.grid(row=3, column=1, sticky="we", padx=15, pady=(0, 20))

                # Hacer que todo el frame sea clickeable
                btn_frame.bind("<Button-1>", lambda e, idx=i: materia_callback(idx))
                icon_label.bind("<Button-1>", lambda e, idx=i: materia_callback(idx))
                nombre_label.bind("<Button-1>", lambda e, idx=i: materia_callback(idx))
                profesor_label.bind("<Button-1>", lambda e, idx=i: materia_callback(idx))
                seccion_label.bind("<Button-1>", lambda e, idx=i: materia_callback(idx))
                ciclo_label.bind("<Button-1>", lambda e, idx=i: materia_callback(idx))

                row = i // 3
                col = i % 3
                btn_frame.grid(row=row, column=col, padx=(5, 10), pady=10, sticky="nsew")
                materias_frame.grid_columnconfigure(col, weight=1)
                
            def materia_callback(idx):
                self.select_option(1)  # Cambia esto si tienes una vista específica para cada materia
        """
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
            pensum = PensumWindow(self.content_frame)
            pensum.pack(fill="both", expand=True)
        # ESTADISTICAS
        if index == 5:
            print("Estadísticas")
        # RECORDATORIOS
        if index == 6:
            print("Recordatorios")
        else:
            pass