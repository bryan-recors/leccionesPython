import toga
import requests
import threading
from consts import *
from toga.style.pack import *  # estilos


class PokeDex(toga.App):
    def __init__(self, title, id):
        toga.App.__init__(self, title, id)  # pasando parametros
        self.title = title  # asignar atributo title
        self.size = (WIDTH, HEIGHT)  # medidas de la ventana
        self.heading = ['Name']  # nombre encabezado Tabla
        self.data = []  # data para la tabla
        self.offset = 0  # pagnas de pokedesk
        self.response_name = ''  # atributo de nombre
        self.response_description = ''  # atributo de decripcion
        self.response_sprite = ''  # imagen del pokemon
        self.create_elements()  # llamar a la creacion de los elementos
        self.load_async_data()  # peticion asyc al servidor pokemons
        self.validate_previous_command()  # validar offset

    def startup(self): #pintar cosas
        self.main_window = toga.MainWindow('main', title=self.title, size=self.size)  # crear la ventana

        information_area = toga.Box(
            children=[self.image_view, self.pokemon_name, self.pokemon_description],
            # elementos del area de informacion
            style=Pack(  # definir estilos
                direction=COLUMN,  # direccion en columnas
                alignment=CENTER  # alinear todoalCentro
            )
        )  #genero una caja

        split = toga.SplitContainer()  # instanciar split para dividir ventana
        split.content = [self.table, information_area]  # indicar la division y su orden
        self.main_window.content = split  # Le asigno a mi ventana el split que tienen la tabla y la caja
        self.main_window.toolbar.add(self.previouse_command, self.next_command)  # añadir el toolBar
        self.main_window.show()  # mostrar la ventana

    def create_elements(self):
        self.create_table()
        self.create_toolbar()
        self.create_image(PIDGEY_ICON)
        self.create_labels()

    def create_toolbar(self):
        self.create_next_command()
        self.create_previouse_command()

    def create_next_command(self):
        self.next_command = toga.Command(self.next, label='Next')

    def create_previouse_command(self):
        self.previouse_command = toga.Command(self.next, label='Previus')

    def create_table(self):
        self.table = toga.Table(self.heading, data=self.data, on_select=self.select_element)


    def create_image(self, path, width=200, height=200):
        self.default_image = toga.Image(path)
        style = Pack(width=width, height=height)
        self.image_view = toga.ImageView(self.default_image, style=style)

    def create_labels(self):
        style = Pack(text_align=CENTER)
        self.pokemon_name = toga.Label(TITLE, style=style)  # centrar
        self.pokemon_description = toga.Label('Description', style=style)
        self.pokemon_name.style.font_size = 20  # tamaño de fuente
        self.pokemon_name.style.padding_bottom = 10  # pading


    def load_data(self):
        path = 'https://pokeapi.co/api/v2/pokemon-form?offset={}&limit=20'.format(self.offset)  # url
        response = requests.get(path)  # peticion
        if response:
            result = response.json()  # convertir a diccionario
            for pokemon in result['results']:  # iterar results
                name = pokemon['name']  # capturo el nombre
                self.data.append(name)  # agregar nombre al ultimo indice de la lista

    def load_async_data(self):
        self.table.data = []  # limpiardatos de la tabla
        self.data.clear()  # limpiar el atributo data
        self.table.data = self.data  # refrescar tabla

        # refrescar information area
        self.image_view.image = None
        self.pokemon_name.text = TITLE
        self.pokemon_description.text = 'Description'

        thread = threading.Thread(target=self.load_data)
        thread.start()
        thread.join()
        self.table.data = self.data  # refrescar tabla
        self.image_view.image = PIDGEY_ICON

    def load_pokemon(self, pokemon):
        path = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)  # crear el path
        response = requests.get(path)  # obtener el detalle con el path
        if response:
            result = response.json()  # convierto a diccionario
            self.response_name = result['forms'][0]['name']  # tomo el nombre del pokemon
            abilities = list()  # defino una lista vacia para abilidades
            for ability in result['abilities']:  # itero las habilidades
                name_ability = ability['ability']['name']  # tomo el nombre de la habilidad
                abilities.append(name_ability)  # paso el nombre a la lista
            self.response_sprite = result['sprites']['front_default']  # tomo una imagen del pokemon
            self.response_description = ' '.join(abilities)  # convertir la lista de habilidades en string


    def load_async_pokemon(self, pokemon):
        thread = threading.Thread(target=self.load_pokemon, args=[pokemon])
        thread.start()
        thread.join()
        # actualizar datos
        self.image_view.image = toga.Image(BULBASUR_ICON)
        self.pokemon_name.text = self.response_name
        self.pokemon_description.text = self.response_description


    # CALLBACKS
    def validate_previous_command(self):
        self.previouse_command.enabled = not self.offset == 0  # no habilidtar si el offset es 0

    def previous(self, widget):
        self.offset -= 1
        self.handler_command(widget)

    def next(self, widget):
        self.offset += 1
        self.handler_command(widget)

    def handler_command(self, widget):
        widget.enabled = False  # desabilitar botones antes de hacer la peticion
        # self.load_data()
        self.load_async_data()
        widget.enabled = True  # desabilitar botones antes de hacer la peticion
        self.validate_previous_command()

    def select_element(self, widget, row):
        if row:
            self.load_async_pokemon(row.name)


if __name__ == '__main__':
    pokedex = PokeDex('PokeDex', 'com.PokeDex')
    pokedex.main_loop()
