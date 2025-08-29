"""
Archivo Configuracion de ruta de archivos para el challenge de Logging Distribuido.
"""

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DB_PATH  = (BASE_DIR / "logs.db").as_posix()   # logs.db al lado de main/client



'''
__file__ es la ruta del archivo actual.
Esta envuelto en Path para trabajar como objeto de ruta.

.resolve()
Convierte a ruta absoluta.

.parent
Me da la carpeta donde 'vive' ese archivo.
La guardo como BASE_DIR.

BASE_DIR / "logs.db"
Con el operador / hago un join de rutas (independiente del SO).
Resultado: un Path apuntando a logs.db al lado de mi archivo.

.as_posix()
Se convierte a string con slashes

'''