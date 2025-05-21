import customtkinter as ctk
from PIL import Image

# Configuración inicial de la app
ctk.set_appearance_mode("light")  # O "dark"
#ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("UEESential")
        self.geometry("1080x720")
        self.after(0, lambda: self.state('zoomed'))
        #self.resizable(False, False)

        # Layout: 3 columnas principales
        self.grid_columnconfigure(0, weight=1)  # Menú lateral
        self.grid_columnconfigure(1, weight=3)  # Contenido principal
        self.grid_columnconfigure(2, weight=1)  # Panel derecho

        # Llamadas para crear las secciones
        self.create_sidebar()
        self.create_main_content()
        self.create_right_panel()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#F7F7F9")
        sidebar.grid(row=0, column=0, rowspan=10, sticky="nsew")
        
        logo_image_path = "src/assets/UEES_logo.png"
        self.logo_image = ctk.CTkImage(light_image=Image.open(logo_image_path),
                                   dark_image=Image.open(logo_image_path),
                                   size=(96, 96))

        # Logo (centrado)
        logo_image = ctk.CTkLabel(sidebar, image=self.logo_image, text="")
        logo_image.pack(pady=30)

        # Botones del menú
        for item in ["Materias", "Actividades", "Notas de Clases", "Horarios", "Pensum", "Ajustes"]:
            btn = ctk.CTkButton(sidebar, text=item, bg_color="transparent", corner_radius=8)
            btn.pack(fill="x", padx=20, pady=5)

    def create_main_content(self):
        content = ctk.CTkFrame(self)
        content.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        content.grid_columnconfigure(0, weight=1)

        # Encabezado
        greeting = ctk.CTkLabel(content, text="Buenos días Dereck!", font=ctk.CTkFont(size=24, weight="bold"))
        greeting.grid(row=0, column=0, sticky="w", pady=(10, 0))

        subtitle = ctk.CTkLabel(content, text="¿En qué vamos a avanzar hoy?")
        subtitle.grid(row=1, column=0, sticky="w")

        # Barra de búsqueda
        search = ctk.CTkEntry(content, placeholder_text="Busca una materia")
        search.grid(row=2, column=0, sticky="we", pady=10)

        # Mis Materias
        title = ctk.CTkLabel(content, text="Mis Materias", font=ctk.CTkFont(size=20, weight="bold"))
        title.grid(row=3, column=0, sticky="w", pady=(10, 0))

        materias_frame = ctk.CTkFrame(content, fg_color="transparent")
        materias_frame.grid(row=4, column=0, sticky="we", pady=5)
        materias_frame.grid_columnconfigure((0, 1), weight=1)

        # Cuadro de materias (4 tarjetas como ejemplo)
        materia_names = [("Programación I", "#0033FF"), ("Matemática I", "#D17BFF"),
                         ("Física I", "#FFD700"), ("Sistemas Operativos", "#FF6A6A")]

        for i, (nombre, color) in enumerate(materia_names):
            tarjeta = ctk.CTkFrame(materias_frame, fg_color=color, width=200, height=100)
            tarjeta.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")
            label = ctk.CTkLabel(tarjeta, text=nombre, text_color="black")
            label.pack(expand=True)

        # Sección de tareas próximas a vencer
        tareas_title = ctk.CTkLabel(content, text="Tareas próximas a vencer", font=ctk.CTkFont(size=16, weight="bold"))
        tareas_title.grid(row=5, column=0, sticky="w", pady=(15, 0))

        for i in range(3):
            tarea = ctk.CTkFrame(content, height=40)
            tarea.grid(row=6+i, column=0, sticky="we", pady=5)

    def create_right_panel(self):
        panel = ctk.CTkFrame(self)
        panel.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        # Perfil
        perfil = ctk.CTkLabel(panel, text="Dereck Méndez\nFuturo Ingeniero en Desarrollo de Software y Ciencia de Datos", justify="center", wraplength=180)
        perfil.pack(pady=10)

        # Espacio para imagen de perfil
        ctk.CTkLabel(panel, text="(Imagen)").pack(pady=10)

        # Sección Horarios
        ctk.CTkLabel(panel, text="Horarios", font=ctk.CTkFont(weight="bold")).pack(pady=(20, 5))
        for _ in range(2):
            ctk.CTkFrame(panel, height=40, width=180).pack(pady=5)

        # Recordatorio
        ctk.CTkLabel(panel, text="Recordatorio", font=ctk.CTkFont(weight="bold")).pack(pady=(20, 5))
        ctk.CTkFrame(panel, height=60, width=180).pack(pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()