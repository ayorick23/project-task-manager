import customtkinter as ctk
from PIL import Image, ImageTk
import datetime
from models.task_manager import *
from views.editor import MarkdownEditor
from views.pensum import PensumWindow
from PIL import ImageDraw
from views.widgets import WeekWidget, ScheduleWidget
import textwrap
from models.task_manager import primeras_info_materias
from views.inicio import InicioView
from views.materias import MateriasView

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
        calendario_widget = WeekWidget(self.right_frame)
        calendario_widget.pack(pady=20, padx=20, fill="x")
        
        #horario_widget = ScheduleWidget(self.right_frame)
        #horario_widget.pack(pady=20, padx=20, fill="x")
        
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
        # MATERIAS
        if index == 1:
            materias = MateriasView(self.content_frame, self.select_option)
            materias.pack(fill="both", expand=True)
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