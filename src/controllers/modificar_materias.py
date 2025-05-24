import tkinter as tk
from models.task_manager import modificar_materia
from views.messageboxes import showwarning

class ModificarMateriaVentana(tk.Toplevel):
    def __init__(self, master, materia_id, profesor='', seccion='', horario='', refresh_callback=None):
        super().__init__(master)
        self.title("Modificar Materia")
        self.materia_id = materia_id
        self.refresh_callback = refresh_callback

        # Labels y entradas
        tk.Label(self, text="Profesor:").grid(row=0, column=0, padx=10, pady=5)
        self.profesor_entry = tk.Entry(self)
        self.profesor_entry.grid(row=0, column=1, padx=10, pady=5)
        self.profesor_entry.insert(0, profesor)

        tk.Label(self, text="Sección:").grid(row=1, column=0, padx=10, pady=5)
        self.seccion_entry = tk.Entry(self)
        self.seccion_entry.grid(row=1, column=1, padx=10, pady=5)
        self.seccion_entry.insert(0, seccion)

        tk.Label(self, text="Horario:").grid(row=2, column=0, padx=10, pady=5)
        self.horario_entry = tk.Entry(self)
        self.horario_entry.grid(row=2, column=1, padx=10, pady=5)
        self.horario_entry.insert(0, horario)

        tk.Button(self, text="Guardar Cambios", command=self.guardar_cambios).grid(row=3, column=0, columnspan=2, pady=10)

    def guardar_cambios(self):
        profesor = self.profesor_entry.get()
        seccion = self.seccion_entry.get()
        horario = self.horario_entry.get()
        if not profesor or not seccion or not horario:
            showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        modificar_materia(self.materia_id, profesor, seccion, horario)
        
        if self.refresh_callback:
            self.refresh_callback()
        self.destroy()