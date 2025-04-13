import tkinter as tk
from tkinter import messagebox, simpledialog
import customtkinter as ctk
from models.gestor_tareas import *

#Modo de color y tema
ctk.set_appearance_mode("system") #modo por defecto del sistema
ctk.set_default_color_theme("blue") #tema azul por defecto

#Cargar los datos
datos = cargarDatos()

#Función intermediaria para pasarle el argumento "datos" a las funciones del main
def ejecutarFuncion(func):
    def wrapper():
        func(datos)
    return wrapper

def pantallaPrincipal():
    ventana = ctk.CTk() #ventana principal
    ventana.iconbitmap("src/assets/icono-principal-48.ico") #icono de la ventana
    ventana.title("Gestor de Tareas")
    ventana.geometry("1000x700")
    ventana.resizable(True, True)
    #ventana.configure(bg="#f5f5f5")

    #Título
    titulo = ctk.CTkLabel(ventana, text="Gestor de Tareas", font=("Segoe UI", 24, "bold")) #bg="#f5f5f5"
    titulo.pack(pady=(20, 5))
    
    #Subtítulo
    subtitulo = ctk.CTkLabel(ventana, text="Universidad Evangélica de El Salvador", font=("Segoe UI", 14)) #bg="#f5f5f5"
    subtitulo.pack(pady=(0, 20))
    
    #Botones
    botonAgregarMateria = ctk.CTkButton(
        ventana,
        text="Registrar una materia",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(registrarMateria)
    )
    botonAgregarMateria.pack(pady=5)
    
    botonAgregarTarea = ctk.CTkButton(
        ventana,
        text="Agregar tarea o actividad",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(agregarTarea)
    )
    botonAgregarTarea.pack(pady=5)
    
    botonVerActividades = ctk.CTkButton(
        ventana,
        text="Ver actividades pendientes",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(verTareas)
    )
    botonVerActividades.pack(pady=5)
    
    botonCompletarTarea = ctk.CTkButton(
        ventana,
        text="Marcar actividad como completada",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(completarTarea)
    )
    botonCompletarTarea.pack(pady=5)
    
    botonTareasProximas = ctk.CTkButton(
        ventana,
        text="Tareas próximas a vencer",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(taresProximas)
    )
    botonTareasProximas.pack(pady=5)
    
    botonMostrarEstadistica = ctk.CTkButton(
        ventana,
        text="Mostrar estadísticas sobre actividades",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(mostrarEstadistica)
    )
    botonMostrarEstadistica.pack(pady=5)
    
    botonBuscarTareas = ctk.CTkButton(
        ventana,
        text="Búsqueda de tareas por palabra clave",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(buscarTareas)
    )
    botonBuscarTareas.pack(pady=5)
    
    botonSalir = ctk.CTkButton(
        ventana,
        text="Salir",
        font=("Segoe UI", 12),
        #bg="#1E1E1E",
        #fg="white",
        width=40,
        height=1,
        command=ventana.quit
    )
    botonSalir.pack(pady=5)

    #Muestra la ventana constantemente
    ventana.mainloop()
    
    return ventana