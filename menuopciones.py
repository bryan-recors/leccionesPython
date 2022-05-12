"""
Realizar un programa que me permita facturar la compra de
de 3 productos, añadir el valor del iva al 12%.
limpiar codigo del cmd usar cls

"""
#menu de opciones usando if ya que switch no existe en python
print("Bienvenido a la facturacion")
menu = """
menu
1) Ingrear Productos
2) Facturar
3) Salir
"""
#import os sirve para ejecutar occines como limpiar pantalla
import os
accion = True;
while accion ==True:
    print(menu)
    op = int(input("Eligue una opcion: "))
    if op is 1:
        print("op 1")
    elif op is 2:
        print("op 2")
    elif op is 3:
        accion = False
    else:
        print("no existe esa opcion")
    #nos permite limpiar pnatalla
    os.system('cls')
