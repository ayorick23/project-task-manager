# Documentación

## Estructura del repositorio

```plaintext
gestor_tareas/
│
├── src/                         #Código fuente principal
│ ├── models/                    #Clases y lógica de datos
│ │ ├── **init**.py
│ │ └── gestor_tareas.py         #Funciones principales
│ │
│ ├── controllers/               #Lógica de negocio
│ │ ├── **init**.py
│ │ └── gestor_tareas.py         #Funciones principales (agregar, completar, etc.)
│ │
│ ├── views/                     #Interfaces gráficas
│ │ ├── **init**.py
│ │ └── main_window.py           #Pantalla principal
│ │
│ └── app.py                     #Punto de entrada (main)
│
├── tests/                       #Pruebas unitarias
│ ├── **init**.py
│ └── test_gestor.py
│
├── requirements.txt             #Dependencias
└── README.md                    #Documentación
```
