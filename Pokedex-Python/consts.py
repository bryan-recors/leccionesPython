import os

WIDTH = 600
HEIGHT = 500

# obtener la ruta actual del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#ruta de los iconos concatenando la base con la carpeta
ICON_DIR = os.path.join(BASE_DIR, 'icons')
# ruta del icono bulbasurc oncatenando la el directorio de iconos con el nombre del icono
BULBASUR_ICON = os.path.join(ICON_DIR, 'bulbasaur_icon.png')
PIDGEY_ICON = os.path.join(ICON_DIR, 'pidgey_icon.png')
SQUIRTLE_ICON = os.path.join(ICON_DIR, 'squirtle_icon.png')
TITLE = 'SELECT A POKEMON'
