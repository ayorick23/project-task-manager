from gestorTareas import *
from pantallaPrincipal import *

"""
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
                
#Ejecución del Main consola para pruebas
if __name__ == "__main__":
    main()
"""

#Ejecución del Main interfaz gráfica
if __name__ == "__main__":
    pantallaPrincipal()