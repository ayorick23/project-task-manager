import tkinter as tk
from tkinter import messagebox, simpledialog
from models.gestor_tareas import *

#Cargar los datos
datos = cargarDatos()

#Función intermediaria para pasarle el argumento "datos" a las funciones del main
def ejecutarFuncion(func):
    def wrapper():
        func(datos)
    return wrapper

def pantallaPrincipal():
    ventana = tk.Tk()
    ventana.title("Gestor de Tareas")
    ventana.geometry("1000x700")
    ventana.resizable(True, True)
    ventana.configure(bg="#f5f5f5")

    #Título
    title = tk.Label(ventana, text="Gestor de Tareas", font=("Segoe UI", 24, "bold"), bg="#f5f5f5")
    title.pack(pady=(20, 5))
    
    #Subtítulo
    subtitle = tk.Label(ventana, text="Universidad Evangélica de El Salvador", font=("Segoe UI", 14), bg="#f5f5f5")
    subtitle.pack(pady=(0, 20))
    
    #Botones
    botonAgregarMateria = tk.Button(
        ventana,
        text="Registrar una materia",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(registrarMateria)
    )
    botonAgregarMateria.pack(pady=5)
    
    botonAgregarTarea = tk.Button(
        ventana,
        text="Agregar tarea o actividad",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(agregarTarea)
    )
    botonAgregarTarea.pack(pady=5)
    
    botonVerActividades = tk.Button(
        ventana,
        text="Ver actividades pendientes",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(verTareas)
    )
    botonVerActividades.pack(pady=5)
    
    botonCompletarTarea = tk.Button(
        ventana,
        text="Marcar actividad como completada",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(completarTarea)
    )
    botonCompletarTarea.pack(pady=5)
    
    botonTareasProximas = tk.Button(
        ventana,
        text="Tareas próximas a vencer",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(taresProximas)
    )
    botonTareasProximas.pack(pady=5)
    
    botonMostrarEstadistica = tk.Button(
        ventana,
        text="Mostrar estadísticas sobre actividades",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(mostrarEstadistica)
    )
    botonMostrarEstadistica.pack(pady=5)
    
    botonBuscarTareas = tk.Button(
        ventana,
        text="Búsqueda de tareas por palabra clave",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ejecutarFuncion(buscarTareas)
    )
    botonBuscarTareas.pack(pady=5)
    
    botonSalir = tk.Button(
        ventana,
        text="Salir",
        font=("Segoe UI", 12),
        bg="#1E1E1E",
        fg="white",
        width=40,
        height=1,
        command=ventana.quit
    )
    botonSalir.pack(pady=5)

    #Muestra la ventana constantemente
    ventana.mainloop()
    
    return ventana