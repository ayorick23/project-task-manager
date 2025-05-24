import customtkinter as ctk
from models.task_manager import primeras_info_materias
from PIL import Image
from controllers.modificar_materias import ModificarMateriaVentana

class MateriasView(ctk.CTkFrame):
    def __init__(self, parent, select_option_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.select_option = select_option_callback
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
        self._build_ui()
    
    def _build_ui(self):

        materias_titulo = ctk.CTkLabel(
            self.content_frame,
            text="Mis Materias",
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color="#222"
        )
        materias_titulo.pack(anchor="w", padx=40, pady=10)

        # Crear un frame scrollable para las materias
        materias_scrollable = ctk.CTkScrollableFrame(
            self.content_frame, 
            fg_color="transparent",
            scrollbar_fg_color="transparent"
        )
        materias_scrollable.pack(fill="both", expand=True, padx=40, pady=(0, 20))

        # Frame interno para organizar las materias en grid
        materias_frame = ctk.CTkFrame(materias_scrollable, fg_color="transparent")
        materias_frame.pack(fill="both", expand=True)

        # Obtener TODAS las materias (sin límite)
        materias_db = primeras_info_materias()
        default_icon_path = "src/assets/programacion.png"
        try:
            default_icon = ctk.CTkImage(light_image=Image.open(default_icon_path), size=(90, 90))
        except Exception:
            default_icon = None

        # Mostrar todas las materias
        materias = materias_db

        for i, materia in enumerate(materias):
            materia_id = i + 1
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
            
            # Ajustar el nombre si es muy largo
            max_length = 22
            if len(nombre) > max_length:
                # Insertar salto de línea en el espacio más cercano antes del límite
                split_idx = nombre.rfind(" ", 0, max_length)
                if split_idx == -1:
                    split_idx = max_length
                nombre = nombre[:split_idx] + "\n" + nombre[split_idx:].lstrip()
                nombre_font_size = 18
            else:
                nombre_font_size = 24
                
            nombre_label = ctk.CTkLabel(
                btn_frame,
                text=nombre,
                font=ctk.CTkFont(size=nombre_font_size, weight="bold"),
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

            # Bind events para hacer clickeable toda la tarjeta
            btn_frame.bind("<Button-1>", lambda e, idx=materia_id: self.materia_callback(idx))
            icon_label.bind("<Button-1>", lambda e, idx=materia_id: self.materia_callback(idx))
            nombre_label.bind("<Button-1>", lambda e, idx=materia_id: self.materia_callback(idx))
            profesor_label.bind("<Button-1>", lambda e, idx=materia_id: self.materia_callback(idx))
            seccion_label.bind("<Button-1>", lambda e, idx=materia_id: self.materia_callback(idx))
            ciclo_label.bind("<Button-1>", lambda e, idx=materia_id: self.materia_callback(idx))

            # Posicionar en grid (3 columnas)
            row = i // 3
            col = i % 3
            btn_frame.grid(row=row, column=col, padx=(5, 10), pady=10, sticky="nsew")
            
        # Configurar las columnas para que se expandan uniformemente
        for col in range(3):
            materias_frame.grid_columnconfigure(col, weight=1)
    
        # Mostrar la ventana ModificarMateriaVentana al hacer clic en una materia
    def materia_callback(self, idx):
        materia_id = idx
        ventana_modificar = ModificarMateriaVentana(self, materia_id)
        ventana_modificar.grab_set()