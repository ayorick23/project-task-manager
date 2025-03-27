import json
import os
from datetime import datetime, timedelta

materias = {}

#Cargar datos desde el archivo
def cargarDatos():
    try:
        with open("datos_tareas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {} #devuelve diccionario vacío

#Guardar los datos en el archivo         
def guardarDatos(datos):
    with open("datos_tareas.json", "w") as archivo:
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
    materia = input("Ingrese la materia: ")
    if materia not in datos:
        datos[materia] = []
        print(f"Materia '{materia}' registrada exitosamente")
    else:
        print("La materia ya está registrada")
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
    materia = input("Ingrese la materia: ")
    if materia in datos:
        descripcion = input("Descripción de la tarea: ")
        fecha_entrega = input("Fecha de entrega (DD/MM/YYYY): ")
        if validarFecha(fecha_entrega):
            datos[materia].append({"descripcion": descripcion, "fecha_entrega": fecha_entrega, "completada": False})
            print("Tarea agregada exitosamente")
        else:
            print("Fecha inválida, vuelva a intentarlo")
    else:
        print("La materia no existe. Por favor, regístrala primero")
    guardarDatos(datos)

#Ver tareas por materia
def verTareas(datos, materia=None): #inicializada en None porque el argumento es opcional
    if materia is None:
        materia = input("Ingrese la materia: ")
    if materia in datos:
        print(f"\nTareas de {materia}")
        for i, tarea in enumerate(datos[materia]): #enumera automáticamente cada iteración
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"   {i + 1}. {tarea['descripcion']} - Fecha de entrega: {tarea['fecha_entrega']} - Estado: {estado}")
    else:
        print("La materia no existe. Por favor, regístrala primero")
    guardarDatos(datos)

#Marcar una tarea como completada
def completarTarea(datos):
    materia = input("Ingrese la materia: ")
    if materia in datos:
        verTareas(datos, materia) #ver las tareas antes de marcar una tarea completada
        indice = int(input("Número de la tarea a completar: ")) - 1
        if 0 <= indice < len(datos[materia]): #validación para que el índice esté dentro del rango
            datos[materia][indice]["completada"] = True
            print("Tarea marcada como completada")
        else:
            print("Número de tarea inválido")
    else:
        print("La materia no existe")
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
        print("No hay tareas próximas a vencer")

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
    clave = input("Ingresa la palabra clave para buscar: ").lower()
    print("Resultados de la búsqueda")
    tareas_encontradas = False #bandera
    
    for materia, tareas in datos.items():
        for tarea in tareas:
            if clave in tarea["descripcion"].lower(): #comparación en minúscula
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"    - {tarea['descripcion']} - Materia: {materia}- Fecha de entrega: {tarea['fecha_entrega']} - Estado: {estado}")
                tareas_encontradas = True
                
    if not tareas_encontradas:
        print("No se encontraron tareas relacionadas")

#Main
def main():
    datos = cargarDatos()
    while True:
        opc = menu()
        match opc:
            case 1:
                registrarMateria(datos)
            case 2:
                agregarTarea(datos)
            case 3:
                verTareas(datos)
            case 4:
                completarTarea(datos)
            case 5:
                taresProximas(datos)
            case 6:
                mostrarEstadistica(datos)
            case 7:
                buscarTareas(datos)
            case 8:
                guardarDatos(datos)
                print("Saliendo...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo")

#Ejecución del Main
if __name__ == "__main__":
    main()