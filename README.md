# Documentación

## Estructura del repositorio

``gestor_tareas/
│
├── src/ # Código fuente principal
│ ├── models/ # Clases y lógica de datos
│ │ ├── **init**.py
│ │ ├── tarea.py # Clase Tarea
│ │ └── materia.py # Clase Materia
│ │
│ ├── controllers/ # Lógica de negocio
│ │ ├── **init**.py
│ │ └── gestor_tareas.py # Funciones principales (agregar, completar, etc.)
│ │
│ ├── views/ # Interfaces gráficas
│ │ ├── **init**.py
│ │ ├── main_window.py # Pantalla principal
│ │ ├── add_task_window.py # Ventana agregar tarea
│ │ └── stats_window.py # Ventana de estadísticas
│ │
│ └── app.py # Punto de entrada (main)
│
├── tests/ # Pruebas unitarias
│ ├── **init**.py
│ └── test_gestor.py
│
├── requirements.txt # Dependencias
└── README.md # Documentación
