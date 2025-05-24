import customtkinter as ctk
from models.task_manager import modificar_materia

class ModificarMateriaFrame(ctk.CTkFrame):
    def __init__(self, master, materia_id, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Widgets
        ctk.CTkLabel(self, text="Nombre del Profesor:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.profesor_entry = ctk.CTkEntry(self)
        #self.profesor_entry.insert(0, profesor_actual)
        self.profesor_entry.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(self, text="Sección:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.seccion_entry = ctk.CTkEntry(self)
        #self.seccion_entry.insert(0, seccion_actual)
        self.seccion_entry.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(self, text="Horario:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.horario_entry = ctk.CTkEntry(self)
        #self.horario_entry.insert(0, horario_actual)
        self.horario_entry.grid(row=2, column=1, padx=10, pady=10)

        self.guardar_btn = ctk.CTkButton(self, text="Guardar Cambios", command=lambda: modificar_materia(materia_id, self.profesor_entry.get(), self.seccion_entry.get(), self.horario_entry.get()))
        self.guardar_btn.grid(row=3, column=0, columnspan=2, pady=20)

        #self.mensaje_label = ctk.CTkLabel(self, text="")
        #self.mensaje_label.grid(row=4, column=0, columnspan=2)

        #modificar_materia(self, materia_id, self.profesor_entry.get(), self.seccion_entry.get(), self.horario_entry.get())

    def destroy(self):
        super().destroy()
        
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root.title("Modificar Materia")
    frame = ModificarMateriaFrame(root, materia_id=1)
    frame.pack(padx=20, pady=20)
    root.mainloop()