import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import sys
import os
from pathlib import Path

#Añade el directorio raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

#Cargar los datos
def cargar_datos(): #se mete en una función para evitar problemas de importación circular
    from models.gestor_tareas import cargarDatos
    datos = cargarDatos()
    return datos

def mostrar_tareas(datos, materia, pantallaPrincipal):
    ventana_tareas = ctk.CTkToplevel(pantallaPrincipal) #crea una ventana secundaria
    ventana_tareas.title("Tareas Registradas")
    ventana_tareas.geometry("950x300")

    #Presenta las tareas en un Treeview (tabla)
    tree = ttk.Treeview(ventana_tareas, columns=("#", "Materia", "Descripción", "Fecha de Entrega", "Estado"), show="headings")
    tree.heading("#", text="#")
    tree.heading("Materia", text="Materia")
    tree.heading("Descripción", text="Descripción")
    tree.heading("Fecha de Entrega", text="Fecha")
    tree.heading("Estado", text="Estado")
    
    for i, tarea in enumerate(datos[materia]):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            tree.insert("", tk.END, values=(i+1, materia, tarea["descripcion"], tarea["fecha_entrega"], estado))
            
    tree.pack(expand=True, fill="both")