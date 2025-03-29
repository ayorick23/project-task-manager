import sys
from pathlib import Path
from views.main_window import *

# Añade el directorio raíz al path de Python
sys.path.append(str(Path(__file__).parent.parent))

if __name__ == "__main__":
    pantallaPrincipal()