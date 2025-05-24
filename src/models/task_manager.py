import pyodbc
from views.messageboxes import showinfo, showerror

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

def modificar_materia(materiaID, profesor, seccion, horario):
        conn = get_connection()
        cursor = conn.cursor()

        materiaID = materiaID
        profesor = profesor
        seccion = seccion
        horario = horario
        try:
            cursor.execute(
                "INSERT INTO Profesores (Nombre) VALUES (?)",
                (profesor)
            )
            #cursor.execute(
            #    "UPDATE Materias SET ProfesorID=? WHERE MateriaID=?",
            #    (profesor, materiaID)
            #)
            cursor.execute(
                "UPDATE Materias SET Seccion=?, Horario=? WHERE MateriaID=?",
                (seccion, horario, materiaID)

            )
            conn.commit()
            return showinfo("Éxito", "Información actualizada correctamente.")
        except Exception as e:
            return showerror("Error", f"Error al actualizar la información: {e}")

def primeras_info_materias():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT 
            m.Nombre AS Materia,
            m.Seccion,
            m.Ciclo,
            m.Icono,
            p.Nombre AS Profesor
        FROM Materias m
        LEFT JOIN Profesores p ON m.ProfesorID = p.ProfesorID
        ORDER BY m.MateriaID
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()
    lista = []
    for row in resultados:
        lista.append({
            "Materia": row[0],
            "Seccion": row[1],
            "Ciclo": row[2],
            "Icono": row[3],
            "Profesor": row[4]
        })
    return lista

# Agregar nuevo usuario a la base de datos
def crear_usuario(entry_user, entry_email, entry_password):
    nombre = entry_user.get()
    email = entry_email.get()
    password = entry_password.get()

    # Validar campos obligatorios
    if not nombre or not email or not password:
        showerror("Error", "Todos los campos son obligatorios.")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
                INSERT INTO Usuarios (Nombre, CorreoElectronico, Contraseña)
                VALUES (?, ?, ?)
            """, (nombre, email, password))
        conn.commit()
        showinfo("Éxito", "Usuario registrado correctamente.")
    except Exception as e:
        showerror("Error", f"No se pudo registrar el usuario.\n{e}")
    conn.close()

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