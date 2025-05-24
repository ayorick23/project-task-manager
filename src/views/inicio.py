import datetime
import customtkinter as ctk
from models.task_manager import primeras_info_materias
from PIL import Image
class InicioView(ctk.CTkFrame):
    def __init__(self, parent, select_option_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.select_option = select_option_callback
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
        self._build_ui()

    def _build_ui(self):
        # Obtener la hora actual
        now = datetime.datetime.now().hour
        if 5 <= now < 12:
            saludo = "¡Buenos días"
        elif 12 <= now < 19:
            saludo = "¡Buenas tardes"
        else:
            saludo = "¡Buenas noches"

        nombre_usuario = "Dereck"

        saludo_label = ctk.CTkLabel(
            self.content_frame,
            text=f"{saludo}, {nombre_usuario}!",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#222"
        )
        saludo_label.pack(anchor="w", padx=40, pady=(30, 0))

        subtitulo_label = ctk.CTkLabel(
            self.content_frame,
            text="¿En qué vamos a avanzar hoy?",
            font=ctk.CTkFont(size=20),
            text_color="#555"
        )
        subtitulo_label.pack(anchor="w", padx=40, pady=(10, 30))

        materias_titulo = ctk.CTkLabel(
            self.content_frame,
            text="Mis Materias",
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color="#222"
        )
        materias_titulo.pack(anchor="w", padx=40, pady=(0, 20))

        materias_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        materias_frame.pack(anchor="w", padx=40, pady=(0, 0))

        materias_db = primeras_info_materias()
        default_icon_path = "src/assets/programacion.png"
        try:
            default_icon = ctk.CTkImage(light_image=Image.open(default_icon_path), size=(90, 90))
        except Exception:
            default_icon = None

        materias = materias_db[:6]

        for i, materia in enumerate(materias):
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

            icon_label = ctk.CTkLabel(btn_frame, image=icon, text="", width=90)
            icon_label.grid(row=0, column=0, rowspan=4, padx=(20, 10), pady=30, sticky="n")

            nombre_label = ctk.CTkLabel(
                btn_frame,
                text=nombre,
                font=ctk.CTkFont(size=24, weight="bold"),
                text_color="#222",
                anchor="w"
            )
            nombre_label.grid(row=0, column=1, sticky="w", padx=15, pady=(20, 10))

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

            btn_frame.bind("<Button-1>", lambda e, idx=i: self.materia_callback(idx))
            icon_label.bind("<Button-1>", lambda e, idx=i: self.materia_callback(idx))
            nombre_label.bind("<Button-1>", lambda e, idx=i: self.materia_callback(idx))
            profesor_label.bind("<Button-1>", lambda e, idx=i: self.materia_callback(idx))
            seccion_label.bind("<Button-1>", lambda e, idx=i: self.materia_callback(idx))
            ciclo_label.bind("<Button-1>", lambda e, idx=i: self.materia_callback(idx))

            row = i // 3
            col = i % 3
            btn_frame.grid(row=row, column=col, padx=(5, 10), pady=10, sticky="nsew")
            materias_frame.grid_columnconfigure(col, weight=1)

    def materia_callback(self, idx):
        self.select_option(1)
"""        
# Obtener la hora actual
now = datetime.datetime.now().hour
if 5 <= now < 12:
    saludo = "¡Buenos días"
elif 12 <= now < 19:
    saludo = "¡Buenas tardes"
else:
    saludo = "¡Buenas noches"

# Nombre del usuario (cambiar por usuario real)
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