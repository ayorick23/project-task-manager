import sys
import os
from pathlib import Path
from views.main_window import *
from controllers.modificar_materias import ModificarMateriaFrame

#Añade el directorio raíz al path de Python
sys.path.append(os.path.abspath(os.path.dirname(__file__))) 

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()