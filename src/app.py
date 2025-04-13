import sys
import os
from pathlib import Path
from views.main_window import *

#Añade el directorio raíz al path de Python
sys.path.append(os.path.abspath(os.path.dirname(__file__))) 

if __name__ == "__main__":
    pantallaPrincipal()