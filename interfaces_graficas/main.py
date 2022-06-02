import toga

def on_press(widget):
    print("hola Mundo utilizando Toga")


def new_button():
    button = toga.Button('Hola Mundo!', on_press=on_press)
    button.style.padding = 20 #padding
    button.style.font_size = 14 # tamaño de letras
    button.style.width = 200 #modificar el ancho
    return button


def build(app):
    box = toga.Box()
    button1 = new_button() #obtener el boton
    box.add(button1)#agregar el boton a la caja
    return box


def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
