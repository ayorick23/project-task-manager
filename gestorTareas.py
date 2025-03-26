import json
import os
import datetime

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
    print("5. Salir")
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
        datetime.datetime.strptime(fecha, "%d/%m/%Y") #DD/MM/YYYY
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
                guardarDatos(datos)
                print("Saliendo...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo")

#Ejecución del Main
if __name__ == "__main__":
    main()