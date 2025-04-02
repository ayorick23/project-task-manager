import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
from pathlib import Path
from main_window import *
from models.gestor_tareas import *

#Añade el directorio raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

#Cargar los datos
datos = cargarDatos()

def mostrar_tareas(datos):
    if materia is None:
        materia = simpledialog.askstring("Registrar Materia", "Ingrese el nombre de la materia:")
    materia = input("Ingrese materia: ")
    if materia in datos:
        ventana_tareas = tk.Toplevel(pantallaPrincipal)
        ventana_tareas.title("Tareas Registradas")
        ventana_tareas.geometry("500x300")
        
        tree = ttk.Treeview(ventana_tareas, columns=("Materia", "Descripción", "Fecha de Entrega", "Estado"), show="headings")
        tree.heading("Materia", text="Materia")
        tree.heading("Descripción", text="Descripción")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Estado", text="Estado")
        
        for tarea in datos[materia]:
            estado = "Completada" if tarea["completada"] else "Pendiente"
            tree.insert("", tk.END, values=(tarea["materia"], tarea["descripcion"], tarea["fecha_entrega"], estado))
            
        tree.pack(expand=True, fill="both")
    else:
        messagebox.showwarning("Advertencia", "La materia no existe. Por favor, regístrala primero")
        
mostrar_tareas(datos)