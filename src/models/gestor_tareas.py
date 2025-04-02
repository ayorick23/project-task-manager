import json
import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
#from views.main_window import *

materias = {}
ruta_archivo = "datos_tareas.json"

#Cargar datos desde el archivo
def cargarDatos():
    try:
        with open(ruta_archivo, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {} #devuelve diccionario vacío

#Guardar los datos en el archivo         
def guardarDatos(datos):
    with open(ruta_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4) #identación de 4 espacios

#Menu
def menu():
    print("\n---------MENÚ PRINCIPAL---------")
    print("1. Registrar materia")
    print("2. Agregar tarea o actividad")
    print("3. Ver actividades pendientes")
    print("4. Marcar actividad como completada")
    print("5. Tareas próximas a vencer")
    print("6. Mostrar estadísticas sobre las tareas")
    print("7. Búsqueda de tareas por palabras clave")
    print("8. Salir")
    opc = int(input("Selecciona una opción: "))
    os.system("cls")
    return opc
 
#Registrar una materia
def registrarMateria(datos):
    materia = simpledialog.askstring("Registrar Materia", "Ingrese el nombre de la materia:")
    if materia == None or materia == "":
        messagebox.showwarning("Advertencia", "Ingresa un nombre para la materia")
    else:
        if materia not in datos:
            datos[materia] = []
            messagebox.showinfo("Materia registrada", f"¡{materia} se registró correctamente!")
        else:
            messagebox.showwarning("Materia registrada", f"¡{materia} ya está registrada!")
    guardarDatos(datos)

#Validar formato de fecha de entrega
def validarFecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y") #DD/MM/YYYY
        return True
    except ValueError:
        return False

#Agregar una tarea  
def agregarTarea(datos):
    materia = simpledialog.askstring("Registrar Materia", "Ingrese el nombre de la materia:")
    if materia in datos:
        descripcion = simpledialog.askstring("Agregar tarea", "Descripción de la tarea:")
        fecha_entrega = simpledialog.askstring("Agregar tarea", "Fecha de entrega (DD/MM/YYYY):")
        if validarFecha(fecha_entrega):
            datos[materia].append({"descripcion": descripcion, "fecha_entrega": fecha_entrega, "completada": False})
            messagebox.showinfo("Agregar tarea", "¡La tarea se agregó correctamente!")
        else:
            messagebox.showwarning("Advertencia", "Fecha inválida, vuelva a intentarlo")
    else:
        messagebox.showwarning("Advertencia", "La materia no existe. Por favor, regístrala primero")
    guardarDatos(datos)

#Ver tareas por materia
def verTareas(datos, materia=None, pantallaPrincipal=None): #inicializada en None porque el argumento es opcional
    if materia is None:
        materia = simpledialog.askstring("Registrar Materia", "Ingrese el nombre de la materia:")
    if materia in datos:
        if pantallaPrincipal is None:
            pantallaPrincipal = tk.Tk()  #crea una nueva instancia de Tk si no se proporciona
            pantallaPrincipal.withdraw()  #esconde la pantalla principal
        
        ventana_tareas = tk.Toplevel(pantallaPrincipal)
        ventana_tareas.title("Tareas Registradas")
        ventana_tareas.geometry("900x300")
        
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
    else:
        messagebox.showwarning("Advertencia", "La materia no existe. Por favor, regístrala primero")
    guardarDatos(datos)

#Marcar una tarea como completada
def completarTarea(datos):
    materia = simpledialog.askstring("Registrar Materia", "Ingrese el nombre de la materia:")
    if materia in datos:
        verTareas(datos, materia) #ver las tareas antes de marcar una tarea completada
        indice = simpledialog.askinteger("Marcar una tarea como completada", "Número de la tarea a completar:") - 1
        if 0 <= indice < len(datos[materia]): #validación para que el índice esté dentro del rango
            if datos[materia][indice]["completada"]: #si "completada" en esa tarea de esa materia es True
                messagebox.showwarning("Advertencia", "¡La tarea ya había sido completada!")
            else:
                datos[materia][indice]["completada"] = True
                messagebox.showinfo("Tarea completada", "Tarea marcada como completada")
        else:
            messagebox.showwarning("Advertencia", "Número de tarea inválido")
    else:
        messagebox.showwarning("Advertencia", "La materia no existe")
    guardarDatos(datos)

#Tareas próximas a vencer
def taresProximas(datos):
    hoy = datetime.now() #devuelve la fecha actual
    limite = hoy + timedelta(days=3) #límite de 3 días adelante
    
    print("\nTareas próximas a vencer")
    tareas_encontradas = False
    for materia, tareas in datos.items(): #iteración por materia y por tarea
        for tarea in tareas:
            try:
                fecha_tarea = datetime.strptime(tarea["fecha_entrega"], "%d/%m/%Y") #convierte la fecha a datetime porque se extra del JSON
                if hoy <= fecha_tarea <= limite and not tarea["completada"]:
                    print(f"- {tarea["descripcion"]} (Entrega: {tarea["fecha_entrega"]}) - Materia: {materia}")
                    tareas_encontradas = True
            except ValueError:
                print(f"Formato de fecha inválido en la tarea '{tarea["descripcion"]}' de {materia}.")
    
    if not tareas_encontradas:
        messagebox.showinfo("Tareas próximas a vencer", "No hay tareas próximas a vencer")

#Mostrar estadísticas sobre las tareas
def mostrarEstadistica(datos):
    print("\nEstadísticas del progreso")
    total_tareas = 0
    total_completadas = 0
    
    for materia, tareas in datos.items():
        completadas = sum(1 for tarea in tareas if tarea["completada"]) #suma las tareas si completada es True
        total_completadas += completadas #contador de completadas por materia
        total_tareas += len(tareas) #total de tareas por materia
        print(f"    - {materia}: {completadas} de {len(tareas)} tareas completadas")
    
    if total_tareas > 0:
        porcentaje = round((total_completadas / total_tareas) * 100, 2) #redondear a dos decimales
        print(f"\nProgreso general: {porcentaje}% completado")
    else:
        print("No hay tareas registradas todavía")

#Búsqueda de tareas
def buscarTareas(datos):
    clave = simpledialog.askstring("Búsqueda de tareas", "Ingrese la palabra clave para buscar:").lower()
    #input("Ingresa la palabra clave para buscar: ").lower()
    print("Resultados de la búsqueda")
    tareas_encontradas = False #bandera
    
    for materia, tareas in datos.items():
        for tarea in tareas:
            if clave in tarea["descripcion"].lower(): #comparación en minúscula
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"    - {tarea['descripcion']} - Materia: {materia}- Fecha de entrega: {tarea['fecha_entrega']} - Estado: {estado}")
                tareas_encontradas = True
                
    if not tareas_encontradas:
        messagebox.showwarning("Búsqueda de tareas", "No se encontraron tareas relacionadas")
        
#Agregar la función de editar y de eliminar tareas y materias