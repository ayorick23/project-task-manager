import pyodbc

# Configuración de la conexión
def get_connection():
    server = 'DESKTOP-0HC2CB3'
    database = 'ProyectoDB'
    username = 'testuser'
    password = '1234'
    
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
    try:
        conn = pyodbc.connect(conn_str)
    except Exception as e:
        print("Error al conectar a la base de datos:")
        print(e)
        
    return conn

# Obtener información de materias
def obtener_info_materias():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Codigo, MateriaID, Nombre, RequisitosPrevios, UnidadesValorativas FROM Materias")
    materias = cursor.fetchall()
    conn.close()
    # Convertir a lista de diccionarios para fácil acceso en labels
    lista_materias = []
    for materia in materias:
        lista_materias.append({
            "Codigo": materia[0],
            "MateriaID": materia[1],
            "Nombre": materia[2],
            "RequisitosPrevios": materia[3],
            "UnidadesValorativas": materia[4]
        })
    return lista_materias
    
# Obtener todas las materias
def obtener_materias():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Materias")
    materias = cursor.fetchall()
    conn.close()
    return materias

# Agregar una nueva materia
def agregar_materia(nombre, descripcion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Materias (nombre, descripcion) VALUES (?, ?)",
        (nombre, descripcion)
    )
    conn.commit()
    conn.close()

# Editar una materia existente
def editar_materia(id_materia, nombre, descripcion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Materias SET nombre = ?, descripcion = ? WHERE id = ?",
        (nombre, descripcion, id_materia)
    )
    conn.commit()
    conn.close()

# Eliminar una materia
def eliminar_materia(id_materia):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Materias WHERE id = ?",
        (id_materia,)
    )
    conn.commit()
    conn.close()